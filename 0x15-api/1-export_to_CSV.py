#!/usr/bin/python3
"""Exports data to CSV"""
from requests import get
from sys import argv
from csv import QUOTE_ALL, writer


empo_url = "https://jsonplaceholder.typicode.com/users/"
tasks_url = "https://jsonplaceholder.typicode.com/todos/"


def data():
    """Parses data form API"""
    if not len(argv):
        return print("Invalid")
    empo_id = argv[1]
    empo = get(empo_url + empo_id).json()
    tasks = get(tasks_url).json()
    with open(empo_id + ".csv", "w") as file:
        Task_writer = writer(file, delimiter=',', quotechar='"',
                             quoting=QUOTE_ALL)
        for i in tasks:
            if i["userId"] == empo.get("id"):
                del i["id"]
                Task_writer.writerow(
                    [empo_id, empo["username"], i["completed"], i["title"]])


if __name__ == "__main__":
    data()
