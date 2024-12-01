left = []
right = []
distance = 0

with open("day1/data.txt") as f:
    for line in f:
        l, r = line.strip().split("   ")
        left.append(int(l))
        right.append(int(r))

left.sort()
right.sort()
print(f"left: {left}")
print(f"right: {right}")

for idx, num in enumerate(left):
    distance += abs(num - right[idx])

print(f"distance: {distance}")
