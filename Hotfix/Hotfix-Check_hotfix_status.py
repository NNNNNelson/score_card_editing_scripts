import re
import requests
import json

IM_string = '''\
Hotfix NO.  CSR NO. Title   Status  Comment
      HFIX-294
4479829-1
Hotfix VMware 5.7.7.3 Release   Resolved    Hot Fix package has been posted to FTP and support has been notified.
      HFIX-296
4420825-1
Hotfix Foglight for Virtualization vApp 8.8.5 Release   Resolved    package posted to FTP
HFIX-297
4512353-1
Found NullPointerException when using Rest API AlarmResource.getAlarmByRuleId   Resolved    Hotfix package has been posted to FTP and support notified.
HFIX-298
4519237-1
4513809
Hotfix Optimizer 5.7.7.1 Release    Under Review    Assign to Ken for package
1.    HFIX-299
4428962-1
4475536
Foglight Management Server 5.9.3 hotfix - database sequence number overflow Resolved    Hotfix package posted to FTP.  Support has been notified.
1.    HFIX-300
4531682 
FSM 4.7.1 HOTFIX Release    Open    Bug fixing
1.    HFIX-301
4532673-1  
Foglight for Cloud manager Hotfix 1.5.2 Under Review    Assign to Ken for package

'''

issue_list = re.findall(r'HFIX\-\d+', IM_string)

url = "https://jira.labs.quest.com/rest/api/2/search"

headers = {'authorization': 'Basic bmVsc29uLndhbmdAcXVlc3QuY29tOlNIRU5NRTM0bWltYQ=='}

for issue in issue_list:
    querystring = {"jql": "key = %s" % (issue)}
    response = requests.request("GET", url, headers=headers, params=querystring)
    myData = json.loads(response.text)
    print(myData['issues'][0]['key'] + ': ' + myData['issues'][0]['fields']['status']['name'])


# querystring = {"jql": "key = %s" % (issue_list[0])}
# response = requests.request("GET", url, headers=headers, params=querystring)
# myData = json.loads(response.text)
# print(myData['issues'][0]['fields']['summary'])
