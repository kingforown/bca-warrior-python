# Vote or not
#indian citizen / foreign citizen


print("-"*50)
print("|      Check if you are Eligible Vote or Not     |")
print("-"*50)
try:
    b=str(input("| You Are 'Indian Citizen' Y (or) N :"))   
    if a == 'Y' or a == 'y':
        print("-"*50)
        print("|     Thanks For Conformation Indian Citizen     |")
        print("-"*50)
        a=int(input("| Enter the your Age :"))

        if a<=17:
            print("-"*50)
            print("|        You Are Not Eligible to vote            |")

        elif a>=18:
            print("-"*50)
            print("|            You Are Eligible to vote            |")
    elif b == "N" or  b == "n":
        print("-"*50)    
        print("|     Sorry only Indian Citizen Are Allowed      |") 
    else:
        print("-"*50)
        print("|          >>>>> USER INPUT ERROR <<<<<          |")

except ValueError:
    print("-"*50)
    print("|          >>>>> USER INPUT ERROR <<<<<          |")
    print("-"*50)
finally:
    print("-"*50)
    print('|            "Thank You Vist Again"              |')
    print("-"*50)
