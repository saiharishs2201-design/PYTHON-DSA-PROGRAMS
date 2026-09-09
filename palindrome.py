def is_palindrome(s):
    return s==s[::-1]
while True :

    user_input =input("Enter the string :")
    if is_palindrome (user_input):
        print(f"{user_input}is a palindrome")
    else:
        print(f"{user_input} is not a palindrome")

    continue_choice =input("want to check another string ?(yse to continue, no to Exit) : ").strip().lower()
    if continue_choice!="yes":
        print("Thankyou...............Exiting!!!!")
        break