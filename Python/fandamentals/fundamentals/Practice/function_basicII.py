#countdowning
def countdown(x):
    return list(range(x, -1, -1))

print(countdown(5))
#Print and Return
def print_and_return(numbers):
    print(numbers[0])
    return numbers[1]

print(print_and_return([1, 2])) 

#First Plus Length
def first_plus_length(first):
    return first[0] + len(first)

print(first_plus_length([1, 2, 3, 4, 5]))

#This Length, That Value

def length_and_value(size, value):
    return [value] * size

print(length_and_value(4, 7)) 
print(length_and_value(6, 2))  


