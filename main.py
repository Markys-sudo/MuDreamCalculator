import tkinter as tk
from tkinter import ttk
from formula import CLASS_FORMULAS

STAT_LIMIT = 32767
LEVEL_LIMIT = 400

def validate_field(entry, value, max_value, label):
    try:
        if value.strip() == "":
            entry.config(background="#ffcccc")
            return False, f"❌ Поле '{label}' порожнє"
        int_val = int(value)
        if 0 <= int_val <= max_value:
            entry.config(background="white")
            return True, ""
        else:
            entry.config(background="#ffcccc")
            return False, f"❌ {label} не може бути більше {max_value}"
    except ValueError:
        entry.config(background="#ffcccc")
        return False, f"❌ {label} має бути числом"

def calculate(*args):
    selected_class = class_var.get()
    if selected_class not in CLASS_FORMULAS:
        result.set("❌ Обери клас зі списку")
        return

    needs_command = (selected_class == "Dark Lord")

    fields = [
        ("Strength", entry_strength, STAT_LIMIT),
        ("Agility", entry_agility, STAT_LIMIT),
        ("Vitality", entry_vitality, STAT_LIMIT),
        ("Energy", entry_energy, STAT_LIMIT),
        ("Level", entry_level, LEVEL_LIMIT)
    ]

    if needs_command:
        fields.append(("Command", entry_command, STAT_LIMIT))

    stats = []
    errors = []

    for label, entry, limit in fields:
        value = entry.get()
        valid, message = validate_field(entry, value, limit, label)
        if not valid:
            errors.append(message)
        else:
            stats.append(int(value))

    if errors:
        result.set("\n".join(errors))
        return

    results = CLASS_FORMULAS[selected_class](tuple(stats))
    result_text = f"📊 {selected_class}:\n"
    for key, value in results.items():
        result_text += f"{key}: {value:.1f}\n"
    # Розрахунок
    results = CLASS_FORMULAS[selected_class](tuple(stats))

    total_stats = sum(stats[:-1]) if needs_command else sum(stats)  # не включати Level в підсумок

    result_text = f"📊 {selected_class}:\n"
    for key, value in results.items():
        result_text += f"{key}: {value:.1f}\n"

    result_text += f"\n🔢 Total Stats Used: {total_stats}"

    result.set(result_text)

def on_class_change(event):
    selected_class = class_var.get()
    if selected_class == "Dark Lord":
        label_command.grid()
        entry_command.grid()
    else:
        label_command.grid_remove()
        entry_command.grid_remove()
    calculate()

root = tk.Tk()
root.title("MU Online Build Calculator")

mainframe = ttk.Frame(root, padding="10")
mainframe.grid(row=0, column=0)

ttk.Label(mainframe, text="Class:").grid(column=0, row=0, sticky=tk.W)
class_var = ttk.Combobox(mainframe, values=list(CLASS_FORMULAS.keys()))
class_var.grid(column=1, row=0, sticky=(tk.W, tk.E))
class_var.bind("<<ComboboxSelected>>", on_class_change)

labels = ["Level", "Strength", "Agility", "Vitality", "Energy"]
entries = {}

for i, label in enumerate(labels, start=1):
    ttk.Label(mainframe, text=label + ":").grid(column=0, row=i, sticky=tk.W)
    entry = ttk.Entry(mainframe, width=10)
    entry.grid(column=1, row=i, sticky=(tk.W, tk.E))
    entry.insert(0, "25")  # <-- Вставляємо 50 за замовчуванням тут
    entries[label.lower()] = entry
    entry.bind("<KeyRelease>", calculate)

entry_level = entries["level"]
entry_strength = entries["strength"]
entry_agility = entries["agility"]
entry_vitality = entries["vitality"]
entry_energy = entries["energy"]

label_command = ttk.Label(mainframe, text="Command:")
entry_command = ttk.Entry(mainframe, width=10)
label_command.grid(column=0, row=6, sticky=tk.W)
entry_command.grid(column=1, row=6, sticky=(tk.W, tk.E))
entry_command.insert(0, "25")  # <-- 50 за замовчуванням для Command
entry_command.bind("<KeyRelease>", calculate)

label_command.grid_remove()
entry_command.grid_remove()

result = tk.StringVar()
ttk.Label(mainframe, textvariable=result, justify="left", padding=10, foreground="black").grid(
    column=2, row=0, rowspan=8, sticky=(tk.N)
)

# Додатково можна викликати calculate() щоб показати результат одразу з 50 в полях
calculate()

root.mainloop()
