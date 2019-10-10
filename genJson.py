#set up paths and vars
import sys
import os
import time

folder = 'sales'
for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        #elif os.path.isdir(file_path): shutil.rmtree(file_path)
    except Exception as e:
        print(e)

csvfile = open("SalesRecords.csv",'r')
jsonfile = open("sales\\SalesRecords.json", 'w')
jheader = '{\n'
jsnEnd = '\n}'
jsonfile.write(jheader);
#os.remove()
arr=[]
headers = []

# Read in the headers/first row
for header in csvfile.readline().split(','):
    header = header.replace('\n','')
    headers.append(header)
rn = 1
fileCounter = 1
fileContent = ""
# Extract the information into the "xx" : "yy" format.
for line in csvfile.readlines():
  rn = rn+1
  line = line.replace('\n','')
  
  fileContent += "{"
  lineStr = ""
  for i,item in enumerate(line.split(',')):
      lineStr+='"'+headers[i] +'":"' + item + '",\n'
    
  lineStr = lineStr.rstrip(',\n')
  lineStr += "},\n"
    
  if( rn % 1000==0):
    lineStr= lineStr.rstrip(',\n')
    lineStr += '\n'
    fileContent += lineStr

    jsonfile.write(fileContent)
    jsonfile.write(jsnEnd)
    jsonfile.close()
    #exit()
    time.sleep(5)
    os.rename("sales\\SalesRecords.json", "sales\\SalesRecords.json"+"."+ str(fileCounter))
    jsonfile = open("sales\\SalesRecords.json", 'w')
    jsonfile.write(jheader)
    fileCounter = fileCounter + 1  
    fileContent = ""
  else :
      fileContent += lineStr

  
csvfile.close()
jsonfile = open("sales\\SalesRecords.json", 'a')
jsonfile.write(jsnEnd)
jsonfile.close()



""" for i in range(len(arr)-1):
    if(i % 10000==0):
        jsonfile.close()
        jsonfile = open("SalesRecords.json", 'a')

    jsn = ""
    if i == len(arr)-2:
        jsn+="{"+str(arr[i])[:-2]+"}\n"
    else:
        jsn+="{"+str(arr[i])[:-2]+"},\n"
    jsonfile.write(jsn) """