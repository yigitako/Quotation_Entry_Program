import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import tkinter.font
import openpyxl
import os, platform
from dates import OpenDate
from Buyer import Customers
from Header import HeaderEntry
from src.erp_grups.erp_calculations import ErpCodeCalculator
from src.Quatation import Quatations


# if "yigit Akoymak" in User_Names:
#    filepath = r"C:\Users\yigit\Desktop\excel_data\kk.xlsx"
#    workbook = openpyxl.load_workbook(filepath)
#    sheet = workbook.active
#
#    workbook.save(filepath)
class DataEntry(OpenDate, Customers, HeaderEntry, ErpCodeCalculator, Quatations):
    cn = []
    def __init__(self):
        super().__init__()
        self.window = tkinter.Tk()
        self.window.configure(background='#31363b')  # eff0f1
        # install a new theme called awdark
        self.window.tk.call('source', r'C:\Users\yigit\PycharmProjects\Sepkon_enter_data\tkBreeze-master/breeze'
                                      r'/breeze.tcl')
        self.window.state('zoomed')
        # apply the theme
        self.s = ttk.Style()
        #self.s.theme_use('breeze')
        self.s.configure('TNotebook.Tab', font=('HACK', 14))
        self.s.configure("my.TButton", font=("Hack", 14))
        self.s.configure('TNotebook.Tab', background="blue")
        self.s.map("TNotebook", background=[("selected", "red")])
        # title of the window
        self.window.title("Data Entry Sepkon")
        self.notebook = ttk.Notebook(self.window)
        self.notebook.pack(fill='y', expand=True)
        self.notebook.grid(row=0, column=0, sticky='W')

        self.frame1 = ttk.Frame(self.notebook, width=400, height=280)
        self.frame2 = ttk.Frame(self.notebook, width=400, height=280)
        self.frame3 = ttk.Frame(self.notebook)
        self.frame1.pack(fill='both', expand=True)
        self.frame2.pack(fill='both', expand=True)
        self.frame3.pack(fill='both', expand=True)
        self.notebook.add(self.frame1, text='Registration Data')
        self.notebook.add(self.frame2, text='Quotation')
        self.notebook.add(self.frame3, text='Open the excel')
        self.notebook.bind("<<NotebookTabChanged>>", self._open_excel)
        # Button below notebook
        # self.button_frame = ttk.Frame(self.window)
        # self.button_frame.grid(sticky="NEWS", row=3,padx=20)
        # fonts
        ttk_font = tkinter.font.Font(size=10, font="Hack")
        ttk_font_header = tkinter.font.Font(size=28, font="Hack")
        ttk_entry_font = tkinter.font.Font(size=8, font="Hack")
        # Buyer LabelFrame
        self.buyer_font = ttk.Label(text="Buyer", font=24)
        self.buyer = ttk.Frame(self.notebook)  # labelwidget=self.buyer_font
        # self.buyer.grid(row=0, column=0, sticky="NW")

        # Buyer info
        self.buyer_info_label = ttk.Label(self.frame1, text='Buyer name', font=ttk_font)
        vcmd = self.buyer.register(self.validate)
        self.buyer_info_combobox = ttk.Combobox(self.frame1, font=ttk_font, validate='key',
                                                validatecommand=(vcmd, '%P'))
        self.buyer_info_label.grid(row=0, column=0)
        self.buyer_info_combobox.grid(row=0, column=1)

        self.buyer_info_combobox.bind("<KeyRelease>", self._check_key)
        # self.buyer_info =
        # Saving User Info
        self.header_font = ttk.Label(text="Header", font=24)
        self.user_info_frame = ttk.LabelFrame(self.window, labelwidget=self.header_font)
        # self.user_info_frame.grid(row=1, column=0, sticky='NW')

        self.Open_Data_label = ttk.Label(self.frame1, text="Open Date", font=ttk_font)
        self.Open_Data_label.grid(row=1, column=0)
        self.Dead_Line_label = ttk.Label(self.frame1, text="Dead Line", font=ttk_font)
        self.Dead_Line_label.grid(row=1, column=1)

        # _Open_Date______________________________________________________________________________________#
        self.namevar = StringVar()
        self.Open_Data_name_entry = ttk.Entry(self.frame1, font=ttk_entry_font, textvariable=self.enter_data)
        self.Dead_Line_entry = ttk.Entry(self.frame1, font=ttk_entry_font)
        self.Open_Data_name_entry.grid(row=2, column=0)
        self.Dead_Line_entry.grid(row=2, column=1)
        self.Open_Data_name_entry.bind('<Key>', lambda event: self._add_slash_to_time(self.Open_Data_name_entry))
        self.Dead_Line_entry.bind('<Key>', lambda event: self._add_slash_to_time(self.Dead_Line_entry))
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
        self.Origin_Restiriction_entry = ttk.Entry(self.frame1, font=ttk_entry_font)
        self.Origin_Restiriction.grid(row=5, column=1)
        self.Origin_Restiriction_entry.grid(row=6, column=1)
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

        for widget in self.frame1.winfo_children():
            widget.grid_configure(padx=5, pady=10)

        # Saving Course Info
        self.courses_frame_font = ttk.Label(text="Registration Data", font=ttk_font_header)
        self.courses_frame = ttk.LabelFrame(self.window, labelwidget=self.courses_frame_font)
        # self.courses_frame.grid(row=2, column=0, sticky='NEWS')

        # Postion of the excel values
        self.pos_label = ttk.Label(self.frame2, text="POS", font=ttk_font)
        self.pos_entry = ttk.Entry(self.frame2, font=ttk_font)
        self.pos_label.grid(row=0, column=0)
        self.pos_entry.grid(row=1, column=0)

        # ERP code
        self.ERP_Grup_label = ttk.Label(self.frame2, text="ERP_Grup", font=ttk_font)
        self.ERP_Entry = ttk.Combobox(self.frame2, values=ErpCodeCalculator()._erp_code_abbreviation(), font=ttk_font)
        self.ERP_Grup_label.grid(row=0, column=0)
        self.ERP_Entry.grid(row=1, column=0)

        # Description
        self.Description_label = ttk.Label(self.frame2, text="Description", font=ttk_font)
        self.Description_box = ttk.Entry(self.frame2, font=ttk_font)
        self.Description_label.grid(row=0, column=1)
        self.Description_box.grid(row=1, column=1, sticky='news')

        # Dimensions_1
        self.Dimensions_label = ttk.Label(self.frame2, text="Dimension_2", font=ttk_font)
        self.Dimensions_box = ttk.Entry(self.frame2, font=ttk_font)
        self.Dimensions_label.grid(row=2, column=0)
        self.Dimensions_box.grid(row=3, column=0)

        # Dimension 2
        self.Dimensions2_label = ttk.Label(self.frame2, text="Dimension_1", font=ttk_font)
        self.Dimensions2_box = ttk.Entry(self.frame2, font=ttk_font)
        self.Dimensions2_label.grid(row=2, column=1)
        self.Dimensions2_box.grid(row=3, column=1)

        # Dimension 3
        self.Dimensions3_label = ttk.Label(self.frame2, text="Dim_3", font=ttk_font)
        self.Dimensions3_box = ttk.Entry(self.frame2, font=ttk_font)
        self.Dimensions3_label.grid(row=4, column=0)
        self.Dimensions3_box.grid(row=5, column=0)

        # L-mm values
        self.l_mm_label = ttk.Label(self.frame2, text="L-mm", font=ttk_font)
        self.l_mm_box = ttk.Entry(self.frame2, font=ttk_font)
        self.l_mm_label.grid(row=4, column=1)
        self.l_mm_box.grid(row=5, column=1)

        for widget in self.frame2.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        # SALES TERMS AND CONDITIONS
        self.sales_terms_conditions_font = ttk.Label(text='SALES TERMS AND CONDITIONS', font=24)
        self.sales_terms_conditions_frame = ttk.LabelFrame(self.window, labelwidget=self.sales_terms_conditions_font)
        # self.sales_terms_conditions_frame.grid(row=0, column=6, sticky='NE')
        # Total Order
        self.total_order_label = ttk.Label(self.sales_terms_conditions_frame, text='Total Order', font=24)
        self.total_order_entery = ttk.Entry(self.sales_terms_conditions_frame, font=ttk_font)
        self.total_order_label.grid(row=0, column=0)
        self.total_order_entery.grid(row=1, column=0)
        # Quantity
        self.quantity_label = ttk.Label(self.sales_terms_conditions_frame, text='Quantity', font=24)
        self.quantity_entery = ttk.Entry(self.sales_terms_conditions_frame, font=ttk_font)
        self.quantity_label.grid(row=2, column=0)
        self.quantity_entery.grid(row=3, column=0)
        # Delivery Term
        self.delivery_term_label = ttk.Label(self.sales_terms_conditions_frame, text='Delivery Term', font=24)
        self.delivery_term_entery = ttk.Entry(self.sales_terms_conditions_frame, font=ttk_font)
        self.delivery_term_label.grid(row=4, column=0)
        self.delivery_term_entery.grid(row=5, column=0)
        # Delivery Time
        self.delivery_time_label = ttk.Label(self.sales_terms_conditions_frame, text='Delivery Time', font=24)
        self.delivery_time_entery = ttk.Entry(self.sales_terms_conditions_frame, font=ttk_font)
        self.delivery_time_label.grid(row=6, column=0)
        self.delivery_time_entery.grid(row=7, column=0)
        # Payment Term
        self.payment_term_label = ttk.Label(self.sales_terms_conditions_frame, text='Payment Term', font=24)
        self.payment_term_entery = ttk.Entry(self.sales_terms_conditions_frame, font=ttk_font)
        self.payment_term_label.grid(row=8, column=0)
        self.payment_term_entery.grid(row=9, column=0)
        # Origin
        self.origin_label = ttk.Label(self.sales_terms_conditions_frame, text='Origin', font=24)
        self.origin_entery = ttk.Entry(self.sales_terms_conditions_frame, font=ttk_font)
        self.origin_label.grid(row=10, column=0)
        self.origin_entery.grid(row=11, column=0)
        # Delivery Tol
        self.delivery_tol_label = ttk.Label(self.sales_terms_conditions_frame, text='Delivery Tol', font=24)
        self.delivery_tol_entery = ttk.Entry(self.sales_terms_conditions_frame, font=ttk_font)
        self.delivery_tol_label.grid(row=12, column=0)
        self.delivery_tol_entery.grid(row=13, column=0)
        # Transport by
        self.transport_by_label = ttk.Label(self.sales_terms_conditions_frame, text='Transport By', font=24)
        self.transport_by_entery = ttk.Entry(self.sales_terms_conditions_frame, font=ttk_font)
        self.transport_by_label.grid(row=12, column=0)
        self.transport_by_entery.grid(row=13, column=0)
        # Partial Shipments
        self.partial_shipments_label = ttk.Label(self.sales_terms_conditions_frame, text='Partial Shipments', font=24)
        self.partial_shipments_entery = ttk.Entry(self.sales_terms_conditions_frame, font=ttk_font)
        self.partial_shipments_label.grid(row=14, column=0)
        self.partial_shipments_entery.grid(row=15, column=0)
        # Validity
        self.validity_label = ttk.Label(self.sales_terms_conditions_frame, text='Partial Shipments', font=24)
        self.validity_entery = ttk.Entry(self.sales_terms_conditions_frame, font=ttk_font)
        self.validity_label.grid(row=16, column=0)
        self.validity_entery.grid(row=17, column=0)

        for widget in self.sales_terms_conditions_frame.winfo_children():
            widget.grid_configure(padx=50, pady=0)

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
        self.button = ttk.Button(self.window, text="Open the file", style='my.TButton', command=self.enter_data,
                                 state=DISABLED)

        self.button.grid(row=3, column=0, sticky="news")
        # self.button.grid(row=4, column=0, sticky="news", padx=20, pady=10)

        self.window.mainloop()

    # -Buyer_combobox-#

    # _________________________________________________________________________________________#
    def validate(self, P):
        self.button.config(state=(NORMAL if P else DISABLED))
        return True
    def _open_excel(self, event):
        current_notebook = self.notebook.index(self.notebook.select())
        DataEntry.cn.append(current_notebook)
        print(DataEntry.cn)
        print(current_notebook)
        if int(self.notebook.index(self.notebook.select())) == int(2):
            DataEntry.cn.pop()
            self.notebook.select(DataEntry.cn[-1])
            print('as',DataEntry.cn)
            filepath = r"C:\Users\yigit\Desktop\excel_data\kk.xlsx"
            if platform.system() == 'Windows':
                os.startfile(filepath)

    # _________________________________________________________________________________________#
    def enter_data(self):

        filepath = r"C:\Users\yigit\Desktop\excel_data\kk.xlsx"
        try:
            workbook = openpyxl.load_workbook(filepath)
        except PermissionError:
            print('The file has been opened ')
        sheet = workbook.active
        OpenDate()._add_time_to_excel(sheet)
        if int(self.notebook.index(self.notebook.select())) == int(0):
            open_date = self.Open_Data_name_entry.get()
            dead_line = self.Dead_Line_entry.get()
            request_type = self.Request_Type_Entry.get()
            tax_exception = self.Tax_Exception_Entry.get()
            required_delivery = self.Required_Delivery.get()
            origin_restiriction = self.Origin_Restiriction_entry.get()
            operation_type = self.Operation_Type_entry.get()
            project_end_use = self.Project_End_Use_Entry.get()
            buyer_name = self.buyer_info_combobox.get()
            bynm = sheet['F9']
            bynm.value = buyer_name
            Customers()._insert_buyer_info_excel(sheet, buyer_name)
            HeaderEntry()._header_entry(sheet, open_date, dead_line, request_type, tax_exception, required_delivery,
                                        origin_restiriction, operation_type, project_end_use)

        if int(self.notebook.index(self.notebook.select())) == int(1):
            # Get the main values
            postion = self.pos_entry.get()
            erp = self.ERP_Entry.get()
            description = self.Description_box.get()
            dim1 = self.Dimensions_box.get()
            dim2 = self.Dimensions2_box.get()
            dim3 = self.Dimensions3_box.get()
            l_mm = self.l_mm_box.get()
            Quatations()._quatations_entry_to(sheet, postion, erp, description, dim1, dim2, dim3, l_mm)
            print(postion, erp, description, dim2, dim1, dim3)

        workbook.save(filepath)
        print('sucsess')


def PdfViewer(self):
    pass
    # root = tkinter.Tk()
    # create object like this.
    #
    # Add your pdf location and width and height.
    # variable2 = variable1.pdf_view(root, pdf_location=r"location", width=50, height=100)
    # variable2.pack()
    # root.mainloop()


de = DataEntry()
while True:
    de
    de._tab_changed()

# User_Names = {"yigit Akoymak": [["London, Greenwich, SE10"],
#                                ["+90 530 068 89 48"],
#                                ["https://www.yigitakoymak.xyz"],
#                                ["Erdogan Akoymak"],
#                                ["akoymakyigit@gmail.com"]]
#
#              }
