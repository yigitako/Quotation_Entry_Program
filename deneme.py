import time
import tkinter as tk
from tkinter import ttk
import re

erp_codes = {
    "PRF": ["Steel Profiles (Beams / Columns / Piles)", None],  # DONE
    "PLT": ["Steel Plates (CS / AS)", None],
    "HSS": ["Hollow Structural Sections", None],
    "PCSW": ["PC Stands and Wires", None],
    "NGL": ["Angles (Equal and Unequal)", None],
    "CFC": ["Steel Sheets Cut From Coils (CS / AS / SS)", None],
    "CHS": ["Tubular Products (API / EN / DIN)", None],
    "SWP": ["SAW Pipes", None],
    "SMP": ["Seamless Heavy Wall Tubes", None],
    "FTG": ["Pipe Fittings", None],
    "VLV": ["Valves", None],
    "BNN": ["Bolts and Nuts", None],
    "SWR": ["Steel Wires / Ropes", None],
    "ALP": ["Aluminum Products", None],
    "CNA": ["Chemicals and Additives", None],
    "CPS": ["Consumables for Steel (Zinc / Electrodes / Steel Shots)", None],
    "UGR": ["UPS, Generator, Regulators", None],
    "GICS": ["Galvanized Steel Coils and Sheets", None],
    "PTRN": ["Expanded Sheets / Tear and Chequered", None],
    "RWA": ["Rails and Accessories", None],
    "GTS": ["Geotechnical Systems", None],
    "PPS": ["Post and Pretensioning Systems", None],
    "FBM": ["Bars (Flat, Square, Hexagonal, Round, Rectangular) Mill", None],
    "DRB": ["Deformed Reinforcing Bars", None],
    "PMP": ["Pumps (Injection)", None],
    "SSPS": ["Stainless Steel Plates / Sheets", None],
    "CLP": ["Cladded Plates", None],
    "HLE": ["Heavy Lifting Equipment", None],
    "MSC": ["Miscellaneous - Not Listed", None]
}


class ModernEntry:
    def __init__(self):
        self.win = tk.Tk()
        self.win.tk.call('source',
                         r'C:\Users\yigit\PycharmProjects\Sepkon_enter_data\tkBreeze-master/breeze/breeze.tcl')
        s = ttk.Style()
        s.theme_use('breeze')
        self.win.geometry("700x350")

        self.entry_1 = ttk.Entry(self.win)
        self.entry_1.bind("<FocusIn>", self.schedule_menu_popup)
        self.entry_1.pack()

        self.popup_menu_id = None

        self.win.mainloop()

    def schedule_menu_popup(self, event):
        if self.popup_menu_id is not None:
            self.win.after_cancel(self.popup_menu_id)  # Cancel previous scheduled popup menu
        self.popup_menu_id = self.win.after(200, self.menu_popup)  # Schedule new popup menu after 200 milliseconds

    def menu_popup(self):
        x = self.entry_1.winfo_rootx()
        y = self.entry_1.winfo_rooty() + self.entry_1.winfo_height()

        # Create a menu widget for the popup menu
        popup_menu = tk.Menu(self.win, tearoff=0)

        command_labels = []

        for code, description in erp_codes.items():
            label = f"{code}"
            popup_menu.add_command(label=label)
            command_labels.append(label)

        # Print the command labels
        value = self.entry_1.get()
        if value == '':
            pass
        else:
            regex = fr'^{value}'
            data = [string for string in command_labels if not re.match(regex, string)]
            for cf in data:
                pass

        # Display the popup menu at the desired location
        self.entry_1.focus()
        popup_menu.post(x, y)


import tkinter as tk
from tkinter import ttk

#def open_dropdown(event):
#    combobox.after(1, lambda: combobox.event_generate('<Down>'))
#    combobox.after(10, lambda: combobox.event_generate("<Entry>"))

root = tk.Tk()

combobox = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"])
combobox.state(['focus'])
combobox.pack()
combobox.bind("<KeyPress>")

root.mainloop()
