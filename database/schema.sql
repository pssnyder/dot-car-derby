-- Dot Car Derby - Initial Database Schema
-- PostgreSQL 15+
-- 
-- This schema creates the core tables needed for MVP functionality
-- Run this file to initialize your database

-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- ============================================================================
-- USERS & AUTHENTICATION
-- ============================================================================

-- Users table - core user accounts
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(255) UNIQUE NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    oauth_provider VARCHAR(50) NOT NULL, -- 'google', 'github', etc.
    oauth_id VARCHAR(255) NOT NULL,
    avatar_url VARCHAR(500),
    created_at TIMESTAMP DEFAULT NOW(),
    last_login TIMESTAMP,
    is_active BOOLEAN DEFAULT true,
    CONSTRAINT unique_oauth UNIQUE (oauth_provider, oauth_id)
);

-- ============================================================================
-- DOT DRIVERS (PLAYER PROFILES)
-- ============================================================================

-- Dot drivers - player racing profiles
CREATE TABLE dot_drivers (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    display_name VARCHAR(100) NOT NULL,
    bio TEXT,
    
    -- Stats
    skill_level INTEGER DEFAULT 1,
    total_races INTEGER DEFAULT 0,
    total_wins INTEGER DEFAULT 0,
    total_podiums INTEGER DEFAULT 0,
    best_lap_time FLOAT,
    
    -- Education progress
    education_score INTEGER DEFAULT 0,
    tutorials_completed TEXT[] DEFAULT ARRAY[]::TEXT[],
    achievements TEXT[] DEFAULT ARRAY[]::TEXT[],
    
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    
    CONSTRAINT one_driver_per_user UNIQUE (user_id)
);

-- ============================================================================
-- DOT VEHICLES
-- ============================================================================

-- Dot vehicles - the "cars" that race
CREATE TABLE dot_vehicles (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    driver_id UUID REFERENCES dot_drivers(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    
    -- Appearance
    color_primary VARCHAR(7) DEFAULT '#0066FF',
    color_secondary VARCHAR(7) DEFAULT '#FF6600',
    pattern VARCHAR(50) DEFAULT 'solid',
    
    -- DNA Configuration (stored as JSONB for flexibility)
    dna_config JSONB NOT NULL DEFAULT '{
        "sensors": [{"type": "distance", "id": "front", "enabled": true}],
        "actions": [{"type": "forward", "id": "forward", "enabled": true}],
        "training": {"algorithm": "genetic", "maxEpochs": 100}
    }'::jsonb,
    
    -- Performance Characteristics
    max_speed FLOAT DEFAULT 5.0,
    acceleration FLOAT DEFAULT 1.0,
    turning_radius FLOAT DEFAULT 45.0,
    brake_power FLOAT DEFAULT 2.0,
    
    -- Available Upgrades
    unlocked_sensors TEXT[] DEFAULT ARRAY['basic_distance'],
    unlocked_actions TEXT[] DEFAULT ARRAY['forward', 'turn'],
    unlocked_algorithms TEXT[] DEFAULT ARRAY['genetic'],
    
    -- Training Limits
    max_epochs_per_day INTEGER DEFAULT 100,
    current_daily_epochs INTEGER DEFAULT 0,
    last_epoch_reset TIMESTAMP DEFAULT NOW(),
    
    -- Metadata
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- ============================================================================
-- DNA TEMPLATES (TRAINED MODELS)
-- ============================================================================

-- DNA templates - saved training results
CREATE TABLE dna_templates (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    vehicle_id UUID REFERENCES dot_vehicles(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    version VARCHAR(20) DEFAULT '1.0.0',
    
    -- Serialized DNA (Brain/Q-Table/Network)
    dna_data JSONB NOT NULL,
    algorithm_type VARCHAR(50) NOT NULL,
    
    -- Training Metadata
    training_epochs INTEGER NOT NULL,
    training_time_seconds INTEGER,
    fitness_score FLOAT,
    training_track_id UUID,
    
    -- Performance Stats
    avg_lap_time FLOAT,
    best_lap_time FLOAT,
    success_rate FLOAT,
    crash_rate FLOAT,
    
    -- Sharing
    is_public BOOLEAN DEFAULT false,
    is_featured BOOLEAN DEFAULT false,
    fork_count INTEGER DEFAULT 0,
    fork_source_id UUID REFERENCES dna_templates(id) ON DELETE SET NULL,
    download_count INTEGER DEFAULT 0,
    vote_score INTEGER DEFAULT 0,
    
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- ============================================================================
-- TRACKS
-- ============================================================================

-- Tracks - race courses
CREATE TABLE tracks (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    description TEXT,
    difficulty_level INTEGER NOT NULL CHECK (difficulty_level BETWEEN 1 AND 10),
    track_type VARCHAR(50) NOT NULL, -- 'drag', 'circuit', 'obstacle', 'technical'
    
    -- Track Data (waypoints, obstacles, boundaries)
    track_data JSONB NOT NULL,
    
    -- Visual
    thumbnail_url VARCHAR(500),
    preview_image_url VARCHAR(500),
    
    -- Requirements
    min_skill_level INTEGER DEFAULT 1,
    required_sensors TEXT[],
    recommended_sensors TEXT[],
    
    -- Metadata
    length_meters FLOAT,
    estimated_time_seconds FLOAT,
    
    -- Stats
    best_time FLOAT,
    best_time_holder_id UUID REFERENCES dot_drivers(id) ON DELETE SET NULL,
    total_attempts INTEGER DEFAULT 0,
    total_completions INTEGER DEFAULT 0,
    
    -- Administrative
    is_active BOOLEAN DEFAULT true,
    is_tournament_eligible BOOLEAN DEFAULT false,
    created_by_user_id UUID REFERENCES users(id) ON DELETE SET NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- ============================================================================
-- RACES
-- ============================================================================

-- Races - individual race attempts/results
CREATE TABLE races (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    track_id UUID REFERENCES tracks(id) ON DELETE CASCADE,
    vehicle_id UUID REFERENCES dot_vehicles(id) ON DELETE CASCADE,
    dna_template_id UUID REFERENCES dna_templates(id) ON DELETE SET NULL,
    
    -- Race Results
    start_time TIMESTAMP DEFAULT NOW(),
    end_time TIMESTAMP,
    completion_time FLOAT, -- seconds
    finished BOOLEAN DEFAULT false,
    did_crash BOOLEAN DEFAULT false,
    crash_reason TEXT,
    
    -- Performance
    best_lap_time FLOAT,
    avg_speed FLOAT,
    max_speed_reached FLOAT,
    checkpoints_reached INTEGER DEFAULT 0,
    
    -- Race Position (for competitive races)
    race_position INTEGER,
    total_participants INTEGER DEFAULT 1,
    
    -- Race Data (for replay)
    race_data JSONB, -- Positions, actions, timestamps
    
    -- Tournament Association
    tournament_id UUID, -- Will reference tournaments table (created later)
    is_practice BOOLEAN DEFAULT true,
    is_validated BOOLEAN DEFAULT false,
    
    created_at TIMESTAMP DEFAULT NOW()
);

-- ============================================================================
-- UPGRADES
-- ============================================================================

-- Upgrades - purchasable improvements
CREATE TABLE upgrades (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    upgrade_type VARCHAR(50) NOT NULL, -- 'sensor', 'action', 'algorithm', 'performance', 'training'
    category VARCHAR(50),
    
    -- Upgrade Data (what it unlocks/modifies)
    upgrade_config JSONB NOT NULL,
    
    -- Visuals
    icon_url VARCHAR(500),
    
    -- Cost and Requirements
    point_cost INTEGER NOT NULL CHECK (point_cost >= 0),
    required_skill_level INTEGER DEFAULT 1,
    prerequisite_upgrade_ids UUID[],
    
    -- Metadata
    tier INTEGER DEFAULT 1 CHECK (tier BETWEEN 1 AND 5),
    is_active BOOLEAN DEFAULT true,
    sort_order INTEGER DEFAULT 0,
    
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- ============================================================================
-- USER UPGRADES (INVENTORY)
-- ============================================================================

-- User upgrades - tracking what upgrades users own
CREATE TABLE user_upgrades (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    driver_id UUID REFERENCES dot_drivers(id) ON DELETE CASCADE,
    upgrade_id UUID REFERENCES upgrades(id) ON DELETE CASCADE,
    vehicle_id UUID REFERENCES dot_vehicles(id) ON DELETE SET NULL,
    
    purchased_at TIMESTAMP DEFAULT NOW(),
    is_equipped BOOLEAN DEFAULT false,
    equipped_at TIMESTAMP,
    
    CONSTRAINT unique_driver_upgrade UNIQUE(driver_id, upgrade_id)
);

-- ============================================================================
-- POINTS & CURRENCY
-- ============================================================================

-- Driver points - virtual currency
CREATE TABLE driver_points (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    driver_id UUID REFERENCES dot_drivers(id) ON DELETE CASCADE,
    
    total_points_earned INTEGER DEFAULT 0 CHECK (total_points_earned >= 0),
    available_points INTEGER DEFAULT 0 CHECK (available_points >= 0),
    spent_points INTEGER DEFAULT 0 CHECK (spent_points >= 0),
    
    updated_at TIMESTAMP DEFAULT NOW(),
    
    CONSTRAINT one_points_record_per_driver UNIQUE (driver_id)
);

-- Point transactions - audit log
CREATE TABLE point_transactions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    driver_id UUID REFERENCES dot_drivers(id) ON DELETE CASCADE,
    
    amount INTEGER NOT NULL, -- Can be positive (earned) or negative (spent)
    transaction_type VARCHAR(50) NOT NULL, -- 'race_completion', 'tournament_reward', 'upgrade_purchase', etc.
    description TEXT,
    
    -- Related entities
    race_id UUID REFERENCES races(id) ON DELETE SET NULL,
    upgrade_id UUID REFERENCES upgrades(id) ON DELETE SET NULL,
    
    created_at TIMESTAMP DEFAULT NOW()
);

-- ============================================================================
-- INDEXES FOR PERFORMANCE
-- ============================================================================

-- Users
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_oauth ON users(oauth_provider, oauth_id);
CREATE INDEX idx_users_active ON users(is_active) WHERE is_active = true;

-- Drivers
CREATE INDEX idx_drivers_user_id ON dot_drivers(user_id);
CREATE INDEX idx_drivers_skill_level ON dot_drivers(skill_level);
CREATE INDEX idx_drivers_total_wins ON dot_drivers(total_wins DESC);

-- Vehicles
CREATE INDEX idx_vehicles_driver_id ON dot_vehicles(driver_id);
CREATE INDEX idx_vehicles_active ON dot_vehicles(is_active) WHERE is_active = true;

-- DNA Templates
CREATE INDEX idx_dna_vehicle_id ON dna_templates(vehicle_id);
CREATE INDEX idx_dna_public ON dna_templates(is_public) WHERE is_public = true;
CREATE INDEX idx_dna_algorithm ON dna_templates(algorithm_type);
CREATE INDEX idx_dna_votes ON dna_templates(vote_score DESC);

-- Tracks
CREATE INDEX idx_tracks_difficulty ON tracks(difficulty_level);
CREATE INDEX idx_tracks_type ON tracks(track_type);
CREATE INDEX idx_tracks_active ON tracks(is_active) WHERE is_active = true;

-- Races
CREATE INDEX idx_races_track_id ON races(track_id);
CREATE INDEX idx_races_vehicle_id ON races(vehicle_id);
CREATE INDEX idx_races_created_at ON races(created_at DESC);
CREATE INDEX idx_races_finished ON races(finished) WHERE finished = true;

-- Upgrades
CREATE INDEX idx_upgrades_type ON upgrades(upgrade_type);
CREATE INDEX idx_upgrades_tier ON upgrades(tier);
CREATE INDEX idx_upgrades_active ON upgrades(is_active) WHERE is_active = true;

-- User Upgrades
CREATE INDEX idx_user_upgrades_driver ON user_upgrades(driver_id);
CREATE INDEX idx_user_upgrades_equipped ON user_upgrades(driver_id, is_equipped) WHERE is_equipped = true;

-- Point Transactions
CREATE INDEX idx_point_trans_driver ON point_transactions(driver_id);
CREATE INDEX idx_point_trans_created ON point_transactions(created_at DESC);

-- ============================================================================
-- TRIGGERS
-- ============================================================================

-- Update timestamps automatically
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Apply to tables with updated_at
CREATE TRIGGER update_dot_drivers_updated_at BEFORE UPDATE ON dot_drivers
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_dot_vehicles_updated_at BEFORE UPDATE ON dot_vehicles
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_dna_templates_updated_at BEFORE UPDATE ON dna_templates
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_tracks_updated_at BEFORE UPDATE ON tracks
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_upgrades_updated_at BEFORE UPDATE ON upgrades
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_driver_points_updated_at BEFORE UPDATE ON driver_points
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- ============================================================================
-- INITIAL DATA COMMENTS
-- ============================================================================

COMMENT ON TABLE users IS 'Core user accounts with OAuth authentication';
COMMENT ON TABLE dot_drivers IS 'Player racing profiles with stats and progression';
COMMENT ON TABLE dot_vehicles IS 'The AI vehicles that players train and race';
COMMENT ON TABLE dna_templates IS 'Saved trained models (brains) for vehicles';
COMMENT ON TABLE tracks IS 'Race courses with difficulty and requirements';
COMMENT ON TABLE races IS 'Individual race attempts and results';
COMMENT ON TABLE upgrades IS 'Purchasable improvements for vehicles and training';
COMMENT ON TABLE user_upgrades IS 'Tracking which upgrades each player owns';
COMMENT ON TABLE driver_points IS 'Virtual currency for purchasing upgrades';
COMMENT ON TABLE point_transactions IS 'Audit log of all point earnings and spending';

-- Schema created successfully!
-- Next steps:
-- 1. Run seeds/initial_tracks.sql to add starter tracks
-- 2. Run seeds/initial_upgrades.sql to add available upgrades
-- 3. Test with your application
