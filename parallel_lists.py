def print_parallel_lists(list1:list[str], list2:list[int]):
    """prints a table with 2 lists. Assumes list1  is string list2 is a list of ints"""
    print("*" * 29)
    print(f"*Song            | Rating *")
    for idx in range(len(list1)):
        # note this assumes the parallel lists have the same number of elements.
        print(f"*{list1[idx].ljust(16)}| {str(list2[idx]).ljust(7)}*")

    print("*" * 29)

def main():
    # printing out a table with parallel lists:
    # parallel lists are two seperate lists where the indexes line up to relate the info
    # the values correspond
    songs = ["imagine", "possible", "Halo Theme Song", "Cry baby Cry"]
    rating = [10, 8, 6, 7]
    print_parallel_lists(songs, rating)

if __name__ == "__main__":
    main()