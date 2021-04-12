def read_to_list(filename):
    with open(filename, 'r') as file:
        nums = file.read().splitlines()
    return nums
