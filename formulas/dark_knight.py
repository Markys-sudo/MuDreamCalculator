def calculate(stats):
    strength, agility, vitality, energy, level = stats

    min_dmg = strength / 6 + energy / 18
    max_dmg = strength / 4 + energy / 12
    combo_dmg = (strength + agility + vitality) / 4
    attack_speed = 6 + agility / 60
    defense = agility / 4
    pvm_def_rate = agility / 3
    pvm_atk_rate = level * 5 + agility * 1.5 + strength / 4
    pvp_def_rate = level * 2 + agility / 2
    pvp_atk_rate = level * 3 + agility * 4.5
    ag = strength * 0.15 + agility * 0.2 + vitality * 0.3 + energy
    hp = vitality * 3
    mana = energy * 1
    skill_percent = min(500, 200 + energy / 10)
    swell_life_percent = min(130, 12 + vitality / 100 + energy / 20)
    swell_life_time = 300 + energy / 300
    death_stab_multi = 2
    twisting_slash_range = 3

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
        "Skill %": skill_percent,
        "Swell Life %": swell_life_percent,
        "Swell Life Time": swell_life_time,
        "Death Stab Multi": death_stab_multi,
        "Twisting Slash Range": twisting_slash_range
    }
