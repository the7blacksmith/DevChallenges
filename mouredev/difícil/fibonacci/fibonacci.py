def fibonacci():
    fib_list = [0, 1]
    while True:
        x = fib_list[-1] + fib_list [-2]
        if x >= 50:
            break
        fib_list.append(x)
    return fib_list

import time

def fibonacci_sequence():
    fib_list = [0, 1]
    print(fib_list[0])
    time.sleep(0.5)
    print(fib_list[-1])
    time.sleep(0.5)
    while True:
        x = fib_list[-1] + fib_list [-2]
        if x >= 30:
            break
        fib_list.append(x)
        print(x)
        time.sleep(0.5)
    return x


    

