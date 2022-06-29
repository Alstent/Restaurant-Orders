# dava pra fazer com class, mas eu nao tinha muito tempo...
def create_database(data):
    database = {}
    all_foods = set()
    all_days = set()
    for list in data:
        person = list[0]
        all_foods.add(list[1])
        all_days.add(list[2])
        if person in database:
            database[person]["ordered_food"].add(list[1])
            database[person]["days"].add(list[2])
            if list[1] in database[person]["quantities"]:
                database[person]["quantities"][list[1]] += 1
            else:
                database[person]["quantities"][list[1]] = 1
        else:
            database[person] = {
                "ordered_food": {list[1]},
                "days": {list[2]},
                "quantities": {
                    list[1]: 1,
                },
            }
    for person in database:
        # minha criatividade com nomes é incrivel...
        # tb tive q fazer esse projeto correndo
        database[person]["days_left"] = set(
            [day for day in all_days if day not in database[person]["days"]]
        )
        database[person]["foods_left"] = set(
            [food for food in all_foods
                if food not in database[person]["ordered_food"]]
        )
    return database
