def baseball_game(ops):
    scores = []

    for op in ops:
        if op == "C":
            scores.pop()
        elif op == "D":
            scores.append(scores[-1] * 2)
        elif op == "+":
            scores.append(scores[-1] + scores[-2])
        else:
            scores.append(int(op))

    return sum(scores)


if __name__ == '__main__':
    ops = ["5", "2", "C", "D", "+"]
    print(baseball_game(ops))
    
    ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
    print(baseball_game(ops))
    
    ops = ["1"]
    print(baseball_game(ops))