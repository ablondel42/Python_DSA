def valid_parentheses(s):
    if len(s) % 2:
        return "invalid"
    
    stack = []

    for p in s:
        if p in "([{":
            stack.append(p)
        else:
            if len(stack):
                if stack[-1] == "(" and p != ")" or \
                    stack[-1] == "[" and p != "]" or \
                    stack[-1] == "{" and p != "}":
                    return "invalid"
                else:
                    stack.pop()
    if len(stack):
        return "invalid"
    return "valid"


if __name__ == "__main__":
    s = "(({}])"
    print(valid_parentheses(s))

