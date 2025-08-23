#!/bin/python3

import math
import os
import sys
import requests  # HackerRank runtime has requests available, so we use it

def getAverageTemperatureForUser(userId):
    url = "https://jsonmock.hackerrank.com/api/medical_records"
    page = 1
    temps = []

    while True:
        response = requests.get(f"{url}?userId={userId}&page={page}").json()

        data = response.get("data", [])
        for record in data:
            temps.append(record["vitals"]["bodyTemperature"])

        # stop after last page
        if page >= response.get("total_pages", 0):
            break
        page += 1

    if not temps:
        return "0"

    avg_temp = sum(temps) / len(temps)
    return f"{avg_temp:.1f}"


if _name_ == '_main_':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    userId = int(input().strip())
    result = getAverageTemperatureForUser(userId)

    fptr.write(result + '\n')
    fptr.close()