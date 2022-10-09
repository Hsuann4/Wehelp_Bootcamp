import json
import urllib.request as request
import re

src ="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data = json.load(response)

clist = data["result"]["results"]
with open("data.csv","w",encoding ="utf-8") as file:
    for i in clist:
        if i["xpostDate"] >= "2015":
            files = str(i["file"]).split("http")
            files_2 = files[0:][1]
        
            print(i["stitle"]+","+i["address"][5:8]+ "," + i["longitude"]+","+i["latitude"]+","+ "http" + files_2 + "\n")
            file.write(i["stitle"]+","+i["address"][5:8]+ "," + i["longitude"]+","+i["latitude"]+ ","+ "http" + files_2  + "\n")
    
       



            
        


