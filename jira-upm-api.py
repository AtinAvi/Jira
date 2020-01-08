import json
import requests
from requests.auth import HTTPBasicAuth
listofplugins=[]
class Plugin:
    def __init__(self,selflink,plugin_enabled,plugin_name,plugin_version,plugin_vendor,
                 license_nearlyExpired,license_pluginKey,license_valid,license_evaluation,
                 license_licenseType,license_expiryDateString,license_SEN):
        self.selflink=selflink
        self.plugin_enabled=plugin_enabled
        self.plugin_name=plugin_name,
        self.plugin_version=plugin_version,
        self.plugin_vendor=plugin_vendor,
        self.license_nearlyExpired=license_nearlyExpired,
        self.license_pluginKey=license_pluginKey,
        self.license_valid=license_valid,
        self.license_evaluation=license_evaluation,
        self.license_licenseType=license_licenseType,
        self.license_expiryDateString=license_expiryDateString,
        self.license_SEN=license_SEN

plugin_resp=requests.get('https://epbyminw6305.minsk.epam.com/jira/rest/plugins/1.0/',auth=HTTPBasicAuth('admin','test'),verify=False)


plugin_object=json.loads(plugin_resp.text)
print(plugin_object["plugins"])


for item in plugin_object["plugins"]:

    try:
        if(item["userInstalled"]==True & item["usesLicensing"]==True):
            plugin_name=item["name"]
            plugin_enabled=item["enabled"]
            plugin_vendor=item["vendor"]["name"]
            plugin_version=item["version"]
            plugin_selflink=item["links"]["self"]

            license_info_url="https://epbyminw6305.minsk.epam.com"+plugin_selflink+"/license"
            print(license_info_url)
            license_resp=requests.get(license_info_url,auth=HTTPBasicAuth("admin","test"),verify=False)

            license_object=json.loads(license_resp.text)
            plugin_license_nearlyExpired=license_object["nearlyExpired"]
            plugin_license_pluginKey=license_object["pluginKey"]
            plugin_license_valid=license_object["valid"]
            plugin_license_evaluation=license_object["evaluation"]
            plugin_license_licenseType=license_object["licenseType"]
            plugin_license_expiryDateString=license_object["expiryDateString"]
            plugin_license_SEN=license_object["supportEntitlementNumber"]

            print(plugin_license_SEN)
            print(plugin_license_expiryDateString)
            x={"selflink":plugin_selflink,
               "Enabled":plugin_enabled,
               "Name":plugin_name,
               "vendor":plugin_vendor,
               "version":plugin_version,
               "License nearlyExpired":plugin_license_nearlyExpired,
               "Plugin key":plugin_license_pluginKey,
               "License Valid":plugin_license_valid,
               "License evaluation":plugin_license_evaluation,
               "License licenseType":plugin_license_licenseType,
               "License Expiry date":plugin_license_expiryDateString,
               "License SEN":plugin_license_SEN}


            PluginObject=Plugin(plugin_selflink,plugin_enabled,plugin_name,plugin_version,plugin_vendor,
                           plugin_license_nearlyExpired,plugin_license_pluginKey,plugin_license_valid,
                           plugin_license_evaluation,plugin_license_licenseType,plugin_license_expiryDateString,
                           plugin_license_SEN)
            listofplugins.append(x)
            jsonTest=json.dumps(listofplugins)


    except Exception as err:
        print(err)
with open ("plugins.json","w") as jsonfile:
    jsonfile.write(jsonTest)





