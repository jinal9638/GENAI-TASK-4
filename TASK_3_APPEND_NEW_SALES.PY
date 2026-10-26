# opening file in append mode
with open("sales_data.txt",'a') as f:
    f.write(f"{5000}\n")
    f.write(f"{2500}\n")
    f.write(f"{1700}\n")

# opening file in read mode
print("---Printing file after appending new sales---")
with open("sales_data.txt",'r') as f:
    print(f.read())

# print the total number of lines after appending
print("---Printing the total number of lines after appending---")
with open("sales_data.txt",'r') as f:
    # iterate on each line and sum of them
    total_lines = sum(1 for line in f)

print(f"Total number of lines:{total_lines}")