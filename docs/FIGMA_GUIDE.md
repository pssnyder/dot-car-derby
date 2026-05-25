# Figma Design System Implementation Guide
**Practical Blueprint for Dot AI Racer UI/UX**

**Version**: 1.0  
**Date**: May 24, 2026  
**Status**: Ready to begin  
**Estimated Time**: 4 weeks (16-20 hours total)

---

## 📋 Table of Contents
1. [Figma Setup](#figma-setup)
2. [Week 1: Design System Foundation](#week-1-design-system-foundation)
3. [Week 2: Priority Screens](#week-2-priority-screens)
4. [Week 3: Core Features](#week-3-core-features)
5. [Week 4: Prototype & Handoff](#week-4-prototype--handoff)
6. [Quick Reference](#quick-reference)
7. [Troubleshooting](#troubleshooting)

---

## 🎨 Figma Setup

### Create Project Structure

```
Dot AI Racer (Project)
├── 📄 Design System (Page)
│   ├── Colors
│   ├── Typography
│   ├── Spacing
│   ├── Components
│   └── Icons
├── 📄 Screens - Desktop (Page)
│   ├── Landing Page
│   ├── Tutorial Flow
│   ├── Dashboard
│   ├── Training Environment
│   └── Configuration
├── 📄 Screens - Mobile (Page)
│   ├── Landing Page
│   ├── Dashboard
│   └── Settings
├── 📄 Prototype Flows (Page)
│   ├── New User Journey
│   ├── Returning User Journey
│   └── Advanced User Journey
└── 📄 Developer Handoff (Page)
    ├── Component Specs
    ├── Spacing Guide
    └── Interaction Notes
```

### Install Useful Plugins

**Essential**:
- **Iconify** - Quick access to icon libraries (use Lucide or Heroicons)
- **Color Blind** - Test colorblind accessibility
- **Stark** - Check contrast ratios (WCAG compliance)
- **Arc** - Create smooth curves for tracks

**Helpful**:
- **Content Reel** - Generate placeholder text/data
- **Figmotion** - Preview animations
- **Autoflow** - Create user flow arrows

---

## 🎯 Week 1: Design System Foundation
**Goal**: Build reusable components library  
**Time**: 4-5 hours  
**Priority**: Critical - everything else depends on this

### Day 1: Colors & Styles (1 hour)

#### Step 1: Create Color Styles

**In Figma**:
1. Select rectangle → Fill with color → Click "+" next to Style
2. Name using slash notation for grouping:

```
Primary/Cyan           #00F0FF
Primary/Magenta        #FF00AA
Primary/Deep Purple    #6B2FFF

Functional/Success     #00FF88
Functional/Warning     #FFD700
Functional/Error       #FF3366
Functional/Info        #00AAFF

Background/Primary     #0A0A0A
Background/Secondary   #1A1A1A
Background/Surface     #242424
Background/Border      #404040

Text/Primary           #FFFFFF
Text/Secondary         #B0B0B0
Text/Disabled          #606060

League/Tin             #8C8C8C
League/Iron            #505050
League/Steel           #C0C0C0
League/Titanium        #E0E0E0
League/Rust            #CD7F32

ROYGBIV/Red            #FF0000
ROYGBIV/Orange         #FF7F00
ROYGBIV/Yellow         #FFFF00
ROYGBIV/Green          #00FF00
ROYGBIV/Blue           #0000FF
ROYGBIV/Indigo         #4B0082
ROYGBIV/Violet         #9400D3
```

**Pro Tip**: Use color contrast checker plugin to verify WCAG AA compliance (4.5:1 minimum for text).

#### Step 2: Create Typography Styles

**Fonts to Add**:
1. File → Add local fonts → Select Inter (700) and Roboto (400, 500)
2. Backup: Use Figma's default fonts if local fonts unavailable

**Text Styles**:
```
Heading/H1
  Font: Inter Bold (700)
  Size: 36px
  Line height: 120%
  Letter spacing: -0.5px

Heading/H2
  Font: Inter Bold (700)
  Size: 28px
  Line height: 120%
  Letter spacing: -0.3px

Heading/H3
  Font: Inter Bold (700)
  Size: 22px
  Line height: 120%
  Letter spacing: 0px

Heading/H4
  Font: Inter Bold (700)
  Size: 18px
  Line height: 120%
  Letter spacing: 0px

Body/Large
  Font: Roboto Regular (400)
  Size: 18px
  Line height: 150%
  Letter spacing: 0px

Body/Regular
  Font: Roboto Regular (400)
  Size: 16px
  Line height: 150%
  Letter spacing: 0px

Body/Small
  Font: Roboto Regular (400)
  Size: 14px
  Line height: 150%
  Letter spacing: 0px

Body/Medium (for emphasis)
  Font: Roboto Medium (500)
  Size: 16px
  Line height: 150%
  Letter spacing: 0px

Caption
  Font: Roboto Regular (400)
  Size: 12px
  Line height: 140%
  Letter spacing: 0.3px

Monospace/Code
  Font: Roboto Mono (400)
  Size: 16px
  Line height: 140%
  Letter spacing: 0px
```

### Day 2: Spacing & Grid (30 minutes)

#### Create Auto Layout Grid

1. Create frame: 1440×1024 (desktop standard)
2. Add layout grid:
   - **Columns**: 12 columns, 24px gutter, 64px margin
   - **Rows**: 8px baseline grid
3. Save as template frame

#### Document Spacing Tokens

Create a reference frame with labeled rectangles:

```
4px   (XXS) - Tight inline
8px   (XS)  - Compact
16px  (SM)  - Default
24px  (MD)  - Comfortable
32px  (LG)  - Spacious
48px  (XL)  - Section breaks
64px  (XXL) - Major sections
```

**Usage in Figma**:
- Use Auto Layout with these gap values
- Cmd/Ctrl + Arrow keys nudge by 1px
- Shift + Cmd/Ctrl + Arrow nudges by 10px
- Create Auto Layout presets for common spacing

### Day 3-4: Component Library - Atoms (2-3 hours)

#### Button Components

**Create Variants** (Component Set):

**Variant Properties**:
- Type: Primary, Secondary, Tertiary, Danger
- State: Default, Hover, Active, Disabled
- Size: Large (48px), Medium (40px), Small (32px)

**Primary Button** (Cyan):
```
Frame (Auto Layout, horizontal)
├── Icon (optional, 24px)
├── Text ("Button Label", Body/Medium)
└── Icon (optional, 24px)

Padding: 12px 24px
Gap: 8px
Border radius: 8px
Fill: Primary/Cyan (#00F0FF)
Text color: Background/Primary (#0A0A0A)

Hover state:
  - Add inner shadow: 0px 0px 8px #00F0FF (glow effect)
  - Opacity: 90%

Active state:
  - Scale: 98%
  - Opacity: 80%

Disabled state:
  - Fill: Text/Disabled (#606060)
  - Text color: Text/Secondary (#B0B0B0)
  - Cursor: not-allowed
```

**Secondary Button** (Outline):
```
Same structure as Primary

Border: 2px solid Primary/Cyan
Fill: Transparent
Text color: Primary/Cyan

Hover state:
  - Fill: Primary/Cyan with 10% opacity
  - Border glow: 0px 0px 6px #00F0FF
```

**Tertiary Button** (Text only):
```
Same structure, no background/border

Text color: Primary/Cyan

Hover state:
  - Underline
  - Text glow: 0px 0px 4px #00F0FF
```

**Pro Tip**: Create one button, then right-click → "Add variant" for states. Use component properties for easy switching.

#### Input Components

**Text Field**:
```
Frame (Auto Layout, vertical)
├── Label (Caption, Text/Secondary)
└── Input Container (Auto Layout, horizontal)
    ├── Icon (optional, 20px)
    ├── Text ("Placeholder", Body/Regular)
    └── Action Icon (optional, clear/show)

Input Container:
  Width: 320px (adjust as needed)
  Height: 48px
  Padding: 12px 16px
  Gap: 8px
  Border radius: 8px
  Border: 1px solid Background/Border (#404040)
  Fill: Background/Surface (#242424)
  Text color: Text/Primary

Focus state:
  - Border: 2px solid Primary/Cyan
  - Glow: 0px 0px 6px #00F0FF

Error state:
  - Border: 2px solid Functional/Error
  - Add error message below (Caption, Error color)
```

**Slider Component**:
```
Frame (Auto Layout, vertical)
├── Header (Auto Layout, horizontal, space-between)
│   ├── Label (Body/Regular)
│   └── Value (Body/Medium, Primary/Cyan)
└── Slider Track (Frame)
    ├── Background (Rectangle, 4px height, Border color)
    ├── Fill (Rectangle, 4px height, Cyan, width = value%)
    └── Thumb (Circle, 20px, Cyan with shadow)

Track width: 280px
Thumb shadow: 0px 2px 4px rgba(0,0,0,0.3)

Hover state (thumb):
  - Scale: 110%
  - Shadow: 0px 0px 8px #00F0FF
```

**Toggle Switch**:
```
Track: 48px × 24px rounded rectangle
Thumb: 20px circle inside track

Off state:
  - Track fill: Background/Border (#404040)
  - Thumb position: Left (2px padding)
  - Thumb fill: Text/Secondary (#B0B0B0)

On state:
  - Track fill: Primary/Cyan (#00F0FF)
  - Thumb position: Right
  - Thumb fill: Background/Primary (#0A0A0A)

Animation: Thumb slides left/right (use Smart Animate in prototype)
```

**Checkbox**:
```
Frame (Auto Layout, horizontal)
├── Box (20px × 20px)
│   └── Checkmark icon (when checked)
└── Label (Body/Regular)

Gap: 8px

Unchecked:
  - Border: 2px solid Background/Border
  - Fill: Transparent

Checked:
  - Border: 2px solid Primary/Cyan
  - Fill: Primary/Cyan
  - Checkmark: Icon (white)
```

#### Icon Library (Use Iconify Plugin)

**Required Icons** (24px, use Lucide or Heroicons):
```
Actions:
- Play, Pause, Fast-forward (training controls)
- Settings, Edit, Delete, Copy, Download, Upload
- Plus, Minus, Close (X)

Sensors & Features:
- Eye (vision sensor)
- Radar (proximity sensor)
- Speedometer (speed)
- Steering wheel (turning)
- Brain (neural network)
- DNA helix (genetics)

Navigation:
- Home, Dashboard, Trophy, Book, User
- ChevronLeft, ChevronRight, ChevronDown
- Menu (hamburger)

Feedback:
- CheckCircle (success)
- AlertTriangle (warning)
- XCircle (error)
- Info (information)
- HelpCircle (tooltip trigger)

Stats:
- TrendingUp, TrendingDown
- BarChart, LineChart
- Clock, Calendar
```

**Icon Component Template**:
```
Frame: 24px × 24px
Icon: Centered, 20px actual size (2px padding for click area)
Color: Text/Primary (default)

Variants by color:
- Primary (cyan)
- Secondary (magenta)
- Success (green)
- Warning (yellow)
- Error (red)
- White
- Disabled (gray)
```

#### Badge Component

**Status Badge**:
```
Frame (Auto Layout, horizontal)
├── Dot (6px circle, optional)
├── Text (Caption, uppercase)

Padding: 4px 8px
Gap: 4px
Border radius: 12px (pill shape)

Variants:
- Success: Green fill, dark green text
- Warning: Yellow fill, dark yellow text
- Error: Red fill, dark red text
- Info: Cyan fill, dark cyan text
- Neutral: Gray fill, light gray text
```

**League Badge** (Circular):
```
Circle: 48px diameter
├── Background (league color with subtle gradient)
├── Icon or initial (centered)
└── Border (2px, lighter shade)

League variants:
- Tin: Gray (#8C8C8C)
- Iron: Dark (#505050)
- Steel: Silver (#C0C0C0)
- Titanium: Bright (#E0E0E0)
- Rust: Bronze (#CD7F32) with texture

Interactive states:
- Hover: Scale 110%, glow effect
- Active: Current league highlighted
```

#### Tooltip Component

**Hover Tooltip**:
```
Frame (Auto Layout, vertical)
├── Content (Body/Small, max-width: 200px)
└── Arrow (triangle pointing to target)

Padding: 8px 12px
Border radius: 6px
Fill: Background/Surface (#242424)
Border: 1px solid Background/Border
Shadow: 0px 4px 12px rgba(0,0,0,0.5)

Position: Above/below target (auto-adjust)
```

**Expandable Tooltip** (Learn More):
```
Frame (Auto Layout, vertical)
├── Trigger (Icon with HelpCircle)
└── Expanded Content (when clicked)
    ├── Title (Body/Medium)
    ├── Layman Explanation (Body/Regular)
    ├── Divider (1px line)
    ├── Technical Explanation (Body/Regular, muted color)
    └── Link ("Learn more →", Tertiary button)

Max-width: 320px
Animation: Fade in + slide down
```

### Day 5: Component Library - Molecules (1 hour)

#### Stat Card

```
Frame (Auto Layout, vertical)
├── Label (Caption, Text/Secondary)
├── Value (Heading/H2, Text/Primary)
└── Trend (Auto Layout, horizontal)
    ├── Icon (TrendingUp/Down, 16px)
    └── Change (Body/Small, Success/Error color)

Padding: 16px
Gap: 4px (between elements)
Border radius: 12px
Fill: Background/Surface
Border: 1px solid Background/Border

Hover state:
  - Border color: Primary/Cyan
  - Subtle glow
  - Lift: 0px 2px 8px rgba(0, 240, 255, 0.2)

Variants:
- Default (just label + value)
- With trend (includes trend indicator)
- Highlighted (cyan accent border)
```

#### Sensor Card (Key Component - Dual Explanation)

```
Frame (Auto Layout, vertical)
├── Header (Auto Layout, horizontal, space-between)
│   ├── Left (Auto Layout, horizontal)
│   │   ├── Icon (sensor type, 32px)
│   │   └── Name (Heading/H4)
│   └── Right (Auto Layout, horizontal)
│       ├── Level Badge ("Level 2")
│       └── Toggle (on/off, include in config)
├── Description Container
│   ├── Layman Explanation (Body/Regular) [default visible]
│   └── Technical Explanation (Body/Regular, muted) [toggle to show]
├── Mode Toggle (small button: "👁️ Layman" / "🔬 Technical")
└── Adjustment Slider (if applicable)
    └── Slider component (weight/importance)

Padding: 20px
Gap: 12px
Border radius: 12px
Fill: Background/Surface
Border: 2px solid Background/Border

Selected state:
  - Border color: Primary/Cyan
  - Glow: 0px 0px 12px rgba(0, 240, 255, 0.3)

Disabled state:
  - Opacity: 50%
  - Toggle grayed out
```

**Example Content**:
```
Layman Mode:
  Name: "Front Vision"
  Icon: Eye icon
  Description: "Your dot's eyes - helps it see walls and obstacles ahead. 
               Higher levels = sees farther down the track."

Technical Mode:
  Name: "Forward Proximity Sensor"
  Icon: Radar icon
  Description: "Normalized distance input (0-1) to neural network input layer. 
               Provides forward obstacle detection with configurable sensitivity."
```

#### DNA Card

```
Frame (Auto Layout, vertical)
├── Preview (Frame, 16:9 aspect ratio)
│   └── Visual representation (simplified neural network diagram or stats)
├── Info (Auto Layout, vertical)
│   ├── Name (Heading/H4)
│   ├── Stats Row (Auto Layout, horizontal)
│   │   ├── Stat ("Gen: 50", Caption)
│   │   ├── Stat ("Fit: 0.87", Caption)
│   │   └── Stat ("Sensors: 3", Caption)
│   └── Date (Caption, Text/Secondary)
└── Actions (Auto Layout, horizontal)
    ├── Button ("Load", Primary)
    ├── IconButton (Download)
    ├── IconButton (Copy)
    └── IconButton (Delete, Danger)

Padding: 16px
Gap: 12px
Border radius: 12px
Fill: Background/Surface
Border: 1px solid Background/Border

Hover state:
  - Border color: Primary/Cyan
  - Lift: 0px 4px 12px rgba(0, 240, 255, 0.1)

Selected state:
  - Border: 2px solid Primary/Cyan
  - Checkmark overlay (top-right corner)
```

#### Achievement Toast

```
Frame (Auto Layout, horizontal)
├── Icon (Celebration, 32px, Success color)
├── Content (Auto Layout, vertical)
│   ├── Title (Body/Medium, "Achievement Unlocked!")
│   └── Description (Body/Small, "50 Generations Trained")
└── Points Badge ("+100 points", Success badge)
└── Close Button (X icon, top-right corner)

Padding: 16px
Gap: 12px
Border radius: 12px
Fill: Background/Surface with success glow
Border: 2px solid Functional/Success
Shadow: 0px 4px 16px rgba(0, 255, 136, 0.3)

Animation:
  - Slide in from top-right
  - Auto-dismiss after 5 seconds (or manual close)
  - Slide out
```

#### Explanation Block (Dual Mode)

```
Frame (Auto Layout, vertical)
├── Header (Auto Layout, horizontal, space-between)
│   ├── Title (Heading/H4)
│   └── Mode Toggle Button ("👁️ Simple" / "🔬 Advanced")
├── Content Container
│   ├── [Layman] Simple Explanation (Body/Regular)
│   │   └── Metaphor + practical example
│   └── [Technical] Advanced Explanation (Body/Regular)
│       └── Accurate terminology + details
└── Learn More Link (Tertiary button, optional)

Padding: 20px
Gap: 12px
Border-left: 4px solid Primary/Cyan
Fill: Background/Surface with cyan tint (5% opacity)

Collapsed variant:
  - Show title + first line only
  - "Read more" button to expand
```

---

## 📱 Week 2: Priority Screens
**Goal**: Design MVP's most critical screens  
**Time**: 5-6 hours  
**Priority**: High - validates design system in practice

### Screen 1: Landing Page (2 hours)

**Desktop (1440×1024)**:

```
┌─────────────────────────────────────────────────┐
│ [Logo]          Home  Features  Docs  [Login]  │ ← Nav Bar (80px height)
├─────────────────────────────────────────────────┤
│                                                 │
│    [Hero Section - 60% viewport height]        │
│                                                 │
│    Heading (H1): "Learn AI by Racing AI"       │
│    Subheading: "Train neural networks..."      │
│                                                 │
│    [Get Started - Primary Button - Large]      │
│    "Watch Demo" - Secondary Button             │
│                                                 │
│    [Animated Dots Training on Track]           │ ← Use Lottie or GIF placeholder
│    (Center stage, 800×400px)                   │
│                                                 │
├─────────────────────────────────────────────────┤
│  [Features Section - 3 columns]                │
│                                                 │
│  [Icon] Train      [Icon] Race    [Icon] Learn │
│  Genetic algo...   Compete...     ML concepts  │
│                                                 │
├─────────────────────────────────────────────────┤
│  [How It Works - 4 steps]                      │
│                                                 │
│  1️⃣ Watch → 2️⃣ Configure → 3️⃣ Train → 4️⃣ Race    │
│                                                 │
├─────────────────────────────────────────────────┤
│  [Social Proof]                                │
│  "Open Source • Educational • Free"            │
│  [GitHub Stars: 234] [Discord Community]       │
│                                                 │
└─────────────────────────────────────────────────┘
  Footer: Links, Socials, Copyright
```

**Components to Use**:
- Nav Bar (create as component)
- Hero Section (Auto Layout, vertical, centered)
- Feature Card (3-col grid)
- Step Indicator (numbered circles)
- Footer (component)

**Design Notes**:
- Hero background: Subtle animated gradient (cyan → purple)
- Dot animation: Placeholder for now (can be Lottie file later)
- Use ROYGBIV gradient for "Learn AI by Racing AI" heading
- Ensure WCAG AA contrast on all text

**Mobile (375×812)**:
- Stack all sections vertically
- Hero: Full viewport height
- Features: Single column
- Steps: Vertical list
- Reduce padding to 16px (vs 64px desktop)

### Screen 2: Tutorial Flow (1.5 hours)

**4 Screens** (use Figma frames, link with prototype):

#### Tutorial 1: Welcome
```
┌─────────────────────────────────────┐
│ [Progress: 1/4] ●○○○                │
├─────────────────────────────────────┤
│                                     │
│   [Dot Character Illustration]      │ ← Friendly, simple dot with "face"
│                                     │
│   Heading (H1):                     │
│   "Welcome to Dot AI Racer!"        │
│                                     │
│   Body:                             │
│   "You're about to train your      │
│    own AI racer from scratch.      │
│    No coding required!"            │
│                                     │
│   [Continue - Primary Button]       │
│   [Skip Tutorial - Tertiary]        │
│                                     │
└─────────────────────────────────────┘
```

#### Tutorial 2: Watch Demo (Pre-trained Dot)
```
┌─────────────────────────────────────┐
│ [Progress: 2/4] ●●○○                │
├─────────────────────────────────────┤
│                                     │
│   [Track View - Drag Strip]         │ ← Use simple rectangle track
│   [Dot Animation - 3 generations]   │   
│                                     │
│   ┌─────────────────────────────┐  │
│   │ Gen 1 → Gen 2 → Gen 3       │  │ ← Fitness chart (simple)
│   │ Fitness: 0.3 → 0.5 → 0.7    │  │
│   └─────────────────────────────┘  │
│                                     │
│   Explanation Box:                  │
│   "Your dot is learning! Each      │
│    generation gets a bit smarter." │
│                                     │
│   [Auto-advance after animation]    │
│                                     │
└─────────────────────────────────────┘
```

#### Tutorial 3: Edit Configuration
```
┌─────────────────────────────────────┐
│ [Progress: 3/4] ●●●○                │
├─────────────────────────────────────┤
│                                     │
│   Heading (H2):                     │
│   "Let's Make It Better!"           │
│                                     │
│   [Sensor Card - Front Vision]      │ ← Use component, highlight interaction
│   👁️ Layman Mode                    │
│   "Helps your dot see walls ahead"  │
│                                     │
│   Slider: Wall Avoidance            │
│   [──●────────] Level 1 → 3         │ ← Animated tutorial arrow pointing
│                                     │
│   Tooltip (pulsing):                │
│   "Drag this slider to the right!" │
│                                     │
│   [Train Again - Primary Button]    │
│                                     │
└─────────────────────────────────────┘
```

#### Tutorial 4: See Results
```
┌─────────────────────────────────────┐
│ [Progress: 4/4] ●●●●                │
├─────────────────────────────────────┤
│                                     │
│   🎉 Achievement Unlocked!          │
│   "First Configuration!"            │
│   +100 points                       │
│                                     │
│   Results Comparison:               │
│   ┌─────────────────────────────┐  │
│   │ Before:  Gen 3, Lap 12.4s   │  │
│   │ After:   Gen 6, Lap 9.8s    │  │
│   │ Improvement: 21% faster! ✓  │  │
│   └─────────────────────────────┘  │
│                                     │
│   Heading (H3):                     │
│   "You're a natural! Ready to race?"│
│                                     │
│   [Go to Dashboard - Primary]       │
│                                     │
└─────────────────────────────────────┘
```

**Prototype Links**:
- Welcome → [Continue] → Watch Demo
- Watch Demo → [Auto-advance after 5s] → Edit Config
- Edit Config → [Train Again] → Results
- Results → [Go to Dashboard] → Dashboard screen

### Screen 3: Dashboard (1.5 hours)

**Desktop Layout**:

```
┌───────────────────────────────────────────────────┐
│ [Logo]  Dashboard  Training  Racing  DNA  [User] │ ← Top Nav (80px)
├───────┬───────────────────────────────────────────┤
│ QUICK │                                           │
│ACTION │   Active Training                         │ ← Main Content Area
│       │   ┌─────────────────────────────────────┐ │
│●Train │   │ [Track Preview]                     │ │
│ Race  │   │ "Speed Demon" - Gen 24/100          │ │
│Config │   │ Fitness: 0.78  ⬆ +12% this session  │ │
│       │   │ [Pause] [Resume] [View Details]     │ │
│DNA LIB│   └─────────────────────────────────────┘ │
│       │                                           │
│STATS  │   Recent Activity                         │
│Points │   ┌──────────┬──────────┬──────────────┐ │
│1,450  │   │[Icon]    │[Icon]    │[Icon]        │ │
│       │   │Gen 50    │1st Place │DNA Saved     │ │
│League │   │+100pts   │+250pts   │"Fast Config" │ │
│Steel  │   └──────────┴──────────┴──────────────┘ │
│       │                                           │
└───────┴───────────────────────────────────────────┘
         Footer
```

**Sidebar** (240px width):
- Quick Actions (icon + label buttons)
- Stats summary (points, league badge)
- Use Background/Secondary fill
- Sticky positioning

**Main Content**:
- Active training card (if training in progress)
- Recent activity grid (3 columns)
- Call-to-action if no active training: "Start Training" hero section

**Mobile Version**:
- Remove sidebar
- Bottom navigation (5 icons: Dashboard, Train, Race, DNA, Profile)
- Stack content vertically
- Swipeable recent activity carousel

### Screen 4: Skeleton/Placeholder Screens (30 min)

Create basic layouts for:
- **Training Environment**: Full-screen frame with track placeholder, controls bottom
- **Vehicle Configuration**: Grid of sensor cards, save/load buttons top-right
- **DNA Library**: Grid of DNA cards with search bar
- **Settings**: List of toggle options

These are low-fidelity placeholders - we'll detail them in Week 3.

---

## 🏋️ Week 3: Core Features
**Goal**: High-fidelity mockups of Training & Configuration  
**Time**: 5-6 hours  
**Priority**: High - these are the core experience

### Screen 5: Training Environment (Full-Screen Immersive) (2.5 hours)

**Layout (1920×1080 - full viewport)**:

```
┌─────────────────────────────────────────────────────────────┐
│ [◀ Exit]  Training: "Speed Demon"    Gen 24/100  [Settings]│ ← Top Bar (minimal, 60px)
├─────────────────────────────────────────────────────────────┤
│                                                             │
│                   [TRACK VISUALIZATION]                     │
│                                                             │
│   ┌───────────────────────────────────────────────────┐   │
│   │                                                     │   │
│   │        [20 Colored Dots Racing]                    │   │ ← Main Stage (80% height)
│   │                                                     │   │   Simple drag strip for MVP
│   │        Drag Strip Track (grey rectangle)           │   │
│   │                                                     │   │
│   │                                                     │   │
│   └───────────────────────────────────────────────────┘   │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│ [Fitness Chart Overlay - Collapsible]                      │
│ ┌─────────────────────────────────────────────────────┐   │ ← Bottom Overlay (20% height)
│ │  Fitness: 0.78  ⬆ +12%        [Minimize] [Expand]   │   │
│ │  ╱╲                                                   │   │   Can collapse to thin bar
│ │ ╱  ╲    Line chart (Gen 1-24)                       │   │
│ │      ╲╱                                              │   │
│ │  Gen: 1────────────────────────────────────────24   │   │
│ │                                                       │   │
│ │  [◼ Stop] [▶ Play / ⏸ Pause] [⏩ Speed: 2x ▼]       │   │ ← Controls
│ │  [💾 Save DNA] [📊 View Details]                     │   │
│ └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

**Components**:

1. **Track Visualization Area**:
   - Background: Background/Primary (#0A0A0A)
   - Track: Rectangle, Background/Surface with borders
   - Dots: 20 circles (8px diameter), ROYGBIV colors
   - Animation: Use Figma's Smart Animate for movement prototype
   - For static mockup: Show dots at various positions

2. **Fitness Chart** (Use plugin or manual chart):
   - Line graph: Cyan stroke (#00F0FF), 2px weight
   - X-axis: Generation number (1-100)
   - Y-axis: Fitness (0-1.0)
   - Grid: Subtle dotted lines (Background/Border)
   - Fill under line: Cyan gradient (100% → 0% opacity)

3. **Control Panel**:
   - Stop: Danger button (red)
   - Play/Pause: Primary button (cyan), toggle icon
   - Speed Selector: Dropdown (1x, 2x, 5x, 10x)
   - Save DNA: Secondary button with icon
   - View Details: Tertiary button

4. **Top Bar**:
   - Minimal chrome (60px height)
   - Exit button (left): Goes back to dashboard
   - Configuration name (center): "Training: Speed Demon"
   - Generation counter (center-right): "Gen 24/100"
   - Settings icon (right): Opens overlay menu

**Overlay States** (create separate frames):
- **Chart Minimized**: Thin bar (80px) with just fitness value + controls
- **Chart Expanded**: Full view (300px) with detailed chart
- **Settings Overlay**: Modal from right (320px wide) with:
  - Population size slider
  - Visualization toggle (trails, labels)
  - Performance mode toggle

**Interaction Notes** (for prototype):
- Click Play → dots animate, chart updates
- Click Pause → freeze animation
- Click Minimize chart → shrinks to bar
- Click Save DNA → success toast appears

### Screen 6: Vehicle Configuration (2 hours)

**Layout (1440×1024)**:

```
┌─────────────────────────────────────────────────────────────┐
│ [Logo] Dashboard  Training  Racing  DNA  [User]             │ ← Nav Bar
├─────────────────────────────────────────────────────────────┤
│ Vehicle Configuration                                        │
│ ┌───────────────────────┬───────────────────────────────┐  │
│ │ Configuration: [▼]    │         Preview Panel         │  │ ← Header
│ │ "Speed Demon"         │   ┌─────────────────────────┐ │  │
│ │ [Save] [Load] [New]   │   │  [Dot Icon]             │ │  │
│ └───────────────────────┤   │  Sensors: 3             │ │  │   Right sidebar
│                          │   │  Actions: 2             │ │  │   (300px wide)
│ ┌──── Sensors ────────┐ │   │  Brain: 600 neurons     │ │  │
│ │                      │ │   │  Mutation: 5%           │ │  │
│ │ [Sensor Card 1]      │ │   │                         │ │  │
│ │ Front Vision  ●ON    │ │   │  Estimated Performance: │ │  │
│ │ 👁️ "Helps dot see..." │ │   │  ⭐⭐⭐⭐☆ (Good)        │ │  │
│ │ [Slider: Level 3]    │ │   └─────────────────────────┘ │  │
│ │                      │ └───────────────────────────────┘  │
│ │ [Sensor Card 2]      │                                    │
│ │ Left Sensor    ●ON   │  ┌──── Actions ────────────────┐  │
│ │ 👁️ "Detects walls..." │  │ [Action Card 1]             │  │
│ │ [Slider: Level 2]    │  │ Engine        ●ON           │  │
│ │                      │  │ "Controls speed"            │  │
│ │ [+ Add Sensor]       │  │ [Slider: Power 70%]         │  │
│ │  (locked, need pts)  │  │                             │  │
│ └──────────────────────┘  │ [Action Card 2]             │  │
│                            │ Suspension    ●ON           │  │
│ ┌──── Advanced ────────┐  │ "Turning ability"           │  │
│ │ Brain Size           │  │ [Slider: Agility 50%]       │  │
│ │ [────●────] 600      │  │                             │  │
│ │                      │  │ [+ Add Action]              │  │
│ │ Mutation Rate        │  │  (locked, need 500pts)      │  │
│ │ [──●──────] 5%       │  └─────────────────────────────┘  │
│ │                      │                                    │
│ │ [🔬 Technical Mode]  │  ┌────────────────────────────┐   │
│ └──────────────────────┘  │ [Train This Config]        │   │ ← Bottom CTA
│                            │ [Save to Library]          │   │
└───────────────────────────┴────────────────────────────────┘
```

**Components** (reuse from Week 1):
- Sensor Card (with dual explanation mode)
- Slider (for adjustments)
- Toggle switch (on/off for each sensor/action)
- Preview Panel (stat cards + performance estimate)
- Lock overlay (for unavailable sensors/actions)

**Interaction Details**:

1. **Sensor/Action Cards**:
   - Toggle switch: Enable/disable
   - Slider: Adjust weight/importance
   - Info icon: Shows expanded tooltip
   - Mode toggle (👁️/🔬): Switches explanation text

2. **Preview Panel**:
   - Updates in real-time as sliders change
   - Performance estimate: 1-5 stars based on config
   - Color-coded: Good (green), Average (yellow), Weak (red)

3. **Advanced Section**:
   - Initially collapsed (click to expand)
   - Brain Size: 400-1000 neurons
   - Mutation Rate: 1-10%
   - Explanation tooltips for each

4. **Locked Items**:
   - Grayed out sensor/action cards
   - Lock icon overlay
   - Tooltip: "Unlock with 500 points" or "Complete tutorial"

5. **Technical Mode Toggle**:
   - Global button (affects all cards)
   - Persists across sessions
   - Smooth text transition (fade)

**Dual Explanation Example** (create both frames):

**Layman Mode**:
```
Front Vision
👁️ Your dot's eyes forward

Helps your dot see walls and obstacles ahead. 
The higher the level, the further it can see down the track.
```

**Technical Mode**:
```
Forward Proximity Sensor
🔬 Input layer feature

Provides normalized distance measurement (0-1) to the neural 
network input layer. Higher values increase sensitivity to 
forward obstacles. Range: 0-100 pixels.
```

### Screen 7: DNA Library (1 hour)

**Layout (1440×1024)**:

```
┌─────────────────────────────────────────────────────────────┐
│ [Logo] Dashboard  Training  Racing  DNA  [User]             │
├─────────────────────────────────────────────────────────────┤
│ DNA Library                           [+ New Configuration]  │
│                                                               │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ [🔍 Search...]  [Filter: All ▼]  [Sort: Newest ▼]       │ │ ← Search Bar
│ └─────────────────────────────────────────────────────────┘ │
│                                                               │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │                                                           │ │
│ │  Grid of DNA Cards (3 columns on desktop)                │ │
│ │                                                           │ │
│ │  ┌────────────┐  ┌────────────┐  ┌────────────┐         │ │
│ │  │ [Preview]  │  │ [Preview]  │  │ [Preview]  │         │ │
│ │  │            │  │            │  │            │         │ │
│ │  │Speed Demon │  │Wall Hugger │  │Experiment  │         │ │
│ │  │Gen: 50     │  │Gen: 30     │  │Gen: 100    │         │ │
│ │  │Fit: 0.87   │  │Fit: 0.72   │  │Fit: 0.91   │         │ │
│ │  │Sensors: 3  │  │Sensors: 2  │  │Sensors: 5  │         │ │
│ │  │            │  │            │  │            │         │ │
│ │  │[Load]      │  │[Load]      │  │[Load]      │         │ │
│ │  │📥 📋 🗑️     │  │📥 📋 🗑️     │  │📥 📋 🗑️     │         │ │
│ │  └────────────┘  └────────────┘  └────────────┘         │ │
│ │                                                           │ │
│ │  [6 more DNA cards in grid...]                           │ │
│ │                                                           │ │
│ └─────────────────────────────────────────────────────────┘ │
│                                                               │
│ [Pagination: < 1 2 3 4 >]                     9 configs      │
└───────────────────────────────────────────────────────────────┘
```

**Components**:
- DNA Card (from Week 1 molecules)
- Search bar with filters
- Grid layout (3 columns, Auto Layout)
- Empty state (when no DNA saved yet)

**Empty State** (create separate frame):
```
┌─────────────────────────────────────┐
│                                     │
│        [DNA Helix Icon]             │
│        (large, 120px)               │
│                                     │
│   No DNA Saved Yet                  │
│                                     │
│   Train a dot and save your first   │
│   configuration to get started!     │
│                                     │
│   [Start Training - Primary Button] │
│                                     │
└─────────────────────────────────────┘
```

---

## 🔗 Week 4: Prototype & Handoff
**Goal**: Interactive prototype + developer documentation  
**Time**: 4-5 hours  
**Priority**: Critical for user testing & development

### Day 1: Link Screens (Prototype Mode) (1.5 hours)

**New User Flow**:
1. Landing Page → [Get Started] → Tutorial Welcome
2. Tutorial Welcome → [Continue] → Watch Demo (Smart Animate)
3. Watch Demo → [Auto] → Edit Config (after 5s delay)
4. Edit Config → [Train Again] → Results (Smart Animate on slider)
5. Results → [Go to Dashboard] → Dashboard
6. Dashboard → [Train] → Training Environment (full-screen)
7. Training → [Configure] → Vehicle Config
8. Config → [Save DNA] → DNA Library

**Interactions to Add**:
- **Hover states**: All buttons, cards, links
- **Click states**: Buttons scale to 98%
- **Smart Animate**: Slider movements, panel expansions, chart updates
- **Overlays**: Settings modal, tooltips, toasts
- **Scroll**: Long pages (landing, DNA library)

**Figma Prototype Settings**:
- Device: Desktop (1440×1024)
- Background: #000000
- Starting frame: Landing Page
- Interaction: On Click (mostly), some On Hover (tooltips)
- Animation: Smart Animate, 300ms ease

### Day 2: Micro-interactions (1 hour)

**Add Polish**:

1. **Button Hover Glow**:
   - Create variant with shadow: `0px 0px 12px #00F0FF`
   - Use Smart Animate for smooth transition

2. **Card Lift on Hover**:
   - Original: `0px 0px 0px transparent`
   - Hover: `0px 4px 16px rgba(0, 240, 255, 0.2)`
   - Smart Animate, 200ms

3. **Tooltip Appear**:
   - Create 2 frames: Hidden (opacity 0%), Visible (100%)
   - Trigger: After delay (500ms hover)
   - Animation: Dissolve + Move (slide down 8px)

4. **Achievement Toast**:
   - Create 3 frames: Offscreen (right +400px), Onscreen, Dismiss
   - Auto-animate: Slide in → Wait 5s → Slide out

5. **Loading States**:
   - Add spinner component
   - Show when "Training" or "Saving DNA"
   - Replace button text temporarily

### Day 3: Mobile Prototype (1 hour)

**Create Mobile Frames** (375×812):
1. Landing Page Mobile
2. Dashboard Mobile (bottom nav)
3. Settings Mobile (full-screen drawer)

**Link Mobile Flow**:
- Landing → Dashboard
- Bottom nav switches between views
- Swipe gestures (use drag interaction for DNA library carousel)

**Responsive Considerations**:
- Stack all sections vertically
- Reduce padding (64px → 16px)
- Larger touch targets (44px minimum)
- Bottom sheet modals instead of center modals

### Day 4: Developer Handoff Prep (1.5 hours)

**Create "Developer Handoff" Page** in Figma:

#### Section 1: Design Tokens Export

**Table format**:

| Token Name | Value | Usage |
|------------|-------|-------|
| `color-primary-cyan` | `#00F0FF` | CTAs, links, focus states |
| `color-bg-primary` | `#0A0A0A` | Page backgrounds |
| `spacing-sm` | `16px` | Default gap |
| ... | ... | ... |

**Export as**:
- CSS variables
- Tailwind config
- JSON (for React/TS)

Example CSS export:
```css
:root {
  --color-primary-cyan: #00F0FF;
  --color-primary-magenta: #FF00AA;
  --color-bg-primary: #0A0A0A;
  --spacing-xs: 8px;
  --spacing-sm: 16px;
  /* ... */
}
```

#### Section 2: Component Specs

For each component, document:

**Example: Primary Button**
```
Component: Button (Primary variant)

States: Default, Hover, Active, Disabled

Default:
  - Height: 48px
  - Padding: 12px 24px
  - Border-radius: 8px
  - Background: #00F0FF
  - Text: Roboto Medium 16px, #0A0A0A
  - Gap (icon + text): 8px

Hover:
  - Shadow: 0px 0px 12px #00F0FF
  - Opacity: 90%
  - Transition: 150ms ease

Active:
  - Transform: scale(0.98)
  - Transition: 100ms ease

Disabled:
  - Background: #606060
  - Text: #B0B0B0
  - Cursor: not-allowed
  - No hover effect
```

#### Section 3: Spacing Reference

Create visual grid showing:
- 8px baseline grid
- Component spacing examples
- Page layout margins

#### Section 4: Interaction Notes

Document animations:
```
Interaction: Achievement Toast

Trigger: On achievement unlock
Entry: Slide from right (400px) over 300ms ease-out
Display: 5 seconds
Exit: Slide to right (400px) over 300ms ease-in
Can dismiss: Yes (close button, immediate exit)
Stacking: Max 3 toasts, queue overflow
```

#### Section 5: Assets Export

Prepare for export:
- **Icons** (SVG, 24px): Export all icons
- **Logos** (SVG + PNG): Logo variations (color, white, dark)
- **Illustrations**: Tutorial dot character, empty states
- **Cursors** (if custom): Pointer, grab, etc.

**Export Settings**:
- SVG: Outline text, flatten transforms
- PNG: 1x, 2x, 3x (for retina displays)
- Naming convention: `icon-[name].svg`, `logo-[variant].svg`

### Deliverables Checklist

**Design Files**:
- [ ] Figma file organized (pages labeled clearly)
- [ ] Design system library complete
- [ ] All MVP screens designed (desktop)
- [ ] Key screens designed (mobile)
- [ ] Interactive prototype linked
- [ ] Developer handoff page created

**Exports**:
- [ ] Design tokens (CSS/JSON)
- [ ] Icon set (SVG)
- [ ] Logo files (SVG/PNG)
- [ ] Component specs documented
- [ ] Interaction notes written

**Testing**:
- [ ] Contrast ratios checked (WCAG AA)
- [ ] Colorblind mode tested
- [ ] Prototype tested on device
- [ ] User testing completed (10-15 users)

---

## 🎯 Quick Reference

### Keyboard Shortcuts (Figma)

**Essential**:
- `F` - Frame tool
- `R` - Rectangle
- `T` - Text
- `O` - Ellipse (circles/dots)
- `Shift + A` - Auto Layout
- `Cmd/Ctrl + D` - Duplicate
- `Cmd/Ctrl + G` - Group
- `Cmd/Ctrl + K` - Create component
- `Cmd/Ctrl + /` - Quick search

**Alignment**:
- `Alt + H` - Horizontal center
- `Alt + V` - Vertical center
- `Alt + A/D` - Align left/right
- `Alt + W/S` - Align top/bottom

**Prototyping**:
- `Shift + E` - Prototype mode
- Click element → Drag to target frame

### Color Picker Shortcuts

- **Eyedropper**: `I` key → Click any color on screen
- **Copy fill**: `Cmd/Ctrl + C` on selected object
- **Paste fill**: `Cmd/Ctrl + V` on target object

### Component Best Practices

1. **Name clearly**: Use `/` for grouping (e.g., `Button/Primary`)
2. **Use variants**: Instead of multiple components (states, sizes)
3. **Make responsive**: Use Auto Layout for flexible sizing
4. **Document**: Add descriptions to component properties
5. **Publish**: Push to library for reuse across pages

### Auto Layout Tips

**Spacing**:
- Gap: Space between children (consistent)
- Padding: Space inside container

**Alignment**:
- Horizontal: Left, Center, Right, Space Between
- Vertical: Top, Center, Bottom, Space Between

**Resizing**:
- Hug contents: Shrinks to fit children
- Fixed: Stays at set size
- Fill container: Expands to parent

**Nesting**:
- Horizontal in Vertical (or vice versa) for complex layouts
- Example: Card (vertical) → Header (horizontal) → Title + Badge

---

## 🔧 Troubleshooting

### Issue: Colors Look Different on Export

**Solution**: Ensure color profile is sRGB
- File → Place Image → Manage missing fonts and color profiles
- Export settings → Color profile: sRGB

### Issue: Text Rendering Blurry

**Solution**: Align to pixel grid
- Select text → Properties → Position (round to whole pixels)
- Avoid fractional font sizes (use 16px, not 16.5px)

### Issue: Prototype Links Not Working

**Solution**: Check interaction settings
- Prototype mode → Click connection → Verify:
  - Trigger: On Click (most common)
  - Action: Navigate to [correct frame]
  - Animation: Instant or Smart Animate

### Issue: Components Not Updating

**Solution**: Publish library changes
- Assets panel → Libraries → Publish changes
- In consuming files: Review and accept updates

### Issue: Export Missing Elements

**Solution**: Check layer visibility and export settings
- Ensure layers are visible (not hidden)
- Right-click frame → Export → Check format (SVG/PNG)
- Verify "Include [layer name]" is checked

### Issue: Slow Performance

**Solution**: Optimize file
- Flatten heavy groups (select → Cmd/Ctrl + E)
- Remove unused components
- Split into multiple files if >500 frames
- Reduce image resolution (max 2x needed)

---

## 📚 Resources

### Figma Learning
- [Figma Docs](https://help.figma.com/)
- [Figma YouTube](https://www.youtube.com/c/Figmadesign) - Official tutorials
- [Figma Community](https://www.figma.com/community) - Free design systems to reference

### Design System Examples
- [Material Design 3](https://m3.material.io/)
- [Ant Design](https://ant.design/)
- [Primer (GitHub)](https://primer.style/)

### Accessibility
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [Who Can Use](https://www.whocanuse.com/) - Color contrast simulator
- [WAVE](https://wave.webaim.org/) - Accessibility checker

### Icons
- [Lucide Icons](https://lucide.dev/) - Clean, consistent set
- [Heroicons](https://heroicons.com/) - Tailwind-friendly
- [Iconify Plugin](https://www.figma.com/community/plugin/735098390272716381) - Access all libraries

### Inspiration
- [Dribbble](https://dribbble.com/tags/dashboard) - Dashboard designs
- [Mobbin](https://mobbin.com/) - Mobile app patterns
- [Awwwards](https://www.awwwards.com/) - Award-winning web design

---

## ✅ Definition of Done

**Week 1 Complete When**:
- [ ] All color styles created and named
- [ ] All text styles created
- [ ] Spacing system documented
- [ ] Button component (all variants) complete
- [ ] Input components (text, slider, toggle) complete
- [ ] Icon library imported (24+ icons)
- [ ] Badge, tooltip, stat card components complete
- [ ] Sensor card, DNA card, explanation block complete

**Week 2 Complete When**:
- [ ] Landing page (desktop + mobile) designed
- [ ] Tutorial flow (4 screens) designed
- [ ] Dashboard (desktop + mobile) designed
- [ ] Skeleton screens created
- [ ] All screens use design system components
- [ ] Contrast ratios checked (WCAG AA pass)

**Week 3 Complete When**:
- [ ] Training environment (full-screen) designed
- [ ] Vehicle configuration (desktop) designed
- [ ] DNA library (desktop) designed
- [ ] All interactions documented
- [ ] Dual explanation mode shown
- [ ] Colorblind mode tested

**Week 4 Complete When**:
- [ ] New user flow prototype linked
- [ ] Returning user flow prototype linked
- [ ] Micro-interactions added (hover, click states)
- [ ] Mobile prototype created
- [ ] Developer handoff page complete
- [ ] Assets exported (icons, logos)
- [ ] User testing completed (10+ users)
- [ ] Feedback incorporated
- [ ] Ready for development handoff

---

**Next Step**: Open Figma, create project, and start Week 1 Day 1! 🎨

