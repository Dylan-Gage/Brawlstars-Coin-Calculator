from constants import lvl_costs

def calc_lvl_coins(lower, upper):
    if lower < upper:
        return sum(lvl_costs[lower-1 : upper-1])
    return 0

def calc_total_coins(level_lower, level_upper, gadget_count, gear_count, starpower_count, hypercharge_count):
    gadget_coins = gadget_count * 1000
    gear_coins = gear_count * 1000
    starpower_coins = starpower_count * 2000
    hypercharge_coins = hypercharge_count * 5000

    return hypercharge_coins + starpower_coins + gear_coins + gadget_coins + calc_lvl_coins(level_lower, level_upper)

