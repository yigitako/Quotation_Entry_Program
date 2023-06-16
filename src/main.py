import tkinter
from tkinter import ttk
from tkinter import *
import tkinter.font
import openpyxl

from pathlib import Path
import os
import platform

from dates import OpenDate
from Buyer import Customers
from Header import HeaderEntry

from src.erp_grups.erp_calculations import ErpCodeCalculator
from src.Quatation import Quotations
from src.sales_terms import SalesAndTerms
from src.widgets.Quatation_entries import QuotationEntries
from src.widgets.Sales_terms_entreis import SalesTermsConditionsEntry
from src.widgets.header_entries import HeaderEntries


class DataEntry(OpenDate, Customers, HeaderEntry, ErpCodeCalculator, Quotations, SalesAndTerms, QuotationEntries,
                SalesTermsConditionsEntry, HeaderEntries):
    notebook_tab_index = []

    def __init__(self):
        super().__init__()

        self.window = tkinter.Tk()
        self.window.configure(background='#eff0f1')
        self.window.tk.call('source', r'C:\Users\yigit\PycharmProjects\Sepkon_enter_data\tkBreeze-master/breeze'
                                      r'/breeze.tcl')
        self.window.state('zoomed')
        self.s = ttk.Style()
        self.s.theme_use('breeze')
        self.s.configure('TNotebook.Tab', font=('HACK', 14))
        self.s.configure("my.TButton", font=("Hack", 14), )
        self.s.configure('TNotebook.Tab', background="blue")
        self.s.map("TNotebook", background=[("selected", "red")])

        self.window.title("Data Entry Sepkon")
        self.notebook = ttk.Notebook(self.window)
        self.notebook.pack()
        self.notebook.grid(row=0, column=0)

        self.frame1 = Frame(self.notebook, width=self.window.winfo_width(),
                            height=self.window.winfo_height())

        self.frame2 = Frame(self.notebook, width=self.window.winfo_width(),
                            height=self.window.winfo_height())

        self.labelframe = LabelFrame(self.frame2, text="This is a LabelFrame")

        self.labelframe.grid(row=7, column=1)
        self.frame4 = Frame(self.notebook, width=400, height=280)
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

        self.Open_Data_name_entry = ttk.Entry(self.frame1, font=ttk_entry_font)
        self.Dead_Line_entry = ttk.Entry(self.frame1, font=ttk_entry_font)
        self.Open_Data_name_entry.grid(row=2, column=0)
        self.Dead_Line_entry.grid(row=2, column=1)

        self.Request_Type_Entry = self._request_type_entry(self.frame1, ttk_font, ttk_entry_font)
        self.Tax_Exception_Entry = self._tax_exception_entry(self.frame1, ttk_font, ttk_entry_font)
        self.Required_Delivery = self.required_delivery_entry(self.frame1, ttk_font, ttk_entry_font)
        self.Origin_Restiriction_combobox = self._origin_restriction_entry(self.frame1, ttk_font, ttk_entry_font,
                                                                           self._origin_check_key)
        self.Operation_Type_entry = self._operation_type_entry(self.frame1, ttk_font, ttk_entry_font)
        self.Project_End_Use_Entry = self._project_end_use_entry(self.frame1, ttk_font, ttk_entry_font)

        self.__line__(self.frame2, ttk_font)

        self.pos_entry = QuotationEntries().pos_label_entry(self.frame2, ttk_font)

        self.ERP_Entry = QuotationEntries().erp_grup_label(self.frame2, ttk_font,
                                                           ErpCodeCalculator()._erp_code_abbreviation())

        self.Description_box = QuotationEntries().Description(self.frame2, ttk_font)

        self.Dimensions_box = QuotationEntries().Dimension_1(self.frame2, ttk_font)

        self.Dimensions2_box = QuotationEntries().Dimension_2(self.frame2, ttk_font)

        self.Dimensions3_box = QuotationEntries().Dimension_3(self.frame2, ttk_font)

        self.l_mm_box = QuotationEntries().l_mm_label_entry(self.frame2, ttk_font)

        self.get_combobox_value(None, self.frame2, ttk_font, self.pos_entry, self.ERP_Entry, self.Description_box,
                                self.Dimensions_box, self.Dimensions2_box, self.Dimensions3_box, self.l_mm_box)
        # Sales and Terms

        self.total_order_entery = self._total_order_entry(self.frame4, ttk_font)

        self.quantity_entry = self._quantity_entry(self.frame4, ttk_font)

        self.delivery_term_entry = self._delivery_term_entry(self.frame4, ttk_font)

        self.delivery_time_entry = self._delivery_time_entry(self.frame4, ttk_font)

        self.payment_term_entry = self._payment_term_entry(self.frame4, ttk_font)

        self.origin_entry = self._origin_entry(self.frame4, ttk_font)

        self.delivery_tol_entry = self._delivery_tol_entry(self.frame4, ttk_font)

        self.transport_by_entry = self._transport_by_entry(self.frame4, ttk_font)

        self.partial_shipments_entry = self._partial_shipments_entry(self.frame4, ttk_font)

        self.validity_entry = self._validity_entry(self.frame4, ttk_font)

        self.button = ttk.Button(self.window, text="Enter data", style='my.TButton',
                                 command=self._put_data_to_excel,
                                 state=DISABLED)

        self.button.grid(row=3, column=0, sticky="news")

        for widget in self.frame1.winfo_children():
            widget.grid_configure(padx=50, pady=10)

        for widget in self.frame2.winfo_children():
            widget.grid_configure(padx=50, pady=10)

        for widget in self.frame4.winfo_children():
            widget.grid_configure(padx=50, pady=10)

        F5 = Frame(self.window, bd=10, relief='groove')
        F5.place(x=1010, y=180, width=350, height=380)

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

        quantity = self.quantity_entry.get()

        delivery_term = self.delivery_term_entry.get()

        delivery_time = self.delivery_time_entry.get()

        payment_term = self.payment_term_entry.get()

        origin = self.origin_entry.get()

        delivery_tol = self.delivery_tol_entry.get()

        transport_by = self.transport_by_entry.get()

        partial_shipment = self.partial_shipments_entry.get()

        validity = self.validity_entry.get()

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
                                          self._from_quatation_entries_get_value()[6],
                                          self._selected_value(None)
                                          )

        workbook.save(
            str(Path.home() / f"Downloads/S{OpenDate()._current_time()[2][2:5]}_{self._from_buyer_entry_get_value()}.xlsx")
        )


de = DataEntry()
de
