sales=[1200,450,980,1500,3000]

print("\n---Reading file in read mode---")
with open('sales_data.txt','r') as f:
    print(f.read())

print("\n---Reading the first line using readline---")
with open('sales_data.txt','r') as f:
    print(f.readline())

print("\n---Reading the all lines using readlines---")
convert_int=[]
with open('sales_data.txt','r') as f:
    print(f.readlines())
    f.seek(0)
    for line in f:
        if line.strip('\n').isdigit():
            cleaned_line=int(line)
            convert_int.append(cleaned_line)
    print("Converted interger list:",convert_int)
    
    