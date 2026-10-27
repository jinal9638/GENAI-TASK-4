# using a empty dict
product={}

# creating range ask only 3 times product name and price
for _ in range(3):
    product_name=input("Enter product name:")
    product_price=float(input("Enter product price:"))
    product[product_name]=product_price

print("\n",product,"\n")

# opening a file which is also create this name file
with open("product.txt",'w') as f:
    f.write(f"Product Name | Product Price \n")
    f.write("-"*30+"\n")
    # iterate on each key and value
    for k,v in product.items():
        f.write(f"{k:<12} | {v} \n")
    f.write("-"*30+"\n")

# open with read mode and printing that file
with open("product.txt",'r') as f:
    print(f.read())
    