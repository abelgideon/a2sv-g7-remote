grid = []
for i in range(5):
    row = input().split()
    grid.append(row)

x1 = 0
y1 = 0

centerX = 2
centerY = 2

for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i][j] == "1":
            x1 = i
            y1 = j

print(abs(centerX - x1) + abs(centerY - y1))