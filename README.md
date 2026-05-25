# 🏁 Dot Car Derby

**An Educational AI Racing Game**

Transform dots into intelligent racers! Train your own AI driver using machine learning algorithms, compete in tournaments, and learn computer science concepts through engaging gameplay.

---

## 🎮 What is Dot Car Derby?

Dot Car Derby is a web-based competitive racing game where players train AI-powered "dots" to navigate race tracks. Built on the foundation of the [Dot AI](https://github.com/RTS-Technology-Solutions/Dot-AI) educational project, this game makes machine learning accessible, fun, and competitive.

### Key Features

🧬 **Train Your Dot** - Use genetic algorithms, Q-learning, and neural networks  
🏆 **Compete** - Weekly tournaments and leaderboards  
🎓 **Learn** - Educational tutorials on AI and ML concepts  
🔧 **Customize** - Earn and equip upgrades to enhance your dot  
🤝 **Community** - Share strategies, DNA templates, and compete with friends  
🌐 **Browser-Based** - No installation required, runs entirely in your browser

---

## 🚀 Quick Start

### Try the Prototype! (Step 1 Complete + Step 2 Ready)

```powershell
# Install dependencies
pip install pygame

# Run the racing simulation
python dot_ai_car.py

# Watch 50 AI dots learn to race with beautiful ROYGBIV gradient colors!
# Red = slow/near start, Violet = fast/near finish
```

**Controls**: 
- **ESC** - Save & Exit
- **S** - Manual save
- **SPACE** - Force next generation
- **1** - Switch to Drag Strip
- **2** - Switch to Oval Track (99% loop)

### Key Features Now Live:
✨ **ROYGBIV Gradient Colors** - Dots colored by distance (Red→Orange→Yellow→Green→Blue→Indigo→Violet)  
🏁 **Data-Driven Tracks** - All track geometry stored in `tracks_database.json`  
🔄 **Dynamic Track Switching** - Switch between tracks without restarting  
📊 **Top 25 Advancement** - Only the best racers proceed to next generation

### For Players (Coming Soon)
Visit [dotcarderby.com](https://dotcarderby.com) when we launch!

---

## 📚 Documentation

### Project Overview
- **[Project Overview](./docs/PROJECT_OVERVIEW.md)** - Vision, goals, and features
- **[Development Roadmap](./docs/DEVELOPMENT_ROADMAP.md)** - Development phases and milestones
- **[Getting Started](./docs/GETTING_STARTED.md)** - Development environment setup

### Technical Documentation
- **[Technical Architecture](./docs/TECHNICAL_ARCHITECTURE.md)** - System design and stack
- **[ML System Design](./docs/ML_SYSTEM_DESIGN.md)** - Algorithms, DNA system, sensors
- **[Project Structure](./docs/PROJECT_STRUCTURE.md)** - File organization and key files

### Contributing
- **[Contributing Guidelines](./CONTRIBUTING.md)** - How to contribute *(coming soon)*
- **[Code of Conduct](./CODE_OF_CONDUCT.md)** - Community standards *(coming soon)*

---

## 🎯 How It Works

### 1. Create Your Driver
Set up your dot driver profile and customize your vehicle with colors and patterns.

### 2. Train Your AI
Configure sensors, actions, and reward functions. Run training simulations locally in your browser.

### 3. Race & Compete
Test your trained dot on various tracks. Compete in tournaments for upgrades and bragging rights.

### 4. Upgrade & Progress
Earn points through performance and achievements. Unlock better sensors, actions, and algorithms.

### 5. Share & Learn
Share your DNA templates, strategies, and learn from the community.

---

## 🛠️ Technology Stack

### Frontend
- **React 18** + TypeScript
- **Three.js** for 3D rendering
- **TensorFlow.js** for client-side ML
- **Vite** for blazing-fast dev experience

### Backend
- **Node.js** + Express + TypeScript
- **PostgreSQL** for data persistence
- **Redis** for caching and sessions
- **WebSockets** for real-time races

### DevOps
- **Docker** for containerization
- **GitHub Actions** for CI/CD
- **AWS/Vercel** for hosting

---

## 🎓 Educational Value

Dot Car Derby teaches:
- **Machine Learning Fundamentals** - Genetic algorithms, reinforcement learning
- **Computational Thinking** - Problem decomposition, pattern recognition
- **Optimization** - Fitness functions, hyperparameter tuning
- **Data Science** - Performance metrics, statistical analysis
- **Software Engineering** - Version control, collaboration, deployment

Perfect for:
- Students learning AI/ML concepts
- Educators teaching computer science
- Hobbyists interested in game AI
- Anyone curious about machine learning

---

## 🏗️ Project Status

**Current Phase**: Phase 0 Complete ✅ | Step 2 Ready 🏗️

### Completed Milestones
- [x] Project concept and documentation
- [x] Technical architecture design
- [x] Database schema design
- [x] **Step 1: Drag Race Prototype** ✅
  - Vertical drag strip with 50 AI racers
  - Genetic algorithm training
  - Ranking system (top 25 advance)
  - **ROYGBIV gradient color system** 🌈
  - **Data-driven track architecture** 📊
  - Dynamic track switching

### Available Now
- [x] **Drag Strip Alpha** - Straight vertical race
- [x] **The Horseshoe Circuit** - 99% oval with separated start/finish

### In Progress
- [ ] Step 3: Full track variety (rally, Daytona, Indy, Maniac Mayhem)
- [ ] Additional track configurations

### Project Files
- `dot_ai_car.py` - Main racing simulation engine
- `race_config.json` - Global configuration
- `tracks_database.json` - **Track geometry database** 🆕
- `dot_ai_legacy.py` - Original implementation reference

See the [Development Roadmap](./docs/DEVELOPMENT_ROADMAP.md) for detailed progress and upcoming milestones.

---

## 🤝 Contributing

We welcome contributions! Whether you're a developer, designer, educator, or just enthusiastic about AI, there's a place for you.

### Ways to Contribute
- 🐛 Report bugs and issues
- 💡 Suggest features and improvements
- 📝 Improve documentation
- 🎨 Design UI/UX
- 💻 Write code (frontend, backend, ML algorithms)
- 🎓 Create educational content

See [CONTRIBUTING.md](./CONTRIBUTING.md) for detailed guidelines *(coming soon)*.

---

## 📊 Roadmap Highlights

| Phase | Status | Target | Key Features |
|-------|--------|--------|--------------|
| **0: Planning** | 🟢 In Progress | Week 2 | Documentation, architecture |
| **1: MVP** | ⚪ Not Started | Week 10 | Basic training & racing |
| **2: Progression** | ⚪ Not Started | Week 16 | Upgrades, skill system |
| **3: Multiplayer** | ⚪ Not Started | Week 24 | Tournaments, live racing |
| **4: Community** | ⚪ Not Started | Week 30 | Sharing, forums, events |
| **5: Polish** | ⚪ Not Started | Week 36 | Advanced ML, optimization |
| **6: Launch** | ⚪ Not Started | Week 38+ | Public release! |

---

## 🌟 Inspiration & Credits

This project is not sponsored. Inspiration came from:
- **Dot AI** by RTS Technology & Solutions LLC *(our foundation)*
- **AI Learns to Drive** by ActivationFunction
- **AIvolution** by Deeon & Lykke Studios
- **Wobbledogs** by Animal Uprising & Secret Mode
- **Dr. Derks Mutant Battlegrounds** by Mount Rouke Studios

*Please check out these amazing projects!*

---

## 📜 License

This project is licensed under the MIT License - see [LICENSE](./LICENSE) file for details.

---

## 📞 Contact & Community

- 🌐 **Website**: [dotcarderby.com](https://dotcarderby.com) *(coming soon)*
- 💬 **Discord**: [Join our community](https://discord.gg/dot-car-derby) *(coming soon)*
- 🐛 **Issues**: [GitHub Issues](https://github.com/RTS-Technology-Solutions/Dot-AI/issues)
- 📧 **Email**: support@rtstechnology.com
- 🐦 **Twitter**: [@DotCarDerby](https://twitter.com/DotCarDerby) *(coming soon)*

---

## 🎮 Let's Build Something Amazing Together!

Dot Car Derby combines education, competition, and community. Whether you're here to learn, compete, or contribute, we're excited to have you!

**Star ⭐ this repo** to follow our progress!

---

*Made with ❤️ by RTS Technology & Solutions and the open-source community*
