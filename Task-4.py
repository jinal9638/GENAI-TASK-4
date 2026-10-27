# create empty list which store value in integer form
sales_int=[]

# initalize variable value as zero
total_sales=0

# using with open and mention path to open a file
with open("D:/JINAL/GEN AI COURSE/sales_data.txt",'r') as f:
    f.read()
    # reading value at start
    f.seek(0)
    # iterate on each line
    for line in f:
        # converting line value into integer
        convert_int=int(line.strip())
        # appending value in empty list
        sales_int.append(convert_int)
        # adding value in zero initalize value variable
        total_sales+=convert_int

    # printing total,max,min and average value of that list
    print("Total Sales:",total_sales)
    print("Highest Sale:",max(sales_int))
    print("Lowest Sale:",min(sales_int))
    print("Average Sales:",total_sales/len(sales_int))
    