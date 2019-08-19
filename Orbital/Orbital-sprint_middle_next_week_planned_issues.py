import requests
import json
from pprint import pprint as pp

url = "https://jira.labs.quest.com/rest/api/2/search"

sprint = "2019 Orbital Sprint13"

outputStr = 'Printing next week planned issues'


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

# querystring = {"jql": "project in (fgl, wcf) and sprint = \"%s\" and status was not in (\"Under Review\", resolved, closed) on \"20191212\" order by type" % (sprint)}
querystring = {"jql": "sprint = \"%s\" and status was not in (\"Under Review\", resolved, closed) on \"201900801\" order by type" % (sprint)}

headers = {'authorization': 'Basic bmVsc29uLndhbmdAcXVlc3QuY29tOlNIRU5NRTM1bWltYQ=='}

print("Querying data from JIRA...")

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
