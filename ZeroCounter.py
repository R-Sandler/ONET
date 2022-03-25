from OnetWebService import OnetWebService
import pandas as pd

if __name__ == "__main__":
    onet_ws = OnetWebService("harqen_ai", "2298huc")
    careerDoc = onet_ws.call('mnm/careers/?sort=name&start=1&end=923')
    careerNames = []
    careerCodes = []
    for item in careerDoc['career']:
        careerNames.append(item['title'])
        careerCodes.append(item['code'])

    careerList = list(zip(careerNames, careerCodes))

    zeroList = []
    for row in careerList:
        code = row[1]
        searchResults = onet_ws.call('mnm/careers/'+code+"/skills")
        try:
            check = item in searchResults['group']
        except:
            zeroList.append(row[0])

    
    print(zeroList)