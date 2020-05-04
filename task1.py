import string
from random import choice

symbols = string.ascii_letters+string.digits
def main():
    return"".join([choice(symbols) for i in range(30)])


if __name__ == "__main__":
    print(main())
