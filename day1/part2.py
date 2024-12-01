left = []
right = []
similarity = 0

with open("day1/data.txt") as f:
    for line in f:
        l, r = line.strip().split("   ")
        left.append(int(l))
        right.append(int(r))

for num in left:
    ocurrences = right.count(num)
    similarity += (num * ocurrences)

print(f"similarity: {similarity}")
