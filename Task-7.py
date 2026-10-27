prices={
    "Mouse":[500],
    "Keyboard":[800],
    "Monitor":[7000],
    "Pendrive":[400],
    "Camera":[5000]
}

for k,v in list(prices.items()):
    discount=int(input(f"Enter discount for the product '{k}':"))
    discounted_price=v[0]-(v[0]*discount/100)
    prices[k].append(discounted_price)

print(prices)

with open("discount_report.txt",'w') as f:
    f.write("-"*50+"\n")
    f.write(f"{'Product':<12} | Original Price | Discounted Price \n")
    f.write("-"*50+"\n")
    for k,v in prices.items():
        f.write(f"{k:<12} | {v[0]:<14} | {v[1]} \n")
    f.write("-"*50+"\n")

with open("discount_report.txt",'r') as f:
    print(f.read())