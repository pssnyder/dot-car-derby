# Dot Car Derby - Project Structure

## 📁 Recommended File Organization

```
dot-car-derby/
│
├── docs/                          # Project documentation
│   ├── PROJECT_OVERVIEW.md        # High-level vision and goals
│   ├── TECHNICAL_ARCHITECTURE.md  # System architecture and stack
│   ├── DEVELOPMENT_ROADMAP.md     # Phases and milestones
│   ├── ML_SYSTEM_DESIGN.md        # ML algorithms and DNA system
│   ├── API_REFERENCE.md           # API endpoint documentation
│   ├── CONTRIBUTING.md            # Contribution guidelines
│   └── DEPLOYMENT.md              # Deployment instructions
│
├── frontend/                      # React web application
│   ├── public/                    # Static assets
│   │   ├── index.html
│   │   ├── favicon.ico
│   │   └── assets/
│   │       ├── images/
│   │       ├── sounds/
│   │       └── fonts/
│   │
│   ├── src/
│   │   ├── main.tsx               # Application entry point
│   │   ├── App.tsx                # Root component
│   │   ├── vite-env.d.ts          # Vite type definitions
│   │   │
│   │   ├── components/            # React components
│   │   │   ├── auth/
│   │   │   │   ├── LoginForm.tsx
│   │   │   │   ├── RegisterForm.tsx
│   │   │   │   └── AuthGuard.tsx
│   │   │   │
│   │   │   ├── dashboard/
│   │   │   │   ├── Dashboard.tsx
│   │   │   │   ├── StatsOverview.tsx
│   │   │   │   └── RecentRaces.tsx
│   │   │   │
│   │   │   ├── training/
│   │   │   │   ├── TrainingInterface.tsx
│   │   │   │   ├── ConfigPanel.tsx
│   │   │   │   ├── ProgressView.tsx
│   │   │   │   └── FitnessGraph.tsx
│   │   │   │
│   │   │   ├── racing/
│   │   │   │   ├── RaceViewer.tsx
│   │   │   │   ├── TrackSelector.tsx
│   │   │   │   ├── Leaderboard.tsx
│   │   │   │   └── ReplayPlayer.tsx
│   │   │   │
│   │   │   ├── garage/
│   │   │   │   ├── VehicleCustomizer.tsx
│   │   │   │   ├── DNAManager.tsx
│   │   │   │   ├── UpgradeShop.tsx
│   │   │   │   └── ColorPicker.tsx
│   │   │   │
│   │   │   ├── tournament/
│   │   │   │   ├── TournamentList.tsx
│   │   │   │   ├── TournamentBracket.tsx
│   │   │   │   ├── Registration.tsx
│   │   │   │   └── Results.tsx
│   │   │   │
│   │   │   ├── community/
│   │   │   │   ├── Forum.tsx
│   │   │   │   ├── DNAMarketplace.tsx
│   │   │   │   ├── SwapMeet.tsx
│   │   │   │   └── StrategyGuides.tsx
│   │   │   │
│   │   │   ├── shared/
│   │   │   │   ├── Button.tsx
│   │   │   │   ├── Modal.tsx
│   │   │   │   ├── Loading.tsx
│   │   │   │   ├── Toast.tsx
│   │   │   │   └── ErrorBoundary.tsx
│   │   │   │
│   │   │   └── layout/
│   │   │       ├── Header.tsx
│   │   │       ├── Sidebar.tsx
│   │   │       ├── Footer.tsx
│   │   │       └── Layout.tsx
│   │   │
│   │   ├── engine/                # Game engine
│   │   │   ├── renderer/
│   │   │   │   ├── RaceRenderer.ts
│   │   │   │   ├── TrackRenderer.ts
│   │   │   │   ├── DotRenderer.ts
│   │   │   │   └── UIRenderer.ts
│   │   │   │
│   │   │   ├── physics/
│   │   │   │   ├── PhysicsEngine.ts
│   │   │   │   ├── Collision.ts
│   │   │   │   ├── Movement.ts
│   │   │   │   └── Vector2.ts
│   │   │   │
│   │   │   ├── track/
│   │   │   │   ├── Track.ts
│   │   │   │   ├── TrackGenerator.ts
│   │   │   │   ├── Checkpoint.ts
│   │   │   │   └── Obstacle.ts
│   │   │   │
│   │   │   ├── entities/
│   │   │   │   ├── Dot.ts
│   │   │   │   ├── Brain.ts
│   │   │   │   └── Sensor.ts
│   │   │   │
│   │   │   ├── replay/
│   │   │   │   ├── ReplayRecorder.ts
│   │   │   │   └── ReplayPlayer.ts
│   │   │   │
│   │   │   └── validation/
│   │   │       ├── InputValidator.ts
│   │   │       └── StateValidator.ts
│   │   │
│   │   ├── ml/                    # Machine learning
│   │   │   ├── algorithms/
│   │   │   │   ├── GeneticAlgorithm.ts
│   │   │   │   ├── QLearning.ts
│   │   │   │   ├── NEAT.ts          # Future
│   │   │   │   └── Algorithm.ts      # Base class
│   │   │   │
│   │   │   ├── dna/
│   │   │   │   ├── DNASchema.ts
│   │   │   │   ├── DNAValidator.ts
│   │   │   │   ├── DNAEncoder.ts
│   │   │   │   └── DNASerializer.ts
│   │   │   │
│   │   │   ├── sensors/
│   │   │   │   ├── DistanceSensor.ts
│   │   │   │   ├── VelocitySensor.ts
│   │   │   │   ├── PositionSensor.ts
│   │   │   │   ├── AngleSensor.ts
│   │   │   │   └── Sensor.ts         # Base class
│   │   │   │
│   │   │   ├── actions/
│   │   │   │   ├── ForwardAction.ts
│   │   │   │   ├── TurnAction.ts
│   │   │   │   ├── BrakeAction.ts
│   │   │   │   └── Action.ts         # Base class
│   │   │   │
│   │   │   ├── training/
│   │   │   │   ├── TrainingEnvironment.ts
│   │   │   │   ├── TrainingWorker.ts
│   │   │   │   ├── Optimizer.ts
│   │   │   │   └── Config.ts
│   │   │   │
│   │   │   └── evaluation/
│   │   │       ├── FitnessCalculator.ts
│   │   │       ├── PerformanceMetrics.ts
│   │   │       └── Evaluator.ts
│   │   │
│   │   ├── data/                  # Data layer
│   │   │   ├── api/
│   │   │   │   ├── client.ts
│   │   │   │   ├── auth.ts
│   │   │   │   ├── users.ts
│   │   │   │   ├── vehicles.ts
│   │   │   │   ├── races.ts
│   │   │   │   ├── tournaments.ts
│   │   │   │   └── community.ts
│   │   │   │
│   │   │   ├── local/
│   │   │   │   ├── IndexedDB.ts
│   │   │   │   ├── DNAStore.ts
│   │   │   │   └── CacheStore.ts
│   │   │   │
│   │   │   └── sync/
│   │   │       ├── SyncManager.ts
│   │   │       └── ConflictResolver.ts
│   │   │
│   │   ├── store/                 # State management
│   │   │   ├── index.ts
│   │   │   ├── authSlice.ts
│   │   │   ├── userSlice.ts
│   │   │   ├── vehicleSlice.ts
│   │   │   ├── raceSlice.ts
│   │   │   └── uiSlice.ts
│   │   │
│   │   ├── hooks/                 # Custom React hooks
│   │   │   ├── useAuth.ts
│   │   │   ├── useTraining.ts
│   │   │   ├── useRace.ts
│   │   │   ├── useWebSocket.ts
│   │   │   └── useLocalStorage.ts
│   │   │
│   │   ├── utils/                 # Utility functions
│   │   │   ├── math.ts
│   │   │   ├── format.ts
│   │   │   ├── validation.ts
│   │   │   └── constants.ts
│   │   │
│   │   ├── types/                 # TypeScript types
│   │   │   ├── models.ts
│   │   │   ├── api.ts
│   │   │   ├── dna.ts
│   │   │   └── race.ts
│   │   │
│   │   ├── styles/                # Global styles
│   │   │   ├── globals.css
│   │   │   ├── variables.css
│   │   │   └── themes/
│   │   │
│   │   └── workers/               # Web Workers
│   │       ├── training.worker.ts
│   │       └── physics.worker.ts
│   │
│   ├── .env.example               # Environment variables template
│   ├── .env.development
│   ├── .env.production
│   ├── index.html
│   ├── package.json
│   ├── tsconfig.json
│   ├── tsconfig.node.json
│   ├── vite.config.ts
│   └── tailwind.config.js
│
├── backend/                       # Node.js API server
│   ├── src/
│   │   ├── index.ts               # Server entry point
│   │   ├── app.ts                 # Express app setup
│   │   │
│   │   ├── config/
│   │   │   ├── database.ts
│   │   │   ├── auth.ts
│   │   │   ├── redis.ts
│   │   │   └── env.ts
│   │   │
│   │   ├── middleware/
│   │   │   ├── auth.ts
│   │   │   ├── validation.ts
│   │   │   ├── errorHandler.ts
│   │   │   ├── rateLimit.ts
│   │   │   └── cors.ts
│   │   │
│   │   ├── routes/
│   │   │   ├── index.ts
│   │   │   ├── auth.routes.ts
│   │   │   ├── users.routes.ts
│   │   │   ├── drivers.routes.ts
│   │   │   ├── vehicles.routes.ts
│   │   │   ├── dna.routes.ts
│   │   │   ├── tracks.routes.ts
│   │   │   ├── races.routes.ts
│   │   │   ├── tournaments.routes.ts
│   │   │   ├── upgrades.routes.ts
│   │   │   └── community.routes.ts
│   │   │
│   │   ├── controllers/
│   │   │   ├── auth.controller.ts
│   │   │   ├── users.controller.ts
│   │   │   ├── drivers.controller.ts
│   │   │   ├── vehicles.controller.ts
│   │   │   ├── dna.controller.ts
│   │   │   ├── tracks.controller.ts
│   │   │   ├── races.controller.ts
│   │   │   ├── tournaments.controller.ts
│   │   │   ├── upgrades.controller.ts
│   │   │   └── community.controller.ts
│   │   │
│   │   ├── services/
│   │   │   ├── auth.service.ts
│   │   │   ├── user.service.ts
│   │   │   ├── driver.service.ts
│   │   │   ├── vehicle.service.ts
│   │   │   ├── dna.service.ts
│   │   │   ├── race.service.ts
│   │   │   ├── tournament.service.ts
│   │   │   ├── validation.service.ts
│   │   │   └── email.service.ts
│   │   │
│   │   ├── models/
│   │   │   ├── User.ts
│   │   │   ├── DotDriver.ts
│   │   │   ├── DotVehicle.ts
│   │   │   ├── DNATemplate.ts
│   │   │   ├── Track.ts
│   │   │   ├── Race.ts
│   │   │   ├── Tournament.ts
│   │   │   └── Upgrade.ts
│   │   │
│   │   ├── validation/
│   │   │   ├── schemas/
│   │   │   │   ├── user.schema.ts
│   │   │   │   ├── vehicle.schema.ts
│   │   │   │   ├── dna.schema.ts
│   │   │   │   └── race.schema.ts
│   │   │   └── validators/
│   │   │       ├── dnaValidator.ts
│   │   │       └── raceValidator.ts
│   │   │
│   │   ├── utils/
│   │   │   ├── logger.ts
│   │   │   ├── crypto.ts
│   │   │   ├── jwt.ts
│   │   │   └── helpers.ts
│   │   │
│   │   ├── types/
│   │   │   ├── express.d.ts
│   │   │   ├── models.ts
│   │   │   └── api.ts
│   │   │
│   │   └── websocket/
│   │       ├── server.ts
│   │       ├── handlers/
│   │       │   ├── race.handler.ts
│   │       │   └── tournament.handler.ts
│   │       └── rooms/
│   │           └── RaceRoom.ts
│   │
│   ├── prisma/                    # Database schema (if using Prisma)
│   │   ├── schema.prisma
│   │   ├── migrations/
│   │   └── seed.ts
│   │
│   ├── tests/
│   │   ├── unit/
│   │   ├── integration/
│   │   └── e2e/
│   │
│   ├── .env.example
│   ├── .env.development
│   ├── .env.production
│   ├── package.json
│   ├── tsconfig.json
│   └── jest.config.js
│
├── database/                      # Database scripts
│   ├── migrations/
│   │   ├── 001_initial_schema.sql
│   │   ├── 002_add_tournaments.sql
│   │   └── ...
│   ├── seeds/
│   │   ├── tracks.sql
│   │   ├── upgrades.sql
│   │   └── sample_data.sql
│   └── schema.sql
│
├── shared/                        # Shared code between frontend/backend
│   ├── types/
│   │   ├── DNA.ts
│   │   ├── Track.ts
│   │   ├── Race.ts
│   │   └── API.ts
│   ├── constants/
│   │   └── game-config.ts
│   └── utils/
│       └── validators.ts
│
├── scripts/                       # Utility scripts
│   ├── setup-dev.sh
│   ├── deploy.sh
│   ├── backup-db.sh
│   └── seed-data.ts
│
├── .github/                       # GitHub configuration
│   ├── workflows/
│   │   ├── ci.yml
│   │   ├── deploy-staging.yml
│   │   └── deploy-production.yml
│   ├── ISSUE_TEMPLATE/
│   └── PULL_REQUEST_TEMPLATE.md
│
├── .gitignore
├── .prettierrc
├── .eslintrc.js
├── docker-compose.yml             # Local development environment
├── Dockerfile                     # Production container
├── README.md
└── LICENSE
```

## 📋 Key File Descriptions

### Frontend Key Files

#### `src/main.tsx`
Application entry point, sets up React and routing.

#### `src/engine/`
Core game engine - handles rendering, physics, and game logic. Keep this separate from React components for performance.

#### `src/ml/`
All machine learning logic. Designed to run in Web Workers for non-blocking training.

#### `src/data/api/`
API client layer. All backend communication goes through here.

#### `src/data/local/`
IndexedDB wrapper for offline storage of DNA and training data.

### Backend Key Files

#### `src/index.ts`
Server entry point, starts Express and WebSocket servers.

#### `src/routes/`
API route definitions. Each file handles one resource type.

#### `src/services/`
Business logic layer. Controllers call services, services interact with models.

#### `src/validation/`
Input validation and anti-cheat systems. Critical for security.

#### `src/websocket/`
Real-time communication for live races and tournaments.

### Shared Files

#### `shared/types/`
TypeScript types used by both frontend and backend. Ensures consistency.

#### `shared/constants/`
Game configuration constants (max speed, sensor ranges, etc.). Single source of truth.

## 🔧 Configuration Files

### Frontend

```json
// frontend/package.json
{
  "name": "dot-car-derby-frontend",
  "version": "0.1.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "preview": "vite preview",
    "test": "vitest",
    "lint": "eslint src --ext ts,tsx",
    "format": "prettier --write src"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.20.0",
    "three": "^0.160.0",
    "@tensorflow/tfjs": "^4.15.0",
    "zustand": "^4.4.7",
    "axios": "^1.6.2",
    "socket.io-client": "^4.6.0"
  },
  "devDependencies": {
    "@types/react": "^18.2.43",
    "@types/react-dom": "^18.2.17",
    "@types/three": "^0.160.0",
    "@vitejs/plugin-react": "^4.2.1",
    "typescript": "^5.3.3",
    "vite": "^5.0.8",
    "vitest": "^1.1.0",
    "tailwindcss": "^3.3.0",
    "autoprefixer": "^10.4.16",
    "postcss": "^8.4.32"
  }
}
```

### Backend

```json
// backend/package.json
{
  "name": "dot-car-derby-backend",
  "version": "0.1.0",
  "type": "module",
  "scripts": {
    "dev": "tsx watch src/index.ts",
    "build": "tsc",
    "start": "node dist/index.js",
    "test": "jest",
    "migrate": "prisma migrate deploy",
    "seed": "tsx prisma/seed.ts"
  },
  "dependencies": {
    "express": "^4.18.2",
    "passport": "^0.7.0",
    "passport-google-oauth20": "^2.0.0",
    "jsonwebtoken": "^9.0.2",
    "bcrypt": "^5.1.1",
    "pg": "^8.11.3",
    "redis": "^4.6.11",
    "socket.io": "^4.6.0",
    "zod": "^3.22.4",
    "prisma": "^5.7.1",
    "@prisma/client": "^5.7.1"
  },
  "devDependencies": {
    "@types/express": "^4.17.21",
    "@types/node": "^20.10.5",
    "@types/passport": "^1.0.16",
    "typescript": "^5.3.3",
    "tsx": "^4.7.0",
    "jest": "^29.7.0",
    "@types/jest": "^29.5.11"
  }
}
```

## 🚀 Development Workflow

### Initial Setup
1. Clone repository
2. Run `npm install` in both `frontend/` and `backend/`
3. Set up PostgreSQL and Redis
4. Copy `.env.example` to `.env` and configure
5. Run database migrations
6. Start development servers

### Daily Development
1. Pull latest changes
2. Start backend: `cd backend && npm run dev`
3. Start frontend: `cd frontend && npm run dev`
4. Make changes
5. Test locally
6. Commit and push

### Adding Features
1. Create feature branch
2. Update types in `shared/types/`
3. Implement backend service + route
4. Implement frontend component + API call
5. Write tests
6. Submit PR

---

**Last Updated**: May 14, 2026
