# 1.create a list of sales amount
sales=[1200,450,980,1500,3000]

# using with open close file automatically 
with open("sales_data.txt","w+") as f:
    # iterate on every element to write each element on newline
    for s in sales:
        # converting element to string
        f.write(str(s) + "\n")

# Note: The file is automatically closed here!


print("\n--- Reading the whole file later in 'r' mode ---")
# Open the file again in standard read mode ('r')

with open("sales_data.txt", "r") as f:
  # Read all lines and print them cleanly
  for line in f:
    print(line.strip())

# Convert each number to a string and join them together with commas
sales_string=",".join(str(s) for s in sales)

with open("sales_data.txt","w+") as f:
   # Write the single comma-separated line to the file
   f.write(sales_string)

   f.seek(0)
   print("--- Reading Comma-Seperated Line from File ---")
   print(f.read())

# converting them into again in a line form for next file operation
with open("sales_data.txt","w+") as f:
    
    for s in sales:
        f.write(str(s) + "\n")