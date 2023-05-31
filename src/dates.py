import datetime
from tkinter import ttk
from tkinter import *


class OpenDate:
    def Date_time(self) -> list:
        """get the month and day of the current time"""
        date = datetime.datetime.now()
        return [str(date.day), str(date.month), str(date.year)]

    def _add_time_to_excel(self, sheet):
        time = sheet['S8']
        time.value = "/".join(self.Date_time())

    def _add_slash_to_time(self, entry, **args):

        name_e = self.namevar.get()
        if " ".join(name_e).split()[-1] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            entry.delete(len(name_e) - 1, END)
            # if len(name_e) > 0 and name_e[-1] == '\r':
            #    self.name.delete(len(name_e) - 1, END)
        else:
            if len(" ".join(name_e).split()) == 2:
                entry.insert(3, '\\')
            elif len(" ".join(name_e).split()) == 5:
                entry.insert(6, '\\')
                entry.icursor(END)
            elif len(" ".join(name_e).split()) == 11:
                self.entry.delete(len(name_e) - 1, END)
