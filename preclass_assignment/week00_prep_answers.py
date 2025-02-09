#Exercise 1
def greet(input_name):
    print('Hello,', input_name)

greet('world')

#Exercise 2
def goldilocks(bed_size):
    if bed_size < 140:
        print('Too small!')
    elif bed_size > 150:
        print('Too large!')
    else:
        print('Just right. :)')

goldilocks(139)
goldilocks(140)
goldilocks(150)
goldilocks(151)

#Exercise 3
def square_list(number_list):
    results_list = [None]*len(number_list) # initialize output list

    for item in range(len(number_list)): 
        results_list[item]= number_list[item]**2
    print(results_list)

square_list([1,2,3])

#Exercise 4
def fibonnaci_stop (max_number):
    if max_number < 1:
        return []  # If max_number is less than 1, return an empty list
    else: 
        iteration=1 #Starts iteration count in 1
        x=1
        next_x=x
        fibonnaci_sequence=[x,next_x]
        while x + next_x <= max_number:
            x = fibonnaci_sequence[iteration]
            next_x= x + fibonnaci_sequence[iteration-1]
            fibonnaci_sequence.append(next_x)
            iteration += 1
    
    print(fibonnaci_sequence)

fibonnaci_stop(30)     

#Exercise 5
def clean_pitch(x, status):

    for i, status_value in enumerate(status):
        if status_value > 0 and (x[i]<0 or x[i]>90):
            x[i]=-999  # Substitutes "bad values" for -999
    print (x)

# Example:
x = [-1, 2, 6, 95]
status = [1, 0, 0, 0]

clean_pitch(x, status)

