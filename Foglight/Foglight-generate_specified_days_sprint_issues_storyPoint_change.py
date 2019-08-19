import datetime
import requests
import json


url = "https://jira.labs.quest.com/rest/api/2/search"

start_day_str = "2019/02/22"
end_day_str = "2019/02/26"
sprint = "2019 ACE.5 Sprint6"

start_day_date = datetime.datetime.strptime(start_day_str, "%Y/%m/%d")
end_day_date = datetime.datetime.strptime(end_day_str, "%Y/%m/%d")

while start_day_date <= end_day_date:
    start_day_date_to_str = datetime.datetime.strftime(start_day_date, "%Y/%m/%d")
    print("----------------------------------\nStory point for %s:" % start_day_date_to_str)

    querystring = {"jql": "project in (fgl, wcf) and sprint = \"%s\" and status was not in (\"Under Review\", resolved, closed) on \"%s 23:59\" order by type" % (sprint, start_day_date_to_str)}

    headers = {'authorization': '*****'}

    response = requests.request("GET", url, headers=headers, params=querystring)

    myData = json.loads(response.text)

    print("Total issues amount: " + str(myData["total"]))

    story_point_sum = 0

    for x in range(0, myData["total"]):
        # print("Issue " + myData["issues"][x]["key"] + " story point: " + str(myData["issues"][x]["fields"]["customfield_10303"]))
        if myData["issues"][x]["fields"]["customfield_10303"] is not None:
            story_point_sum += myData["issues"][x]["fields"]["customfield_10303"]

    print("Total story point is: " + str(story_point_sum))

    start_day_date = start_day_date + datetime.timedelta(days=1)
