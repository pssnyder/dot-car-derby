# Dot Car Derby - Development Setup Guide

## 🚀 Getting Started

This guide will help you set up your development environment for Dot Car Derby.

---

## Prerequisites

### Required Software
- **Node.js** v20+ ([Download](https://nodejs.org/))
- **Git** ([Download](https://git-scm.com/))
- **PostgreSQL** 15+ ([Download](https://www.postgresql.org/download/))
- **Redis** 7+ ([Download](https://redis.io/download))

### Recommended Tools
- **VS Code** with extensions:
  - ESLint
  - Prettier
  - TypeScript
  - Prisma (if using Prisma ORM)
  - GitLens
- **Postman** or **Insomnia** for API testing
- **Docker Desktop** (optional, for containerized development)

---

## Quick Start (Docker - Recommended)

If you have Docker Desktop installed:

```powershell
# Clone the repository
git clone https://github.com/RTS-Technology-Solutions/Dot-AI.git
cd Dot-AI/dot-car-derby

# Start all services
docker-compose up -d

# Install frontend dependencies
cd frontend
npm install

# Install backend dependencies
cd ../backend
npm install

# Run database migrations
npm run migrate

# Seed initial data
npm run seed
```

Frontend: http://localhost:5173  
Backend API: http://localhost:3000  
PostgreSQL: localhost:5432  
Redis: localhost:6379

---

## Manual Setup

### 1. Clone Repository

```powershell
git clone https://github.com/RTS-Technology-Solutions/Dot-AI.git
cd Dot-AI/dot-car-derby
```

### 2. Set Up PostgreSQL

#### Windows (PowerShell)
```powershell
# After installing PostgreSQL, create database
psql -U postgres
```

```sql
-- In PostgreSQL shell
CREATE DATABASE dot_car_derby_dev;
CREATE USER dotuser WITH PASSWORD 'your_password_here';
GRANT ALL PRIVILEGES ON DATABASE dot_car_derby_dev TO dotuser;
\q
```

#### Alternative: Use PostgreSQL GUI (pgAdmin)
1. Open pgAdmin
2. Right-click "Databases" → Create → Database
3. Name: `dot_car_derby_dev`
4. Save

### 3. Set Up Redis

#### Windows
```powershell
# If installed via Chocolatey
redis-server

# Or use Windows Subsystem for Linux (WSL)
wsl
sudo service redis-server start
```

#### Alternative: Use Docker for Redis Only
```powershell
docker run -d -p 6379:6379 --name dot-redis redis:7-alpine
```

### 4. Backend Setup

```powershell
cd backend

# Install dependencies
npm install

# Copy environment template
cp .env.example .env

# Edit .env with your database credentials
# Use notepad or your preferred editor
notepad .env
```

#### Configure `.env`
```env
# Server
NODE_ENV=development
PORT=3000

# Database
DATABASE_URL="postgresql://dotuser:your_password_here@localhost:5432/dot_car_derby_dev"

# Redis
REDIS_URL="redis://localhost:6379"

# JWT
JWT_SECRET="your-super-secret-jwt-key-change-this"
JWT_EXPIRES_IN="7d"

# OAuth (get these from provider consoles)
GOOGLE_CLIENT_ID="your-google-client-id"
GOOGLE_CLIENT_SECRET="your-google-client-secret"
GOOGLE_CALLBACK_URL="http://localhost:3000/api/v1/auth/google/callback"

# Cors
FRONTEND_URL="http://localhost:5173"
```

#### Run Migrations
```powershell
# Create database schema
npm run migrate

# Seed initial data (tracks, upgrades, etc.)
npm run seed
```

#### Start Backend Server
```powershell
npm run dev
```

Server should start on http://localhost:3000

### 5. Frontend Setup

Open a new terminal:

```powershell
cd frontend

# Install dependencies
npm install

# Copy environment template
cp .env.example .env

# Edit .env
notepad .env
```

#### Configure `.env`
```env
VITE_API_URL=http://localhost:3000/api/v1
VITE_WS_URL=ws://localhost:3000
VITE_GOOGLE_CLIENT_ID=your-google-client-id
```

#### Start Frontend Dev Server
```powershell
npm run dev
```

Frontend should start on http://localhost:5173

---

## Verify Setup

### 1. Check Backend Health
Open http://localhost:3000/api/v1/health

Expected response:
```json
{
  "status": "ok",
  "timestamp": "2026-05-14T12:00:00.000Z",
  "database": "connected",
  "redis": "connected"
}
```

### 2. Check Frontend
Open http://localhost:5173

You should see the Dot Car Derby home page.

### 3. Test Authentication
1. Click "Login"
2. Choose OAuth provider
3. Complete authentication
4. You should be redirected to dashboard

---

## Development Workflow

### Running Both Servers

#### Option 1: Two Terminals
```powershell
# Terminal 1 - Backend
cd backend
npm run dev

# Terminal 2 - Frontend
cd frontend
npm run dev
```

#### Option 2: Concurrently (in root)
```powershell
# Install concurrently globally
npm install -g concurrently

# Run both
concurrently "cd backend && npm run dev" "cd frontend && npm run dev"
```

### Hot Reload
Both frontend and backend have hot reload enabled:
- Frontend (Vite): Changes reload automatically
- Backend (tsx watch): Server restarts on file changes

---

## Project Structure

```
dot-car-derby/
├── frontend/          # React app
│   ├── src/
│   ├── public/
│   └── package.json
│
├── backend/           # Node.js API
│   ├── src/
│   ├── prisma/
│   └── package.json
│
├── shared/            # Shared TypeScript types
├── database/          # SQL scripts
├── docs/              # Documentation
└── docker-compose.yml
```

See [PROJECT_STRUCTURE.md](./PROJECT_STRUCTURE.md) for detailed file organization.

---

## Common Tasks

### Database

#### Reset Database
```powershell
cd backend

# Drop all tables and recreate
npm run migrate:reset

# Re-seed data
npm run seed
```

#### Create Migration
```powershell
# If using Prisma
npx prisma migrate dev --name your_migration_name

# If using raw SQL, create file in database/migrations/
```

#### View Database
```powershell
# Prisma Studio (GUI)
npx prisma studio

# Or use pgAdmin
```

### Testing

#### Run Frontend Tests
```powershell
cd frontend
npm test
```

#### Run Backend Tests
```powershell
cd backend
npm test
```

#### E2E Tests
```powershell
# Install Playwright
npm install -D @playwright/test

# Run E2E tests
npx playwright test
```

### Code Quality

#### Lint
```powershell
# Frontend
cd frontend
npm run lint

# Backend
cd backend
npm run lint
```

#### Format
```powershell
# Frontend
cd frontend
npm run format

# Backend
cd backend
npm run format
```

### Build for Production

```powershell
# Frontend
cd frontend
npm run build
# Output in frontend/dist/

# Backend
cd backend
npm run build
# Output in backend/dist/
```

---

## OAuth Setup

### Google OAuth

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing
3. Enable Google+ API
4. Create OAuth 2.0 credentials:
   - Application type: Web application
   - Authorized redirect URIs: `http://localhost:3000/api/v1/auth/google/callback`
5. Copy Client ID and Client Secret to `.env` files

### GitHub OAuth (Optional)

1. Go to GitHub Settings → Developer settings → OAuth Apps
2. Create new OAuth App
3. Homepage URL: `http://localhost:5173`
4. Callback URL: `http://localhost:3000/api/v1/auth/github/callback`
5. Copy Client ID and Secret to `.env`

---

## Troubleshooting

### Port Already in Use

```powershell
# Find process using port 3000 (backend)
netstat -ano | findstr :3000

# Kill process (replace PID)
taskkill /PID <PID> /F

# Or change port in backend/.env
PORT=3001
```

### Database Connection Error

```powershell
# Check PostgreSQL is running
# Windows Services → PostgreSQL

# Or restart it
net stop postgresql-x64-15
net start postgresql-x64-15

# Test connection
psql -U dotuser -d dot_car_derby_dev
```

### Redis Connection Error

```powershell
# Check Redis is running
redis-cli ping
# Should return: PONG

# If not running
redis-server

# Or use Docker
docker start dot-redis
```

### Module Not Found

```powershell
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
```

### TypeScript Errors

```powershell
# Rebuild TypeScript
npm run build

# Check TypeScript version
npx tsc --version
```

---

## VS Code Configuration

### Recommended Settings

Create `.vscode/settings.json`:

```json
{
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": true
  },
  "typescript.tsdk": "node_modules/typescript/lib",
  "files.exclude": {
    "**/node_modules": true,
    "**/dist": true,
    "**/.git": true
  }
}
```

### Recommended Extensions

Create `.vscode/extensions.json`:

```json
{
  "recommendations": [
    "dbaeumer.vscode-eslint",
    "esbenp.prettier-vscode",
    "prisma.prisma",
    "bradlc.vscode-tailwindcss",
    "ms-vscode.vscode-typescript-next"
  ]
}
```

---

## Next Steps

1. ✅ Complete setup
2. 📖 Read [PROJECT_OVERVIEW.md](./PROJECT_OVERVIEW.md)
3. 🏗️ Review [TECHNICAL_ARCHITECTURE.md](./TECHNICAL_ARCHITECTURE.md)
4. 🗺️ Check [DEVELOPMENT_ROADMAP.md](./DEVELOPMENT_ROADMAP.md)
5. 🧬 Understand [ML_SYSTEM_DESIGN.md](./ML_SYSTEM_DESIGN.md)
6. 🎯 Pick a task from GitHub Issues
7. 🚀 Start coding!

---

## Getting Help

- 📧 Email: support@rtstechnology.com
- 💬 Discord: [Join Server](https://discord.gg/dot-car-derby)
- 🐛 Issues: [GitHub Issues](https://github.com/RTS-Technology-Solutions/Dot-AI/issues)
- 📚 Docs: See `/docs` folder

---

**Last Updated**: May 14, 2026  
**Version**: 0.1.0
