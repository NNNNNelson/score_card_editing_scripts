import datetime
import requests
import json


url = "https://jira.labs.quest.com/rest/api/2/search"

start_day_str = "2019/07/26"
end_day_str = "2019/08/01"
# sprint = "2019 ACE.5 Sprint6"

start_day_date = datetime.datetime.strptime(start_day_str, "%Y/%m/%d")
end_day_date = datetime.datetime.strptime(end_day_str, "%Y/%m/%d")

outputStr = 'Printing the not fixed issue count for each of last 7 days'


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


while start_day_date <= end_day_date:
    start_day_date_to_str = datetime.datetime.strftime(start_day_date, "%Y/%m/%d")
    print("%s:" % start_day_date_to_str)

    # querystring = {"jql": "project in (fgl, wcf) and sprint = \"%s\" and status was not in (\"Under Review\", resolved, closed) on \"%s 23:59\" order by type" % (sprint, start_day_date_to_str)}
    querystring = {"jql": "project in (fgl, wcf) and fixversion = ace.5 and status was not in (\"Under Review\", resolved, closed) on \"%s 23:59\" order by type" % (start_day_date_to_str)}

    headers = {'authorization': 'Basic bmVsc29uLndhbmdAcXVlc3QuY29tOlNIRU5NRTM1bWltYQ=='}

    response = requests.request("GET", url, headers=headers, params=querystring)

    myData = json.loads(response.text)

    print("Total issues amount: " + str(myData["total"]))

    start_day_date = start_day_date + datetime.timedelta(days=1)
