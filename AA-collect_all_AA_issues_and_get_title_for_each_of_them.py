import re
import requests
import json

IM_string = '''\
AA-7269, AA-7270, AA-7271, AA-7275, AA-7276 - Done
AA-7285 - In Progress

AA-7274 done
AA-7264 done
AA-7280 done
AA-7281 done
AA-7282 done
'''

issue_list = re.findall(r'AA\-\d+', IM_string)

url = "https://jira.labs.quest.com/rest/api/2/search"

headers = {'authorization': 'Basic bmVsc29uLndhbmdAcXVlc3QuY29tOlNIRU5NRTM1bWltYQ=='}

for issue in issue_list:
    querystring = {"jql": "key = %s" % (issue)}
    response = requests.request("GET", url, headers=headers, params=querystring)
    myData = json.loads(response.text)
    print(myData['issues'][0]['key'] + ': ' + myData['issues'][0]['fields']['summary'])


# querystring = {"jql": "key = %s" % (issue_list[0])}
# response = requests.request("GET", url, headers=headers, params=querystring)
# myData = json.loads(response.text)
# print(myData['issues'][0]['fields']['summary'])
