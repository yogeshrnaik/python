import unittest


def ingredients(order):
    order_ingredients = {
        'Classic': ['strawberry', 'banana', 'pineapple', 'mango', 'peach', 'honey', 'ice', 'yogurt'],
        'Forest Berry': ['strawberry', 'raspberry', 'blueberry', 'honey', 'ice', 'yogurt'],
        'Freezie': ['blackberry', 'blueberry', 'black currant', 'grape juice', 'frozen yogurt'],
        'Greenie': ['green apple', 'kiwi', 'lime', 'avocado', 'spinach', 'ice', 'apple juice'],
        'Vegan Delite': ['strawberry', 'passion fruit', 'pineapple', 'mango', 'peach', 'ice', 'soy milk'],
        'Just Desserts': ['banana', 'ice cream', 'chocolate', 'peanut', 'cherry'],
    }
    order_details = order.split(',')
    order_name = order_details[0]
    ingredients_to_omit = [omit[1:] for omit in order_details if omit != order_name]
    return ','.join(sorted([i for i in order_ingredients[order_name] if i not in ingredients_to_omit]))


# Note: the class must be called Test
class Test(unittest.TestCase):
    def test_classic_smoothie(self):
        self.assertEqual(ingredients("Classic"), "banana,honey,ice,mango,peach,pineapple,strawberry,yogurt")

    def test_without_strawberry(self):
        self.assertEqual(ingredients("Classic,-strawberry"), "banana,honey,ice,mango,peach,pineapple,yogurt")

    def test_just_desserts(self):
        self.assertEqual(ingredients("Just Desserts"), "banana,cherry,chocolate,ice cream,peanut")

    def test_without_ice_cream_and_peanut(self):
        self.assertEqual(ingredients("Just Desserts,-ice cream,-peanut"), "banana,cherry,chocolate")
