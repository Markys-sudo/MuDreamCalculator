def calculate(stats):
    # Розпаковуємо 6 параметрів, останній — Command
    strength, agility, vitality, energy, level, command = stats

    min_phys_dmg = strength / 7 + energy / 14
    max_phys_dmg = strength / 5 + energy / 10
    combo_dmg = (strength + agility + vitality) / 3
    attack_speed = 9 + agility / 90
    defense = agility / 6
    pvm_def_rate = agility / 7
    pvm_atk_rate = level * 5 + agility * 3 + strength / 4 + command / 10
    pvp_def_rate = level * 2 + agility / 2
    pvp_atk_rate = level * 3 + agility * 4
    ag = strength * 0.3 + agility * 0.2 + vitality * 0.1 + energy * 0.15 + command * 0.3
    hp = vitality * 2
    mana = energy * 1.5
    skill_damage_percent = min(500, 200 + energy / 25)

    return {
        "Min Physical DMG": min_phys_dmg,
        "Max Physical DMG": max_phys_dmg,
        "Combo DMG": combo_dmg,
        "Attack Speed": attack_speed,
        "Defense": defense,
        "PvM Defense Rate": pvm_def_rate,
        "PvM Attack Rate": pvm_atk_rate,
        "PvP Defense Rate": pvp_def_rate,
        "PvP Attack Rate": pvp_atk_rate,
        "AG": ag,
        "HP": hp,
        "Mana": mana,
        "Skill Damage %": skill_damage_percent,
    }
