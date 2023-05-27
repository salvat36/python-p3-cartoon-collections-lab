def roll_call_dwarves(dwarves):
    for number, dwarf in enumerate(dwarves):
        print(f"{number + 1}. {dwarf}")

def summon_captain_planet(planeteer_calls):
    calls = [element.title() + "!" for element in planeteer_calls]
    return calls

def long_planeteer_calls(items):
    for item in items: 
        if len(item) > 4:
            return True
    else:
        return False

def find_the_cheese(items):
    for item in items:
        if item == "cheddar" or item == "gouda" or item == "camembert":
            return item
