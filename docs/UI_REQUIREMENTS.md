# UI/UX Requirements & Wireframing Plan
**Dot Car Derby - User Interface Design**

**Date**: May 20, 2026  
**Status**: Planning Phase  
**Priority**: HIGH - Critical path for MVP

---

## 🎯 Design Philosophy

### Core Principles
1. **Education First** - Learning ML should feel natural, not academic
2. **Progressive Disclosure** - Start simple, reveal complexity gradually  
3. **Immediate Feedback** - Show results in real-time
4. **Friendly Competition** - Motivate through rankings without toxicity
5. **Mobile-Friendly** - Works on phones, optimized for desktop

### Target Users
- **Primary**: STEM students (ages 14-22)
- **Secondary**: Hobbyist programmers learning ML
- **Tertiary**: Educators teaching ML concepts

---

## 📱 Screen Inventory

### Public Screens (No Auth Required)
1. **Landing Page** - First impression, value proposition
2. **About/How It Works** - Educational content, ML concepts explained
3. **Public Leaderboard** - Top performers, inspire new users
4. **GitHub Link** - Open source community

### Authentication Flow
5. **Login/Signup** - OAuth (Google, GitHub) + email
6. **Onboarding Tutorial** - First-time user experience (CRITICAL)

### Authenticated Screens
7. **Dashboard** - Command center, main hub
8. **Training Environment** - Watch dots learn in real-time
9. **Testing Environment** - Validate trained drivers
10. **Competition/Racing** - Enter tournaments, compete
11. **Vehicle Configuration** - Customize car/driver settings
12. **Performance Metrics** - Analytics, charts, insights
13. **User Profile** - Settings, achievements, stats
14. **Track Selection** - Browse and select tracks
15. **DNA/Model Library** - Save/load trained models
16. **Tournament Lobby** - Join/create competitions
17. **Replay Viewer** - Watch past races

---

## 🗺️ Navigation Structure

### Primary Navigation (Always Visible)
```
┌─────────────────────────────────────────────────────────┐
│  🏁 Dot Car Derby    [Train] [Race] [Stats] [Profile]  │
└─────────────────────────────────────────────────────────┘
```

**Components:**
- Logo/Home button (left)
- Primary actions: Train, Race, Stats (center)
- User menu: Notifications, Profile, Settings (right)
- Points balance display (top-right, near profile)

### Secondary Navigation (Context-Dependent)

#### Training Section
- Track selector dropdown
- Algorithm selector (Genetic/Q-Learning/NEAT)
- Population settings
- Save/Load buttons

#### Racing Section
- Tournament browser
- Quick race
- Challenge friend
- Race history

#### Stats Section
- Overview dashboard
- Track performance
- Driver rankings
- Achievement progress

---

## 📐 Wireframe Specifications

### 1. Landing Page

**Layout:** Hero + Features + CTA

```
┌────────────────────────────────────────────────────────┐
│  [Logo] Dot Car Derby       [About] [Leaderboard] [Login]  
│                                                         │
│         ┌─────────────────────────────────┐           │
│         │   HERO SECTION                  │           │
│         │   Animated racing dots          │           │
│         │                                  │           │
│         │   "Train AI Racers"              │           │
│         │   "Learn Machine Learning"       │           │
│         │                                  │           │
│         │   [Get Started Free] [Watch Demo]│           │
│         └─────────────────────────────────┘           │
│                                                         │
│   ┌─────────┐  ┌─────────┐  ┌─────────┐              │
│   │ FEATURE │  │ FEATURE │  │ FEATURE │              │
│   │   #1    │  │   #2    │  │   #3    │              │
│   │  Train  │  │  Race   │  │  Learn  │              │
│   └─────────┘  └─────────┘  └─────────┘              │
│                                                         │
│   Recent Champions (Live feed)                         │
│   ┌──────────────────────────────────────┐            │
│   │ @user123 just finished Drag Strip!   │            │
│   │ @racer99 reached Gen 50 on Oval!     │            │
│   └──────────────────────────────────────┘            │
└────────────────────────────────────────────────────────┘
```

**Key Elements:**
- Animated preview of dots racing (eye-catching)
- Clear value propositions (3 pillars: Train, Race, Learn)
- Social proof (recent activity, user count)
- Strong CTAs (Get Started, Watch Demo)

---

### 2. Dashboard (Main Hub)

**Layout:** Card-based, responsive grid

```
┌────────────────────────────────────────────────────────┐
│  🏁 Dot Car Derby    [Train] [Race] [Stats] [@User ▾]  │
├────────────────────────────────────────────────────────┤
│                                                         │
│  Welcome back, User! 👋          Points: 1,250 🏆      │
│                                                         │
│  ┌──────────────────┐  ┌──────────────────┐           │
│  │  QUICK TRAIN     │  │  ACTIVE RACES    │           │
│  │  ┌────────────┐  │  │  ┌────────────┐  │           │
│  │  │ Drag Strip │  │  │  │ Tournament │  │           │
│  │  │ Gen 47/100 │  │  │  │ Starting   │  │           │
│  │  │ [Continue] │  │  │  │ in 2h 15m  │  │           │
│  │  └────────────┘  │  │  │ [Join Now] │  │           │
│  │  + Start New     │  │  └────────────┘  │           │
│  └──────────────────┘  └──────────────────┘           │
│                                                         │
│  ┌──────────────────┐  ┌──────────────────┐           │
│  │  YOUR DRIVERS    │  │  ACHIEVEMENTS    │           │
│  │  • Drag Expert   │  │  ⭐ First Win   │           │
│  │  • Oval Rookie   │  │  ⭐ Gen 50      │           │
│  │  • Rally Ghost   │  │  🔒 Podium 10x  │           │
│  │  [View All]      │  │  [View All]      │           │
│  └──────────────────┘  └──────────────────┘           │
│                                                         │
│  📊 PERFORMANCE SNAPSHOT                               │
│  ┌────────────────────────────────────────┐           │
│  │  Wins: 12  |  Races: 45  |  Rank: #342 │           │
│  │  [Chart: Win rate over time]            │           │
│  └────────────────────────────────────────┘           │
└────────────────────────────────────────────────────────┘
```

**Key Elements:**
- Welcome message (personalized)
- Points balance (prominent, gamification)
- Quick actions (resume training, join race)
- Progress indicators (generation count, time remaining)
- Driver library preview
- Achievement showcase
- Performance snapshot

---

### 3. Training Environment

**Layout:** Full-screen simulation with side panels

```
┌────────────────────────────────────────────────────────┐
│  🏁 Training: Drag Strip Alpha              [@User ▾]  │
├────────────────────────────────────────────────────────┤
│ ┌─────────┐                                            │
│ │ TRACKS  │  ┌──────────────────────────────┐  ┌────┐│
│ │         │  │                              │  │LIVE││
│ │ Drag ✓  │  │    SIMULATION CANVAS         │  │    ││
│ │ Oval    │  │                              │  │Gen ││
│ │ Rally   │  │    [Racing dots visualized]  │  │ 23 ││
│ │ Daytona │  │                              │  │    ││
│ │ Indy    │  │    [ROYGBIV gradient colors] │  │Top ││
│ │ Maniac  │  │                              │  │ 12 ││
│ │         │  │    [HUD overlay]             │  │fin ││
│ └─────────┘  └──────────────────────────────┘  │    ││
│                                                  │Avg ││
│ ┌──────────────────────────────────────────┐   │Fit ││
│ │ CONTROLS                                  │   │320 ││
│ │ [▶ Play] [⏸ Pause] [⏩ Fast] [⏭ Skip Gen]│   └────┘│
│ │ Speed: [1x] [2x] [5x] [10x]              │         │
│ └──────────────────────────────────────────┘         │
│                                                        │
│ ┌──────────────────────────────────────────┐         │
│ │ CONFIGURATION                             │         │
│ │ Algorithm: [Genetic ▾]                    │         │
│ │ Population: [50 ▾]  Top: [25 ▾]          │         │
│ │ Mutation: [0.01]    Brain: [800]         │         │
│ │ [Save DNA] [Load DNA] [Export]            │         │
│ └──────────────────────────────────────────┘         │
│                                                        │
│ ┌──────────────────────────────────────────┐         │
│ │ PROGRESS CHART                            │         │
│ │ [Line graph: Fitness over generations]    │         │
│ │ [Line graph: Finishers over generations]  │         │
│ └──────────────────────────────────────────┘         │
└────────────────────────────────────────────────────────┘
```

**Key Elements:**
- Large simulation canvas (primary focus)
- Track selector (quick switching)
- Live stats (generation, finishers, fitness)
- Playback controls (play/pause/speed)
- Configuration panel (algorithm, parameters)
- Progress charts (real-time updates)
- Save/Load DNA functionality

---

### 4. Competition/Racing Screen

**Layout:** Multi-racer view with leaderboard

```
┌────────────────────────────────────────────────────────┐
│  🏁 Race: Spring Tournament - Finals      [@User ▾]    │
├────────────────────────────────────────────────────────┤
│                                                         │
│  ┌──────────────────────────────────────┐  ┌────────┐ │
│  │                                      │  │ LIVE   │ │
│  │     RACE CANVAS                      │  │ RANKS  │ │
│  │     [8 dots racing]                  │  │        │ │
│  │                                      │  │ 1. You │ │
│  │     Track: Oval 99                   │  │ 2. Bot2│ │
│  │                                      │  │ 3. Bot5│ │
│  │     Lap 2/3                          │  │ 4. Bot1│ │
│  │                                      │  │ 5. Bot3│ │
│  │                                      │  │ 6. Bot4│ │
│  └──────────────────────────────────────┘  │ 7. Bot6│ │
│                                             │ 8. Bot7│ │
│  Your Position: 🥇 1st                     └────────┘ │
│  Current Lap Time: 18.4s                               │
│  Best Lap: 17.9s                                       │
│                                                         │
│  ┌──────────────────────────────────────┐             │
│  │ CHAT / SPECTATORS                    │             │
│  │ @user123: Nice move!                 │             │
│  │ @racer99: GG!                         │             │
│  └──────────────────────────────────────┘             │
└────────────────────────────────────────────────────────┘
```

**Key Elements:**
- Race visualization (all competitors)
- Live leaderboard (updating positions)
- Lap times and stats
- Chat/social features
- Your position highlighted
- Spectator count

---

### 5. Vehicle Configuration

**Layout:** Split view - visual + settings

```
┌────────────────────────────────────────────────────────┐
│  🏁 Vehicle Configuration                  [@User ▾]    │
├────────────────────────────────────────────────────────┤
│                                                         │
│  ┌──────────────────┐  ┌──────────────────────────┐   │
│  │                  │  │ DRIVER                   │   │
│  │   3D PREVIEW     │  │ Name: [Speed Demon    ]  │   │
│  │                  │  │ Color: [🔴 Red      ▾]  │   │
│  │   [Your Dot]     │  │                          │   │
│  │                  │  │ SENSORS (Points: 150)    │   │
│  │   [Rotate view]  │  │ ☑ Distance [Lvl 2] (50)  │   │
│  │                  │  │ ☑ Speed [Lvl 1] (25)     │   │
│  └──────────────────┘  │ ☐ Position [Lvl 1] (25)  │   │
│                        │ ☐ Velocity [Lvl 1] (25)  │   │
│  VEHICLE STATS         │ Available: 50 points     │   │
│  Speed:     ████░ 4/5  │                          │   │
│  Handling:  ███░░ 3/5  │ ACTIONS (Points: 100)    │   │
│  Braking:   ██░░░ 2/5  │ ☑ Accelerate [Lvl 2](40) │   │
│                        │ ☑ Turn [Lvl 1] (30)      │   │
│                        │ ☐ Brake [Lvl 1] (30)     │   │
│                        │ Available: 30 points     │   │
│                        │                          │   │
│                        │ ALGORITHM                │   │
│                        │ Type: [Genetic    ▾]     │   │
│                        │ Brain Size: [800     ]   │   │
│                        │ Mutation: [0.01      ]   │   │
│                        │                          │   │
│                        │ [Reset] [Save] [Apply]   │   │
│                        └──────────────────────────┘   │
│                                                         │
│  💡 Tip: More sensors help learning but cost points!   │
└────────────────────────────────────────────────────────┘
```

**Key Elements:**
- Visual preview (make it feel tangible)
- Sensor selection (checkboxes, point cost)
- Action selection (upgrades)
- Algorithm selector
- Point budget system (progression mechanic)
- Stats visualization
- Helpful tips

---

### 6. Performance Metrics

**Layout:** Analytics dashboard

```
┌────────────────────────────────────────────────────────┐
│  🏁 Performance Metrics                    [@User ▾]    │
├────────────────────────────────────────────────────────┤
│                                                         │
│  OVERVIEW                     Last 30 Days             │
│  ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐         │
│  │ Races  │ │  Wins  │ │  Rank  │ │ Points │         │
│  │   45   │ │   12   │ │  #342  │ │ 1,250  │         │
│  │   +5   │ │   +2   │ │  ↑15   │ │  +150  │         │
│  └────────┘ └────────┘ └────────┘ └────────┘         │
│                                                         │
│  ┌──────────────────────────────────────────┐         │
│  │ WIN RATE OVER TIME                        │         │
│  │ [Line chart: 30-day trend]                │         │
│  └──────────────────────────────────────────┘         │
│                                                         │
│  ┌──────────────────────────────────────────┐         │
│  │ PERFORMANCE BY TRACK                      │         │
│  │ Drag Strip:    ████████░░ 80% (12/15)     │         │
│  │ Oval 99:       ██████░░░░ 60% (6/10)      │         │
│  │ Rally Course:  ████░░░░░░ 40% (4/10)      │         │
│  │ Daytona:       ███████░░░ 70% (7/10)      │         │
│  │ Indy Circuit:  ████░░░░░░ 40% (2/5)       │         │
│  │ Maniac Mayhem: ██░░░░░░░░ 20% (1/5)       │         │
│  └──────────────────────────────────────────┘         │
│                                                         │
│  ┌──────────────────────────────────────────┐         │
│  │ BEST TIMES                                │         │
│  │ Drag Strip:  17.2s  (Global #45)          │         │
│  │ Oval 99:     24.8s  (Global #112)         │         │
│  │ ...                                       │         │
│  └──────────────────────────────────────────┘         │
└────────────────────────────────────────────────────────┘
```

**Key Elements:**
- KPI cards (races, wins, rank, points)
- Trend indicators (up/down arrows)
- Win rate chart
- Per-track breakdown
- Best times with global ranking
- Downloadable reports

---

## 🎨 Visual Design System

### Color Palette

#### Primary Colors
- **Brand Blue**: `#2E86C1` - Primary actions, links
- **Success Green**: `#28B463` - Positive actions, wins
- **Warning Yellow**: `#F39C12` - Cautions, pending
- **Danger Red**: `#E74C3C` - Errors, eliminations

#### ROYGBIV Gradient (Racing)
- Already defined in prototype (Red → Orange → Yellow → Green → Blue → Indigo → Violet)

#### Neutrals
- **Background Dark**: `#121212` - Main background
- **Surface**: `#1E1E1E` - Cards, panels
- **Border**: `#333333` - Dividers
- **Text Primary**: `#FFFFFF` - Main text
- **Text Secondary**: `#B0B0B0` - Secondary text

### Typography

#### Fonts
```css
--font-heading: 'Orbitron', sans-serif;  /* Futuristic, racing theme */
--font-body: 'Inter', sans-serif;        /* Clean, readable */
--font-mono: 'JetBrains Mono', monospace; /* Code, stats */
```

#### Hierarchy
- **H1**: 48px, Bold - Page titles
- **H2**: 36px, Bold - Section headers
- **H3**: 24px, Semibold - Card titles
- **Body**: 16px, Regular - Main text
- **Small**: 14px, Regular - Labels, captions
- **Tiny**: 12px, Regular - Metadata

### Spacing System
```
4px, 8px, 16px, 24px, 32px, 48px, 64px
```

### Components

#### Buttons
- **Primary**: Filled, Brand Blue, White text
- **Secondary**: Outlined, Border only
- **Ghost**: Text only, no border
- **Danger**: Filled, Danger Red

#### Cards
- Background: Surface color
- Border: 1px solid Border color
- Border radius: 8px
- Shadow: Subtle elevation
- Padding: 24px

#### Inputs
- Background: Dark with subtle border
- Focus: Brand Blue border
- Error: Danger Red border
- Labels: Small text, Secondary color

---

## 🎬 Animations & Interactions

### Micro-interactions
1. **Button Hover**: Scale 1.02, transition 150ms
2. **Card Hover**: Lift (shadow increase), 200ms
3. **Progress Bars**: Animate fill on load
4. **Notifications**: Slide in from top-right
5. **Loading States**: Skeleton screens (not spinners)

### Page Transitions
- Fade: 200ms for simple changes
- Slide: 300ms for navigation
- No animations on slow connections

### Racing Simulation
- 60 FPS target
- Smooth dot movement (interpolation)
- Particle effects on crashes (optional)
- Trail effects for fast dots

---

## 📱 Responsive Breakpoints

```css
/* Mobile first approach */
--mobile: 320px;      /* Phones */
--tablet: 768px;      /* Tablets */
--desktop: 1024px;    /* Small desktop */
--large: 1440px;      /* Large desktop */
--xlarge: 1920px;     /* 4K displays */
```

### Mobile Adaptations
- Stack cards vertically
- Hamburger menu for navigation
- Bottom navigation for primary actions
- Smaller simulation canvas
- Simplified charts (fewer data points)

---

## ♿ Accessibility

### WCAG 2.1 AA Compliance
- [x] Color contrast 4.5:1 minimum
- [x] Keyboard navigation support
- [x] Screen reader compatible
- [x] Focus indicators visible
- [x] Alt text for all images
- [x] Aria labels for interactive elements

### Special Considerations
- Colorblind-friendly (not relying solely on ROYGBIV)
- Text alternatives for charts
- Pause/stop controls for animations
- Reduced motion mode support

---

## 🎓 Onboarding Flow (CRITICAL)

### First-Time User Experience

#### Step 1: Welcome (Landing)
"Welcome to Dot Car Derby! Learn machine learning by training AI racers."
- [Skip Tutorial] [Start Tutorial]

#### Step 2: Concept Introduction
"Your dot racer starts with random movements. Through training, it learns to navigate tracks."
- [Visual: Random dot crashing]
- [Next]

#### Step 3: Training Basics
"Watch as your dot tries different strategies. The best performers pass their 'DNA' to the next generation."
- [Visual: Population evolution]
- [Next]

#### Step 4: Interactive Training
"Try it yourself! Press Start and watch generation 1."
- [Simplified training environment]
- [Start Training]
- [Auto-advance after Gen 3]

#### Step 5: Algorithm Selection
"You used Genetic Algorithms! Later, unlock Q-Learning and NEAT for different strategies."
- [Show locked algorithms]
- [Next]

#### Step 6: Points & Progression
"Earn points by completing races. Use points to unlock better sensors and actions."
- [Show point system]
- [Next]

#### Step 7: Competition
"Race against other players in tournaments. Climb the leaderboard!"
- [Show leaderboard preview]
- [Next]

#### Step 8: Dashboard Tour
"Here's your command center. Start training, join races, or check your stats anytime."
- [Highlight navigation]
- [Finish Tutorial]

**Total Time**: 3-5 minutes  
**Completion Reward**: 100 starter points + "Tutorial Complete" achievement

---

## 🚀 Priority for MVP

### Must-Have (P0)
- [ ] Landing page
- [ ] Login/Auth
- [ ] Dashboard
- [ ] Training environment (basic)
- [ ] Track selection
- [ ] Save/Load DNA
- [ ] Public leaderboard
- [ ] Onboarding tutorial

### Should-Have (P1)
- [ ] Performance metrics
- [ ] User profile
- [ ] Vehicle configuration
- [ ] Achievement system
- [ ] Race replay viewer

### Nice-to-Have (P2)
- [ ] Competition/tournaments
- [ ] Chat/social features
- [ ] 3D vehicle preview
- [ ] Advanced analytics
- [ ] Mobile app

---

## 🎯 Next Steps

### Week 1: Wireframing
- [ ] Create detailed wireframes for all P0 screens
- [ ] User flow diagrams
- [ ] Interactive prototype (Figma/Sketch)
- [ ] User testing with 5-10 target users

### Week 2: Visual Design
- [ ] Design system in Figma
- [ ] Component library
- [ ] Icon set
- [ ] Marketing assets

### Week 3: Development Setup
- [ ] React component structure
- [ ] Styling system (CSS-in-JS vs Tailwind)
- [ ] Storybook for components
- [ ] Accessibility testing setup

---

## 📊 Success Metrics

### User Engagement
- **Onboarding Completion**: >70%
- **Return Rate (Day 7)**: >40%
- **Training Sessions per User**: >5
- **Avg Session Duration**: >10 minutes

### Performance
- **Page Load**: <2 seconds
- **Training FPS**: 60 (desktop), 30 (mobile)
- **Time to Interactive**: <3 seconds

### Conversion
- **Signup Rate**: >25% of landing visitors
- **Tutorial Completion**: >60%
- **First Race**: >50% of signups

---

## 💭 Open Questions

1. **Should we have a "sandbox mode" with no points/progression?**
2. **How to handle mobile training (reduced performance)?**
3. **Should we show other players' DNA/code?**
4. **Dark mode only or light mode option?**
5. **How to visualize complex algorithms (Q-learning, NEAT)?**
6. **Should we support custom track creation by users?**
7. **How to prevent cheating in tournaments?**
8. **Should we have a "coach mode" for educators?**

---

**Ready to create detailed wireframes?** 🎨
