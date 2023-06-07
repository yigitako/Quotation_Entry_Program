import tkinter
from tkinter import ttk
from tkinter import *
import tkinter.font
import openpyxl
import os
import platform
from dates import OpenDate
from Buyer import Customers
from Header import HeaderEntry
from src.erp_grups.erp_calculations import ErpCodeCalculator
from src.Quatation import Quotations
from src.sales_terms import SalesAndTerms
from src.widgets.Quatation_entries import QuotationEntries
from pathlib import Path


class DataEntry(OpenDate, Customers, HeaderEntry, ErpCodeCalculator, Quotations, SalesAndTerms, QuotationEntries):
    notebook_tab_index = []

    def __init__(self):
        super().__init__()

        self.window = tkinter.Tk()
        self.window.configure(background='#eff0f1')
        self.window.tk.call('source', r'C:\Users\yigit\PycharmProjects\Sepkon_enter_data\tkBreeze-master/breeze-dark'
                                      r'/breeze-dark.tcl')
        self.window.state('zoomed')
        self.s = ttk.Style()
        self.s.theme_use('breeze-dark')
        self.s.configure('TNotebook.Tab', font=('HACK', 14))
        self.s.configure("my.TButton", font=("Hack", 14))
        self.s.configure('TNotebook.Tab', background="blue")
        self.s.map("TNotebook", background=[("selected", "red")])
        # title of the window
        self.window.title("Data Entry Sepkon")
        self.notebook = ttk.Notebook(self.window)
        self.notebook.pack()  # fill='nswe', expand=True
        self.notebook.grid(row=0, column=0)  # sticky='W'

        self.frame1 = ttk.Frame(self.notebook, width=self.window.winfo_width(),
                                height=self.window.winfo_height())

        self.frame2 = ttk.Frame(self.notebook, width=self.window.winfo_width(),
                                height=self.window.winfo_height())
        self.labelframe = LabelFrame(self.frame2, text="This is a LabelFrame")

        self.labelframe.grid(row=7, column=1)
        self.frame4 = ttk.Frame(self.notebook, width=400, height=280)
        self.frame3 = ttk.Frame(self.notebook)

        self.frame1.pack(fill='both', expand=True)
        self.frame2.pack(fill='both', expand=True)

        self.frame4.pack(fill='both', expand=True)
        self.frame3.pack(fill='both', expand=True)

        self.notebook.add(self.frame1, text='Registration Data')
        self.notebook.add(self.frame2, text='Quotation')
        self.notebook.add(self.frame4, text='Sales Term and Contions')
        self.notebook.add(self.frame3, text='Open the excel')
        self.notebook.bind("<<NotebookTabChanged>>", self._open_excel)

        ttk_font = tkinter.font.Font(size=10, font="Hack")
        ttk_font_header = tkinter.font.Font(size=28, font="Hack")
        ttk_entry_font = tkinter.font.Font(size=8, font="Hack")

        self.buyer_font = ttk.Label(text="Buyer", font=24)
        self.buyer = ttk.Frame(self.notebook)

        self.buyer_info_label = ttk.Label(self.frame1, text='Buyer name', font=ttk_font)
        vcmd = self.buyer.register(self.validate)
        self.buyer_info_combobox = ttk.Combobox(self.frame1, font=ttk_font, validate='key',
                                                validatecommand=(vcmd, '%P'))
        self.buyer_info_label.grid(row=0, column=0)
        self.buyer_info_combobox.grid(row=0, column=1)

        self.buyer_info_combobox.bind("<KeyRelease>", self._check_key)

        self.header_font = ttk.Label(text="Header", font=24)
        self.user_info_frame = ttk.LabelFrame(self.window, labelwidget=self.header_font)

        self.Open_Data_label = ttk.Label(self.frame1, text="Open Date", font=ttk_font)
        self.Open_Data_label.grid(row=1, column=0)
        self.Dead_Line_label = ttk.Label(self.frame1, text="Dead Line", font=ttk_font)
        self.Dead_Line_label.grid(row=1, column=1)

        # _Open_Date______________________________________________________________________________________#
        self.Open_Data_name_entry = ttk.Entry(self.frame1, font=ttk_entry_font)
        self.Dead_Line_entry = ttk.Entry(self.frame1, font=ttk_entry_font)
        self.Open_Data_name_entry.grid(row=2, column=0)
        self.Dead_Line_entry.grid(row=2, column=1)
        # self.Open_Data_name_entry.bind('<Key>', lambda event: self._add_slash_to_time(self.Open_Data_name_entry))
        # self.Dead_Line_entry.bind('<Key>', lambda event: self._add_slash_to_time(self.Dead_Line_entry))
        # _________________________________________________________________________________________________ #
        self.Request_Type_label = ttk.Label(self.frame1, text="Request Type", font=ttk_font)
        self.Request_Type_Entry = ttk.Entry(self.frame1, font=ttk_entry_font)
        self.Request_Type_label.grid(row=3, column=0)
        self.Request_Type_Entry.grid(row=4, column=0)
        # tax Exception section
        self.Tax_Exception_Label = ttk.Label(self.frame1, text="Tax Exception", font=ttk_font)
        self.Tax_Exception_Entry = ttk.Entry(self.frame1, font=ttk_entry_font)
        self.Tax_Exception_Label.grid(row=3, column=1)
        self.Tax_Exception_Entry.grid(row=4, column=1)

        # Required Delivery
        self.Required_Delivery_Label = ttk.Label(self.frame1, text="Requited Delivery", font=ttk_font)
        self.Required_Delivery = ttk.Entry(self.frame1, font=ttk_entry_font)
        self.Required_Delivery_Label.grid(row=5, column=0)
        self.Required_Delivery.grid(row=6, column=0)

        # Origin Restriction
        self.Origin_Restiriction = ttk.Label(self.frame1, text="Origin Restriction", font=ttk_font)
        self.Origin_Restiriction_combobox = ttk.Combobox(self.frame1, font=ttk_entry_font)
        self.Origin_Restiriction.grid(row=5, column=1)
        self.Origin_Restiriction_combobox.grid(row=6, column=1)
        self.Origin_Restiriction_combobox.bind("<KeyRelease>", self._origin_check_key)
        # Operation Type
        self.Operation_Type = ttk.Label(self.frame1, text="Operation Type", font=ttk_font)
        self.Operation_Type_entry = ttk.Entry(self.frame1, font=ttk_entry_font)
        self.Operation_Type.grid(row=7, column=0)
        self.Operation_Type_entry.grid(row=8, column=0)
        # Project end use
        self.Project_End_Use_Label = ttk.Label(self.frame1, text="Project end use", font=ttk_font)
        self.Project_End_Use_Entry = ttk.Entry(self.frame1, font=ttk_entry_font)
        self.Project_End_Use_Label.grid(row=7, column=1)
        self.Project_End_Use_Entry.grid(row=8, column=1)

        self.__line__(self.frame2, ttk_font)


        self.pos_entry = QuotationEntries().pos_label_entry(self.frame2, ttk_font)
        self.ERP_Entry = QuotationEntries().erp_grup_label(self.frame2, ttk_font,
                                                           ErpCodeCalculator()._erp_code_abbreviation())
        self.Description_box = QuotationEntries().Description(self.frame2, ttk_font)
        self.Dimensions_box = QuotationEntries().Dimension_1(self.frame2, ttk_font)
        self.Dimensions2_box = QuotationEntries().Dimension_2(self.frame2, ttk_font)
        self.Dimensions3_box = QuotationEntries().Dimension_3(self.frame2, ttk_font)
        self.l_mm_box = QuotationEntries().l_mm_label_entry(self.frame2, ttk_font)

        event = None

        self.get_combobox_value(event, self.frame2, ttk_font, self.pos_entry, self.ERP_Entry, self.Description_box,
                                    self.Dimensions_box, self.Dimensions2_box, self.Dimensions3_box, self.l_mm_box)

        for widget in self.frame1.winfo_children():
            widget.grid_configure(padx=50, pady=10)

        for widget in self.frame2.winfo_children():
            widget.grid_configure(padx=50, pady=10)

        # SALES TERMS AND CONDITIONS
        self.sales_terms_conditions_font = ttk.Label(text='SALES TERMS AND CONDITIONS', font=24)
        self.sales_terms_conditions_frame = ttk.LabelFrame(self.window, labelwidget=self.sales_terms_conditions_font)
        # self.sales_terms_conditions_frame.grid(row=0, column=6, sticky='NE')
        # Total Order
        self.total_order_label = ttk.Label(self.frame4, text='Total Order', font=24)
        self.total_order_entery = ttk.Entry(self.frame4, font=ttk_font)
        self.total_order_label.grid(row=0, column=0)
        self.total_order_entery.grid(row=1, column=0)
        # Quantity
        self.quantity_label = ttk.Label(self.frame4, text='Quantity', font=24)
        self.quantity_entery = ttk.Entry(self.frame4, font=ttk_font)
        self.quantity_label.grid(row=0, column=1)
        self.quantity_entery.grid(row=1, column=1)

        # Delivery Term
        self.delivery_term_label = ttk.Label(self.frame4, text='Delivery Term', font=24)
        self.delivery_term_entery = ttk.Entry(self.frame4, font=ttk_font)
        self.delivery_term_label.grid(row=4, column=0)
        self.delivery_term_entery.grid(row=5, column=0)
        # Delivery Time
        self.delivery_time_label = ttk.Label(self.frame4, text='Delivery Time', font=24)
        self.delivery_time_entery = ttk.Entry(self.frame4, font=ttk_font)
        self.delivery_time_label.grid(row=4, column=1)
        self.delivery_time_entery.grid(row=5, column=1)
        # Payment Term
        self.payment_term_label = ttk.Label(self.frame4, text='Payment Term', font=24)
        self.payment_term_entery = ttk.Entry(self.frame4, font=ttk_font)
        self.payment_term_label.grid(row=6, column=0)
        self.payment_term_entery.grid(row=7, column=0)
        # Origin
        self.origin_label = ttk.Label(self.frame4, text='Origin', font=24)
        self.origin_entery = ttk.Entry(self.frame4, font=ttk_font)
        self.origin_label.grid(row=6, column=1)
        self.origin_entery.grid(row=7, column=1)
        # Delivery Tol
        self.delivery_tol_label = ttk.Label(self.frame4, text='Delivery Tol', font=24)
        self.delivery_tol_entery = ttk.Entry(self.frame4, font=ttk_font)
        self.delivery_tol_label.grid(row=8, column=0)
        self.delivery_tol_entery.grid(row=9, column=0)
        # Transport by
        self.transport_by_label = ttk.Label(self.frame4, text='Transport By', font=24)
        self.transport_by_entery = ttk.Entry(self.frame4, font=ttk_font)
        self.transport_by_label.grid(row=8, column=1)
        self.transport_by_entery.grid(row=9, column=1)
        # Partial Shipments
        self.partial_shipments_label = ttk.Label(self.frame4, text='Partial Shipments', font=24)
        self.partial_shipments_entery = ttk.Entry(self.frame4, font=ttk_font)
        self.partial_shipments_label.grid(row=10, column=0)
        self.partial_shipments_entery.grid(row=11, column=0)
        # Validity
        self.validity_label = ttk.Label(self.frame4, text='Partial Shipments', font=24)
        self.validity_entery = ttk.Entry(self.frame4, font=ttk_font)
        self.validity_label.grid(row=10, column=1)
        self.validity_entery.grid(row=11, column=1)

        for widget in self.frame4.winfo_children():
            widget.grid_configure(padx=50, pady=10)

        # Accept terms
        self.terms_frame_font = ttk.Label(text='Terms & Conditions', font=24)
        self.terms_frame = ttk.LabelFrame(self.window, labelwidget=self.terms_frame_font)
        # self.terms_frame.grid(row=3, column=0, sticky='nwes')
        self.accept_var_font = ttk.Label(text="I accept the terms and conditions.", font=14)
        self.accept_var = tkinter.StringVar(value="Not Accepted")
        self.terms_check = ttk.Checkbutton(self.terms_frame, text="I accept the terms and conditions.",
                                           variable=self.accept_var, onvalue="Accepted", offvalue="Not Accepted")
        self.terms_check.grid(row=0, column=0)

        # Button enter_data
        self.button = ttk.Button(self.window, text="Enter data", style='my.TButton',
                                 command=self._put_data_to_excel,
                                 state=DISABLED)

        self.button.grid(row=3, column=0, sticky="news")

        self.window.mainloop()

    def validate(self, p):
        self.button.config(state=(NORMAL if p else DISABLED))
        return True

    def _open_excel(self, event):
        current_notebook = self.notebook.index(self.notebook.select())

        self.notebook_tab_index.append(current_notebook)

        if int(self.notebook.index(self.notebook.select())) == int(3):

            self.notebook_tab_index.pop()

            self.notebook.select(self.notebook_tab_index[-1])

            filepath = r"C:\Users\yigit\Desktop\excel_data\kk.xlsx"

            if platform.system() == 'Windows':
                os.startfile(filepath)

    def _from_buyer_entry_get_value(self):
        buyer_name = self.buyer_info_combobox.get()

        return buyer_name

    def _from_entries_get_value_(self):
        open_date = self.Open_Data_name_entry.get()

        dead_line = self.Dead_Line_entry.get()

        request_type = self.Request_Type_Entry.get()

        tax_exception = self.Tax_Exception_Entry.get()

        required_delivery = self.Required_Delivery.get()

        origin_restriction = self.Origin_Restiriction_combobox.get()

        operation_type = self.Operation_Type_entry.get()

        project_end_use = self.Project_End_Use_Entry.get()

        header_list = [open_date, dead_line, request_type, tax_exception, required_delivery,
                       origin_restriction, operation_type, project_end_use]

        return header_list

    def _from_quatation_entries_get_value(self):
        position = self.pos_entry.get()

        erp = self.ERP_Entry.get()

        description = self.Description_box.get()

        dim1 = self.Dimensions_box.get()

        dim2 = self.Dimensions2_box.get()

        dim3 = self.Dimensions3_box.get()

        l_mm = self.l_mm_box.get()

        quotation = [position, erp, description, dim1, dim2, dim3, l_mm]

        return quotation

    def _from_sales_and_terms_entries_get_value(self):
        total_order = self.total_order_entery.get()

        quantity = self.quantity_entery.get()

        delivery_term = self.delivery_term_entery.get()

        delivery_time = self.delivery_time_entery.get()

        payment_term = self.payment_term_entery.get()

        origin = self.origin_entery.get()

        delivery_tol = self.delivery_tol_entery.get()

        transport_by = self.transport_by_entery.get()

        partial_shipment = self.partial_shipments_entery.get()

        validity = self.validity_entery.get()

        sales_terms_and_conditions = [total_order, quantity, delivery_term, delivery_time, payment_term, origin,
                                      delivery_tol, transport_by, partial_shipment, validity]

        return sales_terms_and_conditions

    def _put_data_to_excel(self):

        filepath = r"C:\Users\yigit\Desktop\excel_data\kk.xlsx"

        try:

            workbook = openpyxl.load_workbook(filepath)

        except PermissionError:

            print('The file has been opened ')

        sheet = workbook.active

        bynm = sheet['F9']

        bynm.value = self._from_buyer_entry_get_value()

        OpenDate()._add_time_to_cell(sheet)

        Customers()._insert_buyer_info_excel(sheet, self._from_buyer_entry_get_value())

        HeaderEntry()._header_entry(sheet, self._from_entries_get_value_()[0],
                                    self._from_entries_get_value_()[1], self._from_entries_get_value_()[2],
                                    self._from_entries_get_value_()[3], self._from_entries_get_value_()[4],
                                    self._from_entries_get_value_()[5], self._from_entries_get_value_()[6],
                                    self._from_entries_get_value_()[7])

        SalesAndTerms()._sales_terms_entry_to_cell(sheet, self._from_sales_and_terms_entries_get_value()[0],
                                                   self._from_sales_and_terms_entries_get_value()[1],
                                                   self._from_sales_and_terms_entries_get_value()[2],
                                                   self._from_sales_and_terms_entries_get_value()[3],
                                                   self._from_sales_and_terms_entries_get_value()[4],
                                                   self._from_sales_and_terms_entries_get_value()[5],
                                                   self._from_sales_and_terms_entries_get_value()[6],
                                                   self._from_sales_and_terms_entries_get_value()[7],
                                                   self._from_sales_and_terms_entries_get_value()[8],
                                                   self._from_sales_and_terms_entries_get_value()[9],
                                                   )

        Quotations()._quatations_entry_to(sheet, self._from_quatation_entries_get_value()[0],
                                          self._from_quatation_entries_get_value()[1],
                                          self._from_quatation_entries_get_value()[2],
                                          self._from_quatation_entries_get_value()[3],
                                          self._from_quatation_entries_get_value()[4],
                                          self._from_quatation_entries_get_value()[5],
                                          self._from_quatation_entries_get_value()[6]
                                          )

        workbook.save(
            str(Path.home() / f"Downloads/S{OpenDate()._current_time()[2][2:5]}_{self._from_buyer_entry_get_value()}.xlsx")
        )


de = DataEntry()
de
