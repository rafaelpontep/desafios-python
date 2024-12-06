numbers = """3   4
4   3
2   5
1   3
3   9
3   3"""

# Split the string into rows

rows = numbers.strip().split('\n')

# Create two separate lists
left_column = []
right_column = []

for row in rows:
    left_column.append(int(row.split()[0]))
    right_column.append(int(row.split()[1]))

    
result = []

for i in range(len(left_column)):
   n = right_column.count(left_column[i])
   result.append(n * left_column[i])
   
final_result = sum(result)

print(final_result)
