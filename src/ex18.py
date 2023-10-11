"""
Exercise 18 : Buy 8 get 1 free
"""


def get_cost_of_coffee(qty, amt):
    #logic is 8 free 1
    if qty > 8:
        free = qty // 8
    else:
        free = 0
    cost = (qty - free) * amt
    return cost

def get_cost_of_coffee_2(qty, amt):
    #logic is 8 free 1
    if qty > 8:
        free = qty // 8
    else:
        free = 0
    cost = (qty - free) * amt
    return cost