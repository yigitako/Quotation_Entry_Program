from erp_grups.erp_calculations import ErpCodeCalculator


class Quotations:
    def _quatations_entry_to(self, sheet, postion, erp, description, dim1, dim2, dim3, l_mm, selected_val):
        if selected_val == 'QUOTATION 1':
            print('a')
            pos = sheet['B21']
            pos.value = postion
            # add ERP Grup
            erp_ = sheet['C21']
            erp_.value = erp
            # add Description
            description_ = sheet['D21']
            if erp in ErpCodeCalculator().erp_codes.keys():
                description_.value = ErpCodeCalculator().erp_codes[erp][0]
            else:
                description_.value = None
            description__ = sheet['D22']
            description__.value = description
            # Dimension 1
            dimension_1 = sheet['J21']
            dimension_1.value = dim1
            # Dimension 2
            dimension_2 = sheet['K21']
            dimension_2.value = dim2
            # Dimension 3
            dimension_3 = sheet['L21']
            dimension_3.value = dim3

            l_mm_ = sheet['M21']
            l_mm_.value = l_mm
        if selected_val == 'QUOTATION 2':
            pos = sheet['B23']
            pos.value = postion
            # add ERP Grup
            erp_ = sheet['C23']
            erp_.value = erp
            # add Description
            description_ = sheet['D23']
            if erp in ErpCodeCalculator().erp_codes.keys():
                description_.value = ErpCodeCalculator().erp_codes[erp][0]
            else:
                description_.value = None
            description__ = sheet['D24']
            description__.value = description
            # Dimension 1
            dimension_1 = sheet['J23']
            dimension_1.value = dim1
            # Dimension 2
            dimension_2 = sheet['K23']
            dimension_2.value = dim2
            # Dimension 3
            dimension_3 = sheet['L23']
            dimension_3.value = dim3

            l_mm_ = sheet['M23']
            l_mm_.value = l_mm

        if selected_val == 'QUOTATION 3':
            pass
