import os
import requests
import mimetypes

os.chdir("C:\\test")
# walking thorough directory(searching all subdirectories(issueides))
dirs=os.scandir('c:\\test')
basepath='C:\\test'
for subdir in dirs:
    if os.path.isdir(os.path.join(basepath,subdir)):
      issueid=subdir.name
      #print(issueid)
      fullpath=os.path.join(basepath,issueid)
      #print(fullpath)
      # Searching files inside subdirectory(All attachments)
      folders=os.scandir(os.path.join(fullpath))
      for entry in folders:
          attachname=entry.name
          attachefullpath=os.path.join(fullpath,attachname)
          if os.path.isfile(attachefullpath):
                print(attachefullpath)
                headers = {
                    'X-Atlassian-Token': 'nocheck',
                }
                type = (mimetypes.MimeTypes().guess_type(attachefullpath)[0])
                files = {
                    'file': (attachname, open(attachefullpath, 'rb'), type)
                }
                response = requests.post(
                    'https://demo.softgile.com/testjira/rest/api/2/issue/{}/attachments'.format(issueid),
                    headers=headers, files=files, auth=('Administrator', '******'))
                print(response)
                print(type)

