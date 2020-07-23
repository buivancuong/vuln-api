import sys
from vulners import Vulners

if len(sys.argv) < 2:
    print("Lack of query keyword need to search")
    sys.exit()
if len(sys.argv) == 2:
    query_keyword = str(sys.argv[1])
    print("Default limit result is 100")
    limit_result = 100
if len(sys.argv) > 2:
    query_keyword = str(sys.argv[1])
    limit_result = int(sys.argv[2])

vuln_api = Vulners(api_key='3V1UM5KU2XUPC83L4L1HA5NCGXRRIHQM16WT9BD6OA6H94Y5HI18TGQZ4R7CZQU8')
result = vuln_api.search(query=query_keyword, limit=limit_result)
print(result)
