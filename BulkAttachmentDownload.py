import os
import requests
import urllib.request
import json
array=[]
rootPath="C:\\test\\"
with open('C:\\test\\listofIssues.txt') as file:
    i=0
    for line in file:
        array.append(line.strip("\n"))
#        print(line)
        i=i+1
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
    try:
        response=requests.get(url,headers=headers, auth=('username','p@ssw0rd'))
        print(response)
        responsestring=response.text

        jsonobject=json.loads(responsestring)
        print(jsonobject)
        attachmentNumber=len(jsonobject['fields']['attachment'])
        for n in range(0,attachmentNumber):
            downloadURL=jsonobject['fields']['attachment'][n]['content']
            fileName=jsonobject['fields']['attachment'][n]['filename']
            attachmentID=jsonobject['fields']['attachment'][n]['id']
            resultFilename=attachmentID+fileName
            print(downloadURL)
            print(fileName)
            print(resultFilename)


            index=fileName.rfind(".")
            unicFileName=fileName[:index]+attachmentID+fileName[index:]
            print(index)


            print(attachmentID)
            downloadedContent=requests.get(downloadURL,auth=('username','password'),stream=True)
            open(unicFileName,'wb').write(downloadedContent.content)
    except requests.exceptions.HTTPError as error:
        print("")















#print(attachmentjsonobject['id'])
#print(jsonobject['fields']['attachments'])




