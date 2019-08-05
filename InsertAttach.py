import os
import requests
import mimetypes

os.chdir("C:\\test")
# walking thorough directory(searching all subdirectories(issueides))
for root, dirs, files in os.walk("C:\\test", topdown=False):
    for issueid in dirs:
        # Printing subdirectory full name(root+issueid)
        subdir = os.path.join(root, issueid)

        # Searching files inside subdirectory(All attachments)
        for rootsub, dirssub, filessub in os.walk(subdir, topdown=False):
            # Getting file name inside curl request by attachmentfull name and attachment relative name
            for attachname in filessub:
                print(subdir)
                print(os.path.join(rootsub, attachname))
                #              issuename = issueid
                attachfullpath = os.path.join(rootsub, attachname)
                headers = {
                    'X-Atlassian-Token': 'nocheck',
                }
                type = (mimetypes.MimeTypes().guess_type(attachfullpath)[0])
                files = {
                    'file': (attachname, open(attachfullpath, 'rb'), type)
                }
                response = requests.post(
                    'https://{baseURL}/rest/api/2/issue/{}/attachments'.format(issueid),
                    headers=headers, files=files, auth=('Administrator', '******'))
                print(response)
                print(type)