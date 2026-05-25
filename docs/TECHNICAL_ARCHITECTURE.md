# Dot Car Derby - Technical Architecture

## 🏛️ System Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                     Client (Web Browser)                     │
├──────────────┬──────────────┬──────────────┬────────────────┤
│   UI Layer   │  Game Engine │  ML Training │  Data Storage  │
│   (React)    │  (WebGL/JS)  │  (TensorFlow)│  (IndexedDB)   │
└──────────────┴──────────────┴──────────────┴────────────────┘
                              ↕ HTTPS/WSS
┌─────────────────────────────────────────────────────────────┐
│                      API Gateway                             │
│              (Authentication, Rate Limiting)                 │
└─────────────────────────────────────────────────────────────┘
                              ↕
        ┌──────────────┬──────────────┬──────────────┐
        │              │              │              │
┌───────▼──────┐ ┌────▼─────┐ ┌──────▼──────┐ ┌────▼─────┐
│  Auth Service│ │  User    │ │  Race       │ │Tournament│
│  (OAuth)     │ │  Service │ │  Service    │ │ Service  │
└──────────────┘ └──────────┘ └─────────────┘ └──────────┘
                       ↕              ↕              ↕
                ┌──────────────────────────────────────┐
                │         Database Layer               │
                │  (PostgreSQL + Redis Cache)          │
                └──────────────────────────────────────┘
```

## 🎨 Frontend Architecture

### Technology Stack
- **Framework**: React 18+ with TypeScript
- **State Management**: Redux Toolkit or Zustand
- **Routing**: React Router v6
- **Styling**: Tailwind CSS + styled-components
- **3D/Graphics**: Three.js or PixiJS for race rendering
- **ML Framework**: TensorFlow.js
- **Build Tool**: Vite
- **Testing**: Vitest + React Testing Library

### Core Modules

#### 1. UI Components
```
src/
├── components/
│   ├── auth/           # Login, registration
│   ├── dashboard/      # User home, stats overview
│   ├── training/       # ML training interface
│   ├── racing/         # Race viewer, track selection
│   ├── garage/         # Dot customization, upgrades
│   ├── tournament/     # Tournament brackets, leaderboards
│   └── community/      # Forums, sharing, swap meet
```

#### 2. Game Engine
```
src/
├── engine/
│   ├── renderer/       # WebGL rendering pipeline
│   ├── physics/        # Movement, collision detection
│   ├── track/          # Track generation and validation
│   ├── replay/         # Race replay system
│   └── validation/     # Input validation, anti-cheat
```

#### 3. ML Training Module
```
src/
├── ml/
│   ├── algorithms/
│   │   ├── genetic.ts      # Genetic algorithm implementation
│   │   ├── qlearning.ts    # Q-learning implementation
│   │   └── neat.ts         # NEAT (future enhancement)
│   ├── dna/
│   │   ├── schema.ts       # DNA structure definitions
│   │   ├── validator.ts    # Validate DNA configurations
│   │   └── encoder.ts      # Serialize/deserialize DNA
│   ├── sensors/
│   │   ├── distance.ts     # Distance sensors
│   │   ├── velocity.ts     # Speed sensors
│   │   └── position.ts     # Track position sensors
│   ├── training/
│   │   ├── environment.ts  # Training sandbox
│   │   ├── worker.ts       # Web Worker for background training
│   │   └── optimizer.ts    # Training optimization
│   └── evaluation/
│       ├── fitness.ts      # Fitness function calculations
│       └── metrics.ts      # Performance metrics
```

#### 4. Data Layer
```
src/
├── data/
│   ├── api/            # API client, endpoints
│   ├── local/          # IndexedDB for offline training
│   ├── sync/           # Data synchronization
│   └── cache/          # Client-side caching strategy
```

## 🔧 Backend Architecture

### Technology Stack
- **Runtime**: Node.js 20+ with TypeScript
- **Framework**: Express.js or Fastify
- **API**: RESTful + WebSocket for live races
- **Database**: PostgreSQL 15+
- **Cache**: Redis
- **Authentication**: Passport.js with OAuth providers
- **Validation**: Zod or Joi
- **ORM**: Prisma or TypeORM
- **Testing**: Jest + Supertest

### Microservices

#### 1. Authentication Service
- OAuth integration (Google, GitHub, Discord)
- JWT token management
- Session handling
- Role-based access control (RBAC)

#### 2. User Service
```
Features:
- User profile management
- Dot driver profile CRUD
- Dot vehicle profile CRUD
- Achievement tracking
- Skill level calculation
- Statistics aggregation
```

#### 3. Race Service
```
Features:
- Track management (CRUD)
- Race session creation
- Real-time race validation
- Leaderboard management
- Replay storage and retrieval
- Anti-cheat validation
```

#### 4. Tournament Service
```
Features:
- Tournament scheduling
- Bracket generation
- Ranking calculations
- Reward distribution
- Entry validation
- Results publication
```

#### 5. Training Service
```
Features:
- Training configuration validation
- Epoch limit enforcement
- DNA schema validation
- Training history storage
- Progress tracking
```

#### 6. Community Service
```
Features:
- Forum posts and comments
- Strategy sharing
- Swap meet event management
- Git integration for config sharing
- Voting and reputation system
```

## 💾 Database Schema Design

### Core Tables

#### Users
```sql
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    oauth_provider VARCHAR(50) NOT NULL,
    oauth_id VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    last_login TIMESTAMP,
    is_active BOOLEAN DEFAULT true
);
```

#### Dot Drivers (Player Profiles)
```sql
CREATE TABLE dot_drivers (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    display_name VARCHAR(100) NOT NULL,
    skill_level INTEGER DEFAULT 1,
    total_races INTEGER DEFAULT 0,
    total_wins INTEGER DEFAULT 0,
    total_podiums INTEGER DEFAULT 0,
    best_lap_time FLOAT,
    education_score INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

#### Dot Vehicles
```sql
CREATE TABLE dot_vehicles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    driver_id UUID REFERENCES dot_drivers(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    color_primary VARCHAR(7) DEFAULT '#0066FF',
    color_secondary VARCHAR(7) DEFAULT '#FF6600',
    pattern VARCHAR(50) DEFAULT 'solid',
    
    -- DNA Configuration (stored as JSONB for flexibility)
    dna_config JSONB NOT NULL,
    
    -- Performance Characteristics
    max_speed FLOAT DEFAULT 5.0,
    acceleration FLOAT DEFAULT 1.0,
    turning_radius FLOAT DEFAULT 45.0,
    
    -- Available Upgrades
    unlocked_sensors TEXT[] DEFAULT ARRAY['basic_distance'],
    unlocked_actions TEXT[] DEFAULT ARRAY['forward', 'turn'],
    unlocked_algorithms TEXT[] DEFAULT ARRAY['genetic'],
    
    -- Training Configuration
    max_epochs_per_day INTEGER DEFAULT 100,
    current_daily_epochs INTEGER DEFAULT 0,
    last_epoch_reset TIMESTAMP DEFAULT NOW(),
    
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

#### DNA Templates (Serialized Training Results)
```sql
CREATE TABLE dna_templates (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    vehicle_id UUID REFERENCES dot_vehicles(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    
    -- Serialized DNA (Brain/Q-Table)
    dna_data JSONB NOT NULL,
    algorithm_type VARCHAR(50) NOT NULL,
    
    -- Training Metadata
    training_epochs INTEGER NOT NULL,
    fitness_score FLOAT,
    training_track_id UUID,
    
    -- Performance Stats
    avg_lap_time FLOAT,
    success_rate FLOAT,
    
    -- Sharing
    is_public BOOLEAN DEFAULT false,
    fork_count INTEGER DEFAULT 0,
    vote_score INTEGER DEFAULT 0,
    
    created_at TIMESTAMP DEFAULT NOW()
);
```

#### Tracks
```sql
CREATE TABLE tracks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(100) NOT NULL,
    description TEXT,
    difficulty_level INTEGER NOT NULL,
    track_type VARCHAR(50) NOT NULL, -- 'drag', 'circuit', 'obstacle'
    
    -- Track Data (waypoints, obstacles, boundaries)
    track_data JSONB NOT NULL,
    
    -- Requirements
    min_skill_level INTEGER DEFAULT 1,
    required_sensors TEXT[],
    
    -- Stats
    best_time FLOAT,
    best_time_holder_id UUID REFERENCES dot_drivers(id),
    total_attempts INTEGER DEFAULT 0,
    
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT NOW()
);
```

#### Races
```sql
CREATE TABLE races (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    track_id UUID REFERENCES tracks(id),
    vehicle_id UUID REFERENCES dot_vehicles(id),
    dna_template_id UUID REFERENCES dna_templates(id),
    
    -- Race Results
    completion_time FLOAT,
    finished BOOLEAN DEFAULT false,
    race_position INTEGER,
    
    -- Race Data (for replay)
    race_data JSONB,
    
    -- Tournament Association
    tournament_id UUID,
    
    created_at TIMESTAMP DEFAULT NOW()
);
```

#### Tournaments
```sql
CREATE TABLE tournaments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(100) NOT NULL,
    description TEXT,
    
    -- Schedule
    registration_start TIMESTAMP NOT NULL,
    registration_end TIMESTAMP NOT NULL,
    tournament_start TIMESTAMP NOT NULL,
    tournament_end TIMESTAMP NOT NULL,
    
    -- Configuration
    track_id UUID REFERENCES tracks(id),
    min_skill_level INTEGER,
    max_skill_level INTEGER,
    vehicle_class TEXT[],
    max_participants INTEGER,
    
    -- Status
    status VARCHAR(50) DEFAULT 'upcoming', -- upcoming, registration, active, completed
    
    created_at TIMESTAMP DEFAULT NOW()
);
```

#### Upgrades
```sql
CREATE TABLE upgrades (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(100) NOT NULL,
    description TEXT,
    upgrade_type VARCHAR(50) NOT NULL, -- 'sensor', 'action', 'algorithm', 'performance'
    
    -- Upgrade Data
    upgrade_config JSONB NOT NULL,
    
    -- Cost and Requirements
    point_cost INTEGER NOT NULL,
    required_skill_level INTEGER DEFAULT 1,
    prerequisite_upgrades UUID[],
    
    is_active BOOLEAN DEFAULT true
);
```

#### User Upgrades (Inventory)
```sql
CREATE TABLE user_upgrades (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    driver_id UUID REFERENCES dot_drivers(id) ON DELETE CASCADE,
    upgrade_id UUID REFERENCES upgrades(id),
    vehicle_id UUID REFERENCES dot_vehicles(id),
    
    purchased_at TIMESTAMP DEFAULT NOW(),
    is_equipped BOOLEAN DEFAULT false,
    
    UNIQUE(vehicle_id, upgrade_id)
);
```

#### Points & Currency
```sql
CREATE TABLE driver_points (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    driver_id UUID REFERENCES dot_drivers(id) ON DELETE CASCADE,
    
    total_points INTEGER DEFAULT 0,
    available_points INTEGER DEFAULT 0,
    spent_points INTEGER DEFAULT 0,
    
    updated_at TIMESTAMP DEFAULT NOW()
);
```

### Indexes & Performance
```sql
-- User lookups
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_oauth ON users(oauth_provider, oauth_id);

-- Driver queries
CREATE INDEX idx_dot_drivers_user_id ON dot_drivers(user_id);
CREATE INDEX idx_dot_drivers_skill_level ON dot_drivers(skill_level);

-- Vehicle queries
CREATE INDEX idx_dot_vehicles_driver_id ON dot_vehicles(driver_id);

-- Race queries
CREATE INDEX idx_races_track_id ON races(track_id);
CREATE INDEX idx_races_vehicle_id ON races(vehicle_id);
CREATE INDEX idx_races_tournament_id ON races(tournament_id);

-- DNA template searches
CREATE INDEX idx_dna_templates_vehicle_id ON dna_templates(vehicle_id);
CREATE INDEX idx_dna_templates_public ON dna_templates(is_public) WHERE is_public = true;

-- Tournament queries
CREATE INDEX idx_tournaments_status ON tournaments(status);
CREATE INDEX idx_tournaments_dates ON tournaments(tournament_start, tournament_end);
```

## 🔄 Data Flow

### Training Flow
```
1. User configures training parameters (client)
2. Validate against vehicle limits (client)
3. Run training in Web Worker (client)
4. Save DNA to IndexedDB (client)
5. Sync to server on completion (client → server)
6. Update training history and stats (server)
```

### Racing Flow
```
1. User selects track and DNA template (client)
2. Validate compatibility (client)
3. Load track and DNA (client)
4. Execute race simulation (client)
5. Submit results to server (client → server)
6. Validate race data (server)
7. Update leaderboards and stats (server)
8. Award points and achievements (server)
```

### Tournament Flow
```
1. User registers for tournament (client → server)
2. Server validates eligibility (server)
3. Tournament starts, matches generated (server)
4. Participants receive race assignments (server → client)
5. Execute tournament races (server-side validation)
6. Aggregate results and rankings (server)
7. Distribute rewards (server)
```

## 🔐 Security Considerations

### Client-Side
- Input validation and sanitization
- DNA schema enforcement
- Rate limiting on API calls
- Secure token storage (httpOnly cookies)
- CSP headers to prevent XSS

### Server-Side
- OAuth token validation
- JWT with short expiration
- SQL injection prevention (parameterized queries)
- Rate limiting per user/IP
- Tournament race validation (server re-runs)
- Anti-cheat detection algorithms
- Encrypted sensitive data at rest

## 📡 API Design

### RESTful Endpoints
```
Auth:
POST   /api/v1/auth/login
POST   /api/v1/auth/logout
GET    /api/v1/auth/me

Users:
GET    /api/v1/users/:id
PATCH  /api/v1/users/:id

Drivers:
GET    /api/v1/drivers/:id
PATCH  /api/v1/drivers/:id
GET    /api/v1/drivers/:id/stats

Vehicles:
GET    /api/v1/vehicles/:id
POST   /api/v1/vehicles
PATCH  /api/v1/vehicles/:id
DELETE /api/v1/vehicles/:id

DNA:
GET    /api/v1/dna/:id
POST   /api/v1/dna
GET    /api/v1/dna/public
POST   /api/v1/dna/:id/fork

Tracks:
GET    /api/v1/tracks
GET    /api/v1/tracks/:id
GET    /api/v1/tracks/:id/leaderboard

Races:
POST   /api/v1/races
GET    /api/v1/races/:id
GET    /api/v1/races/:id/replay

Tournaments:
GET    /api/v1/tournaments
GET    /api/v1/tournaments/:id
POST   /api/v1/tournaments/:id/register
GET    /api/v1/tournaments/:id/bracket

Upgrades:
GET    /api/v1/upgrades
POST   /api/v1/upgrades/:id/purchase
POST   /api/v1/vehicles/:id/equip/:upgradeId
```

### WebSocket Events
```
Race Live Updates:
- race:start
- race:position
- race:complete

Tournament Events:
- tournament:bracket_update
- tournament:match_start
- tournament:results

Community:
- forum:new_post
- swapmeet:new_config
```

## 🚀 Deployment Strategy

### Development Environment
- Docker Compose for local services
- Hot reload for frontend and backend
- Local PostgreSQL and Redis instances

### Staging Environment
- AWS ECS or Kubernetes
- RDS for PostgreSQL
- ElastiCache for Redis
- CloudFront CDN for static assets

### Production Environment
- Multi-region deployment
- Load balancing
- Auto-scaling based on metrics
- Backup and disaster recovery
- Monitoring (Datadog, New Relic, or similar)

## 📊 Performance Targets
- Client-side training: 60 FPS during visualization
- Race rendering: 60 FPS
- API response time: < 200ms (p95)
- Page load time: < 2s
- WebSocket latency: < 100ms

---

*This architecture is designed to scale while keeping costs low by leveraging client-side computation for training.*
