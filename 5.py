def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    
    for current_start, current_end in intervals[1:]:
        last_start, last_end = merged[-1]
        
        if current_start <= last_end + 1: 
            merged[-1] = (last_start, max(last_end, current_end))
        else:
            merged.append((current_start, current_end))
    return merged

def part_1(file_path):
    ranges  =[]
    reading_ranges = True
    fresh_count = 0
    try: 
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    if reading_ranges:
                        reading_ranges = False
                        ranges = merge_intervals(ranges)
                    continue
                

                if reading_ranges:
                    try: 
                        start, end = map(int, line.split("-"))
                        ranges.append((start, end))
                    except ValueError:
                        print(f"Skipping malformed range: {line}")
                else: 
                    try:
                        candidate_id = int(line)
                        is_fresh = any(start <= candidate_id <= end for start, end in ranges)

                        if is_fresh:
                            fresh_count +=1
                    except ValueError:
                        print(f"Skipping malformed ID: {line}")

        return fresh_count

    except FileNotFoundError:
        print(f"The file file_path has vanished into the void")
        return 0
    except PermissionError:
        print(f"You lack authority to view file_path")
        return 0 
    

def part_2(file_path): 
    ranges  = []
    reading_ranges = True
    result = 0
    try: 
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    if reading_ranges:
                        reading_ranges = False
                        ranges = merge_intervals(ranges)
                        result = sum((end- start + 1) for start, end in ranges)
                    continue
                
                if reading_ranges:
                    try: 
                        start, end = map(int, line.split("-"))
                        ranges.append((start, end))
                    except ValueError:
                        print(f"Skipping malformed range: {line}")

        return result

    except FileNotFoundError:
        print(f"The file file_path has vanished into the void")
        return 0
    except PermissionError:
        print(f"You lack authority to view file_path")
        return 0 


if __name__ == "__main__":
    file_path = "5.txt"
    print("Part 1")
    print(f"Result: {part_1(file_path)}")
    print("Part 2")
    print(f"Result: {part_2(file_path)}")
