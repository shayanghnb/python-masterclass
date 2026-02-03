matrix = []

for i in range(3):
    while True:
        row = list(map(int, input(f"enter 3 numbers for row {i}: ").split()))
        if len(row) == 3:
            matrix.append(row)
            break
        else:
            print("enter exactly 3 numbers. try again.")
            continue

for i in range(3):
    print(f"sum of row{i} = {sum(matrix[i])}")
    
for i in range(3):
    column_sum = 0
    for j in range(3):
        column_sum += matrix[j][i]
    print(f"sum of column {i} = {column_sum}")