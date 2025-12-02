# Part 1 
def get_password(file_path):
    try:
        # Open file
        with open(file_path, "r", encoding="utf-8") as file: 
            position, password = 50, 0
            for index, line in enumerate(file, 1):

                # Skip empty lines 
                if not line:
                    continue

                clean_line = line.strip()

                direction = clean_line[0].upper()

                # Skip if it doesnt start with R or L 
                if direction not in ('R', 'L'):
                    continue

                try:
                    # Parse distance to integer
                    distance = int(clean_line[1:])

                    # Calculate rotation
                    if direction == 'R':
                        position = (position + distance) % 100
                    if direction == 'L': 
                        position = (position - distance) % 100

                    # Increase the password value if the position is 0
                    if position == 0:
                        password = password + 1
                except ValueError:
                    print(f"Line {index}: doesn't contain a valid number")
    except FileNotFoundError:
        print(f"The file '{file_path}' has vanished into the void")
        return 0
    except PermissionError:
        print(f"You lack tha uthority to view '{file_path}'")
        return 0
    return password

file_path = "1.csv"
print(f"{ get_password(file_path) } is the actual password.")


##################################################################
# Part 2 

def calculate_with_new_method(file):
    try: 
        with open(file_path, "r", encoding="utf-8") as file: 
            current_pos = 50
            total_zeros = 0

            for index, line in enumerate(file, 1): 

                line = line.strip()
                # Skip empty lines 
                if not line:
                    continue

                direction = line[0].upper()

                # Skip if it doesnt start with R or L 
                if direction not in ('R', 'L'):
                    continue

                try:
                    try: 
                        distance = int(line[1:])
                    except: 
                        continue

                    # Calculate rotation
                    if direction == 'R':
                        next_pos = current_pos + distance
                        zeros_hit = (next_pos // 100) - (current_pos // 100)
                        total_zeros += zeros_hit
                        current_pos = next_pos % 100

                    if direction == 'L': 
                        target_pos = current_pos - distance
                            
                        zeros_hit = ((current_pos - 1) // 100) - ((target_pos - 1) // 100)
                        total_zeros += zeros_hit
                            
                        current_pos = target_pos % 100

                    
                except ValueaError:
                    print(f"Line {index}: doesn't contain a valid number")
    except FileNotFoundError:
        print(f"The file '{file_path}' has vanished into the void")
        return 0
    except PermissionError:
        print(f"You lack tha uthority to view '{file_path}'")
        return 0
    
    return total_zeros


print(f"{calculate_with_new_method(file_path)}")


