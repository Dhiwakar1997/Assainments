address="180.8.170.9/18"

print(f"The given network address : {address}")

netAddrs = address.split(".")
subnetDict = {"1":int(netAddrs[0]),"2":int(netAddrs[1]),
            "3":int(netAddrs[2]),"4":int(netAddrs[3].split("/")[0]), "subnet":int(netAddrs[3].split("/")[1]),}
#print(subnetDict)

subnet = subnetDict["subnet"]

classNum = 1
first_address=""
last_address = ""

while subnet>0:
    if subnet<8:
        #print(2**subnet)
        numOfSubnet = 2**subnet
        subnetNumOfIP= 256//numOfSubnet
        #print(255//subnetNumOfIP)
        subnetIndex = (subnetDict[str(classNum)]//subnetNumOfIP)+1
        #print(first_address)
        first_address = first_address+f"{int(subnetNumOfIP*(subnetIndex-1))}."
        last_address = last_address+f"{int(subnetNumOfIP*subnetIndex)-1}."
        subnet-=8
        #print(first_address)
        continue

    first_address= first_address+f"{subnetDict[str(classNum)]}."
    #print(first_address)
    last_address= last_address+f"{subnetDict[str(classNum)]}."
    classNum+=1
    subnet -=8

while classNum<4:
    first_address= first_address+f"0."
    last_address= last_address+f"0."
    classNum+=1

first_address = first_address[:-1]
last_address = last_address[:-1]

print(f"Number of IP addresses in the block = {subnetNumOfIP}")
print(f"{first_address = }")
print(f"{last_address = }")