import tkinter as tk


def save_data():
    # Retrieve data from the entry boxes and save it
    data = []
    for row in range(1, 21):  # Iterate over rows 1 to 20
        row_data = []
        for col in range(7):  # Iterate over 7 columns
            entry = entry_boxes[row][col]
            row_data.append(entry.get())
        data.append(row_data)

    # Print the data (you can save it to a file or perform other operations)
    for row_data in data:
        print(row_data)


root = tk.Tk()

# Create labels for each entry box
label1 = tk.Label(root, text="Pos")
label1.grid(row=0, column=0)
label2 = tk.Label(root, text="Erp")
label2.grid(row=0, column=1)
label3 = tk.Label(root, text="Description")
label3.grid(row=0, column=2)
label4 = tk.Label(root, text="d1")
label4.grid(row=0, column=3)
label5 = tk.Label(root, text="d2")
label5.grid(row=0, column=4)
label6 = tk.Label(root, text="d3")
label6.grid(row=0, column=5)
label7 = tk.Label(root, text="L-mm")
label7.grid(row=0, column=6)

# Create entry boxes for each row and column
entry_boxes = []
for row in range(1, 21):  # Create 20 rows
    row_boxes = []
    for col in range(7):  # Create 7 columns
        entry = tk.Entry(root)
        entry.grid(row=row, column=col)
        row_boxes.append(entry)
    entry_boxes.append(row_boxes)

# Create a button to save the data
save_button = tk.Button(root, text="Save", command=save_data)
save_button.grid(row=21, column=0, columnspan=7)

root.mainloop()
