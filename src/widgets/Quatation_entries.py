from tkinter import *
import tkinter as tk
from tkinter import ttk


class QuotationEntries:
    comb_entry = {}
    label_entries = {}

    def get_combobox_value(self, event, frame2, ttk_font, pos_entry, ERP_Entry, Description_box,
                           Dimensions_box, Dimensions2_box, Dimensions3_box, l_mm_box):
        selected_value = lst_com.get()

        pos_entry.config(state=(DISABLED if str(selected_value) == '' else NORMAL))

        ERP_Entry.config(state=(DISABLED if str(selected_value) == '' else NORMAL))

        Description_box.config(state=(DISABLED if str(selected_value) == '' else NORMAL))

        Dimensions_box.config(state=(DISABLED if str(selected_value) == '' else NORMAL))

        Dimensions2_box.config(state=(DISABLED if str(selected_value) == '' else NORMAL))

        Dimensions3_box.config(state=(DISABLED if str(selected_value) == '' else NORMAL))

        l_mm_box.config(state=(DISABLED if str(selected_value) == '' else NORMAL))

        cont = 0
        if self._selected_value(event) in self.comb_entry.keys():
            for entry in self.label_entries.values():
                entry.delete(0, tk.END)
                print(self.comb_entry[self._selected_value(event)])
                entry.insert(0, str(self.comb_entry[self._selected_value(event)][cont][1]))
                cont += 1
        else:
            for entry in self.label_entries.values():
                entry.delete(0, tk.END)
                entry.insert(0, "")

        lst_com_label = ttk.Label(frame2, text=f" EDITING {selected_value}", font=ttk_font)
        lst_com_label.configure(foreground='#3daee9')
        lst_com_label.grid(row=9, column=0)

    @staticmethod
    def _selected_value(event):
        select_value_lst = lst_com.get()
        return select_value_lst

    def __line__(self, frame2, ttk_font):
        global lst_com
        line_select = ttk.Label(frame2, text='Select Quotation', font=ttk_font)
        lst_com = ttk.Combobox(frame2, font=ttk_font)
        lst_com['values'] = ('QUOTATION 1', 'QUOTATION 2', 'QUOTATION 3',
                             'QUOTATION 4', 'QUOTATION 5', 'QUOTATION 6',
                             'QUOTATION 7', 'QUOTATION 8', 'QUOTATION 9',
                             'QUOTATION 10', 'QUOTATION 11', 'QUOTATION 12',
                             'QUOTATION 13', 'QUOTATION 14', 'QUOTATION 15',
                             'QUOTATION 16', 'QUOTATION 17', 'QUOTATION 18',)
        line_select.grid(row=6, column=1)
        lst_com.grid(row=7, column=1)

        lst_com.bind("<<ComboboxSelected>>",
                     lambda event: self.get_combobox_value(None,frame2, ttk_font, pos_entry, ERP_Entry,
                                                           Description_box, Dimensions_box,
                                                           Dimensions2_box, Dimensions3_box,
                                                           l_mm_box))

    def on_focus_out(self,event):
        value = event.widget.get()
        label_text = event.widget.label_text
        self.comb_entry.setdefault(self._selected_value(event), []).append([label_text, value])
        print(self.comb_entry)

    def pos_label_entry(self, frame2, ttk_font):
        pos_label = ttk.Label(frame2, text="POS", font=ttk_font)

        global pos_entry

        pos_entry = ttk.Entry(frame2, font=ttk_font)

        pos_entry.bind("<FocusOut>", self.on_focus_out)

        pos_entry.label_text = "POS"

        self.label_entries["POS"] = pos_entry

        pos_entry.bind("<FocusOut>", self.on_focus_out)

        pos_label.grid(row=6, column=0)

        pos_entry.grid(row=7, column=0)

        return pos_entry

    def erp_grup_label(self, frame2, ttk_font, erp_code_calculator):
        ERP_Grup_label = ttk.Label(frame2, text="ERP_Grup", font=ttk_font)

        global ERP_Entry


        ERP_Entry = ttk.Combobox(frame2, values=erp_code_calculator, font=ttk_font)

        ERP_Entry.bind("<FocusOut>", self.on_focus_out)

        ERP_Entry.label_text = "ERP_Grup"

        self.label_entries["ERP_Grup"] = ERP_Entry

        ERP_Grup_label.grid(row=0, column=0)

        ERP_Entry.grid(row=1, column=0)

        return ERP_Entry

    def Description(self, frame2, ttk_font):
        Description_label = ttk.Label(frame2, text="Description", font=ttk_font)

        global Description_box

        Description_box = ttk.Entry(frame2, font=ttk_font)

        pos_entry.bind("<FocusOut>", self.on_focus_out)

        Description_box.label_text = "Description"

        self.label_entries["Description"] = Description_box

        Description_label.grid(row=0, column=1)

        Description_box.grid(row=1, column=1, sticky='news')

        return Description_box

    def Dimension_1(self, frame2, ttk_font):
        Dimensions_label = ttk.Label(frame2, text="Dimension_2", font=ttk_font)

        global Dimensions_box

        Dimensions_box = ttk.Entry(frame2, font=ttk_font)

        Dimensions_box.bind("<FocusOut>", self.on_focus_out)

        Dimensions_box.label_text = "Dimension_2"
        self.label_entries["Dimension_2"] = Dimensions_box

        Dimensions_label.grid(row=2, column=0)

        Dimensions_box.grid(row=3, column=0)

        return Dimensions_box

    def Dimension_2(self, frame2, ttk_font):
        Dimensions2_label = ttk.Label(frame2, text="Dimension_1", font=ttk_font)

        global Dimensions2_box

        Dimensions2_box = ttk.Entry(frame2, font=ttk_font)

        Dimensions2_box.bind("<FocusOut>", self.on_focus_out)

        self.label_entries['Dimension_1'] = Dimensions2_box

        Dimensions2_label.grid(row=2, column=1)

        Dimensions2_box.grid(row=3, column=1)

        return Dimensions2_box

    def Dimension_3(self, frame2, ttk_font):
        Dimensions3_label = ttk.Label(frame2, text="Dim_3", font=ttk_font)

        global Dimensions3_box

        Dimensions3_box = ttk.Entry(frame2, font=ttk_font)

        Dimensions3_box.bind("<FocusOut>", self.on_focus_out)

        self.label_entries["Dim_3"] = Dimensions3_box

        Dimensions3_label.grid(row=4, column=0)

        Dimensions3_box.grid(row=5, column=0)

        return Dimensions3_box

    def l_mm_label_entry(self, frame2, ttk_font):
        l_mm_label = ttk.Label(frame2, text="L-mm", font=ttk_font)

        global l_mm_box

        l_mm_box = ttk.Entry(frame2, font=ttk_font)

        self.label_entries["L-mm"] = l_mm_box

        l_mm_box.bind("<FocusOut>", self.on_focus_out)

        l_mm_label.grid(row=4, column=1)

        l_mm_box.grid(row=5, column=1)

        return l_mm_box
