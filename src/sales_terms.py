class SalesAndTerms:
    def _sales_terms_entry_to_cell(self, sheet, total_order, Quantity, delivery_term, delivery_time, payment_term,
                                   origin, delivery_tol, transport_by, partial_shipments, validity):
        total_order_ = sheet['H52']
        total_order_.value = total_order

        quantity_ = sheet['H53']
        quantity_.value = Quantity

        delivery_term_ = sheet['H54']
        delivery_term_.value = delivery_term

        delivery_time_ = sheet['H55']
        delivery_time_.value = delivery_time

        payment_term_ = sheet['H56']
        payment_term_.value = payment_term

        origin_ = sheet['H59']
        origin_.value = origin

        delivery_tol_ = sheet['F60']
        delivery_tol_.value = delivery_tol

        transport_by_ = sheet['H62']
        transport_by_.value = transport_by

        partial_shipments_ = sheet['H63']
        partial_shipments_.value = partial_shipments

        validity_ = sheet['H64']
        validity_.value = validity

