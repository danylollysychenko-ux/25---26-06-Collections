def main():
    favorites = []
    while True:
        enter = input("Enter your favorite thing or press Q to quit: ").strip()
        if enter != "Q":
            favorites.append(enter)
        elif enter.upper == "Q":
            for i, favorite in enumerate(favorites, start = 1):
                print(f"{i}. {favorite}")
        
        while True:
            try:
                enter = int(input("Enter a index to see specific snack (99 to quit) -> "))
                if enter == 99:
                    break
                else:
                    print(favorites[enter])
            
            except ValueError:
                print("Please enter a index.")
            except IndexError:
                print(f"Please enter a index from 0 to {len(favorites)}.")

if __name__ == "__main__":
    main()