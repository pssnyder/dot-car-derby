# 🏁 Track Database Guide

**Dot Car Derby - Data-Driven Track System**

---

## Overview

All track configurations are stored in `tracks_database.json`. This data-driven approach means:
- ✅ Add new tracks without touching code
- ✅ Easy to export to Firestore for production
- ✅ Consistent schema across all tracks
- ✅ Version control friendly

## Track Schema

Each track in the database contains:

### Required Fields

```json
{
  "id": "unique_track_id",
  "name": "Display Name",
  "description": "Track description for players",
  "type": "drag|oval|rally|circuit|technical",
  "difficulty": "easy|medium|hard|extreme",
  "start_position": { "x": 400, "y": 550 },
  "finish_position": { "x": 400, "y": 50 }
}
```

### Track Geometry

#### Surfaces
Areas where dots can drive:
```json
"surfaces": [
  {
    "type": "rect",
    "x": 325, "y": 0,
    "width": 150, "height": 600,
    "color": [40, 40, 40]
  }
]
```

#### Barriers (Dead Zones)
Areas that eliminate dots on contact:
```json
"barriers": [
  {
    "type": "rect",
    "x": 0, "y": 0,
    "width": 325, "height": 600,
    "name": "left_wall"
  },
  {
    "type": "circle",
    "x": 400, "y": 300,
    "radius": 100,
    "name": "center_obstacle"
  }
]
```

#### Decorative Lines
Visual guides (not collision objects):
```json
"decorative_lines": [
  {
    "type": "center_line",
    "start": [400, 0],
    "end": [400, 600],
    "color": [255, 255, 0],
    "width": 2,
    "dashed": true,
    "dash_length": 20,
    "gap_length": 10
  },
  {
    "type": "racing_line",
    "center": [400, 300],
    "radius": 150,
    "color": [100, 100, 100],
    "width": 1,
    "is_circle": true,
    "dashed": true
  }
]
```

#### Markers
Start and finish line visuals:
```json
"start_marker": {
  "type": "line",
  "start": [325, 550],
  "end": [475, 550],
  "width": 3
},
"finish_marker": {
  "type": "line",
  "start": [325, 50],
  "end": [475, 50],
  "width": 5
}
```

#### Finish Zone
Area that triggers race completion:
```json
"finish_zone": {
  "type": "line",
  "direction": "horizontal",
  "position": 50
}
```
OR
```json
"finish_zone": {
  "type": "rect",
  "x": 350, "y": 250,
  "width": 40, "height": 100
}
```

---

## Current Tracks

### 1. Drag Strip Alpha
**ID**: `drag_strip`  
**Type**: Drag race  
**Difficulty**: Easy

Simple vertical track - perfect for learning the basics.

### 2. The Horseshoe Circuit
**ID**: `oval_99`  
**Type**: Oval  
**Difficulty**: Medium

99% circular track with center barrier preventing shortcuts. Start and finish are separated by a divider - dots must complete the full loop!

---

## Adding New Tracks

### Step 1: Design Your Track
Sketch out:
- Track dimensions (800x600 screen)
- Start position
- Finish position  
- Barriers/obstacles
- Surface areas

### Step 2: Add to Database
Open `tracks_database.json` and add a new entry under `"tracks"`:

```json
"your_track_id": {
  "id": "your_track_id",
  "name": "Your Track Name",
  "description": "What makes this track special?",
  "type": "circuit",
  "difficulty": "medium",
  "start_position": { "x": 100, "y": 500 },
  "finish_position": { "x": 700, "y": 500 },
  "surfaces": [...],
  "barriers": [...],
  "decorative_lines": [...],
  "start_marker": {...},
  "finish_marker": {...},
  "finish_zone": {...}
}
```

### Step 3: Update race_config.json
Set the track to load:
```json
{
  "current_track": "your_track_id",
  ...
}
```

### Step 4: Test!
```bash
python dot_ai_car.py
```

---

## Tips for Track Design

### Balance
- **Too easy**: Dots finish too quickly, little learning
- **Too hard**: Dots can't make progress, slow evolution
- **Just right**: Most dots crash, but top performers occasionally finish

### Interesting Challenges
- **Tight corners**: Require precise movement
- **Long straights**: Reward speed optimization
- **Chicanes**: Test quick direction changes
- **Multiple paths**: Allow strategy variation

### Visual Clarity
- Use decorative lines to hint at optimal racing line
- Make barriers visually distinct from track surface
- Place start/finish markers clearly

---

## Future: Firestore Migration

This schema is designed for easy Firestore export:

```javascript
// Firestore collection: tracks
{
  trackId: "drag_strip",
  name: "Drag Strip Alpha",
  type: "drag",
  difficulty: "easy",
  geometry: {
    surfaces: [...],
    barriers: [...],
    decorativeLines: [...]
  },
  spawns: {
    start: { x: 400, y: 550 },
    finish: { x: 400, y: 50 }
  },
  metadata: {
    created: "2026-05-15",
    author: "system",
    plays: 0,
    avgCompletionRate: 0.0
  }
}
```

---

## Track Types

- **Drag**: Straight-line speed
- **Oval**: Continuous turning, endurance
- **Rally**: Point-to-point with varied terrain
- **Circuit**: Lap-based racing with multiple turns
- **Technical**: Complex obstacles, multiple paths, extreme difficulty

---

## Next Steps

**Planned Tracks** (in `tracks_database.json`):
- Rally Point-to-Point
- Daytona Speedway (NASCAR oval)
- Indianapolis Motor Speedway
- Maniac Mayhem (TrackMania-inspired chaos)

**Your Ideas?**
The system is ready for whatever creative tracks you design!
