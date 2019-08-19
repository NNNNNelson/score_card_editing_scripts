import requests
import json


def printEqualSign(outputStr):
    for i in range(len(outputStr)):
        print('=', end='')
        if i == len(outputStr) - 1:
            print('')


def printOutput(outputStr):
    printEqualSign(outputStr)
    print(outputStr)
    printEqualSign(outputStr)


url = "https://jira.labs.quest.com/rest/api/2/search?maxResults=100"
headers = {'authorization': 'Basic bmVsc29uLndhbmdAcXVlc3QuY29tOlNIRU5NRTM0bWltYQ=='}

sprint_start_days = ['02/19', '03/05', '03/19', '04/02', '04/16', '04/30', '05/21', '06/04', '06/18', '07/02']
# sprint_end_days = ['03/04', '03/18', '04/01', '04/15', '04/29', '05/20', '06/03', '06/17', '07/01', '07/15']
sprint_end_days_next_day = ['03/05', '03/19', '04/02', '04/16', '04/30', '05/21', '06/04', '06/18', '07/02', '07/16']

for i in range(9, 10):
    # Print total issue count and total issue story points
    printOutput("Sprint " + str(i + 2) + " total issues count:")
    querystring = {"jql": "sprint = \"2019 Orbital Sprint" + str(i + 2) + "\" and status was not resolved on \"2019/" + sprint_start_days[i] + " 06:00\""}
    response = requests.request("GET", url, headers=headers, params=querystring)
    myData = json.loads(response.text)
    print(str(myData["total"]))
    printOutput("Sprint " + str(i + 2) + " total issues story points:")
    story_point_sum = 0
    for x in range(0, myData["total"]):
        # print("Issue " + myData["issues"][x]["key"] + " story point: " + str(myData["issues"][x]["fields"]["customfield_10303"]))
        if myData["issues"][x]["fields"]["customfield_10303"] is not None:
            story_point_sum += myData["issues"][x]["fields"]["customfield_10303"]
    print(str(story_point_sum))
    print(querystring['jql'])

    # Print closed issue count and closed issue story points
    printOutput("Sprint " + str(i + 2) + " closed issues count:")
    querystring = {"jql": "sprint = \"2019 Orbital Sprint" + str(i + 2) + "\" and status was closed on \"2019/" + str(sprint_end_days_next_day[i]) + " 23:59\" and status was not resolved on \"2019/" + sprint_start_days[i] + " 06:00\""}
    response = requests.request("GET", url, headers=headers, params=querystring)
    myData = json.loads(response.text)
    print(str(myData["total"]))
    printOutput("Sprint " + str(i + 2) + " closed issues story points:")
    story_point_sum = 0
    for x in range(0, myData["total"]):
        # print("Issue " + myData["issues"][x]["key"] + " story point: " + str(myData["issues"][x]["fields"]["customfield_10303"]))
        if myData["issues"][x]["fields"]["customfield_10303"] is not None:
            story_point_sum += myData["issues"][x]["fields"]["customfield_10303"]
    print(str(story_point_sum))
    print(querystring['jql'])

    # Print resolved issue count and resolved issue story points
    printOutput("Sprint " + str(i + 2) + " resolved issues count:")
    querystring = {"jql": "sprint = \"2019 Orbital Sprint" + str(i + 2) + "\" and status was resolved on \"2019/" + str(sprint_end_days_next_day[i]) + " 23:59\" and status was not resolved on \"2019/" + sprint_start_days[i] + " 06:00\""}
    response = requests.request("GET", url, headers=headers, params=querystring)
    myData = json.loads(response.text)
    print(str(myData["total"]))
    printOutput("Sprint " + str(i + 2) + " resolved issues story points:")
    story_point_sum = 0
    for x in range(0, myData["total"]):
        # print("Issue " + myData["issues"][x]["key"] + " story point: " + str(myData["issues"][x]["fields"]["customfield_10303"]))
        if myData["issues"][x]["fields"]["customfield_10303"] is not None:
            story_point_sum += myData["issues"][x]["fields"]["customfield_10303"]
    print(str(story_point_sum))
    print(querystring['jql'])

# Below are test code
# i = 9

# printOutput("Sprint " + str(i + 2) + " total issues count:")
# querystring = {"jql": "sprint = \"2019 Orbital Sprint" + str(i + 2) + "\" and status was not resolved on \"2019/" + sprint_start_days[i] + " 06:00\""}
# response = requests.request("GET", url, headers=headers, params=querystring)
# myData = json.loads(response.text)
# # print(myData)
# # print(myData["issues"][0]["fields"]["customfield_10303"])
# print(str(myData["total"]))
# printOutput("Sprint " + str(i + 2) + " total issues story points:")
# story_point_sum = 0
# for x in range(0, myData["total"]):
#     # print('Add issue ' + str(x))
#     # print("Issue " + myData["issues"][x]["key"] + " story point: " + str(myData["issues"][x]["fields"]["customfield_10303"]))
#     if myData["issues"][x]["fields"]["customfield_10303"] is not None:
#         story_point_sum += myData["issues"][x]["fields"]["customfield_10303"]
# print(str(story_point_sum))
