from tkinter import ttk, DISABLED, NORMAL


class QuotationEntries:
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

        lst_com_label = ttk.Label(frame2, text=f" EDITING {selected_value}", font=ttk_font)
        lst_com_label.configure(foreground='#3daee9', background='#31363b')
        lst_com_label.grid(row=9, column=0)

        return True

    def __line__(self, frame2, ttk_font):
        global lst_com, pos_entry
        line_select = ttk.Label(frame2, text='Select Quotation', font=ttk_font)
        lst_com = ttk.Combobox(frame2, font=ttk_font)
        lst_com['values'] = ('QUOTATION 1', 'QUOTATION 2', 'QUOTATION 3')
        line_select.grid(row=6, column=1)
        lst_com.grid(row=7, column=1)

        pos_entry = self.pos_label_entry(frame2, ttk_font)

        lst_com.bind("<<ComboboxSelected>>",
                     lambda event: self.get_combobox_value(event, frame2, ttk_font, pos_entry, ERP_Entry,
                                                           Description_box, Dimensions_box,
                                                           Dimensions2_box, Dimensions3_box,
                                                           l_mm_box))

    def pos_label_entry(self, frame2, ttk_font):
        pos_label = ttk.Label(frame2, text="POS", font=ttk_font)
        global pos_entry
        pos_entry = ttk.Entry(frame2, font=ttk_font)
        pos_label.grid(row=6, column=0)
        pos_entry.grid(row=7, column=0)
        return pos_entry

    def erp_grup_label(self, frame2, ttk_font, erp_code_calculator):
        ERP_Grup_label = ttk.Label(frame2, text="ERP_Grup", font=ttk_font)
        global ERP_Entry
        ERP_Entry = ttk.Combobox(frame2, values=erp_code_calculator, font=ttk_font)
        ERP_Grup_label.grid(row=0, column=0)
        ERP_Entry.grid(row=1, column=0)
        return ERP_Entry

    def Description(self, frame2, ttk_font):
        Description_label = ttk.Label(frame2, text="Description", font=ttk_font)
        global Description_box
        Description_box = ttk.Entry(frame2, font=ttk_font)
        Description_label.grid(row=0, column=1)
        Description_box.grid(row=1, column=1, sticky='news')
        vcmd = Description_box.register(self.get_combobox_value)
        Description_box.config(validate='key', validatecommand=(vcmd, '%P'))
        return Description_box

    def Dimension_1(self, frame2, ttk_font):
        Dimensions_label = ttk.Label(frame2, text="Dimension_2", font=ttk_font)
        global Dimensions_box
        Dimensions_box = ttk.Entry(frame2, font=ttk_font)
        Dimensions_label.grid(row=2, column=0)
        Dimensions_box.grid(row=3, column=0)
        vcmd = Dimensions_box.register(self.get_combobox_value)
        Dimensions_box.config(validate='key', validatecommand=(vcmd, '%P'))
        return Dimensions_box

    def Dimension_2(self, frame2, ttk_font):
        Dimensions2_label = ttk.Label(frame2, text="Dimension_1", font=ttk_font)
        global Dimensions2_box
        Dimensions2_box = ttk.Entry(frame2, font=ttk_font)
        Dimensions2_label.grid(row=2, column=1)
        Dimensions2_box.grid(row=3, column=1)
        vcmd = Dimensions2_box.register(self.get_combobox_value)
        Dimensions2_box.config(validate='key', validatecommand=(vcmd, '%P'))
        return Dimensions2_box

    def Dimension_3(self, frame2, ttk_font):
        Dimensions3_label = ttk.Label(frame2, text="Dim_3", font=ttk_font)
        global Dimensions3_box
        Dimensions3_box = ttk.Entry(frame2, font=ttk_font)
        Dimensions3_label.grid(row=4, column=0)
        Dimensions3_box.grid(row=5, column=0)
        vcmd = Dimensions3_box.register(self.get_combobox_value)
        Dimensions3_box.config(validate='key', validatecommand=(vcmd, '%P'))
        return Dimensions3_box

    def l_mm_label_entry(self, frame2, ttk_font):
        l_mm_label = ttk.Label(frame2, text="L-mm", font=ttk_font)
        global l_mm_box
        l_mm_box = ttk.Entry(frame2, font=ttk_font)
        l_mm_label.grid(row=4, column=1)
        l_mm_box.grid(row=5, column=1)
        vcmd = l_mm_box.register(self.get_combobox_value)
        l_mm_box.config(validate='key', validatecommand=(vcmd, '%P'))
        return l_mm_box
