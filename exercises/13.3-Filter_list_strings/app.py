
names = ['Liam','Emma','Noah','Olivia','William','Ava','James','Isabella','Logan','Sophia',
'Benjamin','Mia','Mason','Charlotte','Elijah','Amelia','Oliver','Evelyn','Jacob','Abigail',
'Lucas','Harper','Michael','Emily','Alexander','Elizabeth','Ethan','Avery','Daniel','Sofia',
'Matthew','Ella','Aiden','Madison','Henry','Scarlett','Joseph','Victoria','Jackson','Aria',
'Samuel','Grace','Sebastian','Chloe','David','Camila','Carter','Penelope','Wyatt','Riley']


#Your code go here:
def filterNames(name):
    if name.find('am') != -1:
        return name

new_names = list(filter(filterNames, names))
print(new_names)