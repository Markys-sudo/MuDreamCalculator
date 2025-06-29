from formulas.dark_knight import calculate as calc_dark_knight
from formulas.dark_wizard import calculate as calc_dark_wizard
from formulas.elf import calculate as calc_elf
from formulas.summoner import calculate as calc_summoner
from formulas.magic_gladiator import calculate as calc_magic_gladiator
from formulas.dark_lord import calculate as calc_dark_lord
from formulas.rage_fighter import calculate as calc_rage_fighter

CLASS_FORMULAS = {
    "Dark Knight": calc_dark_knight,
    "Dark Wizard": calc_dark_wizard,
    "Elf": calc_elf,
    "Summoner": calc_summoner,
    "Magic Gladiator": calc_magic_gladiator,
    "Dark Lord": calc_dark_lord,
    "Rage Fighter": calc_rage_fighter,
}
