# system port scanner + txt report
# goals: 
# 1. have the script scan the ip address
# 2. print that x common ports or more [up to 10] are open and that they should be closed
# 3. have the output data be put onto a txt file and have that printed in a set format 


import ipaddress

print("IP Address Port Scanner + Report")


while True:
    user = input("Enter an IP address or range to be scanned (1.1.1.1/24): ").strip()
    try:
        ip_obj = ipaddress.ip_address(user)
        print(f"valid IPv{ip_obj.version} address entered: {ip_obj}")
    except ValueError:
        print("invalid adress. try again.")


