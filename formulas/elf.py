def calculate(stats):
    strength, agility, vitality, energy, level = stats

    min_dmg = (strength + agility) / 6
    max_dmg = (strength + agility) / 4
    combo_dmg = (agility + vitality + energy) / 3
    attack_speed = 12 + agility / 120
    defense = agility / 8 + vitality / 10
    pvm_def_rate = agility / 4
    pvm_atk_rate = level * 5 + agility * 1.5 + strength / 4
    pvp_def_rate = level * 2 + agility / 10
    pvp_atk_rate = level * 3 + agility * 2
    ag = strength * 0.3 + agility * 0.2 + vitality * 0.3 + energy * 0.2
    hp = vitality * 2
    mana = energy * 1.5
    buffs_duration = 120  # seconds

    return {
        "Min Physical DMG": min_dmg,
        "Max Physical DMG": max_dmg,
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
        "Buffs Duration (sec)": buffs_duration
    }
