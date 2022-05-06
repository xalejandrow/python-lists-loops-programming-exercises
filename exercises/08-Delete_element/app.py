people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    #Your code go here:
    new_list = []
    for person in people:
        if person != person_name:
            new_list.append(person)
    return new_list
    
print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))