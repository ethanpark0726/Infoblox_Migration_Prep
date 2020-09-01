import requests
import pprint

routerList = list()
device = response = requests.get('https://akips11.hsnet.ufl.edu/api-script?password=1r0nM@1d3n;function=web_export_device_list;', verify=False)

for elem in device.text.splitlines():
    line = elem.split(',')
    temp = list()
    if line[0][1].startswith('R'):
        temp.append(line[0])
        temp.append(line[1].strip())
        routerList.append(temp)

pprint.pprint(routerList)

print(len(routerList))

#=IF(RIGHT(LEFT(A2, 2), 1)="R", "Router", "Non-router")