def calculate(stats):
    strength, agility, vitality, energy, level = stats

    min_phys_dmg = strength / 7 + vitality / 15
    max_phys_dmg = strength / 5 + vitality / 12
    combo_dmg = (strength + agility + vitality) / 3
    attack_speed = 6 + agility / 50
    defense = agility / 5 + vitality / 12
    pvm_def_rate = agility / 10
    pvm_atk_rate = level * 3 + agility * 1.25 + strength / 6
    pvp_def_rate = level * 1.5 + agility / 5
    pvp_atk_rate = level * 2.6 + agility * 3.6
    ag = strength * 0.15 + agility * 0.2 + vitality * 0.3 + energy
    hp = vitality * 2
    mana = energy * 1.3
    melee_damage_percent = min(500, 50 + strength / 15)
    divine_damage_percent = min(500, 200 + energy / 15)
    skill_damage_percent = min(500, 200 + agility / 20 + energy / 15)
    killing_blow_multi = 3
    beast_uppercut_multi = 3
    chain_drive_multi = 3

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
        "Melee Damage %": melee_damage_percent,
        "Divine Damage %": divine_damage_percent,
        "Skill Damage %": skill_damage_percent,
        "Killing Blow Multi-attack": killing_blow_multi,
        "Beast Uppercut Multi-attack": beast_uppercut_multi,
        "Chain Drive Multi-attack": chain_drive_multi
    }
