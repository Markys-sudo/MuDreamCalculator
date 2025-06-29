def calculate(stats):
    strength, agility, vitality, energy, level = stats

    min_wiz_dmg = energy / 9 + agility / 12 + strength / 24
    max_wiz_dmg = energy / 4 + agility / 12 + strength / 12
    combo_dmg = (agility + vitality + energy) / 3
    attack_speed = 7 + agility / 70
    defense = agility / 3
    pvm_def_rate = agility / 4
    pvm_atk_rate = level * 5 + agility * 1.5 + strength / 4
    pvp_def_rate = level * 2 + agility / 2
    pvp_atk_rate = level * 3 + agility * 3.5
    ag = strength * 0.2 + agility * 0.25 + vitality * 0.3 + energy * 0.15
    hp = vitality * 2
    mana = energy * 1.5
    berserker_buff = min(100, energy / 50)
    reflection_buff = min(100, 30 + energy / 150)
    weakness_debuff = 30
    innovation_debuff = 30
    max_chance_weakness = 70
    max_chance_innovation = 70
    chain_lightning_multi_attack = 3

    return {
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
        "Berserker Buff %": berserker_buff,
        "Reflection Buff %": reflection_buff,
        "Weakness Debuff %": weakness_debuff,
        "Innovation Debuff %": innovation_debuff,
        "Max Chance Weakness %": max_chance_weakness,
        "Max Chance Innovation %": max_chance_innovation,
        "Chain Lightning Multi Attack": chain_lightning_multi_attack,
    }
