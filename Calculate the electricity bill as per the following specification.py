# Calculate the electricity bill as per the following specification ?
#   For first 50 units, 0.50/unit
#   For next 100 units, 0.75/unit
#   For next 150 units, 1.20/unit
#   For remaining units , 1.50/unit
#   Add 20% additional surcharge



print("-"*48)
print("|             WELCOME TO APCPDCL               |")
print("-"*48)
try:
    previous=int(input("| Enter The previous Month Unit :"))
    print("-"*48)
    current=int(input("| Enter The Current Month  Unit :"))
    print("-"*48)
    store=current-previousS
    STOREONE=50*0.50
    STORETWO=50*0.75
    STORETHREE=50*1.20
    if current<previous:
        print("|     Enter Previous Month Less Than Unit      |")
        print("-"*48)

    elif store<=50:
        MP=store*0.50
        MP2=MP*0.20
        print("| ENERGY CHRGS:","RS",MP,"                       |")
        print("-"*48)
        print("| SURCHARGE   :","RS",MP2,"                        |")
        print("-"*48)
        print("| TOTAL DUE   :","RS",MP+MP2,"                       |")
        print("-"*48)
        
    elif store<=100:
        ultra1=50*0.50
        ultra2=store-50
        ultra3=ultra2*0.75
        SUR=ultra1+ultra3
        SUR1=SUR*0.20
        print("| ENERGY CHRGS:","RS",ultra1+ultra3,"                       |")
        print("-"*48)
        print("| SURCHARGE   :","RS",SUR1,"                       |")
        print("-"*48)
        print("| TOTAL DUE   :","RS",ultra1+ultra3+SUR1,"                       |")
        print("-"*48)

    elif store<=150:
        ultra1=STOREONE+STORETWO
        ultra2=store-100
        ultra3=ultra2*1.20
        SUR=ultra1+ultra3
        SUR1=SUR*0.20
        print("| ENERGY CHRGS:","RS",ultra1+ultra3,"                      |")
        print("-"*48)
        print("| SURCHARGE   :","RS",SUR1,"                       |")
        print("-"*48)
        print("| TOTAL DUE   :","RS",ultra1+ultra3+SUR1,"                      |")
        print("-"*48)

    elif store>=250:
        ultra1=STOREONE+STORETWO+STORETHREE
        ultra2=store-150
        ultra3=ultra2*1.50
        SUR=ultra1+ultra3
        SUR1=SUR*0.20
        print("| ENERGY CHRGS:","RS",ultra1+ultra3,"                      |")
        print("-"*48)
        print("| SURCHARGE   :","RS",SUR1,"                       |")
        print("-"*48)
        print("| TOTAL DUE   :","RS",ultra1+ultra3+SUR1,"                      |")
        print("-"*48)
 
except ValueError:
        print("-"*48)
        print("|>>>>>>>>>> USER INPUT VALUE ERROR ! <<<<<<<<<<|")
        print("-"*48)
finally: 
        print("-"*48)      
        print('|\t    "Thank You Visit Again"            |')
        print("-"*48)
