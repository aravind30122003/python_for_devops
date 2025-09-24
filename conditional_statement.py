
# Conditional Statements (if, elif, else)

age = 18

if age < 18:
    print("You are a minor")
elif age == 18:
    print("You just became an adult")
else:
    print("You are an adult")

# for loops

# Print numbers from 0 to 4
for i in range(5):
    print(i)

# Print elements of a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


# while loops

count = 0
while count < 5:
    print("Count is", count)
    count += 1

# break , continue , pass 

for i in range(5):
    if i == 3:
        break
    print(i)
for i in range(5):
    if i == 3:
        continue
    print(i)
for i in range(5):
    if i == 3:
        pass  # We can implement later
    print(i)
