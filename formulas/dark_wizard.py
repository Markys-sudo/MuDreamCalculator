def calculate(stats):
    strength, agility, vitality, energy, level = stats

    min_wiz_dmg = energy / 7 + agility / 24
    max_wiz_dmg = energy / 4 + agility / 16
    combo_dmg = (agility + vitality + energy) / 3
    attack_speed = 8 + agility / 80
    defense = agility / 5
    pvm_def_rate = agility / 3
    pvm_atk_rate = level * 5 + agility * 1.5 + strength / 4
    pvp_def_rate = level * 2 + agility / 4
    pvp_atk_rate = level * 3 + agility * 4
    ag = strength * 0.2 + agility * 0.4 + vitality * 0.3 + energy * 0.2
    hp = vitality * 2
    mana = energy * 2
    soul_barrier_absorb = min(20, 10 + agility / 50 + energy / 200)
    soul_barrier_duration = 120 + energy / 400

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
        "Soul Barrier Absorb %": soul_barrier_absorb,
        "Soul Barrier Duration": soul_barrier_duration
    }
