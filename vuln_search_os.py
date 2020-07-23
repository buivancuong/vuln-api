import sys
from vulners import Vulners

if len(sys.argv) < 3: 
    print("Lack of OS name and version")
    sys.exit()
os_name = str(sys.argv[1])
os_ver = str(sys.argv[2])

vuln_api = Vulners(api_key='3V1UM5KU2XUPC83L4L1HA5NCGXRRIHQM16WT9BD6OA6H94Y5HI18TGQZ4R7CZQU8')
result = vuln_api.distributive(os=os_name, version=os_ver)
print(result)