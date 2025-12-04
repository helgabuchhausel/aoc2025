import re

def part_1(file_path):
    accessible_count = 0

    try: 
        with open(file_path, "r", encoding="utf-8") as file:
            grid = [list(line.strip()) for line in file if line.strip()]
        
        rows = len(grid)
        cols = len(grid[0])
        accessible_count = 0
        
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        for r in range(rows):
            for c in range(cols):
                # Current cell is a roll of paper
                if grid[r][c] == '@':
                    neighbor_rolls = 0
                    
                    # Check all 8 neighbors
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        
                        # Boundary checks
                        if 0 <= nr < rows and 0 <= nc < cols:
                           if grid[nr][nc] == '@':
                                neighbor_rolls += 1
                    
                    #  Fewer than 4 neighbors
                    if neighbor_rolls < 4:
                        accessible_count += 1

        print(f"Accessible Rolls: {accessible_count}")
    except FileNotFoundError:
        print(f"The file file_path has vanished into the void")
        return 0
    except PermissionError:
        print(f"You lack authority to view file_path")
        return 0 
     
    return accessible_count

def part_2(file_path): 
    try:
        # Load the Grid
        with open(file_path, 'r') as f:
            grid = [list(line.strip()) for line in f if line.strip()]
        
        rows = len(grid)
        cols = len(grid[0])
        total_removed = 0
        

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        while True:
            candidates_to_remove = []
            
            #  Scan the entire grid 
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == '@':
                        neighbor_rolls = 0
                        
                        # Count neighbors
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < rows and 0 <= nc < cols:
                                # Only '@' counts as a neighbor roll. 
                                # 'x' or '.' are empty space.
                                if grid[nr][nc] == '@':
                                    neighbor_rolls += 1
                        
                        # Check the rule: Fewer than 4 neighbors
                        if neighbor_rolls < 4:
                            candidates_to_remove.append((r, c))
            
            # Check for Stabilization
            if not candidates_to_remove:
                break 
            
            # Update the Grid 
            # Remove all identified candidates simultaneously
            total_removed += len(candidates_to_remove)
            for r, c in candidates_to_remove:
                grid[r][c] = '.' 
                
        print(f"Total Rolls Removed: {total_removed}")
        return total_removed

    except FileNotFoundError:
        print("File not found.")


if __name__ == "__main__":
    file_path = "4.txt"
    print("Part 1")
    print(f"Result: {part_1(file_path)}")
    print("Part 2")
    print(f"Result: {part_2(file_path)}")


