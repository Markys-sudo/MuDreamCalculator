def calculate(stats):
    strength, agility, vitality, energy, level = stats

    min_phys_dmg = strength / 6 + energy / 12 + vitality / 14
    max_phys_dmg = strength / 4 + energy / 6 + vitality / 7
    min_wiz_dmg = energy / 7 + agility / 25 + vitality / 14
    max_wiz_dmg = energy / 4 + agility / 20 + vitality / 7
    combo_dmg = (strength + agility + vitality) / 3
    attack_speed = 6 + agility / 65
    defense = agility / 4 + vitality / 8
    pvm_def_rate = agility / 3
    pvm_atk_rate = level * 5 + agility * 1.5 + strength / 4
    pvp_def_rate = level * 2 + agility / 4
    pvp_atk_rate = level * 3 + agility * 3.5
    ag = strength * 0.2 + agility * 0.25 + vitality * 0.3 + energy * 0.15
    hp = vitality * 2
    mana = energy * 2
    swell_life_buff = min(80, 12 + vitality / 100 + energy / 20)
    twisting_slash_range = 3

    return {
        "Min Physical DMG": min_phys_dmg,
        "Max Physical DMG": max_phys_dmg,
        "Min Wizardry DMG": min_wiz_dmg,
        "Max Wizardry DMG": max_wiz_dmg,
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
        "Swell Life Buff %": swell_life_buff,
        "Twisting Slash Range": twisting_slash_range
    }
