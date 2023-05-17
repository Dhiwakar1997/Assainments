address="193.8.17.9"# input()

print(f"The given network address : {address}")

netAddrs = address.split(".")
subnetDict = {"1":int(netAddrs[0]),"2":int(netAddrs[1]),
            "3":int(netAddrs[2]),"4":int(netAddrs[3])}

if subnetDict["1"]<128:
    subnetNumOfIP = 2**24
    first_address = f"{subnetDict['1']}.0.0.0"
    last_address = f"{subnetDict['1']}.255.255.255"
elif subnetDict["1"]<192:
    subnetNumOfIP = 2**16
    first_address = f"{subnetDict['1']}.{subnetDict['2']}.0.0"
    last_address = f"{subnetDict['1']}.{subnetDict['2']}.255.255"
elif subnetDict["1"]<223:
    subnetNumOfIP = 2**8
    first_address = f"{subnetDict['1']}.{subnetDict['2']}.{subnetDict['3']}.0"
    last_address = f"{subnetDict['1']}.{subnetDict['2']}.{subnetDict['3']}.255"
else:
    first_address = f"{subnetDict['1']}.{subnetDict['2']}.{subnetDict['3']}.{subnetDict['4']}"
    last_address = f"{subnetDict['1']}.{subnetDict['2']}.{subnetDict['3']}.{subnetDict['4']}"

print(f"Number of IP addresses in the block = {subnetNumOfIP}")
print(f"{first_address=}")
print(f"{last_address=}")