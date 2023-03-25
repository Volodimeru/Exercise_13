def main():
    #ask name of variable to user.
    name = input("camelCase: ")
    print("snake_case: ", end="")
    #convert and print variable name in snake_case.
    for c in name:
        if c.isupper():
            print("_" + c.lower(), end="")
        else:
            print(c, end="")
    print()
main()