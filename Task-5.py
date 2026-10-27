product={}

for _ in range(3):
    product_name=input("Enter product name:")
    product_price=float(input("Enter product price:"))
    product[product_name]=product_price

print("\n",product,"\n")


with open("product.txt",'w') as f:
    f.write(f"Product Name | Product Price \n")
    f.write("-"*30+"\n")
    for k,v in product.items():
        f.write(f"{k:<12} | {v} \n")
    f.write("-"*30+"\n")

with open("product.txt",'r') as f:
    print(f.read())
    