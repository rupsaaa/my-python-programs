stack = []
string = input("Enter an expression: ")
is_valid = True
for i in string:
    if i in ["{", "[", "("]:
        stack.append(i)
    elif i in ["}", "]", ")"]:
        if not stack:
            is_valid = False
            break
        top = stack.pop()
        if i == "}" and top != "{":
            is_valid = False
            break
        if i == "]" and top != "[":
            is_valid = False
            break
        if i == ")" and top != "(":
            is_valid = False
            break

if is_valid and len(stack) == 0:
    print("Balanced")
else:
    print("Not Balanced")

