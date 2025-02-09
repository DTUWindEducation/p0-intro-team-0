def greet(input_name):
    print('Hello,', input_name)

greet('world')


def goldilocks(bed_size):
    if bed_size < 140:
        print('Too small!')
    elif bed_size > 150:
        print('Too large!')
    else:
        print('Just right. :)')

goldilocks(139)
goldilocks(140)
goldilocks(151)

def square_list(number_list):
    results_list = [None]*len(number_list) # initialize output list

    for item in range(len(number_list)): 
        results_list[item]= number_list[item]**2
    print(results_list)

square_list([1,2,3])

def fibonnaci_stop (max_number):
    if max_number < 1:
        return []  # If max_number is less than 1, return an empty list
    else: 
        iteration=1
        x=1
        next_x=x
        fibonnaci_sequence=[x,next_x]
        while x <= max_number:
            next_x= x + fibonnaci_sequence[iteration-1]
            fibonnaci_sequence.append(next_x)
            iteration += 1
            x = fibonnaci_sequence[iteration]
    
    print(fibonnaci_sequence)

fibonnaci_stop(30)     

def clean_pitch(x, status):
    cleaned_angles = []  # List to store cleaned pitch angles

    for pitch, status_value in zip(x, status):
        if (pitch < 0 or pitch > 90) and status_value > 0:
            cleaned_angles.append(-999)  # Mark bad values
        else:
            cleaned_angles.append(pitch)  # Keep good values as is

    return cleaned_angles

# Example:
x = [-1, 2, 6, 95]
status = [1, 0, 0, 0]

cleaned = clean_pitch(x, status)
print(cleaned)


