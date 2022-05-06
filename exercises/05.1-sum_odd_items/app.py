arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:
def sum_odd_values(items):

    total= 0
    #The magic happens here:
    for i in arr:
        if i % 2 != 0:
            total += i
    return total

print(sum_odd_values(arr))


