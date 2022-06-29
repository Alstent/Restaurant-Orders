class TrackOrders:
    def __init__(self):
        self.orders = {}
        self.all_foods = set()
        self.all_days = set()
        self.day_count = {}

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.all_foods.add(order)
        self.all_days.add(day)

        if day in self.day_count:
            self.day_count[day] += 1
        else:
            self.day_count[day] = 1

        if costumer in self.orders:
            self.orders[costumer]["ordered_food"].add(order)
            self.orders[costumer]["days"].add(day)
            if order in self.orders[costumer]["food_count"]:
                self.orders[costumer]["food_count"][order] += 1
            else:
                self.orders[costumer]["food_count"][order] = 1
        else:
            self.orders[costumer] = {
                "ordered_food": {order},
                "days": {day},
                "food_count": {
                    order: 1,
                },
                "day_count": {
                    day: 1,
                },
            }

    def get_most_ordered_dish_per_costumer(self, costumer):
        return max(
            [(quantity, food) for food, quantity
                in self.orders[costumer]["food_count"].items()]
        )[1]

    def get_never_ordered_per_costumer(self, costumer):
        return set(
            [food for food in self.all_foods
                if food not in self.orders[costumer]["ordered_food"]]
        )

    def get_days_never_visited_per_costumer(self, costumer):
        return set(
            [day for day in self.all_days
                if day not in self.orders[costumer]["days"]]
        )

    def get_busiest_day(self):
        return max(
            [(quantity, day) for day, quantity in self.day_count.items()]
        )[1]

    def get_least_busy_day(self):
        return min(
            [(quantity, day) for day, quantity in self.day_count.items()]
        )[1]
