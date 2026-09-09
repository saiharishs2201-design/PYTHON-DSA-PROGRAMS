def is_valid(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack.pop() != pairs[ch]:
                return False

    return len(stack) == 0


s = input("Enter parentheses: ")

if is_valid(s):
    print("Valid Parentheses")
else:
    print("Invalid Parentheses")