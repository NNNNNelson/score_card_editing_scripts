import datetime
import requests
import json


url = "https://jira.labs.quest.com/rest/api/2/search"

target_date = "2019/08/01"
sprint = "2019 Orbital Sprint13"

outputStr = 'Printing scorecard day issue status'


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

print("Querying Unresolved issue count...")
headers = {'authorization': '*****'}
querystring = {"jql": "sprint = \"%s\" and status was not in (resolved, closed) on \"%s 23:59\" " % (sprint, target_date)}
response = requests.request("GET", url, headers=headers, params=querystring)
myData = json.loads(response.text)
unresolvedCount = myData["total"]
print("Unresolved issue count is: " + str(unresolvedCount))

print("Querying Resolved issue count...")
headers = {'authorization': '*****'}
querystring = {"jql": "sprint = \"%s\" and status was resolved on \"%s 23:59\" " % (sprint, target_date)}
response = requests.request("GET", url, headers=headers, params=querystring)
myData = json.loads(response.text)
resolvedCount = myData["total"]
print("Resolved issue count is: " + str(resolvedCount))

print("Querying Closed issue count...")
headers = {'authorization': '*****'}
querystring = {"jql": "sprint = \"%s\" and status was closed on \"%s 23:59\" " % (sprint, target_date)}
response = requests.request("GET", url, headers=headers, params=querystring)
myData = json.loads(response.text)
closedCount = myData["total"]
print("Closed issue count is: " + str(closedCount))
