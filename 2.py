import re

def part_1(file_path):

    line = ""
    try: 
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()          
    except FileNotFoundError:
        print(f"The file file_path has vanished into the void")
        return 0
    except PermissionError:
        print(f"You lack authority to view file_path")
        return 0 
     
    result = 0
    line = line.split(",")
    for item in line:
        try:
            first_id, second_id = int(item.split("-")[0]), int(item.split("-")[1])
        except ValueError:
            print(f"Invalid item format: {item}")
            continue

        current_range = range(first_id, second_id + 1)

        # Check for numbers with repeated consecutive patterns
        for number in current_range:
            if not re.search(r"^(.+)\1$", str(number)) == None: 
                result += number
    return result

def part_2(file_path): 
    line = ""
    try: 
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()          
    except FileNotFoundError:
        print(f"The file file_path has vanished into the void")
        return 0
    except PermissionError:
        print(f"You lack authority to view file_path")
        return 0 
     
    result = 0
    line = line.split(",")
    for item in line:
        try:
            first_id, second_id = int(item.split("-")[0]), int(item.split("-")[1])
        except ValueError:
            print(f"Invalid item format: {item}")
            continue

        current_range = range(first_id, second_id + 1)

        for number in current_range:
            if not re.search(r"^(.+)\1+$", str(number)) == None: 
                result += number
    return result


if __name__ == "__main__":
    file_path = "2.txt"
    print("Part 1")
    print(f"Result: {part_1(file_path)}")
    print("Part 2")
    print(f"Result: {part_2(file_path)}")


