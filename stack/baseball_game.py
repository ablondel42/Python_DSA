def baseball_game(ops: list[str]) -> int:
    stack = []

    for op in ops:
        if op not in "+DC":
            stack.append(int(op))
        else:
            if op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(stack[-1] * 2)
            elif op == '+':
                stack.append(stack[-1] + stack[-2])
    
    return sum(stack)


if __name__ == '__main__':
    ops = ["5", "2", "C", "D", "+"]
    print(baseball_game(ops))
    
    ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
    print(baseball_game(ops))
    
    ops = ["1"]
    print(baseball_game(ops))