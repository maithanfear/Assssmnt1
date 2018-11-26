
#define lists
custNumb = (1)
carModel = ["Corsa","Astra","Combo","Vectra","Omega"]
carPrice = [10000,12500,14000,16500,21000]
profMarg = [0.09,0.115,0.123,0.128,0.131]
delivFee = [0.034,0.04,0.051,0.056,0.061]
#various model sales lists
corSales = [0,0,0,0,0]
astSales = [0,0,0,0,0]
comSales = [0,0,0,0,0]
vecSales = [0,0,0,0,0]
omeSales = [0,0,0,0,0]
totSales = [0,0,0,0,0]
#price breakdown lists
delivTot = [0,0,0,0,0]
profiTot = [0,0,0,0,0]
salesTot = [0,0,0,0,0]

#function to get a positive whole number only
def getPosInt(screenMessage, errorMessage):
    while True:
        try:
            fInteger = int(input(screenMessage))
        except ValueError:
            print(errorMessage)
        else:
            if fInteger < 1:
                print(errorMessage)
            else:
                return(fInteger)

#function to get a number in a defined range
def getOption(screenMessage,errorMessage):
    while True:
        try:
            fInteger = int(input(screenMessage))
        except ValueError:
            print(errorMessage)
        else:
            if fInteger < 1:
                print(errorMessage)
            elif fInteger > 5:
                print(errorMessage)
            else:
                return(fInteger)
            
#function
def getString(screenMessage):
    while True:
        fString = input(screenMessage)
        if not fString.isalnum():
            print("Invalid entry, please try again.")
        else:
            return fString

#function to validate only allowed characters are entered
def getName (screenMessage,errorMessage):
    valid_characters = " aábcdeéfghiíjklmnoópqrstuúvwxyzAÁBCDEÉFGHIÍJKLMNOÓPQRSTUÚVWXYZ'-"
    # Just insert other characters into that string if you want to accept anything else.
    while True:
        firstName = input("What's your first name? ")
        if all(char in valid_characters for char in firstName):
            break
        print(errorMessage)
    return firstName
    
#function
def getSales():
    errorMessage = ('''
=================================
That's invalid, please try again:
=================================''')
    userName = getName ("Please enter your name: ",errorMessage)
    carMod = getOption('''
Please select a model from the list below.
1 - Opel Corsa
2 - Opel Astra
3 - Opel Combo
4 - Opel Vectra
5 - Opel Omega
ENTER 1-5:''',errorMessage)
    carNum = getPosInt("Please enter the quantity you require: ",errorMessage)
    totSales[x] = carNum
    y= carMod-1
    if carMod is 1 :
        corSales [x] = carNum
    if carMod is 2 :
        astSales [x] = carNum
    if carMod is 3 :
        comSales [x] = carNum        
    if carMod is 4 :
        vecSales [x] = carNum
    if carMod is 5 :
        omeSales [x] = carNum
    salesTot [x] = totSales [x] * (carPrice[y]*(delivFee[y]+1))
    profiTot [x] = totSales [x] * (carPrice[y]* profMarg[y])
    delivTot [x] = totSales [x] * (carPrice[y]* delivFee[y])
        
    print ('''

Sales details for {name}:
============================

Model:       {car}
Quantity:    {num}
Total Cost: €{tot}
============================
'''.format (name=userName, car=carMod, num = carNum, tot= (carNum * carPrice[y])*(1 + delivFee[y])))

    

for x in range (custNumb):
    getSales()

print('''
Opel Sales Summary Information
================================================

Total Opel Models Sold  :{total}
================================================
Total Opel Corsa  sales :{corsa}
Total Opel Astra  sales :{astra}
Total Opel Combo  sales :{combo}
Total Opel Vectra sales :{vectra}
Total Opel Omega  sales :{omega}
=================================================
Total Sales including delivery charges: €{sales}

Total profit: €{profit}

Average profit generated per customer: €{average})
'''.format(total=sum(totSales),corsa = sum(corSales),astra = sum(astSales),combo = sum(comSales),
           vectra = sum(vecSales), omega = sum(omeSales),sales = sum(salesTot), profit =sum(profiTot),average = sum(profiTot)/custNumb))




