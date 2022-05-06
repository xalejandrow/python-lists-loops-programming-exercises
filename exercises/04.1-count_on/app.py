my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

#your code go here:
new_list = []
for i in my_list:
    if str(type(i)) == "<class 'dict'>" or str(type(i)) == "<class 'list'>":
        new_list.append(i)

print(new_list)
