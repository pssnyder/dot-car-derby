# Architecture Refactoring Plan
**Separating Car, Driver, Training, and Simulation**

**Date**: May 16, 2026  
**Status**: Planning Phase

---

## 🎯 Objectives

Split the monolithic `dot_ai_car.py` into modular components:

1. **Car (Vehicle)** - Physical entity that moves through space
2. **Driver (Brain/AI)** - Intelligence that controls the car
3. **Training Mode** - Genetic algorithm evolution
4. **Simulation/Replay Mode** - Run pre-trained drivers
5. **User Configuration** - Individual user settings
6. **Runtime Engine** - Core simulation logic

---

## 📊 Current State Analysis

### Current File Structure
```
dot_ai_car.py (600+ lines)
├── Brain class (genetic DNA)
├── RacingDot class (car + driver combined)
├── RacingPopulation class (training logic)
├── Rendering functions
├── Main game loop
└── Configuration loading
```

### Problems with Current Design
- ❌ Car physics mixed with AI logic
- ❌ Training and replay code intermingled  
- ❌ No separation between user-specific and general code
- ❌ Hard to reuse components
- ❌ Difficult to test individual parts
- ❌ Can't easily swap AI algorithms

---

## 🏗️ Proposed Architecture

### Directory Structure
```
dot-car-derby/
├── engine/                    # Core simulation engine (general runtime)
│   ├── __init__.py
│   ├── vehicle.py            # Car physics and movement
│   ├── track.py              # Track loading and collision detection
│   ├── renderer.py           # Visualization engine
│   └── physics.py            # Physics constants and helpers
│
├── drivers/                   # AI driver implementations
│   ├── __init__.py
│   ├── base_driver.py        # Abstract base class for all drivers
│   ├── genetic_driver.py     # Genetic algorithm driver
│   ├── qlearning_driver.py   # Q-learning driver (future)
│   └── neat_driver.py        # NEAT driver (future)
│
├── training/                  # Training systems
│   ├── __init__.py
│   ├── genetic_trainer.py    # Genetic algorithm training
│   ├── population.py         # Population management
│   ├── fitness.py            # Fitness function evaluators
│   └── evolution.py          # Selection, crossover, mutation
│
├── simulation/                # Simulation/replay mode
│   ├── __init__.py
│   ├── race_simulator.py     # Run races with trained drivers
│   ├── replay_system.py      # Replay saved races
│   └── leaderboard.py        # Track rankings and stats
│
├── config/                    # Configuration management
│   ├── __init__.py
│   ├── user_config.py        # User-specific settings
│   ├── track_config.py       # Track configurations
│   └── driver_config.py      # Driver/AI configurations
│
├── data/                      # Data files
│   ├── tracks/
│   │   └── tracks_database.json
│   ├── trained_drivers/      # Saved driver DNA/models
│   │   ├── drag_strip_champion.pkl
│   │   ├── oval_expert.pkl
│   │   └── ...
│   └── user_profiles/        # User-specific data
│       └── ...
│
├── utils/                     # Utilities
│   ├── __init__.py
│   ├── logger.py
│   └── serialization.py
│
├── main.py                    # Entry point (training mode)
├── play.py                    # Entry point (simulation/replay mode)
├── race_config.json           # Global configuration
└── tracks_database.json       # Track database
```

---

## 🚗 Component Specifications

### 1. Vehicle (engine/vehicle.py)

**Purpose**: Pure physical entity with no intelligence

```python
class Vehicle:
    \"\"\"
    A racing vehicle with physics but no intelligence.
    Controlled by a Driver.
    \"\"\"
    
    def __init__(self, vehicle_id: int, start_position: Tuple[float, float]):
        self.id = vehicle_id
        self.position = list(start_position)
        self.velocity = [0.0, 0.0]
        self.acceleration = [0.0, 0.0]
        self.max_speed = 5.0
        
        # State
        self.crashed = False
        self.finished = False
        self.finish_time = 0
        
        # Stats
        self.distance_traveled = 0.0
        self.frames_alive = 0
        
    def apply_force(self, force: Tuple[float, float]):
        \"\"\"Apply a force vector to the vehicle\"\"\"
        pass
        
    def update_physics(self, dt: float = 1.0):
        \"\"\"Update position based on physics\"\"\"
        pass
        
    def get_state(self) -> Dict:
        \"\"\"Get current vehicle state for driver input\"\"\"
        return {
            'position': self.position,
            'velocity': self.velocity,
            'speed': self.get_speed(),
            'frames_alive': self.frames_alive
        }
        
    def reset(self, start_position: Tuple[float, float]):
        \"\"\"Reset vehicle to starting state\"\"\"
        pass
```

### 2. Driver (drivers/base_driver.py)

**Purpose**: Intelligence that controls a vehicle

```python
class BaseDriver(ABC):
    \"\"\"
    Abstract base class for all driver AI implementations.
    Receives vehicle state, returns control commands.
    \"\"\"
    
    def __init__(self, driver_id: str):
        self.id = driver_id
        self.type = "base"  # genetic, qlearning, neat, etc.
        
    @abstractmethod
    def get_action(self, vehicle_state: Dict, track_state: Dict) -> Tuple[float, float]:
        \"\"\"
        Given current state, return force vector to apply.
        
        Args:
            vehicle_state: Current vehicle state
            track_state: Current track information
            
        Returns:
            (force_x, force_y): Force vector to apply
        \"\"\"
        pass
        
    @abstractmethod
    def save(self, filepath: str):
        \"\"\"Save driver to file\"\"\"
        pass
        
    @abstractmethod
    def load(filepath: str) -> 'BaseDriver':
        \"\"\"Load driver from file\"\"\"
        pass
        
    @abstractmethod
    def clone(self) -> 'BaseDriver':
        \"\"\"Create a copy of this driver\"\"\"
        pass
```

### 3. Genetic Driver (drivers/genetic_driver.py)

```python
class GeneticDriver(BaseDriver):
    \"\"\"
    Driver controlled by genetic algorithm DNA.
    Uses pre-programmed sequence of movements.
    \"\"\"
    
    def __init__(self, driver_id: str, dna_length: int = 800):
        super().__init__(driver_id)
        self.type = "genetic"
        self.dna = self._generate_random_dna(dna_length)
        self.current_step = 0
        
    def get_action(self, vehicle_state: Dict, track_state: Dict) -> Tuple[float, float]:
        \"\"\"Return next action from DNA sequence\"\"\"
        if self.current_step < len(self.dna):
            action = self.dna[self.current_step]
            self.current_step += 1
            return action
        return (0.0, 0.0)  # No more actions
        
    def mutate(self, mutation_rate: float = 0.01):
        \"\"\"Apply random mutations to DNA\"\"\"
        pass
        
    def reset(self):
        \"\"\"Reset to beginning of DNA sequence\"\"\"
        self.current_step = 0
```

### 4. Race Simulator (simulation/race_simulator.py)

**Purpose**: Run races with any combination of drivers

```python
class RaceSimulator:
    \"\"\"
    Runs races with any drivers on any track.
    Decoupled from training logic.
    \"\"\"
    
    def __init__(self, track_config: Dict):
        self.track = Track(track_config)
        self.vehicles = []
        self.drivers = []
        
    def add_racer(self, driver: BaseDriver, vehicle: Vehicle = None):
        \"\"\"Add a racer (driver + vehicle pair)\"\"\"
        if vehicle is None:
            vehicle = Vehicle(len(self.vehicles), self.track.start_position)
        self.vehicles.append(vehicle)
        self.drivers.append(driver)
        
    def run_race(self, max_frames: int = 1000) -> RaceResults:
        \"\"\"
        Run a single race.
        Returns results but doesn't train.
        \"\"\"
        frame = 0
        while not self._race_finished() and frame < max_frames:
            for vehicle, driver in zip(self.vehicles, self.drivers):
                if not vehicle.crashed and not vehicle.finished:
                    # Get driver decision
                    action = driver.get_action(
                        vehicle.get_state(),
                        self.track.get_state()
                    )
                    
                    # Apply to vehicle
                    vehicle.apply_force(action)
                    vehicle.update_physics()
                    
                    # Check collisions
                    if self.track.check_collision(vehicle.position):
                        vehicle.crashed = True
                    elif self.track.check_finish(vehicle.position):
                        vehicle.finished = True
                        vehicle.finish_time = frame
            
            frame += 1
            
        return self._compile_results()
```

### 5. Genetic Trainer (training/genetic_trainer.py)

**Purpose**: Evolution and training logic separate from simulation

```python
class GeneticTrainer:
    \"\"\"
    Handles genetic algorithm training.
    Uses RaceSimulator to evaluate fitness.
    \"\"\"
    
    def __init__(self, track_config: Dict, population_size: int = 50):
        self.simulator = RaceSimulator(track_config)
        self.population = Population(population_size)
        self.generation = 1
        
    def train_generation(self) -> GenerationStats:
        \"\"\"Train one generation\"\"\"
        # 1. Create vehicles for all drivers
        for driver in self.population.drivers:
            vehicle = Vehicle(driver.id, self.simulator.track.start_position)
            self.simulator.add_racer(driver, vehicle)
            
        # 2. Run race
        results = self.simulator.run_race()
        
        # 3. Calculate fitness
        self.population.calculate_fitness(results)
        
        # 4. Evolve
        self.population.evolve()
        
        self.generation += 1
        return self._get_stats()
```

### 6. User Configuration (config/user_config.py)

**Purpose**: User-specific settings separate from runtime

```python
class UserConfig:
    \"\"\"
    User-specific configuration.
    Can be stored in Firestore for web app.
    \"\"\"
    
    def __init__(self, user_id: str):
        self.user_id = user_id
        
        # Display preferences
        self.preferred_theme = "dark"
        self.show_eliminated = True
        self.fps_limit = 60
        
        # Training preferences
        self.auto_save_frequency = 10
        self.population_size = 50
        self.advancement_count = 25
        
        # Driver library
        self.trained_drivers = {}  # track_id -> driver_filepath
        self.favorite_tracks = []
        
    def save(self, filepath: str = None):
        \"\"\"Save to JSON or Firestore\"\"\"
        pass
        
    @staticmethod
    def load(user_id: str) -> 'UserConfig':
        \"\"\"Load from JSON or Firestore\"\"\"
        pass
```

---

## 🔄 Migration Plan

### Phase 1: Extract Vehicle Class ✅
- [x] Create `engine/vehicle.py`
- [ ] Move physics logic from RacingDot
- [ ] Add unit tests

### Phase 2: Extract Driver System
- [ ] Create `drivers/base_driver.py`
- [ ] Create `drivers/genetic_driver.py`
- [ ] Move Brain class logic
- [ ] Add tests for drivers

### Phase 3: Separate Training from Simulation
- [ ] Create `simulation/race_simulator.py`
- [ ] Create `training/genetic_trainer.py`
- [ ] Refactor RacingPopulation
- [ ] Add tests

### Phase 4: Configuration Management
- [ ] Create `config/user_config.py`
- [ ] Create `config/track_config.py`
- [ ] Migrate existing configs
- [ ] Add config validation

### Phase 5: Create Entry Points
- [ ] `main.py` - Training mode
- [ ] `play.py` - Replay/simulation mode
- [ ] CLI arguments for mode selection

### Phase 6: Database Integration (Future)
- [ ] Firestore schema for user configs
- [ ] Firestore schema for trained drivers
- [ ] Cloud storage for race replays

---

## 🎮 Usage Examples

### Training Mode
```python
# main.py
from training.genetic_trainer import GeneticTrainer
from config.user_config import UserConfig
from config.track_config import load_track

user = UserConfig("user123")
track = load_track("drag_strip")
trainer = GeneticTrainer(track, user.population_size)

for gen in range(100):
    stats = trainer.train_generation()
    print(f"Gen {gen}: {stats.finishers} finished")
    
    if gen % 10 == 0:
        trainer.save_champion(f"champions/drag_strip_gen{gen}.pkl")
```

### Simulation/Replay Mode
```python
# play.py
from simulation.race_simulator import RaceSimulator
from drivers.genetic_driver import GeneticDriver
from config.track_config import load_track

track = load_track("drag_strip")
simulator = RaceSimulator(track)

# Load trained drivers
champion1 = GeneticDriver.load("champions/drag_strip_gen100.pkl")
champion2 = GeneticDriver.load("champions/drag_strip_gen200.pkl")

simulator.add_racer(champion1)
simulator.add_racer(champion2)

results = simulator.run_race()
print(f"Winner: {results.winner.id}")
```

### Web Application (Future)
```python
# User signs in, selects track
user_config = UserConfig.load_from_firestore(user_id)
track = load_track_from_firestore(selected_track_id)

# Load user's trained driver for this track
driver_path = user_config.trained_drivers.get(selected_track_id)
if driver_path:
    driver = GeneticDriver.load_from_cloud(driver_path)
else:
    # Start new training
    trainer = GeneticTrainer(track, user_config.population_size)
    driver = trainer.train(generations=50)
    driver.save_to_cloud(f"users/{user_id}/drivers/{selected_track_id}.pkl")

# Race against others
simulator = MultiplayerRaceSimulator(track)
simulator.add_racer(driver, user_id)
# ... add other players' drivers
```

---

## 📝 Benefits of New Architecture

### ✅ Separation of Concerns
- Car physics independent of AI
- Training separate from simulation
- User config separate from runtime code

### ✅ Reusability
- Same vehicle class for all driver types
- Swap AI algorithms without changing simulation
- Use same track system for training and replay

### ✅ Testability
- Unit test each component independently
- Mock dependencies easily
- Test drivers without graphics

### ✅ Scalability
- Easy to add new driver types (Q-learning, NEAT, RL)
- Easy to add new training methods
- Easy to add multiplayer features

### ✅ Web-Ready
- Clear separation for frontend/backend
- User configs map to Firestore
- Drivers can be stored in cloud

---

## 🚀 Next Steps

1. **Review this plan** - Get feedback and approval
2. **Start Phase 1** - Extract Vehicle class
3. **Write tests** - Establish testing framework
4. **Iterate** - Complete phases 2-5
5. **Deploy** - Integrate with web app

---

**Questions to Address:**

1. Should we support hot-swapping drivers during races?
2. How should we handle driver "upgrades" (user progression)?
3. Should vehicles have customizable properties (speed, handling)?
4. How to handle real-time multiplayer synchronization?
5. Should we support hybrid drivers (e.g., genetic + Q-learning)?
