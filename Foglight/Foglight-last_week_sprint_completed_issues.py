import requests
import json
from pprint import pprint as pp

url = "https://jira.labs.quest.com/rest/api/2/search"

the_first_day = "2019/07/26"

sprint1 = "2019 ACE.5 Sprint6"
sprint2 = "2019 ACE.5 Sprint6"

outputStr = 'Printing last week completed issues'


def printEqualSign(outputStr):
    for i in range(len(outputStr)):
        print('=', end='')
        if i == len(outputStr) - 1:
            print('')


def printOutput():
    printEqualSign(outputStr)
    print(outputStr)
    printEqualSign(outputStr)


printOutput()

# querystring = {"jql": "project in (fgl, wcf) and sprint in (\"%s\", \"%s\") and status was not in (\"Under Review\", resolved, closed) on \"%s 04:00\" and status in (\"Under Review\", resolved, closed) order by type" % (sprint1, sprint2, the_first_day)}
querystring = {"jql": "project in (fgl, wcf) and status was not in (\"Under Review\", resolved, closed) on \"%s 04:00\" and status was in (\"Under Review\", resolved, closed) on \"2019/08/01\" order by type" % (the_first_day)}

headers = {'authorization': 'Basic bmVsc29uLndhbmdAcXVlc3QuY29tOlNIRU5NRTM1bWltYQ=='}

response = requests.request("GET", url, headers=headers, params=querystring)

myData = json.loads(response.text)

if myData['total'] == 0:
    print("No issue complete yet.")
else:
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
