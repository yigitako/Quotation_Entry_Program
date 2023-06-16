from tkinter import ttk
class HeaderEntries:
    def _request_type_entry(self, frame1, ttk_font,ttk_entry_font):

        Request_Type_label = ttk.Label(frame1, text="Request Type", font=ttk_font)

        Request_Type_Entry = ttk.Entry(frame1, font=ttk_entry_font)

        Request_Type_label.grid(row=3, column=0)

        Request_Type_Entry.grid(row=4, column=0)

        return Request_Type_Entry

    def _tax_exception_entry(self,frame1, ttk_font, ttk_entry_font):
        Tax_Exception_Label = ttk.Label(frame1, text="Tax Exception", font=ttk_font)

        Tax_Exception_Entry = ttk.Entry(frame1, font=ttk_entry_font)

        Tax_Exception_Label.grid(row=3, column=1)

        Tax_Exception_Entry.grid(row=4, column=1)

        return Tax_Exception_Entry
    def required_delivery_entry(self, frame1, ttk_font, ttk_entry_font):
        Required_Delivery_Label = ttk.Label(frame1, text="Requited Delivery", font=ttk_font)

        Required_Delivery = ttk.Entry(frame1, font=ttk_entry_font)

        Required_Delivery_Label.grid(row=5, column=0)

        Required_Delivery.grid(row=6, column=0)

        return Required_Delivery
    def _origin_restriction_entry(self, frame1, ttk_font, ttk_entry_font,_origin_check_key):
        Origin_Restiriction = ttk.Label(frame1, text="Origin Restriction", font=ttk_font)

        Origin_Restiriction_combobox = ttk.Combobox(frame1, font=ttk_entry_font)

        Origin_Restiriction.grid(row=5, column=1)

        Origin_Restiriction_combobox.grid(row=6, column=1)

        Origin_Restiriction_combobox.bind("<KeyRelease>", _origin_check_key)

        return Origin_Restiriction_combobox
    def _operation_type_entry(self, frame1, ttk_font, ttk_entry_font):
        Operation_Type = ttk.Label(frame1, text="Operation Type", font=ttk_font)

        Operation_Type_entry = ttk.Entry(frame1, font=ttk_entry_font)

        Operation_Type.grid(row=7, column=0)

        Operation_Type_entry.grid(row=8, column=0)

        return Operation_Type_entry
    def _project_end_use_entry(self, frame1, ttk_font, ttk_entry_font):
        Project_End_Use_Label = ttk.Label(frame1, text="Project end use", font=ttk_font)

        Project_End_Use_Entry = ttk.Entry(frame1, font=ttk_entry_font)

        Project_End_Use_Label.grid(row=7, column=1)

        Project_End_Use_Entry.grid(row=8, column=1)

        return Project_End_Use_Entry
