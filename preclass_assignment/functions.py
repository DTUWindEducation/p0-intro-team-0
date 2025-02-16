def greet(str):
    print(f'Hello, {str}!')

def goldilocks(length):
    if length < 140:
        print('Too small!')
    elif length > 150:
        print('Too large!')
    else:
        print('Just right. :)')

def square_list(input):
    res = [x**2 for x in input]
    return res

def fibonacci_stop(end_val):
    fib_list = [1, 1]
    while (next_val := fib_list[-1]+fib_list[-2]) <= end_val:
        fib_list.append(next_val)
    return fib_list

def clean_pitch(pitch, status):
    for i, status in enumerate(status):
        if status == 1 and not (0 < pitch[i] < 90):
            pitch[i] = -999
    return pitch
