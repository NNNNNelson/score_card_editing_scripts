import datetime
import requests
import json


url = "https://jira.labs.quest.com/rest/api/2/search"

query_target_day_str = "2019/08/01"

outputStr = 'Printing scorecard day issue count status'


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

headers = {'authorization': '*****'}

# Query unresolved issue count
print("Querying " + query_target_day_str + " Unresolved issue count...")
querystring = {"jql": "project in (fgl, wcf) and fixversion = ace.5 and status was not in (resolved, closed) on \"%s 23:59\" order by type" % (query_target_day_str)}
response = requests.request("GET", url, headers=headers, params=querystring)
myData = json.loads(response.text)
unresolved_issue_count = str(myData["total"])
print(query_target_day_str + " Unresolved issue count is: " + unresolved_issue_count)

# Query resolved issue count
print("Querying " + query_target_day_str + " Resolved issue count...")
querystring = {"jql": "project in (fgl, wcf) and fixversion = ace.5 and status was resolved on \"%s 23:59\" order by type" % (query_target_day_str)}
response = requests.request("GET", url, headers=headers, params=querystring)
myData = json.loads(response.text)
resolved_issue_count = str(myData["total"])
print(query_target_day_str + " Resolved issue count is: " + resolved_issue_count)

# Query closed issue count
print("Querying " + query_target_day_str + " Closed issue count...")
querystring = {"jql": "project in (fgl, wcf) and fixversion = ace.5 and status was closed on \"%s 23:59\" order by type" % (query_target_day_str)}
response = requests.request("GET", url, headers=headers, params=querystring)
myData = json.loads(response.text)
closed_issue_count = str(myData["total"])
print(query_target_day_str + " Closed issue count is: " + closed_issue_count)
