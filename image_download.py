import csv
import  wget

urls = []
products = []
with open("KostiaT.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=",")
    for row in readCSV:
        if row[3] and row[3] not in urls:
            urls.append(row[3])
            products.append(row[2])
urls = urls[1:]
products = products[1:]

for i in range(0,len(urls)):
    try:
        img = wget.download(urls[i],out="./result_img/" + products[i].replace("\\","").replace("/","").replace(":","").replace("*","")
                            .replace("?","").replace("<","").replace(">","").replace("|","").replace('"',"") + ".jpg")
    except:
        print(products[i],"error")
        continue