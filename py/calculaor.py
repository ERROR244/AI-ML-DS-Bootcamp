def main():
    x = int(input("what's x? "))
    print("x squared is,", square(x))

def square(n):
    return n + n
    # return n ** 2
    # return pow(n)

if __name__ == "__main__":
    main()