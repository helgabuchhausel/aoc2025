import re 
def part_1(file_path):
    result = 0
    num = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                bank = line.strip()
                if bank.isdigit():
                    if len(bank) > 2:
                        search_area_first = bank[:-1]
                        first_digit = max(search_area_first)
                        

                        first_idx = bank.find(first_digit)
                    
                        search_area_second = bank[first_idx+1:]
                        second_digit = max(search_area_second)
                    
                        num = int(first_digit + second_digit)
                        
                        result += num
                    else:
                        print("Bank number must be more than 2 digits")
                else:
                    print("Invalid bank number")
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except PermissionError:
        print(f"Permission denied when trying to read {file_path}.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return result

def part_2(file_path):
    result = 0
    target_length = 12
    total_joltage = 0
    try:
        with open(file_path, 'r') as file:
            for line in file:
                bank = line.strip()
                if bank.isdigit():
                    if len(bank) > 2:
                        current_search_start = 0
                        result_digits = ""
                        
                        # We need to find exactly 12 digits
                        for i in range(target_length):
                            needed_after = target_length - 1 - i
                            
                            # The furthest index/position we can search to.
                            search_end = len(bank) - needed_after
                            
                            # Define the window we are allowed to search in
                            window = bank[current_search_start : search_end]
                            
                            # Find the max digit in this window
                            best_digit = max(window)
                            
                            # Find WHERE that digit is (relative to the window start)
                            offset = window.find(best_digit)
                            
                            # Calculate absolute index in the original string
                            real_index = current_search_start + offset
                            
                            result_digits += best_digit
                            
                            # Move our start point to just after the digit we just picked
                            current_search_start = real_index + 1
                        
                        total_joltage += int(result_digits)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except PermissionError:
        print(f"Permission denied when trying to read {file_path}.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return total_joltage

if __name__ == "__main__":
    print(f"{part_1('3.txt')}") 
    print(f"{part_2('3.txt')}")