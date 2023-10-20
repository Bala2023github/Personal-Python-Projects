
# users = {0:"Mario", 1: "Luigi", 3:"James"}
# print(users.values())

# print(users.keys())

# popped = users.pop(1)

# print(popped)

# users.popitem()

# print(users)


# sample: dict = {0:['a','b'], 1:['c','d']}

# my_copy = sample.copy()

# # print(id(sample))

# # print(id(my_copy))

# my_copy[0]='!!!!'

# print(sample)

# print(my_copy)


# users = {0:"Mario", 1: "Luigi", 3:"James"}

# print(users.get(0))

# print(users.get(123,"Missing"))

# print(users.setdefault(999,'///'))

# print(users)

# people: list[str] = ['Mario','Luigi','James']

# users: dict = dict.fromkeys(people, 'unknown')

# print(users)

users = {0:"Mario", 1: "Luigi", 3:"James"}

users |={1:'Ooi'}

print(users.items())

for k,v in users.items():
    print(k,v)