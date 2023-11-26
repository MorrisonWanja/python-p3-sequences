def print_fibonacci(length):
    fib_sequence = [0, 1]
    if length == 0:
        print("[]")
        return
    elif length == 1:
        print("[0]")
        return
    while len(fib_sequence) < length:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    print(fib_sequence)
