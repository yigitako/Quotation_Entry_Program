import tkinter as tk
from tkinter import ttk
import json

# Sample JSON data
data = '''
{
  "orders": [
    {
      "orderNumber": "S23-XYZ",
      "buyerName": "John Doe",
      "address": "123 Main Street",
      "tel": "555-1234",
      "web": "www.example.com",
      "taxOfficeNo": "T12345",
      "contactPerson": "Jane Smith",
      "email": "johndoe@example.com",
      "cc": "accounts@example.com",
      "openDate": "2023-06-01",
      "deadLine": "2023-06-15",
      "requestType": "Purchase",
      "taxExceptionRequired": true,
      "delivery": {
        "required": true,
        "originRestriction": "None",
        "operationType": "Standard",
        "projectEndUse": "Construction",
        "techSpec": "Specifications go here"
      },
      "erpGroup": "GroupA",
      "dimensions": {
        "dimension1": "Value1",
        "dimension2": "Value2",
        "dimension3": "Value3",
        "length": "100",
        "unitPrice": 10.99,
        "lineTotal": 109.90,
        "totalOrder": 109.90,
        "quantity": 10,
        "deliveryTerm": "FOB",
        "deliveryTime": "2 weeks",
        "paymentTerm": "Net 30",
        "origin": "USA",
        "deliveryTolerance": "5%"
      }
    }
  ]
}
'''

# Create the main window
root = tk.Tk()
root.title("JSON Treeview")

# Create a Treeview widget
tree = ttk.Treeview(root)
tree.pack(fill="both", expand=True)

# Add columns to the Treeview
tree["columns"] = ("Value")
tree.column("#0", width=200)
tree.column("Value", width=200)

# Add headers to the Treeview columns
tree.heading("#0", text="Key")
tree.heading("Value", text="Value")

# Load the JSON data
json_data = json.loads(data)["orders"]

# Filter the JSON data based on order number "S23-XYZ"
filtered_data = next((item for item in json_data if item["orderNumber"] == "S23-XYZ"), None)

# Populate the Treeview with the filtered JSON data
if filtered_data:
    for key, value in filtered_data.items():
        if isinstance(value, dict) or isinstance(value, list):
            parent_id = tree.insert("", "end", text=key, open=True)
            tree.item(parent_id, values=(""))
            for k, v in value.items():
                tree.insert(parent_id, "end", text=k, values=(v,))
        else:
            tree.insert("", "end", text=key, values=(value,))

# Start the main event loop
root.mainloop()
