import random
name_string = input("Give me everybody's names, seperate d by a comma. ")
name = name_string.split(',')
index = random.randint(0,len(name)-1)
# or we can write print(random.choice(names) is going to by a meal)
print(f'{name[index]} is going to buy a meal today')


boy = ['anjesh','sarang','rahul']
girl = ['koyal','kalpana','mannu']
nested_list = [boy,girl]
print(nested_list)