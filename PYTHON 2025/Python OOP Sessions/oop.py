#CS50
# https://www.youtube.com/watch?v=e4fwY9ZsxPw

def main():
    name = input("Name: ")
    house = input("House: ")
    print(f"{name} is from {house}")

def get_name():
    return input("Name:")

def get_house():
    return input("House: ")

if __name__ == "__main__":
    main()