class HeaderEntry:
    def _header_entry(self, sheet, open_date, dead_line, request_type, tax_exception, required_delivery,
                      origin_restiriction, operation_type, project_end_use):
        # Add Open date and deadline
        opdv, ddl = sheet['S10'], sheet['S11']
        opdv.value, ddl.value = open_date, dead_line
        # Request Type, Tax exceptation
        rtyp, txex = sheet['S12'], sheet['S13']
        rtyp.value, txex.value = request_type, tax_exception
        # Requred delivery, Origin Restiriction
        rqd, org = sheet['S14'], sheet['S15']
        rqd.value, org.value = required_delivery, origin_restiriction
        # Operation Type and Project and Use
        opt, prju = sheet['S16'], sheet['S17']
        opt.value, prju.value = operation_type, project_end_use
