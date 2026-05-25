"""
Track Validation Script
Tests that all 6 tracks can load and simulate successfully
"""

import json
import sys

def test_all_tracks():
    """Test that all tracks in database are valid"""
    
    print("=" * 60)
    print("TRACK VALIDATION TEST")
    print("=" * 60)
    
    # Load tracks database
    try:
        with open("tracks_database.json", 'r') as f:
            tracks_db = json.load(f)
        print("✓ tracks_database.json loaded successfully")
    except Exception as e:
        print(f"✗ Failed to load tracks_database.json: {e}")
        return False
    
    # Validate each track
    track_order = tracks_db.get('track_order', [])
    print(f"\nFound {len(track_order)} tracks to test:\n")
    
    all_passed = True
    
    for i, track_id in enumerate(track_order, 1):
        print(f"{i}. Testing '{track_id}'...")
        
        track = tracks_db['tracks'].get(track_id)
        if not track:
            print(f"   ✗ Track '{track_id}' not found in database")
            all_passed = False
            continue
        
        # Check required fields
        required_fields = [
            'id', 'name', 'description', 'type', 'difficulty',
            'start_position', 'finish_position', 'surfaces',
            'barriers', 'start_marker', 'finish_marker', 'finish_zone'
        ]
        
        missing = []
        for field in required_fields:
            if field not in track:
                missing.append(field)
        
        if missing:
            print(f"   ✗ Missing fields: {', '.join(missing)}")
            all_passed = False
            continue
        
        # Validate positions
        try:
            start_x = track['start_position']['x']
            start_y = track['start_position']['y']
            finish_x = track['finish_position']['x']
            finish_y = track['finish_position']['y']
            
            if not (0 <= start_x <= 800 and 0 <= start_y <= 600):
                print(f"   ✗ Start position out of bounds: ({start_x}, {start_y})")
                all_passed = False
                continue
            
            if not (0 <= finish_x <= 800 and 0 <= finish_y <= 600):
                print(f"   ✗ Finish position out of bounds: ({finish_x}, {finish_y})")
                all_passed = False
                continue
        except Exception as e:
            print(f"   ✗ Invalid position data: {e}")
            all_passed = False
            continue
        
        # Count elements
        num_surfaces = len(track['surfaces'])
        num_barriers = len(track['barriers'])
        num_decorative = len(track.get('decorative_lines', []))
        
        print(f"   ✓ {track['name']}")
        print(f"      Type: {track['type']}, Difficulty: {track['difficulty']}")
        print(f"      Surfaces: {num_surfaces}, Barriers: {num_barriers}, Lines: {num_decorative}")
        print(f"      Start: ({start_x}, {start_y}) → Finish: ({finish_x}, {finish_y})")
    
    print("\n" + "=" * 60)
    if all_passed:
        print("✓ ALL TRACKS VALID")
        print("=" * 60)
        return True
    else:
        print("✗ SOME TRACKS FAILED VALIDATION")
        print("=" * 60)
        return False

if __name__ == "__main__":
    success = test_all_tracks()
    sys.exit(0 if success else 1)
