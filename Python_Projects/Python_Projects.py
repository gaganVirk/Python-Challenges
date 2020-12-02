# 4_1 Pizzas 
pizzas = ['vege', 'meat', 'fish']

for pizza in pizzas:
    print("i like " + pizza)

print("i am learning python")
print("i am loving it!")

# 4_2 Animals
animals = ['tiger', 'cat', 'dog']
for animal in animals:
    print(animal[0] + " is a dangerous animal.")
    
print("Any of those animals would be a great pet.")

#4_3 Counting to Twenty
for i in range(1,21):
    print(i)

#4_4 One Million

for num in range(1,1000000):
    print(num) 

# 4_5 Summing a Million
value = list(range(1,1000001))
print(min(value))
print(max(value))
print(sum(value))

# 4_6 Odd Numbers
for i  in range(1,20):
    if i % 2 != 0:
        print(i)

# 4_7 Threes
for i in range(1,11):
    three = i * 3
    print(three)

# 4_8 Cubes
for i in range(1, 11):
    cube = i ** 3
    print(cube)

# 4_9 Cube Comprehension
cubes = [value ** 3 for value in range(1,11)]
print(cubes)