import numpy as np

def read_puzzle(filename):
    """
    Reads wordsearch as list of strings
    """
    puzzle = list()
    try:
        with open(filename) as f:
            for line in f:
                puzzle.append(line.strip())
    except FileNotFoundError:
        print("File '" + filename + "' not found")
        exit

def match_horizontal(puzzle):
    kernel = np.asarray([list("XMAS")])

def main():
    pass

if __name__ == "__main__":
    main()