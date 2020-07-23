import sys
from vulners import Vulners

if len(sys.argv) < 2:
    print("Lack of indentificator need to search for document")
    sys.exit()
if len(sys.argv) >= 2:
    identificator = str(sys.argv[1])

vuln_api = Vulners(api_key='3V1UM5KU2XUPC83L4L1HA5NCGXRRIHQM16WT9BD6OA6H94Y5HI18TGQZ4R7CZQU8')
result = vuln_api.document(identificator=identificator)
print(result)
