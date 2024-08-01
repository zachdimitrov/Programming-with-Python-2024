class Hero:

    def __init__(self, name, hit, mana):
        self.name = name
        self.hit = hit
        self.mana = mana
        self.alive = True

    def cast_spell(self, mana_needed, spell_name):
        if self.mana >= mana_needed:
            self.mana -= mana_needed
            print(f"{self.name} has successfully cast {spell_name} and now has {self.mana} MP!")
        else:
            print(f"{self.name} does not have enough MP to cast {spell_name}!")

    def take_damage(self, damage, attacker):
        if self.hit > damage:
            self.hit -= damage
            print(f"{self.name} was hit for {damage} HP by {attacker} and now has {self.hit} HP left!")
        else:
            print(f"{self.name} has been killed by {attacker}!")
            self.alive = False

    def recharge(self, amount):
        old_mana = self.mana
        if self.mana + amount > 200:
            self.mana = 200
        else:
            self.mana += amount
        print(f"{self.name} recharged for {self.mana - old_mana} MP!")

    def heal(self, amount):
        old_hit = self.hit
        if self.hit + amount > 100:
            self.hit = 100
        else:
            self.hit += amount
        print(f"{self.name} healed for {self.hit - old_hit} HP!")

    def __repr__(self):
        print(self.name)
        print(f"  HP: {self.hit}")
        print(f"  MP: {self.mana}")


def find_hero(nm):
    for h in heroes:
        if h.name == nm:
            return h


n = int(input())
heroes = []
for i in range(n):
    new_hero = input().split(" ")
    heroes.append(Hero(new_hero[0], int(new_hero[1]), int(new_hero[2])))

command = input()
while command != "End":
    line = command.split(" - ")
    name = line[1]
    hero = find_hero(name)
    if line[0] == "CastSpell":
        mana_need = int(line[2])
        spell = line[3]
        hero.cast_spell(mana_need, spell)
    elif line[0] == "TakeDamage":
        damage = int(line[2])
        attacker = line[3]
        hero.take_damage(damage, attacker)
        if not hero.alive:
            heroes.remove(hero)
    elif line[0] == "Recharge":
        amount = int(line[2])
        hero.recharge(amount)
    elif line[0] == "Heal":
        amount = int(line[2])
        hero.heal(amount)

    command = input()

for hero in heroes:
    hero.__repr__()
