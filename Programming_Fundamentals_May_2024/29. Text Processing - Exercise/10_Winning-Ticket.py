import re
pattern = r"(#{6,}|@{6,}|\${6,}|\^{6,})"
tickets = list(map(lambda s: s.strip(), input().split(",")))
is_valid = True
for ticket in tickets:
    if len(ticket) != 20:
        is_valid = False
        print("invalid ticket")
    else:
        first_half = ticket[0:10]
        second_half = ticket[10:20]
        if re.search(pattern, first_half) and re.search(pattern, second_half):
            first_match = re.findall(pattern, first_half)[0]
            second_match = re.findall(pattern, second_half)[0]
            if len(first_match) == 10 and len(second_match) == 10:
                print(f"ticket \"{ticket}\" - 10{first_match[0]} Jackpot!")
            elif len(first_match) >= 6 and len(second_match) >= 6:
                shortest = min(len(first_match), len(second_match))
                print(f"ticket \"{ticket}\" - {shortest}{first_match[0]}")
            else:
                print(f"ticket \"{ticket}\" - no match")
        else:
            print(f"ticket \"{ticket}\" - no match")
