NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

i = 0
while i < len(NAMES):
    print(NAMES[i], AGES[i])
    i += 1

for name in NAMES:
    print(name)

for name, age in zip(NAMES, AGES):
    print(f"{name} {age}")

for name in reversed(NAMES):
    print(name)

for i in range(5):
    print(i)


# enumerate
for i, name in enumerate(NAMES):
    print(f"{i} {name}")

for name, age in zip(NAMES, AGES):
    print(f"{name} is {age} years old")  
         
for i, (name, age) in enumerate(zip(NAMES, AGES)):
    print(f"{i} {name} is {age} years old")

