def draw_cards(*tuples, **kvps):
    cards = {}

    for name, type in tuples:
        if type not in cards:
            cards[type] = []
        cards[type].append(name)

    for name, type in kvps.items():
        if type not in cards:
            cards[type] = []
        cards[type].append(name)
    sorted_monster = []
    sorted_spell = []

    if "monster" in cards:
        sorted_monster = sorted(cards["monster"], reverse=True)
    if "spell" in cards:
        sorted_spell = sorted(cards["spell"])

    result = ""
    if sorted_monster:
        result += "Monster cards:\n"
        for c in sorted_monster:
            result += f"  ***{c}\n"

    if sorted_spell:
        result += "Spell cards:\n"
        for c in sorted_spell:
            result += f"  $$${c}\n"
    return result


print(draw_cards(("cyber dragon", "monster"), freeze="spell", ))
print(draw_cards(("celtic guardian", "monster"), ("earthquake", "spell"), ("fireball", "spell"), raigeki="spell",
                 destroy="spell", ))
print(draw_cards(("brave attack", "spell"), ("freeze", "spell"), lightning_bolt="spell", fireball="spell", ))
