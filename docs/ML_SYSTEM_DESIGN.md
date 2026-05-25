# Dot Car Derby - ML System Design

## 🧬 DNA System Architecture

The DNA system is the core of Dot Car Derby's ML implementation. Each dot's "brain" is encoded as DNA, which determines its behavior on the track.

---

## DNA Schema

### DNA Structure
```typescript
interface DotDNA {
  // Metadata
  id: string;
  version: string; // Schema version for migrations
  algorithmType: 'genetic' | 'qlearning' | 'neat' | 'dqn';
  
  // Configuration
  config: DNAConfig;
  
  // Trained Data
  brain: BrainData;
  
  // Performance Metadata
  metadata: DNAMetadata;
}

interface DNAConfig {
  // Available Sensors
  sensors: SensorConfig[];
  
  // Available Actions
  actions: ActionConfig[];
  
  // Training Parameters
  training: TrainingConfig;
  
  // Fitness Function
  fitness: FitnessConfig;
}

interface SensorConfig {
  type: 'distance' | 'velocity' | 'position' | 'acceleration' | 'angle' | 'checkpoint';
  id: string;
  enabled: boolean;
  parameters: Record<string, any>;
}

interface ActionConfig {
  type: 'forward' | 'backward' | 'turn_left' | 'turn_right' | 'brake' | 'boost';
  id: string;
  enabled: boolean;
  range: [number, number]; // Min/max values
}

interface TrainingConfig {
  algorithm: string;
  populationSize?: number; // For genetic
  mutationRate?: number; // For genetic
  learningRate?: number; // For RL
  discountFactor?: number; // For RL
  epsilon?: number; // For RL
  maxSteps: number;
  maxEpochs: number;
}

interface FitnessConfig {
  components: FitnessComponent[];
}

interface FitnessComponent {
  type: 'distance' | 'time' | 'crashes' | 'checkpoints' | 'speed';
  weight: number; // Importance multiplier
  params: Record<string, any>;
}

interface BrainData {
  // For Genetic Algorithm
  genes?: number[]; // Movement instructions
  
  // For Q-Learning
  qTable?: Record<string, Record<string, number>>;
  
  // For Neural Networks (NEAT, DQN)
  network?: NetworkStructure;
}

interface NetworkStructure {
  layers: Layer[];
  connections: Connection[];
  nodes: Node[];
}

interface DNAMetadata {
  trainingTime: number; // Seconds
  trainingEpochs: number;
  bestFitness: number;
  avgFitness: number;
  trackId: string;
  createdAt: Date;
  updatedAt: Date;
}
```

---

## Algorithms

### 1. Genetic Algorithm

#### Overview
Population-based evolution where dots with better performance pass their "genes" to the next generation.

#### Implementation
```typescript
class GeneticAlgorithm {
  population: Dot[];
  generation: number;
  bestDot: Dot | null;
  
  constructor(
    populationSize: number,
    mutationRate: number,
    brainSize: number
  ) {
    this.population = this.createPopulation(populationSize, brainSize);
    this.generation = 0;
  }
  
  createPopulation(size: number, brainSize: number): Dot[] {
    return Array.from({ length: size }, () => 
      new Dot(this.randomBrain(brainSize))
    );
  }
  
  randomBrain(size: number): number[] {
    return Array.from({ length: size }, () => 
      Math.random() * Math.PI * 2 // Random angle
    );
  }
  
  update(track: Track): void {
    // Update all dots
    this.population.forEach(dot => {
      if (!dot.isDead && !dot.reachedGoal) {
        dot.update(track);
      }
    });
    
    // Check if generation is complete
    if (this.isGenerationDone()) {
      this.evolve();
    }
  }
  
  isGenerationDone(): boolean {
    return this.population.every(dot => 
      dot.isDead || dot.reachedGoal
    );
  }
  
  evolve(): void {
    // Calculate fitness for all dots
    this.calculateFitness();
    
    // Find best dot
    this.bestDot = this.findBestDot();
    
    // Create new generation
    this.population = this.naturalSelection();
    
    this.generation++;
  }
  
  calculateFitness(): void {
    this.population.forEach(dot => {
      dot.calculateFitness();
    });
  }
  
  findBestDot(): Dot {
    return this.population.reduce((best, dot) => 
      dot.fitness > best.fitness ? dot : best
    );
  }
  
  naturalSelection(): Dot[] {
    const newPopulation: Dot[] = [];
    
    // Keep best dot (elitism)
    if (this.bestDot) {
      newPopulation.push(this.bestDot.clone());
    }
    
    // Fill rest with offspring
    while (newPopulation.length < this.population.length) {
      const parent = this.selectParent();
      const child = parent.clone();
      child.mutate(this.mutationRate);
      newPopulation.push(child);
    }
    
    return newPopulation;
  }
  
  selectParent(): Dot {
    // Fitness-proportionate selection (roulette wheel)
    const totalFitness = this.population.reduce(
      (sum, dot) => sum + dot.fitness, 0
    );
    
    let random = Math.random() * totalFitness;
    
    for (const dot of this.population) {
      random -= dot.fitness;
      if (random <= 0) {
        return dot;
      }
    }
    
    return this.population[this.population.length - 1];
  }
}
```

#### Fitness Function
```typescript
class Dot {
  fitness: number = 0;
  
  calculateFitness(): void {
    let fitness = 0;
    
    // Distance to goal component
    const distanceToGoal = this.getDistanceToGoal();
    const maxDistance = this.getMaxPossibleDistance();
    const distanceScore = (1 - distanceToGoal / maxDistance) * 1000;
    fitness += distanceScore;
    
    // Goal reached bonus
    if (this.reachedGoal) {
      fitness += 10000;
      
      // Time bonus (faster is better)
      const timeBonus = 10000 / this.brain.step;
      fitness += timeBonus;
    }
    
    // Penalty for crashes
    if (this.crashed) {
      fitness *= 0.5;
    }
    
    // Checkpoint bonuses
    fitness += this.checkpointsReached * 500;
    
    // Smooth driving bonus (less erratic movement)
    const smoothness = this.calculateSmoothness();
    fitness += smoothness * 100;
    
    this.fitness = Math.max(fitness, 1); // Ensure positive
  }
  
  calculateSmoothness(): number {
    // Measure variance in velocity changes
    // Lower variance = smoother = higher score
    const velocityChanges = this.velocityHistory
      .map((v, i, arr) => i > 0 ? Math.abs(v - arr[i-1]) : 0);
    
    const avgChange = velocityChanges.reduce((a, b) => a + b, 0) / velocityChanges.length;
    
    return 1 / (1 + avgChange); // Normalize
  }
}
```

---

### 2. Q-Learning (Reinforcement Learning)

#### Overview
Single agent learns optimal actions through trial and error with rewards and penalties.

#### Implementation
```typescript
class QLearningAgent {
  qTable: Map<string, Map<string, number>>;
  learningRate: number; // Alpha
  discountFactor: number; // Gamma
  epsilon: number; // Exploration rate
  
  constructor(config: QLearningConfig) {
    this.qTable = new Map();
    this.learningRate = config.learningRate;
    this.discountFactor = config.discountFactor;
    this.epsilon = config.epsilon;
  }
  
  getState(dot: Dot, track: Track): string {
    // Discretize continuous state into grid cells
    const gridX = Math.floor(dot.x / GRID_SIZE);
    const gridY = Math.floor(dot.y / GRID_SIZE);
    const velocity = Math.floor(dot.velocity.magnitude() / 2);
    const angle = Math.floor(dot.angle / (Math.PI / 4)); // 8 directions
    
    // Get sensor readings
    const sensors = dot.getSensorReadings(track)
      .map(r => Math.floor(r / 50)); // Discretize distances
    
    return `${gridX},${gridY},${velocity},${angle},${sensors.join(',')}`;
  }
  
  getAction(state: string): string {
    // Epsilon-greedy action selection
    if (Math.random() < this.epsilon) {
      // Explore: random action
      return this.randomAction();
    } else {
      // Exploit: best known action
      return this.getBestAction(state);
    }
  }
  
  getBestAction(state: string): string {
    const stateActions = this.qTable.get(state);
    
    if (!stateActions || stateActions.size === 0) {
      return this.randomAction();
    }
    
    let bestAction = '';
    let bestValue = -Infinity;
    
    stateActions.forEach((value, action) => {
      if (value > bestValue) {
        bestValue = value;
        bestAction = action;
      }
    });
    
    return bestAction || this.randomAction();
  }
  
  randomAction(): string {
    const actions = ['forward', 'turn_left', 'turn_right', 'brake'];
    return actions[Math.floor(Math.random() * actions.length)];
  }
  
  update(
    state: string,
    action: string,
    reward: number,
    nextState: string,
    done: boolean
  ): void {
    // Initialize state-action if not exists
    if (!this.qTable.has(state)) {
      this.qTable.set(state, new Map());
    }
    
    const stateActions = this.qTable.get(state)!;
    const currentQ = stateActions.get(action) || 0;
    
    // Calculate max Q-value for next state
    let maxNextQ = 0;
    if (!done && this.qTable.has(nextState)) {
      const nextStateActions = this.qTable.get(nextState)!;
      maxNextQ = Math.max(...Array.from(nextStateActions.values()));
    }
    
    // Q-learning update rule
    const newQ = currentQ + this.learningRate * (
      reward + this.discountFactor * maxNextQ - currentQ
    );
    
    stateActions.set(action, newQ);
  }
  
  getReward(dot: Dot, track: Track): number {
    let reward = 0;
    
    // Reached goal
    if (dot.reachedGoal) {
      return 1000;
    }
    
    // Crashed
    if (dot.crashed) {
      return -100;
    }
    
    // Progress toward goal
    const distanceToGoal = dot.getDistanceToGoal();
    const previousDistance = dot.previousDistanceToGoal || distanceToGoal;
    const progress = previousDistance - distanceToGoal;
    reward += progress * 2;
    
    // Checkpoint reached
    if (dot.justReachedCheckpoint) {
      reward += 50;
    }
    
    // Staying on track
    if (dot.isOnTrack(track)) {
      reward += 1;
    } else {
      reward -= 5;
    }
    
    // Speed bonus (encourage movement)
    reward += dot.velocity.magnitude() * 0.1;
    
    // Time penalty (encourage efficiency)
    reward -= 0.1;
    
    return reward;
  }
  
  decayEpsilon(episode: number, maxEpisodes: number): void {
    // Exponential decay
    const minEpsilon = 0.01;
    const decay = 0.995;
    this.epsilon = Math.max(
      minEpsilon,
      this.epsilon * decay
    );
  }
}
```

---

### 3. NEAT (NeuroEvolution of Augmenting Topologies)

#### Overview (Advanced Feature)
Evolves neural network topology along with weights. Starts with simple networks and complexifies over time.

```typescript
interface NEATConfig {
  inputNodes: number; // Sensor count
  outputNodes: number; // Action count
  populationSize: number;
  survivalThreshold: number;
  mutationRates: {
    addNode: number;
    addConnection: number;
    weightMutation: number;
    toggleConnection: number;
  };
}

// Simplified structure - full NEAT is complex
class NEATEvolution {
  species: Species[];
  innovation: number;
  
  evolve(): void {
    // 1. Evaluate all genomes
    // 2. Separate into species
    // 3. Calculate adjusted fitness
    // 4. Remove weakest genomes
    // 5. Breed within species
    // 6. Mutate offspring
  }
}
```

---

## Sensors

### Available Sensor Types

#### 1. Distance Sensor
```typescript
class DistanceSensor {
  angle: number; // Relative to dot's heading
  maxDistance: number;
  
  read(dot: Dot, track: Track): number {
    const ray = this.castRay(dot, track);
    return ray.distance / this.maxDistance; // Normalize 0-1
  }
  
  castRay(dot: Dot, track: Track): { distance: number, hit: Vector2 } {
    // Raycast from dot in sensor direction
    // Return distance to nearest obstacle/boundary
  }
}
```

**Unlock Progression**:
- Level 1: 1 forward sensor
- Level 2: +2 angled sensors (±30°)
- Level 3: +2 wide sensors (±60°)
- Level 4: +2 side sensors (±90°)
- Level 5: Rear sensor

#### 2. Velocity Sensor
```typescript
class VelocitySensor {
  read(dot: Dot): number {
    return dot.velocity.magnitude() / dot.maxSpeed; // 0-1
  }
}
```

#### 3. Position Sensor
```typescript
class PositionSensor {
  type: 'track_center' | 'goal' | 'checkpoint';
  
  read(dot: Dot, track: Track): number {
    // Returns distance/angle to target
    switch (this.type) {
      case 'track_center':
        return dot.distanceFromTrackCenter(track);
      case 'goal':
        return dot.getAngleToGoal();
      case 'checkpoint':
        return dot.getDistanceToNextCheckpoint(track);
    }
  }
}
```

#### 4. Acceleration Sensor
```typescript
class AccelerationSensor {
  read(dot: Dot): number {
    return dot.acceleration / dot.maxAcceleration;
  }
}
```

#### 5. Angle Sensor
```typescript
class AngleSensor {
  type: 'absolute' | 'relative_to_track' | 'relative_to_goal';
  
  read(dot: Dot, track: Track): number {
    // Returns normalized angle (-1 to 1)
  }
}
```

---

## Actions

### Available Actions

```typescript
interface Action {
  type: string;
  execute(dot: Dot, intensity: number): void;
}

class ForwardAction implements Action {
  type = 'forward';
  
  execute(dot: Dot, intensity: number): void {
    // intensity: 0 to 1
    dot.accelerate(intensity * dot.maxAcceleration);
  }
}

class TurnAction implements Action {
  type: 'turn';
  direction: 'left' | 'right';
  
  execute(dot: Dot, intensity: number): void {
    // intensity: 0 to 1
    const turnRate = intensity * dot.maxTurnRate;
    dot.rotate(this.direction === 'left' ? -turnRate : turnRate);
  }
}

class BrakeAction implements Action {
  type = 'brake';
  
  execute(dot: Dot, intensity: number): void {
    dot.decelerate(intensity * dot.brakePower);
  }
}

class BoostAction implements Action {
  type = 'boost';
  
  execute(dot: Dot, intensity: number): void {
    // Temporary speed boost (unlock required)
    if (dot.boostAvailable) {
      dot.applyBoost(intensity);
    }
  }
}
```

**Unlock Progression**:
- Level 1: Forward only (0-100%)
- Level 2: Basic turning (±15°)
- Level 3: Wider turning (±30°)
- Level 4: Brake action
- Level 5: Reverse (negative forward)
- Level 6: Boost action

---

## Training Environment

### Client-Side Training Architecture

```typescript
class TrainingEnvironment {
  worker: Worker;
  track: Track;
  algorithm: Algorithm;
  onProgress: (stats: TrainingStats) => void;
  
  async train(config: TrainingConfig): Promise<DotDNA> {
    // Run training in Web Worker to avoid blocking UI
    this.worker = new Worker('/training-worker.js');
    
    return new Promise((resolve, reject) => {
      this.worker.postMessage({
        type: 'start_training',
        config,
        track: this.track.serialize()
      });
      
      this.worker.onmessage = (e) => {
        switch (e.data.type) {
          case 'progress':
            this.onProgress(e.data.stats);
            break;
          case 'complete':
            resolve(e.data.dna);
            break;
          case 'error':
            reject(e.data.error);
            break;
        }
      };
    });
  }
  
  visualize(): void {
    // Real-time visualization during training
    // Show best dot, fitness graph, generation count
  }
}
```

### Web Worker Training
```typescript
// training-worker.ts
self.onmessage = (e) => {
  const { config, track } = e.data;
  
  const algorithm = createAlgorithm(config);
  const trackInstance = Track.deserialize(track);
  
  for (let epoch = 0; epoch < config.maxEpochs; epoch++) {
    // Run one epoch
    algorithm.runEpoch(trackInstance);
    
    // Report progress every 10 epochs
    if (epoch % 10 === 0) {
      self.postMessage({
        type: 'progress',
        stats: {
          epoch,
          bestFitness: algorithm.getBestFitness(),
          avgFitness: algorithm.getAvgFitness(),
          generationTime: algorithm.getGenerationTime()
        }
      });
    }
  }
  
  // Training complete
  self.postMessage({
    type: 'complete',
    dna: algorithm.getBestDNA()
  });
};
```

---

## Performance Optimization

### Training Speed
- Run physics at reduced accuracy during training (speed over precision)
- Use simplified collision detection
- Batch update operations
- Early termination for failed dots

### Memory Management
- Limit Q-table size (prune rarely-used states)
- Compress DNA before storage
- Use typed arrays for numerical data
- Clean up dead dots immediately

### Parallel Processing
- Evaluate population dots in parallel (genetic algorithm)
- Use SharedArrayBuffer for multi-threaded physics (advanced)
- Distribute tournament races across clients

---

## Validation & Anti-Cheat

### DNA Validation
```typescript
function validateDNA(dna: DotDNA, vehicle: DotVehicle): ValidationResult {
  // 1. Check schema version
  if (!isSupportedVersion(dna.version)) {
    return { valid: false, reason: 'Unsupported DNA version' };
  }
  
  // 2. Verify sensors match vehicle
  const allowedSensors = vehicle.unlocked_sensors;
  for (const sensor of dna.config.sensors) {
    if (!allowedSensors.includes(sensor.type)) {
      return { valid: false, reason: `Unauthorized sensor: ${sensor.type}` };
    }
  }
  
  // 3. Verify actions match vehicle
  const allowedActions = vehicle.unlocked_actions;
  for (const action of dna.config.actions) {
    if (!allowedActions.includes(action.type)) {
      return { valid: false, reason: `Unauthorized action: ${action.type}` };
    }
  }
  
  // 4. Check training parameters are within limits
  if (dna.metadata.trainingEpochs > vehicle.max_epochs_per_day) {
    return { valid: false, reason: 'Exceeds epoch limit' };
  }
  
  // 5. Validate brain data structure
  if (!isValidBrainData(dna.brain, dna.algorithmType)) {
    return { valid: false, reason: 'Invalid brain data' };
  }
  
  return { valid: true };
}
```

### Tournament Race Validation
```typescript
async function validateTournamentRace(
  raceResult: RaceResult,
  dna: DotDNA,
  track: Track
): Promise<boolean> {
  // Server re-runs the race with submitted DNA
  const serverRace = new RaceSimulation(track, dna);
  const serverResult = await serverRace.run();
  
  // Allow small variance due to floating-point differences
  const tolerance = 0.01; // 1% difference allowed
  
  const timeDiff = Math.abs(serverResult.time - raceResult.time);
  const timeMatch = timeDiff / raceResult.time < tolerance;
  
  // Check path similarity
  const pathSimilarity = calculatePathSimilarity(
    serverResult.path,
    raceResult.path
  );
  
  return timeMatch && pathSimilarity > 0.95;
}
```

---

## Future Enhancements

### Advanced Algorithms
- **PPO (Proximal Policy Optimization)**: More stable than basic RL
- **A3C (Asynchronous Advantage Actor-Critic)**: Parallel training
- **Imitation Learning**: Learn from human demonstrations
- **Curriculum Learning**: Progressive difficulty in training

### Meta-Learning
- Transfer learning between tracks
- Pre-trained base models
- Few-shot adaptation to new tracks
- Learning to learn (meta-optimization)

### Multi-Agent
- Cooperative racing (team strategies)
- Adversarial training (competitive learning)
- Swarm behaviors

---

**Last Updated**: May 14, 2026
