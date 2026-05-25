"""
Dot Car Derby - Step 1: Drag Race Simulation
Based on the original Dot AI project, modified for racing gameplay.

This version features:
- Vertical drag strip track (bottom to top)
- Population of 50 dots with top 25 advancing
- Ranking system with visual indicators
- JSON configuration for future Firestore compatibility
"""

import pygame
import random
import math
import pickle
import os
import logging
import datetime
import json
from typing import List, Tuple, Dict, Any

# --- 📁 CONFIGURATION LOADING ---
def load_config(config_file: str = "race_config.json") -> Dict[str, Any]:
    """Load configuration from JSON file"""
    try:
        with open(config_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logging.error(f"Configuration file '{config_file}' not found!")
        raise
    except json.JSONDecodeError as e:
        logging.error(f"Error parsing configuration file: {e}")
        raise

def load_track_config(track_name: str = "drag_strip") -> Dict[str, Any]:
    """Load track configuration from tracks database file"""
    try:
        with open("tracks_database.json", 'r') as f:
            tracks_db = json.load(f)
        
        if track_name not in tracks_db['tracks']:
            raise ValueError(f"Track '{track_name}' not found in database")
        
        return tracks_db['tracks'][track_name]
    except FileNotFoundError:
        logging.error("tracks_database.json not found!")
        raise

def get_all_tracks() -> List[Dict[str, Any]]:
    """Get list of all available tracks"""
    try:
        with open("tracks_database.json", 'r') as f:
            tracks_db = json.load(f)
        return [
            {**tracks_db['tracks'][track_id], 'track_id': track_id}
            for track_id in tracks_db.get('track_order', [])
        ]
    except FileNotFoundError:
        logging.error("tracks_database.json not found!")
        return []

# Load configuration
CONFIG = load_config()
TRACK_CONFIG = load_track_config(CONFIG.get('current_track', 'drag_strip'))

# Extract settings from config
TRACK = CONFIG['track_settings']
DOT_CFG = CONFIG['dot_settings']
DISPLAY = CONFIG['display_settings']
SIM_CFG = CONFIG['simulation_settings']

# --- 🎮 CORE SETTINGS (from config) ---
WIDTH, HEIGHT = TRACK['width'], TRACK['height']
POPULATION_SIZE = DOT_CFG['population_size']
ADVANCEMENT_COUNT = DOT_CFG['advancement_count']
MAX_VELOCITY = DOT_CFG['max_velocity']
BRAIN_SIZE = DOT_CFG['brain_size']
MUTATION_RATE = DOT_CFG['mutation_rate']

# Track geometry (from track config)
START_POS = TRACK_CONFIG['start_position']
FINISH_POS = TRACK_CONFIG['finish_position']

# Colors (converted from config lists to tuples)
SCREEN_COLOR = tuple(DISPLAY['screen_color'])
TRACK_COLOR = tuple(TRACK['track_color'])
BARRIER_COLOR = tuple(TRACK['barrier_color'])
START_LINE_COLOR = tuple(TRACK['start_line_color'])
FINISH_LINE_COLOR = tuple(TRACK['finish_line_color'])
CENTER_LINE_COLOR = tuple(TRACK['center_line_color'])
ELIMINATED_COLOR = tuple(DOT_CFG['eliminated_dot_color'])
FONT_COLOR = tuple(DISPLAY['font_color'])

# --- 🌈 COLOR GRADIENT SYSTEM ---
def get_gradient_color(progress: float) -> Tuple[int, int, int]:
    """Get ROYGBIV gradient color based on progress (0.0 = red/slow, 1.0 = violet/fast)"""
    # Clamp progress between 0 and 1
    progress = max(0.0, min(1.0, progress))
    
    # ROYGBIV gradient points (Red -> Orange -> Yellow -> Green -> Blue -> Indigo -> Violet)
    colors = [
        (255, 0, 0),      # Red (0.0 - slowest)
        (255, 127, 0),    # Orange (0.166)
        (255, 255, 0),    # Yellow (0.333)
        (0, 255, 0),      # Green (0.5)
        (0, 127, 255),    # Cyan/Blue (0.666)
        (75, 0, 130),     # Indigo (0.833)
        (200, 0, 255)     # Violet (1.0 - fastest/podium)
    ]
    
    # Find which two colors to interpolate between
    num_segments = len(colors) - 1
    segment = progress * num_segments
    idx = int(segment)
    
    if idx >= num_segments:
        return colors[-1]  # Return violet for 1.0
    
    # Interpolate between the two colors
    t = segment - idx
    c1 = colors[idx]
    c2 = colors[idx + 1]
    
    r = int(c1[0] + (c2[0] - c1[0]) * t)
    g = int(c1[1] + (c2[1] - c1[1]) * t)
    b = int(c1[2] + (c2[2] - c1[2]) * t)
    
    return (r, g, b)

# --- 📝 LOGGING SETUP ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
log = logging.getLogger('dot_racer')

# Create save directory
os.makedirs(SIM_CFG['save_directory'], exist_ok=True)
log.info(f"Save directory '{SIM_CFG['save_directory']}' is ready.")

# --- 🧠 BRAIN CLASS ---
class Brain:
    """The 'DNA' of a racing dot - its movement instructions"""
    
    def __init__(self, size: int):
        self.size = size
        self.directions: List[Tuple[float, float]] = [self.random_vector() for _ in range(size)]
        self.step: int = 0

    def random_vector(self) -> Tuple[float, float]:
        """Generate a random direction vector"""
        angle = random.uniform(0, 2 * math.pi)
        return (math.cos(angle), math.sin(angle))

    def clone(self) -> 'Brain':
        """Create a copy of this brain"""
        cloned_brain = Brain(self.size)
        cloned_brain.directions = self.directions[:]
        return cloned_brain

    def mutate(self):
        """Apply random mutations to the brain"""
        for i in range(len(self.directions)):
            if random.random() < MUTATION_RATE:
                self.directions[i] = self.random_vector()

# --- 🏎️ DOT CLASS (Racing Car) ---
class RacingDot:
    """A racing dot competing in the drag race"""
    
    def __init__(self, dot_id: int):
        self.id = dot_id
        
        # Starting position from track config
        start_x = START_POS['x'] + random.uniform(-20, 20)
        start_y = START_POS['y'] + random.uniform(-5, 5)
        self.pos: List[float] = [float(start_x), float(start_y)]
        
        self.vel: List[float] = [0.0, 0.0]
        self.acc: List[float] = [0.0, 0.0]
        
        # Racing state
        self.dead: bool = False
        self.finished: bool = False
        self.finish_time: int = 0  # Frame count when finished
        self.fitness: float = 0.0
        self.rank: int = 0  # Current rank (1 = first place)
        self.is_eliminated: bool = False
        
        # AI brain
        self.brain: Brain = Brain(BRAIN_SIZE)
        
    def move(self, current_frame: int):
        """Update position based on brain instructions"""
        if self.dead or self.finished:
            return
            
        # Get instruction from brain
        if self.brain.step < len(self.brain.directions):
            self.acc = list(self.brain.directions[self.brain.step])
            self.brain.step += 1
        else:
            self.dead = True
            return
        
        # Update velocity
        self.vel[0] += self.acc[0]
        self.vel[1] += self.acc[1]
        
        # Limit velocity
        speed_sq = self.vel[0]**2 + self.vel[1]**2
        if speed_sq > MAX_VELOCITY**2:
            speed = math.sqrt(speed_sq)
            self.vel[0] = (self.vel[0] / speed) * MAX_VELOCITY
            self.vel[1] = (self.vel[1] / speed) * MAX_VELOCITY
        
        # Update position
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
        # Check boundaries - collision with barriers
        if self.check_barrier_collision():
            self.dead = True
            return
        
        # Check if finished (reached finish position)
        if self.check_finish():
            self.finished = True
            self.finish_time = current_frame
            log.info(f"Dot #{self.id} finished at frame {current_frame}!")
    
    def check_barrier_collision(self) -> bool:
        """Check if dot collided with any barrier or screen boundaries"""
        # Check screen boundaries first
        if self.pos[0] < 0 or self.pos[0] > WIDTH or self.pos[1] < 0 or self.pos[1] > HEIGHT:
            return True
        
        # Check configured barriers
        for barrier in TRACK_CONFIG['barriers']:
            if barrier['type'] == 'rect':
                x, y, w, h = barrier['x'], barrier['y'], barrier['width'], barrier['height']
                if x <= self.pos[0] <= x + w and y <= self.pos[1] <= y + h:
                    return True
            elif barrier['type'] == 'circle':
                cx, cy, r = barrier['x'], barrier['y'], barrier['radius']
                dist_sq = (self.pos[0] - cx)**2 + (self.pos[1] - cy)**2
                if dist_sq <= r**2:
                    return True
        return False
    
    def check_finish(self) -> bool:
        """Check if dot reached the finish zone"""
        finish = TRACK_CONFIG['finish_zone']
        if finish['type'] == 'line':
            # Check if crossed the line (y-coordinate)
            if finish['direction'] == 'horizontal':
                return self.pos[1] <= finish['position']
            else:  # vertical
                return self.pos[0] >= finish['position']
        elif finish['type'] == 'rect':
            x, y, w, h = finish['x'], finish['y'], finish['width'], finish['height']
            return x <= self.pos[0] <= x + w and y <= self.pos[1] <= y + h
        return False
    
    def get_distance_from_start(self) -> float:
        """Calculate distance traveled from start position"""
        dx = self.pos[0] - START_POS['x']
        dy = self.pos[1] - START_POS['y']
        return math.sqrt(dx*dx + dy*dy)
    
    def calculate_fitness(self):
        """Calculate racing fitness score"""
        if self.finished:
            # Finished: reward based on speed (fewer steps = better)
            time_bonus = 100000.0 / (self.finish_time + 1)
            self.fitness = 10000.0 + time_bonus
        else:
            # Didn't finish: reward based on distance traveled
            distance = self.get_distance_from_start()
            self.fitness = distance * 10.0
            
            # Penalty for dying early
            if self.dead:
                self.fitness *= 0.5
    
    def clone(self) -> 'RacingDot':
        """Create offspring with same brain"""
        new_dot = RacingDot(self.id)
        new_dot.brain = self.brain.clone()
        return new_dot
    
    def reset(self):
        """Reset for new race"""
        start_x = START_POS['x'] + random.uniform(-20, 20)
        start_y = START_POS['y'] + random.uniform(-5, 5)
        self.pos = [float(start_x), float(start_y)]
        self.vel = [0.0, 0.0]
        self.acc = [0.0, 0.0]
        self.dead = False
        self.finished = False
        self.finish_time = 0
        self.brain.step = 0

# --- 🏁 RACING POPULATION ---
class RacingPopulation:
    """Manages the racing population with ranking and elimination"""
    
    def __init__(self, size: int):
        self.population_size = size
        self.dots: List[RacingDot] = [RacingDot(i) for i in range(size)]
        self.generation: int = 1
        self.current_frame: int = 0
        self.champion: RacingDot = None
        
        # Performance tracking
        self.best_time: int = float('inf')
        self.generation_stats: Dict[str, Any] = {}
    
    def update(self):
        """Update all dots for one frame"""
        self.current_frame += 1
        
        for dot in self.dots:
            if not dot.is_eliminated:
                dot.move(self.current_frame)
    
    def all_done(self) -> bool:
        """Check if generation is complete"""
        active_dots = [d for d in self.dots if not d.is_eliminated]
        return all(d.dead or d.finished for d in active_dots)
    
    def calculate_fitness_and_rank(self):
        """Calculate fitness and assign rankings"""
        # Calculate fitness for all dots
        for dot in self.dots:
            dot.calculate_fitness()
        
        # Sort by fitness (highest first)
        sorted_dots = sorted(self.dots, key=lambda d: d.fitness, reverse=True)
        
        # Assign ranks
        for rank, dot in enumerate(sorted_dots, start=1):
            dot.rank = rank
        
        # Update champion
        self.champion = sorted_dots[0]
        if self.champion.finished and self.champion.finish_time < self.best_time:
            self.best_time = self.champion.finish_time
        
        # Mark eliminated dots (below advancement count)
        for dot in sorted_dots[ADVANCEMENT_COUNT:]:
            dot.is_eliminated = True
        
        # Store stats
        finishers = [d for d in self.dots if d.finished]
        self.generation_stats = {
            'generation': self.generation,
            'champion_fitness': self.champion.fitness,
            'champion_finished': self.champion.finished,
            'champion_time': self.champion.finish_time if self.champion.finished else None,
            'total_finishers': len(finishers),
            'best_all_time': self.best_time if self.best_time != float('inf') else None,
            'avg_fitness': sum(d.fitness for d in self.dots) / len(self.dots)
        }
        
        log.info(f"Generation {self.generation} complete!")
        log.info(f"  Champion Fitness: {self.champion.fitness:.2f}")
        log.info(f"  Finishers: {len(finishers)}/{self.population_size}")
        log.info(f"  Average Fitness: {self.generation_stats['avg_fitness']:.2f}")
    
    def evolve(self):
        """Create next generation from top performers"""
        # Sort by fitness
        sorted_dots = sorted(self.dots, key=lambda d: d.fitness, reverse=True)
        
        new_generation: List[RacingDot] = []
        
        # Elite: Keep champion
        champion_clone = sorted_dots[0].clone()
        champion_clone.id = 0
        new_generation.append(champion_clone)
        
        # Fill remaining slots from top performers
        top_performers = sorted_dots[:ADVANCEMENT_COUNT]
        
        for i in range(1, self.population_size):
            # Select parent from top performers
            parent = random.choice(top_performers)
            child = parent.clone()
            child.id = i
            child.brain.mutate()  # Mutate except champion
            new_generation.append(child)
        
        self.dots = new_generation
        self.generation += 1
        self.current_frame = 0
        
        # Reset all dots for new race
        for dot in self.dots:
            dot.reset()
            dot.is_eliminated = False
        
        log.info(f"Evolved to generation {self.generation}")
    
    def save(self):
        """Save population state"""
        timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        filename = os.path.join(
            SIM_CFG['save_directory'],
            f"drag_race_gen{self.generation}_{timestamp}.pkl"
        )
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
            log.info(f"Saved to {filename}")
        except Exception as e:
            log.error(f"Save failed: {e}")

# --- 🎨 RENDERING ---
def draw_track(screen: pygame.Surface):
    """Draw track based on configuration data"""
    # Draw track surface
    for surface in TRACK_CONFIG.get('surfaces', []):
        if surface['type'] == 'rect':
            rect = pygame.Rect(surface['x'], surface['y'], surface['width'], surface['height'])
            pygame.draw.rect(screen, tuple(surface['color']), rect)
        elif surface['type'] == 'circle':
            pygame.draw.circle(screen, tuple(surface['color']), 
                             (surface['x'], surface['y']), surface['radius'])
    
    # Draw barriers (dead zones)
    for barrier in TRACK_CONFIG.get('barriers', []):
        if barrier['type'] == 'rect':
            rect = pygame.Rect(barrier['x'], barrier['y'], barrier['width'], barrier['height'])
            pygame.draw.rect(screen, BARRIER_COLOR, rect)
        elif barrier['type'] == 'circle':
            pygame.draw.circle(screen, BARRIER_COLOR,
                             (barrier['x'], barrier['y']), barrier['radius'])
    
    # Draw decorative lines
    for line in TRACK_CONFIG.get('decorative_lines', []):
        # Check if it's a circle (for oval tracks)
        if line.get('is_circle', False):
            # Draw dashed circle
            if line.get('dashed', False):
                cx, cy = line['center']
                radius = line['radius']
                num_segments = 60
                dash_on = True
                
                for i in range(num_segments):
                    if dash_on:
                        angle1 = (i / num_segments) * 2 * math.pi
                        angle2 = ((i + 0.5) / num_segments) * 2 * math.pi
                        x1 = cx + radius * math.cos(angle1)
                        y1 = cy + radius * math.sin(angle1)
                        x2 = cx + radius * math.cos(angle2)
                        y2 = cy + radius * math.sin(angle2)
                        pygame.draw.line(screen, tuple(line['color']),
                                       (int(x1), int(y1)), (int(x2), int(y2)), line.get('width', 2))
                    dash_on = not dash_on
            else:
                # Solid circle
                pygame.draw.circle(screen, tuple(line['color']),
                                 tuple(line['center']), line['radius'], line.get('width', 2))
            continue
        
        if line.get('dashed', False):
            # Draw dashed line
            dash_length = line.get('dash_length', 20)
            gap_length = line.get('gap_length', 10)
            x1, y1 = line['start']
            x2, y2 = line['end']
            
            # Calculate line length and direction
            dx = x2 - x1
            dy = y2 - y1
            length = math.sqrt(dx*dx + dy*dy)
            
            if length > 0:
                dx_norm = dx / length
                dy_norm = dy / length
                
                current = 0
                while current < length:
                    next_dash = min(current + dash_length, length)
                    start_x = x1 + dx_norm * current
                    start_y = y1 + dy_norm * current
                    end_x = x1 + dx_norm * next_dash
                    end_y = y1 + dy_norm * next_dash
                    pygame.draw.line(screen, tuple(line['color']),
                                   (start_x, start_y), (end_x, end_y), line.get('width', 2))
                    current += dash_length + gap_length
        else:
            # Draw solid line
            pygame.draw.line(screen, tuple(line['color']),
                           tuple(line['start']), tuple(line['end']), line.get('width', 2))
    
    # Draw start marker
    start = TRACK_CONFIG['start_marker']
    if start['type'] == 'line':
        pygame.draw.line(screen, START_LINE_COLOR,
                       tuple(start['start']), tuple(start['end']), start.get('width', 3))
    
    # Draw finish marker  
    finish = TRACK_CONFIG['finish_marker']
    if finish['type'] == 'line':
        pygame.draw.line(screen, FINISH_LINE_COLOR,
                       tuple(finish['start']), tuple(finish['end']), finish.get('width', 5))

def draw_dots(screen: pygame.Surface, population: RacingPopulation):
    """Draw all racing dots with ROYGBIV gradient based on distance"""
    # Calculate max distance for normalization
    max_distance = max(dot.get_distance_from_start() for dot in population.dots) if population.dots else 1.0
    
    for dot in population.dots:
        # Skip eliminated dots if configured
        if dot.is_eliminated and not DISPLAY['show_eliminated']:
            continue
        
        # Determine color based on distance (gradient: red=slow, violet=fast)
        if dot.is_eliminated:
            color = ELIMINATED_COLOR
            size = 2
        else:
            # Calculate progress (0.0 to 1.0)
            distance = dot.get_distance_from_start()
            progress = distance / max_distance if max_distance > 0 else 0.0
            
            # Get gradient color
            color = get_gradient_color(progress)
            
            # Size based on whether finished
            if dot.finished:
                size = DOT_CFG['dot_size'] + 2
            else:
                size = DOT_CFG['dot_size']
        
        # Draw dot
        pygame.draw.circle(screen, color, (int(dot.pos[0]), int(dot.pos[1])), size)

def draw_track_menu(screen: pygame.Surface, all_tracks: List[Dict], current_track_id: str, font: pygame.font.Font):
    """Draw track selection menu at the bottom"""
    menu_y = HEIGHT - 80
    menu_x = 10
    small_font = pygame.font.SysFont(None, 16)
    
    # Title
    title = small_font.render("Tracks: ", True, FONT_COLOR)
    screen.blit(title, (menu_x, menu_y))
    menu_x += 50
    
    # Track buttons
    for i, track in enumerate(all_tracks, 1):
        track_id = track['track_id']
        is_current = track_id == current_track_id
        
        # Color based on difficulty and selection
        if is_current:
            color = (200, 0, 255)  # Violet for current track
        elif track['difficulty'] == 'easy':
            color = (0, 255, 0)
        elif track['difficulty'] == 'medium':
            color = (255, 255, 0)
        elif track['difficulty'] == 'hard':
            color = (255, 127, 0)
        else:  # extreme
            color = (255, 0, 0)
        
        # Track number and name
        text = f"{i}:{track['name'][:8]}"
        rendered = small_font.render(text, True, color)
        screen.blit(rendered, (menu_x, menu_y))
        menu_x += 95

def draw_hud(screen: pygame.Surface, population: RacingPopulation, font: pygame.font.Font):
    """Draw heads-up display with race information"""
    y_offset = 10
    spacing = 22
    
    # Race info
    info_lines = [
        f"Track: {TRACK_CONFIG['name']}",
        f"Generation: {population.generation}",
        f"Frame: {population.current_frame}",
        f"Best Time: {population.best_time if population.best_time != float('inf') else 'N/A'}",
        "",
        f"Active Racers: {sum(1 for d in population.dots if not d.is_eliminated)}/{population.population_size}",
        f"Finished: {sum(1 for d in population.dots if d.finished)}",
        f"Crashed: {sum(1 for d in population.dots if d.dead and not d.finished)}",
    ]
    
    for i, line in enumerate(info_lines):
        if line:  # Skip empty lines
            text = font.render(line, True, FONT_COLOR)
            screen.blit(text, (10, y_offset + i * spacing))
    
    # Rankings (top 5)
    if DISPLAY['show_rankings'] and population.champion:
        rank_y = 10
        rank_x = WIDTH - 200
        
        title = font.render("Top 5 Racers", True, (200, 0, 255))  # Violet for title
        screen.blit(title, (rank_x, rank_y))
        rank_y += spacing
        
        sorted_dots = sorted(population.dots, key=lambda d: d.rank)[:5]
        for dot in sorted_dots:
            status = "✓" if dot.finished else ("X" if dot.dead else "•")
            rank_text = f"{dot.rank}. Car #{dot.id} {status}"
            # Get color based on dot's distance
            max_distance = max(d.get_distance_from_start() for d in population.dots) if population.dots else 1.0
            progress = dot.get_distance_from_start() / max_distance if max_distance > 0 else 0.0
            color = get_gradient_color(progress)
            text = font.render(rank_text, True, color)
            screen.blit(text, (rank_x, rank_y))
            rank_y += spacing - 2
    
    # Controls help (bottom)
    controls = [
        "ESC: Exit | S: Save | SPACE: Next Gen | 1-6: Switch Track"
    ]
    help_font = pygame.font.SysFont(None, 16)
    for i, line in enumerate(controls):
        text = help_font.render(line, True, FONT_COLOR)
        screen.blit(text, (10, HEIGHT - 25 + i * 18))

# --- 🎮 MAIN GAME LOOP ---
def reload_track(track_name: str):
    """Reload configuration with new track"""
    global TRACK_CONFIG, START_POS, FINISH_POS
    TRACK_CONFIG = load_track_config(track_name)
    START_POS = TRACK_CONFIG['start_position']
    FINISH_POS = TRACK_CONFIG['finish_position']
    
    # Update config file
    CONFIG['current_track'] = track_name
    with open('race_config.json', 'w') as f:
        json.dump(CONFIG, f, indent=2)
    
    log.info(f"Track switched to: {TRACK_CONFIG['name']}")

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(f"Dot Car Derby - {TRACK_CONFIG['name']}")
    
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, DISPLAY['font_size'])
    
    # Load all tracks for menu
    all_tracks = get_all_tracks()
    current_track_id = CONFIG.get('current_track', 'drag_strip')
    
    # Create population
    population = RacingPopulation(POPULATION_SIZE)
    log.info(f"Race initialized: {POPULATION_SIZE} dots on {TRACK_CONFIG['name']}")
    
    running = True
    paused = False
    
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                population.save()
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    population.save()
                    running = False
                elif event.key == pygame.K_s:
                    population.save()
                elif event.key == pygame.K_SPACE:
                    # Force next generation
                    if not paused:
                        population.calculate_fitness_and_rank()
                        population.evolve()
                elif event.key == pygame.K_p:
                    paused = not paused
                    log.info(f"Simulation {'paused' if paused else 'resumed'}")
                elif event.key == pygame.K_1:
                    reload_track('drag_strip')
                    current_track_id = 'drag_strip'
                    population = RacingPopulation(POPULATION_SIZE)
                    pygame.display.set_caption(f"Dot Car Derby - {TRACK_CONFIG['name']}")
                elif event.key == pygame.K_2:
                    reload_track('oval_99')
                    current_track_id = 'oval_99'
                    population = RacingPopulation(POPULATION_SIZE)
                    pygame.display.set_caption(f"Dot Car Derby - {TRACK_CONFIG['name']}")
                elif event.key == pygame.K_3:
                    reload_track('rally_course')
                    current_track_id = 'rally_course'
                    population = RacingPopulation(POPULATION_SIZE)
                    pygame.display.set_caption(f"Dot Car Derby - {TRACK_CONFIG['name']}")
                elif event.key == pygame.K_4:
                    reload_track('daytona_oval')
                    current_track_id = 'daytona_oval'
                    population = RacingPopulation(POPULATION_SIZE)
                    pygame.display.set_caption(f"Dot Car Derby - {TRACK_CONFIG['name']}")
                elif event.key == pygame.K_5:
                    reload_track('indy_circuit')
                    current_track_id = 'indy_circuit'
                    population = RacingPopulation(POPULATION_SIZE)
                    pygame.display.set_caption(f"Dot Car Derby - {TRACK_CONFIG['name']}")
                elif event.key == pygame.K_6:
                    reload_track('maniac_mayhem')
                    current_track_id = 'maniac_mayhem'
                    population = RacingPopulation(POPULATION_SIZE)
                    pygame.display.set_caption(f"Dot Car Derby - {TRACK_CONFIG['name']}")
        
        # Update
        if not paused:
            population.update()
            
            # Check if generation complete
            if population.all_done():
                population.calculate_fitness_and_rank()
                
                # Auto-save
                if population.generation % SIM_CFG['auto_save_frequency'] == 0:
                    population.save()
                
                # Evolve to next generation
                population.evolve()
        
        # Render
        screen.fill(SCREEN_COLOR)
        draw_track(screen)
        draw_dots(screen, population)
        draw_hud(screen, population, font)
        draw_track_menu(screen, all_tracks, current_track_id, font)
        
        pygame.display.flip()
        clock.tick(DISPLAY['fps'])
    
    pygame.quit()
    log.info("Simulation ended")

if __name__ == "__main__":
    main()
