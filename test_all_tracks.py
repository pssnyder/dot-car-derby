"""
Quick Simulation Test for All Tracks
Runs each track for 3 generations to verify they work correctly
"""

import pygame
import sys
import os

# Suppress pygame welcome message
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

# Import the main simulation
sys.path.insert(0, os.path.dirname(__file__))

def quick_test_track(track_id, track_name, max_generations=3):
    """Run a quick test on a specific track"""
    print(f"\n{'='*60}")
    print(f"Testing: {track_name} ({track_id})")
    print(f"{'='*60}")
    
    # Update config to use this track
    import json
    with open('race_config.json', 'r') as f:
        config = json.load(f)
    config['current_track'] = track_id
    with open('race_config.json', 'w') as f:
        json.dump(config, f, indent=2)
    
    # Import fresh (reloads config)
    if 'dot_ai_car' in sys.modules:
        del sys.modules['dot_ai_car']
    
    import dot_ai_car
    
    # Run headless simulation
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption(f"Testing: {track_name}")
    clock = pygame.time.Clock()
    
    # Create population
    population = dot_ai_car.RacingPopulation(50)
    
    results = {
        'track_id': track_id,
        'track_name': track_name,
        'generations': [],
        'success': True,
        'error': None
    }
    
    try:
        for gen in range(1, max_generations + 1):
            # Run generation
            frame_count = 0
            max_frames = 1000  # Prevent infinite loops
            
            while not population.all_done() and frame_count < max_frames:
                population.update()
                frame_count += 1
                
                # Render occasionally to keep window responsive
                if frame_count % 100 == 0:
                    screen.fill((18, 18, 18))
                    pygame.display.flip()
                    
                    # Check for quit events
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            raise KeyboardInterrupt("User quit")
            
            # Calculate fitness and evolve
            population.calculate_fitness_and_rank()
            
            gen_result = {
                'generation': gen,
                'frames': frame_count,
                'finishers': sum(1 for d in population.dots if d.finished),
                'champion_fitness': population.champion.fitness if population.champion else 0,
                'avg_fitness': sum(d.fitness for d in population.dots) / len(population.dots)
            }
            results['generations'].append(gen_result)
            
            print(f"  Gen {gen}: {gen_result['finishers']}/{50} finished, "
                  f"Avg Fitness: {gen_result['avg_fitness']:.1f}, "
                  f"Frames: {frame_count}")
            
            if gen < max_generations:
                population.evolve()
        
        print(f"✓ {track_name} passed all tests!")
        
    except Exception as e:
        results['success'] = False
        results['error'] = str(e)
        print(f"✗ {track_name} FAILED: {e}")
    
    finally:
        pygame.quit()
    
    return results

def main():
    """Test all tracks"""
    import json
    
    print("\n" + "="*60)
    print("TRACK SIMULATION TEST")
    print("Running 3 generations on each track...")
    print("="*60)
    
    # Load track order
    with open('tracks_database.json', 'r') as f:
        tracks_db = json.load(f)
    
    track_order = tracks_db.get('track_order', [])
    all_results = []
    
    for track_id in track_order:
        track = tracks_db['tracks'][track_id]
        result = quick_test_track(track_id, track['name'])
        all_results.append(result)
    
    # Summary
    print("\n" + "="*60)
    print("SIMULATION TEST SUMMARY")
    print("="*60)
    
    passed = sum(1 for r in all_results if r['success'])
    failed = len(all_results) - passed
    
    for result in all_results:
        status = "✓" if result['success'] else "✗"
        print(f"{status} {result['track_name']}")
        if not result['success']:
            print(f"   Error: {result['error']}")
    
    print("\n" + "="*60)
    if failed == 0:
        print(f"✓ ALL {len(all_results)} TRACKS PASSED SIMULATION")
    else:
        print(f"✗ {failed}/{len(all_results)} TRACKS FAILED")
    print("="*60 + "\n")
    
    return failed == 0

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\nTest interrupted by user")
        sys.exit(1)
