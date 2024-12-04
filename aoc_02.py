MAX_DIFF = 3
MIN_DIFF = 1

def read_lists(filename):
    """
    Read numbers into two lists and return
    """
    lists = list()
    with open(filename) as f:
        for line in f:
            line_list = [int(char) for char in line.strip().split()]
            lists.append(line_list)
    return lists

def slow_continuous(list):
    """
    Determines if a list on integers in continuously changing by at least
    1 and no more than 3. List can be either decreasing or increasing. A
    list that follows the rules returns True, others return False
    """
    increase = list[0] - list[1] < 0
    for idx in range(len(list) - 1):
        diff = list[idx] - list[idx +1]
        # check valid direction
        if increase and (-diff < MIN_DIFF):
            return False
        elif not increase and (diff < MIN_DIFF):
            return False
        
        # check magnitude
        if abs(diff) > MAX_DIFF:
            return False
        
        # list follows rules
    return True

def slow_cont_damped(list):
    bad_count = 0
    increase = list[0] - list[1] < 0
    for idx in range(len(list) - 1):
        diff = list[idx] - list[idx +1]
        # check valid direction
        if increase and (-diff < MIN_DIFF):
            bad_count += 1
        elif not increase and (diff < MIN_DIFF):
            bad_count += 1
        # check magnitude
        elif abs(diff) > MAX_DIFF:
            bad_count += 1
        
        if bad_count >= 2:
            return False
        
    # list follows rules
    return True

def main():
    lists = read_lists("02_input.txt")
    valids = 0
    damped_valids = 0
    for record in lists:
        if slow_continuous(record):
            valids += 1
        if slow_cont_damped(record):
            damped_valids += 1
        
    
    print("Number valid:", valids)
    print("Number damped valid:", damped_valids)

if __name__ == "__main__":
    main()
