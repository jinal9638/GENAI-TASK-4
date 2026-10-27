sales_int=[]
total_sales=0

with open("D:/JINAL/GEN AI COURSE/sales_data.txt",'r') as f:
    f.read()
    f.seek(0)
    for line in f:
        convert_int=int(line.strip())
        sales_int.append(convert_int)
        total_sales+=convert_int

    print("Total Sales:",total_sales)
    print("Highest Sale:",max(sales_int))
    print("Lowest Sale:",min(sales_int))
    print("Average Sales:",total_sales/len(sales_int))
    