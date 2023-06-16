import tkinter as tk
from tkinter import ttk

comb_entry = {}


def _current_combo(event):
    return combo.get()


def on_focus_out(event):
    value = event.widget.get()
    label_text = event.widget.label_text
    print(label_text)
    comb_entry.setdefault(_current_combo(event), []).append([label_text, value])



def on_combobox_select(event):
    cont = 0
    if combo.get() in comb_entry.keys():
        for entry in label_entries.values():
            print(entry)
            entry.delete(0, tk.END)
            entry.insert(0, str(comb_entry[combo.get()][cont][1]))
            cont += 1
    else:
        for entry in label_entries.values():
            entry.delete(0, tk.END)
            entry.insert(0, "")


root = tk.Tk()

labels = ['Label 1', 'Label 2', 'Label 3', 'Label 4', 'Label 5']

label_entries = {}
for label_text in labels:
    label = ttk.Label(root, text=label_text)
    label.pack()

    entry = ttk.Entry(root)
    entry.pack()
    entry.bind("<FocusOut>", on_focus_out)
    entry.label_text = label_text
    label_entries[label_text] = entry
    print(label_entries)

combo = ttk.Combobox(root, values=('QUOTATION 1', 'QUOTATION 2', 'QUOTATION 3',
                                   'QUOTATION 4', 'QUOTATION 5', 'QUOTATION 6',
                                   'QUOTATION 7', 'QUOTATION 8', 'QUOTATION 9',
                                   'QUOTATION 10', 'QUOTATION 11', 'QUOTATION 12',
                                   'QUOTATION 13', 'QUOTATION 14', 'QUOTATION 15',
                                   'QUOTATION 16', 'QUOTATION 17', 'QUOTATION 18',))
combo.pack()
combo.bind("<<ComboboxSelected>>", on_combobox_select)

root.mainloop()
