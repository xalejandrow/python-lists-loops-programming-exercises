def lyrics_generator(matrix):
    result = ""
    text1 = "Boom "
    text2 = "Drop the base "
    text3 = "!!!Break the base!!! "
    aux = 0
    for num in matrix:
        if num == 0:
            result += text1
        if num == 1:
            result += text2
            aux += 1
        if aux == 3:
            result += text3
            aux = 0
    return result

# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))