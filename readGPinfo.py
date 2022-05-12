import requests
import lxml.html as lh
import pandas as pd
import readLinksGP


resultLinks = readLinksGP.raceresult()
print(resultLinks)


url="https://www.formula1.com/en/results.html/2022/races/1124/bahrain/race-result.html"

page = requests.get(url)

doc = lh.fromstring(page.content)

tr_elements = doc.xpath('//tr')

#Checking the len of the first 12 rows
[len(T)for T in tr_elements[:12]]

col = []
i = 0

col=[]
i=0

#For each row, store each first element (header) and an empty list
for t in tr_elements[0]:
    i+=1
    name=t.text_content()
    #print ('%d:"%s"'%(i,name))
    col.append((name,[]))


for j in range(1,len(tr_elements)):
    #T is our j'th row
    T=tr_elements[j]
    
    #If row is not of size 10, the //tr data is not from our table 
    if len(T)!=9:
        break
    
    #i is the index of our column
    i=0
    
    #Iterate through each element of the row
    for t in T.iterchildren():
        
        data=t.text_content() 
        #Check if row is empty
        if i>0:
        #Convert any numerical value to integers
            try:
                data=int(data)
            except:
                pass
        #Append the data to the empty list of the i'th column
        col[i][1].append(data)
        #Increment i for the next column
        i+=1

Dict={title:column for (title,column) in col}


df=pd.DataFrame(Dict)

df.drop("",inplace=True, axis=1)

dfDrivers = pd.read_excel(r"I:\Documentos\Programacao\Repos\GitHub\BotF1discord\databases\main_database.xlsx",sheet_name="db_drivers")

df["Driver"] = df["No"].map(dfDrivers.set_index("No")["driver_name"])


df.to_excel(r"I:\Documentos\Programacao\Repos\GitHub\BotF1discord\databases\Bahrein.xlsx",sheet_name="Bahrein")