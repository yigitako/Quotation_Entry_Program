import tkinter as tk
from tkinter import ttk

def change_tab_color(tab_id, color):
    style = ttk.Style()
    style.configure("CustomTab.TNotebook.Tab",
                    background=[(f"!selected", color)],
                    foreground=[(f"!selected", "white")])

# Create the main window
window = tk.Tk()

# Create a Notebook widget
notebook = ttk.Notebook(window, style="CustomTab.TNotebook")

# Create tabs in the Notebook
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")

# Change the color of Tab 2 to red
change_tab_color(1, "red")

notebook.pack()

# Run the main window event loop
window.mainloop()
