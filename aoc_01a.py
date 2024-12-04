def read_pairs(filename):
    """
    Read numbers into two lists and return
    """
    list_1 = list()
    list_2 = list()
    with open(filename) as f:
        for line in f:
            a, b = line.strip().split()
            list_1.append(int(a))
            list_2.append(int(b))
    return sorted(list_1), sorted(list_2)

def pair_differences(list_1, list_2):
    """
    Calculate the sum of differences between two ordered lists
    """
    diffs = list()
    for i in range(len(list_1)):
        pair_diff = list_1[i] - list_2[i]
        diffs.append(abs(pair_diff))
    return sum(diffs)

def similarity(list_1, list_2):
    list_count = dict()
    for num in list_2:
        if not num in list_count:
            list_count[num] = 0
        list_count[num] += 1
    
    score = 0
    for num in list_1:
        if not num in list_count:
            continue

        score += num * list_count[num]
    return score

def main():
    input_lists = "01_input.txt"
    list_1, list_2 = read_pairs(input_lists)
    print("difference sum:", pair_differences(list_1, list_2))
    print("similarity score:", similarity(list_1, list_2))

if __name__ == "__main__":
    main()