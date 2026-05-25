# Dot AI Racer - Design Brief
**Product Design Vision & Specifications**

**Version**: 1.0  
**Date**: May 24, 2026  
**Project**: Dot AI Car Derby  
**Target Launch**: 2027  
**Development Approach**: Solo dev, iterative user stories, agile sprints

---

## 🎯 Project Vision

### Mission Statement
"To disarm the fear factor of AI and machine learning and expose players to a controlled environment where anyone can gain an understanding of fundamental ML concepts through engaging, hands-on experimentation with racing AI."

### Core Objectives
1. **Educational First**: Teach ML concepts (genetic algorithms, neural networks, fitness functions) through relatable metaphors and dual-mode explanations
2. **Addicting Gameplay**: Semi-idler mechanics - train dots, race opponents, climb leagues, unlock features
3. **Portfolio Showcase**: Demonstrate E2E game development, ML understanding, and approachable product design
4. **Open Source Community**: Share knowledge, accept donations, eventual sponsorships

### Target Audience
- **Primary**: Technical professionals and hobbyists seeking gamified ML learning
- **Secondary**: Complete beginners (16+) curious about AI with zero ML background
- **Skill Range**: Mixed technical levels - from "what is AI?" to data scientists wanting to experiment

---

## 🧠 Core Concept: Dual Explanation System

**The Innovation**: Toggle between two explanation modes throughout the entire experience.

### Mode 1: Layman's Terms (Default)
- Metaphorical explanations (Mr. Potato Head, natural selection, brain pathways)
- Simple language, relatable concepts
- Focus on "what does this do?" vs "how does it work?"
- Example: "This gives your dot 'eyes' to see walls ahead"

### Mode 2: Technical Terms (Advanced Toggle)
- Accurate ML terminology
- Scientific explanations
- Data science perspective
- Example: "Front proximity sensor provides normalized distance input to the neural network input layer"

**UI Implementation**:
- Global toggle in settings (persists across sessions)
- Inline toggle icon next to any technical term (👁️ or 🔬)
- Smooth transition - same UI, different copy
- "Learn More" expansions available in both modes

---

## 📚 Educational Framework

### Just-In-Time Documentation (Inspired by "The Farmer Was Replaced")
- New concepts unlock when first encountered
- Documentation pages added to user's library
- Searchable, revisitable knowledge base
- Progress tracker: "12/47 concepts learned"

### Three-Tier Learning Model

**Tier 1: Inline Tooltips** (5-10 words)
- Hover/tap any concept for quick definition
- Always visible, non-intrusive
- Example: `Fitness Function - How we measure success`

**Tier 2: "Learn More" Expansion** (2-3 sentences)
- Click tooltip for deeper explanation
- Includes metaphor + practical application
- Links to Tier 3 resources

**Tier 3: Documentation Library**
- Full articles, diagrams, examples
- External links to research papers, tutorials
- Best practices, advanced techniques

### Core Metaphors

| ML Concept | Technical Term | Layman's Metaphor |
|------------|----------------|-------------------|
| Genetic Algorithm | Evolutionary algorithm with selection, crossover, mutation | Logic that mimics natural selection - the best racers pass on their 'driving skills' to the next generation, with random variation for creativity |
| Neural Network | Multi-layer perceptron with activation functions | New experiences create pathways in your dot's brain, helping it learn what works and what doesn't |
| Fitness Function | Objective function optimized iteratively | A repeatable way of finding 'best' - make small adjustments until you get closer to the perfect racing skills |
| Sensors | Input layer features from environment state | Your dot's senses - what it can see and feel |
| Actions | Output layer controlling agent behavior | What your dot can do - speed up, turn, brake |
| Weights/Biases | Neural network parameters | How strongly your dot listens to each sense when making decisions |
| Overfitting | Model learns training data too specifically | When your dot memorizes one track perfectly but can't handle others |
| Mutation Rate | Probability of random parameter change | How often we try completely new ideas instead of tweaking what works |

---

## 🎮 Core Gameplay Loop

### The New User Journey (First 5 Minutes)

**1. Landing Page** (15 seconds)
- Hero animation: Dots training on drag strip
- CTA: "Get Started" 
- Value prop: "Learn AI by racing AI"

**2. Welcome Tutorial - "Training 101 in a Box"** (2 minutes)
- **Pre-configured Starter Dot**:
  - 3 sensors: Forward, Left, Right (Level 1)
  - 2 actions: Engine (Level 1), Suspension (Level 1)
  - Pre-trained: 10-20 epochs, can complete drag strip slowly
  - Bumps walls, imperfect, but functional
- **Visual: Mr. Potato Head Assembly**:
  - "Your dot needs eyes to see (sensors)"
  - "Legs to move (engine)"
  - "Arms to feel the sides (steering)"
- **Watch Phase**: Auto-plays 3 generations
  - Highlight: "Generation 1 → 2 → 3, getting smarter!"
  - Show fitness chart climbing
- **Explanation Phase**:
  - "See those sensors? They're your dot's eyes"
  - "The engine controls speed"
  - "Let's make it faster!"

**3. First Configuration Edit** (2 minutes)
- **Task**: "Make your dot avoid walls better"
- **Guided Steps**:
  1. Increase front sensor level (slider 1 → 3)
  2. Explanation: "Higher = dot cares more about walls ahead"
  3. Warning preview: "Too high? Dot might freeze up!"
- **Train Again**: Watch Gen 4-6
- **Result**: Faster lap time, fewer collisions
- **Reward**: +100 points, unlock save/load

**4. Dashboard Arrival** (30 seconds)
- "Welcome to your garage!"
- Available actions highlighted:
  - Continue training
  - Challenge time trial
  - View DNA library
- First achievement: "Training Complete! 🎉"

### Ongoing Gameplay Loop

```
Train → Configure → Race → Earn → Unlock → Repeat
  ↑                                              ↓
  └──────────── Climb Leagues ←─────────────────┘
```

**Idler Mechanics**:
- Training can run idle (background generations)
- Queue races while offline
- Check results on mobile (view-only)
- 5-minute active sessions, hours of passive progress

**Active Engagement**:
- Configuration tweaking (experimentation)
- Tournament participation (timed events)
- DNA library management (organize strategies)
- Rust League antics (creative experiments)

---

## 🎨 Visual Design System

### Aesthetic: Moderate Cyberpunk

**Inspiration**: Valorant UI (glowing edges, clean typography) meets educational product (accessible, not intimidating)

**Characteristics**:
- Dark backgrounds with neon accents
- Holographic-style cards and panels
- Subtle glow effects on interactive elements
- Animated accent lines for visual hierarchy
- Minimal scan-line effects (accessibility toggle)
- Clean, modern typography (not overly futuristic)

**Flexibility**:
- Dynamic theme system for accessibility (high contrast, colorblind modes)
- Custom race/event themes (special tournaments can have unique aesthetics)
- League-specific subtle accents (metallic tones for Tin/Iron/Steel/Titanium)

### Color Palette

#### Primary Colors
- **Cyan** (#00F0FF) - Primary accent, CTAs, success states
- **Magenta** (#FF00AA) - Secondary accent, highlights, premium features
- **Deep Purple** (#6B2FFF) - Tertiary accent, advanced features

#### Functional Colors
- **Success/Positive**: Neon Green (#00FF88)
- **Warning**: Electric Yellow (#FFD700)
- **Error/Danger**: Hot Pink/Red (#FF3366)
- **Info**: Sky Blue (#00AAFF)

#### Background & Neutrals
- **Primary BG**: Near-black (#0A0A0A)
- **Secondary BG**: Dark gray (#1A1A1A)
- **Surface**: Charcoal (#242424)
- **Border**: Muted gray (#404040)
- **Text Primary**: White (#FFFFFF)
- **Text Secondary**: Light gray (#B0B0B0)
- **Text Disabled**: Dark gray (#606060)

#### ROYGBIV Gradient (Performance Visualization)
- Red → Orange → Yellow → Green → Blue → Indigo → Violet
- Used for: Fitness progression, generation quality, performance tiers
- Accessible alternative: Green → Yellow → Red (traffic light model)

#### League Colors (Metallic Theme)
- **Tin League**: Dull gray (#8C8C8C)
- **Iron League**: Dark gunmetal (#505050)
- **Steel League**: Silver (#C0C0C0)
- **Titanium League**: Bright metallic (#E0E0E0)
- **Rust League**: Orange-brown (#CD7F32) - celebration badge

### Typography

**Heading Font**: Inter (700 weight)
- Modern, clean, excellent web rendering
- Sizes: H1 (36px), H2 (28px), H3 (22px), H4 (18px)

**Body Font**: Roboto (400 regular, 500 medium)
- Highly legible, technical feel
- Sizes: Body (16px), Small (14px), Caption (12px)

**Monospace Font**: Roboto Mono (400 weight)
- Used for: DNA codes, technical stats, data displays
- Size: Matches body (16px)

**Accessibility**:
- Minimum 16px body text
- 1.5 line height for paragraphs
- 1.2 line height for headings
- WCAG AA contrast ratios (4.5:1 minimum)

### Spacing System (8px Grid)

- **XXS**: 4px (tight inline spacing)
- **XS**: 8px (compact)
- **SM**: 16px (default)
- **MD**: 24px (comfortable)
- **LG**: 32px (spacious)
- **XL**: 48px (section breaks)
- **XXL**: 64px (major sections)

### Animation Principles

**Performance-Focused**:
- 60 FPS target at all times
- Hardware acceleration (CSS transforms)
- Reduced motion mode (respects `prefers-reduced-motion`)

**Timing**:
- **Micro-interactions**: 150ms (hover, focus states)
- **Transitions**: 300ms (panel opens, modals)
- **Page changes**: 500ms (route transitions)
- **Celebrations**: 1000ms (achievements, unlocks)

**Easing**:
- Default: `cubic-bezier(0.4, 0.0, 0.2, 1)` (Material Design standard)
- Bouncy: `cubic-bezier(0.68, -0.55, 0.265, 1.55)` (celebrations only)

**What to Animate**:
- ✅ Opacity (fades)
- ✅ Transform (position, scale, rotate)
- ✅ Background glow (neon effects)
- ❌ Width/Height (causes reflow)
- ❌ Box-shadow (performance hit)

---

## 🖼️ Screen Inventory & Priority

### MVP Phase 1 Screens (2026 Q2-Q3)

1. **Landing Page** ⭐ PRIORITY 1
   - Hero animation
   - Value proposition
   - CTA: Get Started
   - Social proof (GitHub stars, testimonials)

2. **Tutorial Flow** ⭐ PRIORITY 1
   - Welcome screen
   - Pre-configured dot demo
   - First configuration edit
   - First race
   - Dashboard introduction

3. **Dashboard** ⭐ PRIORITY 1
   - Active dots status
   - Quick actions (Train, Race, Configure)
   - Recent achievements
   - Points balance
   - Navigation hub

4. **Training Environment** ⭐ PRIORITY 1
   - Track visualization (drag strip)
   - Dot population display (20 default)
   - Generation counter
   - Fitness chart (real-time)
   - Controls: Play/Pause, Speed (1x, 2x, 5x, 10x)
   - Save DNA snapshot

5. **Vehicle Configuration** ⭐ PRIORITY 2
   - Sensor selection (3 available at start)
   - Action selection (2 available at start)
   - Brain size slider
   - Mutation rate slider
   - Dual explanation mode toggle
   - Preview stats
   - Save/Load templates

6. **DNA Library** ⭐ PRIORITY 2
   - Saved configurations grid
   - Search/filter
   - Rename, duplicate, delete
   - Export (JSON, CSV)
   - Import from file

7. **Racing - Time Trial** ⭐ PRIORITY 2
   - Select track
   - Select your DNA
   - Watch race simulation
   - Results: Lap time, comparison to best
   - Earn points

### Beta Phase Screens (2026 Q4)

8. **Leaderboards**
   - Global rankings
   - Track-specific rankings
   - Filter by league
   - Complexity-adjusted scores
   - View opponent DNA (research vision unlock)

9. **Profile & Stats**
   - User profile (badge display)
   - Training statistics
   - Racing statistics
   - Achievement showcase
   - DNA collection

10. **Settings**
    - Explanation mode (Layman/Technical)
    - Theme (Dark/Light, accessibility modes)
    - Performance (population limit, graphics)
    - Audio preferences
    - Export all data

### Full Launch Screens (2027)

11. **Leagues & Progression**
    - Current league display
    - Rank requirements
    - Promotion/demotion history
    - League-specific stats
    - Rust League opt-out

12. **Tournaments**
    - Daily/weekly/monthly schedule
    - Entry interface
    - Bracket/standings
    - Prize pools
    - Past results

13. **The Shop** (Community Features)
    - DNA sharing marketplace
    - Request assistance (forum-style)
    - Community voting
    - Earn points for helpful contributions

14. **Advanced Analytics**
    - Heatmaps (crash locations)
    - A/B comparison tools
    - DNA inspector (neural network visualization)
    - Performance predictor
    - Replay analyzer

15. **Documentation Library**
    - JIT-unlocked articles
    - Search documentation
    - External resource links
    - Concept progress tracker

---

## 🏗️ Component Library

### Atomic Design System

#### Atoms
- **Buttons**: Primary (cyan), Secondary (outline), Tertiary (text only), Danger (red)
- **Inputs**: Text field, Number slider, Toggle switch, Checkbox, Radio
- **Icons**: Consistent 24px iconography (Lucide or Heroicons)
- **Labels**: Badges, tags, status indicators
- **Tooltips**: Hover popover, click expansion
- **Loader**: Circular spinner (cyan), progress bar

#### Molecules
- **Stat Card**: Label + Value + Trend indicator
- **Sensor Card**: Icon + Name + Level + Description + Toggle
- **DNA Card**: Thumbnail + Name + Stats + Actions (Load/Delete/Export)
- **Achievement Toast**: Icon + Message + Points earned
- **Search Bar**: Input + Filter dropdown + Clear button
- **Explanation Block**: Title + Layman text + Technical text (toggle) + Learn More

#### Organisms
- **Navigation Bar**: Logo + Main nav + Profile dropdown + Points display
- **Training Panel**: Track view + Controls + Fitness chart + Generation counter
- **Configuration Form**: Sensors section + Actions section + Advanced settings + Save/Load
- **Leaderboard Table**: Rank + User + Score + DNA preview + View DNA button
- **Tournament Bracket**: Round nodes + Match connections + Winners path

#### Templates
- **Dashboard Layout**: Sidebar nav + Main content + Right panel (stats)
- **Full-screen Simulation**: Immersive view (training/racing) + Minimal UI overlay
- **Modal Layout**: Overlay + Card + Header + Content + Footer actions
- **Documentation Page**: Sidebar TOC + Article content + Related links

---

## 🎯 Key User Flows

### Flow 1: First-Time User → First Race (5 minutes)

```
Landing Page
  ↓ [Get Started]
Welcome Screen
  ↓ [Continue]
Watch Pre-trained Dot (Gen 1-3)
  ↓ [Automatic]
"Let's Make It Better!" Prompt
  ↓ [Edit Configuration]
Guided Sensor Adjustment
  ↓ [Train Again]
Watch Improved Dot (Gen 4-6)
  ↓ [Automatic]
"Ready to Race?" Prompt
  ↓ [Start Race]
Time Trial on Drag Strip
  ↓ [Automatic]
Results Screen
  ↓ [Go to Dashboard]
Dashboard (+ Achievement Toast)
```

### Flow 2: Returning User → Train & Race (2 minutes)

```
Dashboard
  ↓ [Select DNA from Library]
Training Environment
  ↓ [Play, watch 10 gens]
Save Improved DNA
  ↓ [Queue Race]
Select Tournament
  ↓ [Submit]
(Results delivered later)
  ↓ [Return to Dashboard]
Check Points Balance
```

### Flow 3: Advanced User → Experiment & Share (10 minutes)

```
Dashboard
  ↓ [New Configuration]
Vehicle Configuration
  ↓ [Advanced settings toggle]
Tweak Mutation Rate, Brain Size
  ↓ [Save as "Experiment_01"]
Training Environment (Rust League track)
  ↓ [Train 50 generations]
Weird behavior detected!
  ↓ [Rust League flag triggered]
"Your dot completed a lap backwards! 🎉"
  ↓ [View in Rust League]
Opt-in to Rust League ranking
  ↓ [Share DNA to community]
The Shop (post-MVP)
```

---

## 🎮 Rust League: Celebration of Creativity

### Philosophy
Rust League is **not a punishment** - it's a celebration of:
- Experimentation and risk-taking
- Creative solutions to racing challenges
- Glitches turned features
- Learning through failure ("fastest path to success")

### Trigger Behaviors
Dots flagged for Rust League when they exhibit:
- Completing lap in reverse
- Slowest lap time in history (epic failure)
- Behavior >3 standard deviations from norm
- Unique strategies (e.g., wall-riding, deliberate crashes)
- Intentional "goofy" configurations

### User Experience
- **Opt-out Available**: Settings toggle (default: opt-in)
- **Positive Messaging**: "🎉 Your dot broke physics! Welcome to Rust League!"
- **Unique Rewards**: Exclusive badges, rust-colored profile accent
- **Community Showcase**: "Best Fails of the Week" leaderboard
- **Educational Value**: "Why did this happen? Let's learn!"

### Visual Design
- Badge: Circular dot with rust texture (#CD7F32)
- Profile accent: Subtle rust glow on avatar border
- Rust League page: Warmer color scheme, playful animations
- No negative indicators (no red X's, warnings, or penalties)

---

## ♿ Accessibility Requirements

### WCAG 2.1 AA Compliance

**Visual**:
- Color contrast: Minimum 4.5:1 (text), 3:1 (UI components)
- Colorblind-friendly modes:
  - Deuteranopia (red-green)
  - Protanopia (red-green)
  - Tritanopia (blue-yellow)
- Text resize: Support up to 200% without horizontal scrolling
- Focus indicators: 2px cyan outline on all interactive elements

**Motor**:
- Keyboard navigation: 100% functionality without mouse
- Large click targets: Minimum 44×44px (mobile), 32×32px (desktop)
- No time-based interactions (or generous timeouts with warnings)
- Sticky headers/controls (no excessive scrolling)

**Cognitive**:
- Reduced motion mode (respects `prefers-reduced-motion`)
- Clear, consistent navigation
- Progressive disclosure (don't overwhelm)
- Error prevention + helpful error messages
- Undo/redo where possible

**Assistive Technology**:
- ARIA labels on all interactive elements
- Screen reader tested (NVDA, JAWS, VoiceOver)
- Semantic HTML (proper heading hierarchy)
- Alt text for all non-decorative images

---

## 📊 Success Metrics

### User Engagement
- **Tutorial Completion Rate**: Target >80%
- **Return User Rate (Day 7)**: Target >40%
- **Average Session Length**: Target 15-20 minutes
- **Idle Training Adoption**: Target >60% of users

### Educational Impact
- **Documentation Views**: Track most-viewed concepts
- **Explanation Mode**: Measure layman vs technical usage
- **"Learn More" Clicks**: Engagement with deeper learning
- **User Feedback**: Surveys on learning outcomes

### Gameplay
- **Generations Trained**: Average per user per week
- **Races Completed**: Daily/weekly active racing
- **DNA Saved**: Library size growth over time
- **Tournament Participation**: Entry rates for events

### Community (Post-MVP)
- **DNA Shares**: Upload/download from The Shop
- **Helpful Votes**: Quality of community assistance
- **Rust League Opt-in Rate**: % who embrace creativity league

### Technical
- **Performance**: 60 FPS at 100 dot population (target hardware)
- **Load Times**: <2 seconds (initial), <500ms (navigation)
- **Crash Rate**: <0.1% of sessions
- **Accessibility**: Pass automated + manual audits

---

## 🚀 Phased Rollout Plan

### 2026 Q2-Q3: MVP Development
**Focus**: Core training loop + educational foundation

**Deliverables**:
- Landing page
- Tutorial (Training 101 in a Box)
- Training environment (drag strip only)
- Basic vehicle configuration
- DNA library (save/load/export)
- Time trial racing
- Dashboard

**User Stories** (examples):
```
US-001: As a new user, I want to watch a pre-trained dot race 
        so I can understand what the game is about

US-002: As a beginner, I want to adjust sensor levels with sliders 
        so I can improve my dot without understanding ML

US-003: As a user, I want to toggle explanation modes 
        so I can learn at my preferred depth

US-004: As a trained dot owner, I want to save my DNA 
        so I can reuse successful configurations

US-005: As a competitive user, I want to race against my best time 
        so I can track improvement
```

### 2026 Q4: Beta Expansion
**Focus**: Competition + progression systems

**Additions**:
- Leaderboards (global + track-specific)
- Profile & achievements
- Settings & preferences
- 2 additional tracks (curves, obstacles)
- Research vision unlock (view DNA of defeated opponents)

### 2027 Q1-Q2: Full Launch Preparation
**Focus**: Social features + advanced systems

**Additions**:
- Leagues (Tin/Iron/Steel/Titanium/Rust)
- Tournaments (daily/weekly/monthly)
- Advanced analytics (heatmaps, comparisons)
- Documentation library (JIT unlocks)
- Performance optimizations

### 2027 Q3+: Community & Expansion
**Focus**: User-generated content + new challenges

**Additions**:
- The Shop (DNA sharing, community assistance)
- Stakes racing (pink-slip mechanics)
- Custom track editor (stretch goal)
- Mobile responsive optimization
- New challenge types beyond racing (post-MVP vision)

---

## 🛠️ Technical Constraints

### Platform
- **Primary**: Web browser (Chrome, Firefox, Safari)
- **Secondary**: Mobile web (responsive, view-only training)
- **Infrastructure**: Docker containerized, PostgreSQL database

### Performance Targets
- **60 FPS**: At 100 dot population on 2019+ hardware
- **Auto-scaling**: Reduce population on lower-end devices (with user override)
- **Offline Training**: Local storage, manual cloud sync when online
- **Load Times**: <2s initial, <500ms navigation

### Stack (Confirmed)
- **Frontend**: React 18+, TypeScript
- **Backend**: Node.js, Express
- **Database**: PostgreSQL 15+
- **ML**: TensorFlow.js (browser-based training)
- **Styling**: TBD (Tailwind CSS recommended for rapid development)

### Browser Support
- **Chrome**: Latest 2 versions
- **Firefox**: Latest 2 versions
- **Safari**: Latest 2 versions
- **Edge**: Latest 2 versions
- **Mobile**: iOS Safari 14+, Chrome Android 90+

---

## 💡 Design Principles

### 1. Education Without Intimidation
- Assume zero prior knowledge
- Use metaphors over jargon (with technical mode available)
- Celebrate failure as learning opportunity
- Progressive complexity (crawl → walk → run)

### 2. Engagement Through Agency
- Users make meaningful choices (sensor selection, configuration)
- Immediate visual feedback (watch dots improve)
- Clear cause-effect relationships (slider up = more wall avoidance)
- Experimentation encouraged (Rust League celebrates weirdness)

### 3. Accessibility as Core, Not Addon
- WCAG 2.1 AA from day one
- Colorblind modes built into design system
- Keyboard navigation tested throughout
- Reduced motion respected
- Dual explanation modes serve cognitive accessibility

### 4. Performance Over Polish
- 60 FPS non-negotiable
- Minimal graphics (focus on data)
- Efficient animations (hardware accelerated)
- Auto-scaling for device capabilities
- Educational value > visual spectacle

### 5. Community as Amplifier
- DNA sharing spreads knowledge
- The Shop helps struggling users
- Rust League normalizes failure
- Open source invites contribution
- Transparency builds trust

---

## 📋 Content Tone Guidelines

### Button Labels: Clear + Personal
- ✅ "Train My Racer" (active, personal)
- ✅ "Start Training" (clear action)
- ❌ "Train" (too terse)
- ❌ "Let's Learn!" (too cutesy)
- ❌ "Begin Evolution" (too technical for default)

### Error Messages: Friendly + Educational
**Scenario**: User tries to train without sensors

✅ **Good**:
"Oops! Your racer needs at least one sensor to see the track. 
Add a sensor to get started! 
[Learn about sensors →]"

❌ **Too Casual**:
"Hey, don't forget sensors lol"

❌ **Too Technical**:
"Error: Input layer requires minimum 1 feature. Configure sensors."

### Achievements: Celebration + Context
**Scenario**: User reaches Generation 50

✅ **Good**:
"Incredible! 50 generations trained 🎉
Your racer's brain has evolved through 50 cycles of selection and mutation.
+100 points!"

✅ **Layman Mode**:
"Wow! 50 generations! 🎉
Your dot has learned from 50 rounds of practice.
The best drivers taught the next generation how to improve.
+100 points!"

✅ **Technical Mode**:
"Milestone: 50 Generations 🎉
Genetic algorithm has completed 50 iterations of selection, crossover, and mutation.
Population fitness increased 340% from Generation 1.
+100 points!"

### Tooltips: Concise + Accurate
- **Layman**: "Sensors are your dot's eyes - help it see walls, turns, and obstacles"
- **Technical**: "Sensors provide normalized distance inputs to the neural network input layer"

---

## 🎨 Next Steps: Figma Design System

### Week 1: Foundation (May 27-31, 2026)
1. **Figma File Setup**
   - Create design system library
   - Define color styles (all palette variants)
   - Define text styles (all typography scales)
   - Define spacing tokens (8px grid)

2. **Component Library - Atoms**
   - Buttons (all variants + states)
   - Input fields (text, slider, toggle, checkbox)
   - Icons (24px set - sensor, action, stat icons)
   - Tooltips (hover + expanded states)
   - Badges (league, achievement, status)

3. **Component Library - Molecules**
   - Stat card
   - Sensor card (layman + technical variants)
   - DNA card
   - Achievement toast
   - Explanation block (dual mode)

### Week 2: Priority Screens (June 3-7, 2026)
1. **Landing Page** (desktop + mobile)
   - Hero section with dot animation
   - Value proposition
   - CTA
   - Social proof

2. **Tutorial Flow** (3-4 screens)
   - Welcome screen
   - Pre-trained dot demo view
   - First configuration edit
   - First race results

3. **Dashboard** (desktop + mobile)
   - Navigation
   - Quick action cards
   - Stats overview
   - Recent activity

### Week 3: Core Features (June 10-14, 2026)
1. **Training Environment** (full-screen immersive)
   - Track visualization (drag strip)
   - Dot population
   - Controls (play/pause/speed)
   - Fitness chart overlay

2. **Vehicle Configuration** (desktop)
   - Sensor selection cards
   - Action selection cards
   - Advanced sliders (brain size, mutation)
   - Dual explanation mode toggle
   - Save/load interface

### Week 4: Interactive Prototype (June 17-21, 2026)
1. **Link Screens** (Figma prototype)
   - New user flow: Landing → Tutorial → Dashboard → Training → Race
   - Returning user flow: Dashboard → Configure → Train → Race
   - Settings flow

2. **Add Micro-interactions**
   - Hover states
   - Focus states
   - Transitions between screens
   - Modal overlays

3. **Prepare for User Testing**
   - Create clickable prototype
   - Write test scenarios
   - Recruit 10-15 target users

---

## 📎 Appendix

### Visual References
1. **AI Learns To Drive** by ActivationFunction - Training visualization style
2. **Evolution** by Keiwan - Creature customization UI
3. **AIvolution** by Deeon & Lykke Studios - Educational integration
4. **Dr. Derks Mutant Battlegrounds** - Competition/tournament structure
5. **The Farmer Was Replaced** - JIT documentation system
6. **Valorant** - Moderate cyberpunk UI aesthetic
7. **Spotify** - Dark mode, clean typography

### Key Documents
- [Product Requirements Survey](PRODUCT_REQUIREMENTS_SURVEY.md) - Full user responses
- [Clarification Requests](CLARIFICATION_REQUESTS.md) - Design decisions
- [UI Requirements](UI_REQUIREMENTS.md) - Screen specifications
- [Wireframes](WIREFRAMES.md) - ASCII layouts
- [UI Roadmap](UI_ROADMAP.md) - Timeline and process

### Design Deliverables Checklist
- [ ] Figma design system library
- [ ] Component library (atoms, molecules, organisms)
- [ ] Landing page mockup (desktop + mobile)
- [ ] Tutorial flow (4 screens)
- [ ] Dashboard mockup (desktop + mobile)
- [ ] Training environment mockup (full-screen)
- [ ] Vehicle configuration mockup (desktop)
- [ ] DNA library mockup (desktop)
- [ ] Interactive prototype (clickable flows)
- [ ] Design handoff documentation (developer specs)
- [ ] Asset export (icons, logos, illustrations)

---

**Document Status**: ✅ Complete  
**Next Action**: Begin Figma design system setup (Week 1)  
**Owner**: Solo developer (design + implementation)  
**Review Cycle**: Iterative feedback throughout development

