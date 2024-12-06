num = """3   4
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

lefts = sorted(left_column)
rights = sorted(right_column)

result = []

for i in range (len(lefts)):
    result.append(abs(lefts[i]-rights[i]))
    
final_result=sum(result)

print(final_result)
