squares = [x ** 2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squares = []
for x in range(10):
  squares.append(x ** 2)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

odds = [x for x in range(10) if x % 2 != 0]
# [1, 3, 5, 7, 9]

List = [x ** 2 if x % 2 == 0 else x ** 3 for x in range(10)]
# [0, 1, 4, 27, 16, 125, 36, 343, 64, 729]

first = []

for x in range(1, 5):
  for y in range(5, 1, -1):
    if x != y:
      first.append((x, y))

second = [(x, y) for x in range(1, 5) for y in range(5, 1, -1) if x != y]

print(first == second)
print(first)