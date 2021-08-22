#Python_Code to check the Grocery List
"Computer Programming Tutor,  Aug 19,2021"

while True:
    try:
        budamt = float(input("Enter your Budget,[£]: "))
        totbudget = budamt
    except ValueError:
        print("PRINT NUMBER AS AN AMOUNT")
        continue
    else:
        break
a = {"Name:":[],"Quant":[],"Price":[]}
# Converting dictionary to list
b = list(a.values())
na = b[0]
qty = b[1]
price = b[2]

while True:
    try:
        ch = int(input("1.ADD\n2.EXIT\nEnter Your Choice:"))
    except ValueError:
        print("\nERROR: Choose Only digits from the given Option")
        continue
    else:
        if ch == 1 and totbudget > 0:
            prodname = input("Enter Product Name:")
            q = input("Enter Quantity: ")
            # Input Price of the Product
            p = float(input("Enter Price of the Product,[£]:"))
            if p > totbudget:
                print("\nCAN, T BUT THE PRODUCT")
                continue
            else:
                if prodname in na:
                    ind = na.index(prodname)
                    qty.remove(qty[ind])
                    price.remove(price[ind])
                    qty.insert(ind,q)
                    price.insert(ind,p)
                    totbudget = budamt - sum(price)
                    print("\nAmount Left",totbudget)
                else:
                    na.append(prodname)
                    qty.append(q)
                    price.append(p)
                    totbudget = budamt - sum(price)
                    print("\nAmount Left",totbudget)


        elif totbudget <= 0:
            print("\nNO BUDGET")
        else:
            break
print("\nAmount Left: Rs.",totbudget)
if totbudget in price:
    print("\nAmount Left can Buy you a",na[price.index(totbudget)])
print("\nGROCERY LIST")
# Print Final Grocery List
for i in range(len(na)):
    print(na[i],qty[i],price[i])

        
