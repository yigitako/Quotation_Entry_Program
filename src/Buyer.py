import json
import re


class Customers:
    def _from_json_to_dict(self):
        with open('../user_names.json', 'r') as file:
            json_data = file.read()
            data_user = json.loads(json_data)
        return data_user

    def _buyers_list(self) -> list:
        user_keys = list(self._from_json_to_dict().keys())
        return user_keys

    def _insert_buyer_info_excel(self,sheet_int,buyer_names):
        usr_sheet_local = ['F11', 'F13', 'F14', 'F16', 'F17']
        for i in range(len(usr_sheet_local)):
            cell_location = usr_sheet_local[i]
            cell = sheet_int[cell_location]
            cell.value = self._from_json_to_dict()[buyer_names][i][0]
    def _update(self, data):
        self.buyer_info_combobox['values'] = data

    def _check_key(self, event):
        value = self.buyer_info_combobox.get()
        # get data from la
        if value == "":
            data = self._buyers_list()
        else:
            regex = fr'^{value}'
            data = [string for string in self._buyers_list() if re.match(regex, string)]
        # update data in combobox
        self._update(data)
