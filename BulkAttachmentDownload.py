import os
import requests
import urllib.request
import json
array=[]
rootPath="C:\\test\\"

#Opening file with Issue list and adding issue names to array
with open('C:\\test\\listofIssues.txt') as file:
    i=0
    for line in file:
        array.append(line.strip("\n"))
#        print(line)
        i=i+1
#Creating folder structure according array    
for i in range(0,len(array)):
    print(array[i])
    os.chdir(rootPath)
    DirectoryPathString=rootPath+array[i]
    os.mkdir(DirectoryPathString)
    os.chdir(DirectoryPathString)
    print(DirectoryPathString)
    headers = {
                    'X-Atlassian-Token': 'nocheck',
                }
    url="baseURL/rest/api/2/issue/"+array[i]
    print(url)
#Sending http request for getting attachment information
    try:
        response=requests.get(url,headers=headers, auth=('username','p@ssw0rd'))
        print(response)
        responsestring=response.text
#Converting http response to JSON object
        jsonobject=json.loads(responsestring)
        print(jsonobject)
#Getting information about attachment number of every issue
        attachmentNumber=len(jsonobject['fields']['attachment'])
        for n in range(0,attachmentNumber):
            downloadURL=jsonobject['fields']['attachment'][n]['content']
            fileName=jsonobject['fields']['attachment'][n]['filename']
            attachmentID=jsonobject['fields']['attachment'][n]['id']
            resultFilename=attachmentID+fileName
            print(downloadURL)
            print(fileName)
            print(resultFilename)

#Creating unique attachment filename for storing on local disk(If attachemnt have same name)
            index=fileName.rfind(".")
            unicFileName=fileName[:index]+attachmentID+fileName[index:]
            print(index)

#Downloading attachment to local disk
            print(attachmentID)
            downloadedContent=requests.get(downloadURL,auth=('username','password'),stream=True)
            open(unicFileName,'wb').write(downloadedContent.content)
    except requests.exceptions.HTTPError as error:
        print("error")















#print(attachmentjsonobject['id'])
#print(jsonobject['fields']['attachments'])




