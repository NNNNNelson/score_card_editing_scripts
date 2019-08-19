import requests
import json
from pprint import pprint as pp

url = "https://jira.labs.quest.com/rest/api/2/search"

currentSprint = "2019 ACE.5 Sprint4"
nextSprint = "2019 ACE.5 Sprint5"

# querystring = {"jql": "project in (fgl, wcf) and sprint in (\"%s\", \"%s\") and status not in (\"Under Review\", resolved, closed) order by type" % (currentSprint, nextSprint)}
querystring = {"jql": "project in (fgl, wcf) and sprint in (\"%s\", \"%s\") and status was not in (\"Under Review\", resolved, closed) on \"20190214\"order by type" % (currentSprint, nextSprint)}


headers = {'authorization': 'Basic bmVsc29uLndhbmdAcXVlc3QuY29tOlNIRU5NRTMxbWltYQ=='}

response = requests.request("GET", url, headers=headers, params=querystring)

myData = json.loads(response.text)

typeTempComparison = myData['issues'][0]['fields']['issuetype']['name']

for x in range(0, myData['total']):
    if x == 0:
        print(myData['issues'][x]['fields']['issuetype']['name'] + '\n' + myData['issues'][x]['key'] + ': ' + myData['issues'][x]['fields']['summary'])
        typeTempComparison = myData['issues'][0]['fields']['issuetype']['name']
    else:
        if myData['issues'][x]['fields']['issuetype']['name'] == typeTempComparison:
            print(myData['issues'][x]['key'] + ': ' + myData['issues'][x]['fields']['summary'])
        else:
            print(myData['issues'][x]['fields']['issuetype']['name'] + '\n' + myData['issues'][x]['key'] + ': ' + myData['issues'][x]['fields']['summary'])
        typeTempComparison = myData['issues'][x]['fields']['issuetype']['name']
