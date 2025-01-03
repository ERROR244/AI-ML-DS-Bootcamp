def main():
    # Ask user for their name, Remove whitespace and capitalize user's name
    name = input("What's your name?\n").strip().title()
    # or
    # name = input("What's your name?\n")

    # Remove whitespace from str and capitalize user's name
    # name = name.strip().title()
    #or 
    # name = name.strip().capitalize()



    # Say hello to world
    hello()
    # Say hello to user
    hello(name)

def hello(to="world"):
    # print("Hello, " + name)
    # print("Hello,", name)
    print("Hello,", to)

main()