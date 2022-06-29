import csv
from .create_database import create_database


def analyze_log(path_to_file):
    with open(path_to_file) as file:
        data = list(csv.reader(file))
        database = create_database(data)

        answer1 = max(
            [(quantity, food) for food, quantity
                in database["maria"]["quantities"].items()]
        )[1]
        answer2 = database["arnaldo"]["quantities"]["hamburguer"]
        answer3 = database["joao"]["foods_left"]
        answer4 = database["joao"]["days_left"]

        with open("data/mkt_campaign.txt", "w") as file:
            file.write(f"{answer1}\n{answer2}\n{answer3}\n{answer4}\n")
