from tkinter import ttk, DISABLED


class SalesTermsConditionsEntry:
    @staticmethod
    def _total_order_entry(frame4, ttk_font):
        total_order_label = ttk.Label(frame4, text='Total Order', font=24)

        total_order_entry = ttk.Entry(frame4, font=ttk_font)

        total_order_label.grid(row=0, column=0)

        total_order_entry.grid(row=1, column=0)

        return total_order_entry
    @staticmethod
    def _quantity_entry(frame4, ttk_font):
        quantity_label = ttk.Label(frame4, text='Quantity', font=24)

        quantity_entery = ttk.Entry(frame4, font=ttk_font)

        quantity_label.grid(row=0, column=1)

        quantity_entery.grid(row=1, column=1)

        return quantity_entery
    @staticmethod
    def _delivery_term_entry(frame4, ttk_font):
        delivery_term_label = ttk.Label(frame4, text='Delivery Term', font=24)

        delivery_term_entery = ttk.Entry(frame4, font=ttk_font)

        delivery_term_label.grid(row=4, column=0)

        delivery_term_entery.grid(row=5, column=0)

        return delivery_term_entery
    @staticmethod
    def _delivery_time_entry(frame4, ttk_font):
        delivery_time_label = ttk.Label(frame4, text='Delivery Time', font=24)

        delivery_time_entery = ttk.Entry(frame4, font=ttk_font)

        delivery_time_label.grid(row=4, column=1)

        delivery_time_entery.grid(row=5, column=1)

        return delivery_time_entery
    @staticmethod
    def _payment_term_entry(frame4, ttk_font):
        payment_term_label = ttk.Label(frame4, text='Payment Term', font=24)

        payment_term_entery = ttk.Entry(frame4, font=ttk_font)

        payment_term_label.grid(row=6, column=0)

        payment_term_entery.grid(row=7, column=0)

        return payment_term_entery
    @staticmethod
    def _origin_entry(frame4, ttk_font):
        origin_label = ttk.Label(frame4, text='Origin', font=24)

        origin_entery = ttk.Entry(frame4, font=ttk_font)

        origin_label.grid(row=6, column=1)

        origin_entery.grid(row=7, column=1)

        return origin_entery

    @staticmethod
    def _delivery_tol_entry(frame4, ttk_font):
        delivery_tol_label = ttk.Label(frame4, text='Delivery Tol', font=24)

        delivery_tol_entery = ttk.Entry(frame4, font=ttk_font)

        delivery_tol_label.grid(row=8, column=0)

        delivery_tol_entery.grid(row=9, column=0)

        return delivery_tol_entery

    @staticmethod
    def _transport_by_entry(frame4, ttk_font):
        transport_by_label = ttk.Label(frame4, text='Transport By', font=24)

        transport_by_entery = ttk.Entry(frame4, font=ttk_font)

        transport_by_label.grid(row=8, column=1)

        transport_by_entery.grid(row=9, column=1)

        return transport_by_entery
    @staticmethod
    def _partial_shipments_entry(frame4, ttk_font):
        partial_shipments_label = ttk.Label(frame4, text='Partial Shipments', font=24)

        partial_shipments_entery = ttk.Entry(frame4, font=ttk_font)

        partial_shipments_label.grid(row=10, column=0)

        partial_shipments_entery.grid(row=11, column=0)

        return partial_shipments_entery
    @staticmethod
    def _validity_entry(frame4, ttk_font):
        validity_label = ttk.Label(frame4, text='Partial Shipments', font=24)

        validity_entery = ttk.Entry(frame4, font=ttk_font)

        validity_label.grid(row=10, column=1)

        validity_entery.grid(row=11, column=1)

        return validity_entery
    def _enter_data_button(self, window, _put_data_to_excel):
        button = ttk.Button(window, text="Enter data", style='my.TButton',
                            command=_put_data_to_excel,
                            state=DISABLED)

        button.grid(row=3, column=0, sticky="news")
