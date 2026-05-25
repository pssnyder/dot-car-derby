# Wireframes - Dot Car Derby
**Detailed UI Mockups**

**Date**: May 20, 2026  
**Tool**: ASCII Wireframes (will be converted to Figma)  
**Status**: Draft

---

## 📱 Mobile-First Wireframes

### 1. Landing Page (Mobile)

```
┌─────────────────────┐
│ ☰  Dot Car Derby    │ [Header: Fixed]
├─────────────────────┤
│                     │
│   🏁  [Animation]   │ [Hero Section]
│   Racing Dots       │
│                     │
│  Train AI Racers    │ [H1]
│  Learn ML by Racing │ [Subhead]
│                     │
│  ┌───────────────┐  │
│  │ Get Started   │  │ [Primary CTA]
│  └───────────────┘  │
│  ┌───────────────┐  │
│  │ Watch Demo ▶  │  │ [Secondary CTA]
│  └───────────────┘  │
│                     │
├─────────────────────┤
│ 🧠 Train            │ [Feature 1]
│ Use genetic algos   │
│ to teach dots       │
│                     │
│ 🏆 Race             │ [Feature 2]
│ Compete in          │
│ tournaments         │
│                     │
│ 📚 Learn            │ [Feature 3]
│ Understand ML       │
│ concepts hands-on   │
├─────────────────────┤
│ Recent Activity     │ [Social Proof]
│ 12,345 users        │
│ 500+ races today    │
│                     │
│ @user finished!     │
│ @racer Gen 50!      │
├─────────────────────┤
│ [Links]  [About]    │ [Footer]
│ [GitHub] [Login]    │
└─────────────────────┘
```

### 2. Dashboard (Mobile)

```
┌─────────────────────┐
│ ☰  Dashboard    👤  │ [Header]
├─────────────────────┤
│ Hi User! 👋         │
│ Points: 1,250 🏆    │
├─────────────────────┤
│ QUICK TRAIN         │ [Card 1]
│ ┌─────────────────┐ │
│ │ Drag Strip      │ │
│ │ Gen 47/100      │ │
│ │ [Continue →]    │ │
│ └─────────────────┘ │
│ + Start New         │
├─────────────────────┤
│ ACTIVE RACES        │ [Card 2]
│ ┌─────────────────┐ │
│ │ Tournament      │ │
│ │ Starts in 2h    │ │
│ │ [Join Now →]    │ │
│ └─────────────────┘ │
├─────────────────────┤
│ YOUR DRIVERS        │ [Card 3]
│ • Drag Expert       │
│ • Oval Rookie       │
│ [View All →]        │
├─────────────────────┤
│ PERFORMANCE         │ [Card 4]
│ Wins: 12 | Rank: #342│
│ [View Stats →]      │
├─────────────────────┤
│ [Train] [Race] [Me] │ [Bottom Nav]
└─────────────────────┘
```

### 3. Training Environment (Mobile)

```
┌─────────────────────┐
│ ← Training          │ [Header]
├─────────────────────┤
│ Drag Strip Alpha    │ [Track Name]
│ [Dropdown ▾]        │
├─────────────────────┤
│                     │
│   [SIMULATION]      │ [Canvas]
│   [Racing dots]     │ [Fullscreen]
│   [ROYGBIV]         │
│                     │
├─────────────────────┤
│ Gen 23 | 12 fin     │ [Stats Bar]
│ Avg Fit: 320        │
├─────────────────────┤
│ [▶] [⏸] [⏭]  1x ▾  │ [Controls]
├─────────────────────┤
│ ⚙️ Settings ▾       │ [Collapsed]
│                     │
│ 📊 Progress ▾       │ [Collapsed]
│                     │
│ [Save DNA]          │ [Action]
└─────────────────────┘
```

---

## 💻 Desktop Wireframes

### 1. Dashboard (Desktop - 1440px)

```
┌────────────────────────────────────────────────────────────────────────┐
│  🏁 Dot Car Derby    [Train] [Race] [Stats]      Points: 1,250  [@User▾]│
├────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  Welcome back, User! 👋                                                │
│                                                                         │
│  ┌─────────────────────────┐  ┌─────────────────────────┐             │
│  │ QUICK TRAIN             │  │ ACTIVE RACES            │             │
│  │                         │  │                         │             │
│  │ ┌─────────────────────┐ │  │ ┌─────────────────────┐ │             │
│  │ │ 📍 Drag Strip       │ │  │ │ 🏆 Spring Finals    │ │             │
│  │ │ Generation: 47/100  │ │  │ │ Starts in: 2h 15m   │ │             │
│  │ │ Best Time: 17.2s    │ │  │ │ Prize: 500 points   │ │             │
│  │ │ [Continue Training→]│ │  │ │ [Join Tournament →] │ │             │
│  │ └─────────────────────┘ │  │ └─────────────────────┘ │             │
│  │                         │  │                         │             │
│  │ + Start New Training    │  │ 📅 Upcoming Events      │             │
│  │                         │  │ • Daily Race (6h)       │             │
│  │ Recent Saves:           │  │ • Week Finals (2d)      │             │
│  │ • Oval Gen50 (May 19)   │  │                         │             │
│  │ • Rally Gen30 (May 18)  │  │ [View All Races →]      │             │
│  └─────────────────────────┘  └─────────────────────────┘             │
│                                                                         │
│  ┌─────────────────────────┐  ┌─────────────────────────┐             │
│  │ YOUR DRIVERS            │  │ ACHIEVEMENTS            │             │
│  │                         │  │                         │             │
│  │ 🏁 Drag Expert          │  │ ⭐ First Win (May 10)  │             │
│  │    Best: 17.2s (#45)    │  │ ⭐ Generation 50        │             │
│  │                         │  │ ⭐ 10 Races Complete    │             │
│  │ 🔄 Oval Rookie          │  │ 🔒 Podium Finish 10x   │             │
│  │    Best: 24.8s (#112)   │  │ 🔒 Master All Tracks   │             │
│  │                         │  │                         │             │
│  │ 🏔️ Rally Ghost         │  │ Progress: 5/20          │             │
│  │    Training...          │  │ Next: Speed Demon       │             │
│  │                         │  │                         │             │
│  │ [View All 3 Drivers →]  │  │ [View All →]            │             │
│  └─────────────────────────┘  └─────────────────────────┘             │
│                                                                         │
│  ┌───────────────────────────────────────────────────────────────────┐ │
│  │ 📊 PERFORMANCE SNAPSHOT                                           │ │
│  │                                                                   │ │
│  │  Races: 45    Wins: 12 (27%)    Global Rank: #342 (↑15)         │ │
│  │                                                                   │ │
│  │  Win Rate Over Time                                              │ │
│  │  [Line Chart: Last 30 days showing trend]                        │ │
│  │                                                                   │ │
│  └───────────────────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────────────────┘
```

### 2. Training Environment (Desktop - Immersive)

```
┌────────────────────────────────────────────────────────────────────────┐
│  🏁 Training: Drag Strip Alpha         [Save] [Load]      [@User▾]     │
├────┬───────────────────────────────────────────────────────────┬────────┤
│    │                                                           │        │
│    │                                                           │ LIVE   │
│ T  │                                                           │        │
│ R  │          SIMULATION CANVAS (800x600)                      │ Gen 23 │
│ A  │                                                           │        │
│ C  │          [Racing dots with ROYGBIV gradient]              │ Finish │
│ K  │                                                           │ 12/50  │
│ S  │          [Start/finish markers]                           │        │
│    │          [Barriers visualized]                            │ Alive  │
│ □  │                                                           │ 38/50  │
│ 1  │          [HUD overlay: Gen, Stats]                        │        │
│ □  │                                                           │ Top    │
│ 2  │                                                           │ #3     │
│ □  │                                                           │ 18.2s  │
│ 3  │                                                           │        │
│ □  │                                                           │ Avg    │
│ 4  │                                                           │ Fit    │
│ □  │                                                           │ 485    │
│ 5  │                                                           │        │
│ □  │                                                           │ Best   │
│ 6  │                                                           │ Fit    │
│    │                                                           │ 1,240  │
└────┴───────────────────────────────────────────────────────────┴────────┘
│                                                                         │
│  ┌───────────────────────────────────────────────────────────────────┐ │
│  │ [▶ Play] [⏸ Pause] [⏩ Fast] [⏭ Skip Gen]  Speed: [1x▾]          │ │
│  └───────────────────────────────────────────────────────────────────┘ │
│                                                                         │
│  ┌──────────────────────────┐  ┌──────────────────────────────────────┐│
│  │ CONFIGURATION            │  │ PROGRESS CHARTS                      ││
│  │                          │  │                                      ││
│  │ Algorithm: [Genetic ▾]   │  │ Fitness Over Generations             ││
│  │ Population: [50]         │  │ [Line chart with trend]              ││
│  │ Advance: [25]            │  │                                      ││
│  │ Mutation: [0.01]         │  │ Finishers Over Generations           ││
│  │ Brain Size: [800]        │  │ [Line chart showing improvement]     ││
│  │                          │  │                                      ││
│  │ [Reset] [Apply Changes]  │  │ Best Time: 17.2s (Gen 47)            ││
│  │                          │  │ [View Details →]                     ││
│  └──────────────────────────┘  └──────────────────────────────────────┘│
└────────────────────────────────────────────────────────────────────────┘
```

### 3. Vehicle Configuration (Desktop)

```
┌────────────────────────────────────────────────────────────────────────┐
│  🏁 Vehicle Configuration                                  [@User▾]    │
├────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌────────────────────────┐  ┌─────────────────────────────────────┐  │
│  │                        │  │ DRIVER CONFIGURATION                │  │
│  │                        │  │                                     │  │
│  │   [3D DOT PREVIEW]     │  │ Name: [Speed Demon            ]     │  │
│  │                        │  │ Color: [🔴 Red            ▾]       │  │
│  │   [Rotating view]      │  │ Avatar: [Upload Image]              │  │
│  │   [Your customization] │  │                                     │  │
│  │                        │  │ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │  │
│  │   [Drag to rotate]     │  │                                     │  │
│  │                        │  │ SENSORS (Budget: 150 points)        │  │
│  └────────────────────────┘  │                                     │  │
│                               │ ☑ Distance Sensor                   │  │
│  CURRENT STATS                │   Level: [1] [2] [3-Locked]         │  │
│  ┌──────────────────────┐    │   Cost: 50 points                   │  │
│  │ Speed:    ████░ 4/5  │    │   Info: ℹ Detect nearby barriers    │  │
│  │ Handling: ███░░ 3/5  │    │                                     │  │
│  │ Braking:  ██░░░ 2/5  │    │ ☑ Speed Sensor                      │  │
│  │ Sensors:  ██░░░ 2/5  │    │   Level: [1] [2-Locked] [3-Locked]  │  │
│  │ Actions:  ███░░ 3/5  │    │   Cost: 25 points                   │  │
│  └──────────────────────┘    │   Info: ℹ Know current velocity     │  │
│                               │                                     │  │
│  UPGRADE POINTS               │ ☐ Position Sensor [Locked]          │  │
│  Available: 50                │   Unlock: Reach Gen 50              │  │
│  Earned: 250                  │   Cost: 25 points                   │  │
│  Used: 200                    │                                     │  │
│                               │ ☐ Velocity Vector [Locked]          │  │
│  [Earn More Points →]         │   Unlock: Win 10 races              │  │
│                               │   Cost: 25 points                   │  │
│                               │                                     │  │
│                               │ Spent: 75 / Available: 50 ⚠️       │  │
│                               │                                     │  │
│                               │ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │  │
│                               │                                     │  │
│                               │ ACTIONS (Budget: 100 points)        │  │
│                               │                                     │  │
│                               │ ☑ Accelerate                        │  │
│                               │   Level: [1] [2] [3-Locked]         │  │
│                               │   Cost: 40 points                   │  │
│                               │                                     │  │
│                               │ ☑ Turn                              │  │
│                               │   Level: [1] [2-Locked] [3-Locked]  │  │
│                               │   Cost: 30 points                   │  │
│                               │                                     │  │
│                               │ ☐ Brake [Locked]                    │  │
│                               │   Unlock: Complete Tutorial         │  │
│                               │   Cost: 30 points                   │  │
│                               │                                     │  │
│                               │ Spent: 70 / Available: 30           │  │
│                               │                                     │  │
│                               │ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │  │
│                               │                                     │  │
│                               │ ALGORITHM                           │  │
│                               │                                     │  │
│                               │ Type: [Genetic Algorithm    ▾]      │  │
│                               │ ℹ️ Evolves through generations      │  │
│                               │                                     │  │
│                               │ Brain Size: [800]                   │  │
│                               │ Mutation Rate: [0.01]               │  │
│                               │                                     │  │
│                               │ 🔒 Q-Learning (Unlock: 500pts)      │  │
│                               │ 🔒 NEAT (Unlock: 1000pts)           │  │
│                               │                                     │  │
│                               │ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │  │
│                               │                                     │  │
│                               │ [Reset to Default] [Save] [Apply]   │  │
│                               └─────────────────────────────────────┘  │
│                                                                         │
│  💡 Tip: Balance your points! More sensors help, but you need actions  │
│     to use what you learn. Experiment to find the best combination!    │
│                                                                         │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 🎯 Component Library Needed

Based on these wireframes, we need:

### Navigation
- [ ] Top navigation bar
- [ ] Mobile hamburger menu
- [ ] Bottom mobile navigation
- [ ] Breadcrumbs

### Cards
- [ ] Dashboard card
- [ ] Stat card (KPI)
- [ ] Driver card
- [ ] Achievement card
- [ ] Event card

### Forms
- [ ] Text input
- [ ] Dropdown select
- [ ] Checkbox
- [ ] Toggle switch
- [ ] Slider
- [ ] File upload

### Data Display
- [ ] Progress bar
- [ ] Stats bars (horizontal)
- [ ] Line chart
- [ ] Leaderboard list
- [ ] Activity feed

### Actions
- [ ] Primary button
- [ ] Secondary button
- [ ] Icon button
- [ ] Button group (play/pause/etc)

### Feedback
- [ ] Toast notification
- [ ] Modal dialog
- [ ] Loading skeleton
- [ ] Empty state
- [ ] Error state

### Canvas
- [ ] Simulation canvas wrapper
- [ ] HUD overlay
- [ ] Live stats panel
- [ ] Track selector

---

## 🚀 Next: Convert to Figma

These ASCII wireframes should be converted to proper designs:

1. **Figma Setup**
   - Create design system with colors, typography, spacing
   - Build component library
   - Create reusable templates

2. **Detailed Screens**
   - All 17 screens from UI_REQUIREMENTS.md
   - Desktop (1440px) and Mobile (375px) variants
   - Interactive prototype with clickable flows

3. **User Testing**
   - Share prototype with 5-10 target users
   - Collect feedback on usability
   - Iterate on designs

Would you like me to help with:
- Creating a Figma file structure?
- Defining the component system in detail?
- User flow diagrams?
