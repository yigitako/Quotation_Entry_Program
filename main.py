import datetime
import tkinter
from tkinter import ttk
from tkinter import messagebox
import os
import openpyxl
import time


class DataEntry:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.configure(background='#33393b')
        # install a new theme called awdark
        self.window.tk.call('lappend', 'auto_path', 'awthemes-10.4.0')
        self.window.tk.call('package', 'require', 'awdark')
        self.window.state('zoomed')
        # apply the theme
        self.s = ttk.Style()
        self.s.theme_use('awdark')
        # title of the window
        self.window.title("Data Entry Sepkon")
        self.frame = ttk.Frame(self.window)
        # background colour
        # Saving User Info
        self.user_info_frame = ttk.LabelFrame(self.window, text="Header")
        self.user_info_frame.grid(row=0, column=0, padx=20, pady=10, sticky='w')

        self.Open_Data_label = ttk.Label(self.user_info_frame, text="Open Date")
        self.Open_Data_label.grid(row=0, column=0, sticky='w')
        self.Dead_Line_label = ttk.Label(self.user_info_frame, text="Dead Line")
        self.Dead_Line_label.grid(row=0, column=1)

        self.Open_Data_name_entry = ttk.Entry(self.user_info_frame)
        self.Dead_Line_entry = ttk.Entry(self.user_info_frame)
        self.Open_Data_name_entry.grid(row=1, column=0)
        self.Dead_Line_entry.grid(row=1, column=1)

        self.Request_Type_label = ttk.Label(self.user_info_frame, text="Request Type")
        self.Request_Type_Entry = ttk.Entry(self.user_info_frame)
        self.Request_Type_label.grid(row=0, column=2)
        self.Request_Type_Entry.grid(row=1, column=2)
        # tax Exception section
        self.Tax_Exception_Label = ttk.Label(self.user_info_frame, text="Tax Exception")
        self.Tax_Exception_Entry = ttk.Entry(self.user_info_frame)
        self.Tax_Exception_Label.grid(row=2, column=0)
        self.Tax_Exception_Entry.grid(row=3, column=0)

        # Required Delivery
        self.Required_Delivery_Label = ttk.Label(self.user_info_frame, text="Requited Delivery")
        self.Required_Delivery = ttk.Entry(self.user_info_frame)
        self.Required_Delivery_Label.grid(row=2, column=1)
        self.Required_Delivery.grid(row=3, column=1)
        # Origin Restriction
        self.Origin_Restiriction = ttk.Label(self.user_info_frame, text="Origin Restriction")
        self.Origin_Restiriction_entry = ttk.Entry(self.user_info_frame)
        self.Origin_Restiriction.grid(row=2, column=2)
        self.Origin_Restiriction_entry.grid(row=3, column=2)
        # Operation Restriction
        self.Operation_Restiriction = ttk.Label(self.user_info_frame, text="Operation Restriction")
        self.Operation_Restiriction_entry = ttk.Entry(self.user_info_frame)
        self.Operation_Restiriction.grid(row=4, column=0)
        self.Operation_Restiriction_entry.grid(row=5, column=0)
        # Operation Type
        self.Operation_Type = ttk.Label(self.user_info_frame, text="Operation Type")
        self.Operation_Type_entry = ttk.Entry(self.user_info_frame)
        self.Operation_Type.grid(row=4, column=1)
        self.Operation_Type_entry.grid(row=5, column=1)
        # Project end use
        self.Project_End_Use_Label = ttk.Label(self.user_info_frame, text="Project end use")
        self.Project_End_Use_Entry = ttk.Entry(self.user_info_frame)
        self.Project_End_Use_Label.grid(row=4, column=2)
        self.Project_End_Use_Entry.grid(row=5, column=2)

        for widget in self.user_info_frame.winfo_children():
            widget.grid_configure(padx=5, pady=5)

        # Saving Course Info
        self.courses_frame = ttk.LabelFrame(self.window, text="Main")
        self.courses_frame.grid(row=1, column=0)

        # self.registered_label = ttk.Label(self.courses_frame, text="Registration Status")

        # self.reg_status_var = tkinter.StringVar(value="Not Registered")
        # self.registered_check = ttk.Checkbutton(self.courses_frame, text="Currently Registered",
        #                                        variable=self.reg_status_var, onvalue="Registered",
        #                                        offvalue="Not registered")

        # self.registered_label.grid(row=0, column=0)
        # self.registered_check.grid(row=1, column=0)

        # Postion of the excel values
        self.pos_label = ttk.Label(self.courses_frame, text="POS")
        self.pos_entry = ttk.Entry(self.courses_frame)
        self.pos_label.grid(row=0, column=0)
        self.pos_entry.grid(row=1, column=0)

        # ERP code
        self.ERP_Grup_label = ttk.Label(self.courses_frame, text="ERP_Grup")
        self.ERP_Entry = ttk.Entry(self.courses_frame)
        self.ERP_Grup_label.grid(row=0, column=1)
        self.ERP_Entry.grid(row=1, column=1)

        # Description
        self.Description_label = ttk.Label(self.courses_frame, text="Description")
        self.Description_box = ttk.Entry(self.courses_frame)
        self.Description_label.grid(row=2, column=0)
        self.Description_box.grid(row=3, column=0)

        # Dimensions_1
        self.Dimensions_label = ttk.Label(self.courses_frame, text="Dim_1")
        self.Dimensions_box = ttk.Entry(self.courses_frame)
        self.Dimensions_label.grid(row=4, column=0)
        self.Dimensions_box.grid(row=5, column=0)

        # Dimension 2
        self.Dimensions2_label = ttk.Label(self.courses_frame, text="Dim_2")
        self.Dimensions2_box = ttk.Entry(self.courses_frame)
        self.Dimensions2_label.grid(row=4, column=1)
        self.Dimensions2_box.grid(row=5, column=1)

        # Dimension 3
        self.Dimensions3_label = ttk.Label(self.courses_frame, text="Dim_3")
        self.Dimensions3_box = ttk.Entry(self.courses_frame)
        self.Dimensions3_label.grid(row=6, column=0)
        self.Dimensions3_box.grid(row=7, column=0)

        # L-mm values
        self.l_mm_label = ttk.Label(self.courses_frame, text="L-mm")
        self.l_mm_box = ttk.Entry(self.courses_frame)
        self.l_mm_label.grid(row=6, column=1)
        self.l_mm_box.grid(row=7, column=1)

        # Quantity
        # self.kg_p_label = ttk.Label(self.courses_frame,t)
        for widget in self.courses_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        # Accept terms
        self.terms_frame = ttk.LabelFrame(self.window, text="Terms & Conditions")
        self.terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

        self.accept_var = tkinter.StringVar(value="Not Accepted")
        self.terms_check = ttk.Checkbutton(self.terms_frame, text="I accept the terms and conditions.",
                                           variable=self.accept_var, onvalue="Accepted", offvalue="Not Accepted")
        self.terms_check.grid(row=0, column=0)

        # Button
        self.button = ttk.Button(self.window, text="Enter data", command=self.enter_data)
        self.button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

        self.window.mainloop()

    def Buyer(self):
        pass

    def Date_time(self) -> list:
        """get the month and day of the current time"""
        date = datetime.datetime.now()
        return [str(date.day), str(date.month), str(date.year)[-2:]]

    def enter_data(self):
        accepted = self.accept_var.get()
        if accepted == "Accepted":
            # Get the header values
            open_date = self.Open_Data_name_entry.get()
            dead_line = self.Dead_Line_entry.get()
            request_type = self.Request_Type_Entry.get()
            tax_exception = self.Tax_Exception_Entry.get()
            required_delivery = self.Required_Delivery.get()
            origin_restiriction = self.Origin_Restiriction_entry.get()
            operation_Restriction = self.Operation_Restiriction_entry.get()
            operation_type = self.Operation_Type_entry.get()
            project_end_use = self.Project_End_Use_Entry.get()
            # Get the main values
            postion = self.pos_entry.get()
            erp = self.ERP_Entry.get()
            description = self.Description_box.get()
            dim1 = self.Dimensions_box.get()
            dim2 = self.Dimensions2_box.get()
            dim3 = self.Dimensions3_box.get()
            l_mm = self.l_mm_box.get()
            print(postion,erp,description,dim2,dim1,dim3)
            # Course info
            #registration_status = self.reg_status_var.get()
            #numcourses = self.pos_entry.get()
            #numsemesters = self.ERP_Entry.get()

            #print("First name: ", open_date, "ERP_GROUP: ", dead_line)
            #print("Title: ", request_type, "Age: ", tax_exception, "Nationality: ")
            #print("# Courses: ", numcourses, "# Semesters: ", numsemesters)
            #print("Registration status", registration_status)
            #print("------------------------------------------")

            filepath = r"C:\Users\yigit\Desktop\excel_data\kk.xlsx"

            if not os.path.exists(filepath):
                workbook = openpyxl.Workbook()
                sheet = workbook.active
                heading = ["First Name",tax_exception, "Erp_group", "Title", "Age", "Nationality",
                           "# Courses", "# Semesters", "Registration status"]
                sheet.append(heading)
                workbook.save(filepath)
            workbook = openpyxl.load_workbook(filepath)
            sheet = workbook.active
            # Add Open date and deadline
            opdv, ddl = sheet['S10'], sheet['S11']
            opdv.value, ddl.value = open_date, dead_line
            # Request Type, Tax exceptation
            rtyp, txex = sheet['S12'], sheet['S13']
            rtyp.value, txex.value = request_type, tax_exception
            # Requred delivery, Origin Restiriction
            rqd,org = sheet['S14'],sheet['S15']
            rqd.value, org.value = required_delivery, origin_restiriction
            #Operation type, Origin Restriciton
            #opt = sheet['S16']
            #opr.value, opt.value = operation_Restriction, origin_restiriction
            # Add time to the excel
            time = sheet['S8']
            time.value = "/ ".join(self.Date_time())
            #
            sheet.append([open_date, dead_line, request_type, tax_exception])
            workbook.save(filepath)
        else:
            tkinter.messagebox.showwarning(title="Error", message="You have not accepted the terms")


def PdfViewer(self):
    root = tkinter.Tk()
    # create object like this.
    variable1 = pdf.ShowPdf()
    # Add your pdf location and width and height.
    variable2 = variable1.pdf_view(root, pdf_location=r"location", width=50, height=100)
    variable2.pack()
    root.mainloop()


DataEntry()
