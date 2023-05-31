class Quatations():
    def _quatations_entry_to(self, sheet, postion, erp, description, dim1, dim2, dim3, l_mm):
        # Add postion
        pos = sheet['B21']
        pos.value = postion
        # add ERP Grup
        erp_ = sheet['C21']
        erp_.value = erp
        # add Description
        description_ = sheet['D21']
        description_.value = self.erp_codes['PRF'][0]
        description__ = sheet['H21']
        description__ = description
        # Dimension 1
        dim1_ = sheet['J21']
        dim1_.value = dim1
        # Dimension 2
        dim2_ = sheet['K21']
        dim2_.value = dim2
        # Dimension 3
        dim3_ = sheet['L21']
        dim3_.value = dim3
        # l-mm
        l_mm_ = sheet['M21']
        l_mm_.value - l_mm
