def string_reverse(str):
    return str[::-1]

while True:
    str = input("Enter the string : ")
    reverse_str = string_reverse(str)
    print(reverse_str)

    continue_choice = input("want to reverse another string ? (yes to continue, no to Exit) : ").strip().lower()
    if continue_choice != "yes" :
        print("Exiting the string reverse .........Goodbye!")
        break