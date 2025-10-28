def declare_winner(fighter1, fighter2, first_attacker):
    attacker, defender = (
        (fighter1, fighter2)
        if fighter1.name == first_attacker
        else (fighter2, fighter1)
    )
    defender.health -= attacker.damage_per_attack
    if defender.health <= 0:
        return attacker.name
    return declare_winner(attacker, defender, defender.name)