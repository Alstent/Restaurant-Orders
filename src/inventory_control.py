class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self.inventory = {
            'pao': 0,
            'carne': 0,
            'queijo': 0,
            'molho': 0,
            'presunto': 0,
            'massa': 0,
            'frango': 0,
        }

    def add_new_order(self, costumer, order, day):
        for ing in self.INGREDIENTS[order]:
            if self.inventory[ing] < self.MINIMUM_INVENTORY[ing]:
                self.inventory[ing] += 1
            else:
                return False

    def get_quantities_to_buy(self):
        return self.inventory

    def get_available_dishes(self):
        available_dishes = set()
        for food in self.INGREDIENTS:
            check = False
            for ing in self.INGREDIENTS[food]:
                if self.inventory[ing] < self.MINIMUM_INVENTORY[ing]:
                    check = True
                else:
                    check = False
                    break
            if check:
                available_dishes.add(food)
        return available_dishes
