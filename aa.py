import tkinter as tk
from tkinter import ttk
import re
x = {"Lloyd Inc": [
    [
        "98894 Lisa Vista Apt. 072\nJennyberg, DC 03028"
    ],
    [
        "773-214-7873x579"
    ],
    [
        "https://www.king-gregory.net/"
    ],
    [
        "Natalie Jackson"
    ],
    [
        "bradleyrodriguez@example.net"
    ]
],
    "Munoz, Martinez and Ashley": [
        [
            "47941 Charles Coves\nNew Madison, AS 80797"
        ],
        [
            "(196)160-6525"
        ],
        [
            "http://mcmahon-mueller.biz/"
        ],
        [
            "Kimberly Miller"
        ],
        [
            "nelsonkristen@example.net"
        ]
    ],
    "Blair-Cross": [
        [
            "2454 Brown Ramp\nEast Shannon, IL 34361"
        ],
        [
            "196.781.7855"
        ],
        [
            "https://www.brock-hall.com/"
        ],
        [
            "Timothy Parker"
        ],
        [
            "rodriguezbrenda@example.org"
        ]
    ],
    "Anderson PLC": [
        [
            "52412 Pollard Expressway\nNew Joann, MN 23144"
        ],
        [
            "2208013898"
        ],
        [
            "http://www.medina-vargas.com/"
        ],
        [
            "Tamara Hoffman"
        ],
        [
            "wpotter@example.net"
        ]
    ],
    "Zavala Ltd": [
        [
            "92882 Cox Keys Apt. 950\nKarenberg, NV 82300"
        ],
        [
            "001-846-918-4534x0511"
        ],
        [
            "https://www.patel.com/"
        ],
        [
            "Curtis Johnson"
        ],
        [
            "alvaradofernando@example.com"
        ]
    ],
    "Martin and Sons": [
        [
            "97929 Lopez Mountain Apt. 396\nTaraland, KS 72336"
        ],
        [
            "362-772-7859x03859"
        ],
        [
            "https://johnson.com/"
        ],
        [
            "David Day"
        ],
        [
            "vasquezelizabeth@example.org"
        ]
    ],
    "Reyes, Johnson and King": [
        [
            "57645 Kathryn Coves Apt. 534\nEast Robert, MN 12099"
        ],
        [
            "827.334.9240"
        ],
        [
            "http://www.hammond.com/"
        ],
        [
            "Sabrina Russell"
        ],
        [
            "richardsonkenneth@example.com"
        ]
    ],
    "Best and Sons": [
        [
            "343 Richardson Estates Suite 415\nTiffanyshire, NH 44770"
        ],
        [
            "001-065-485-4254x0435"
        ],
        [
            "http://www.smith.net/"
        ],
        [
            "Eric Martinez"
        ],
        [
            "qfoster@example.net"
        ]
    ],
    "Simmons, Lynch and Lynn": [
        [
            "5883 Gill Mount\nWest Sharonland, FM 77120"
        ],
        [
            "(572)128-2188x0942"
        ],
        [
            "http://thompson-graham.com/"
        ],
        [
            "Emily Baker"
        ],
        [
            "csoto@example.com"
        ]
    ],
    "Moore, Mccarthy and Davis": [
        [
            "046 Joshua Rest\nLake Benjaminside, TX 99918"
        ],
        [
            "001-281-268-2016x432"
        ],
        [
            "http://cole.com/"
        ],
        [
            "Samantha Massey"
        ],
        [
            "cmartinez@example.net"
        ]
    ],
    "Turner, Giles and Torres": [
        [
            "34045 Stephens Station Apt. 047\nWest Tiffanyport, WV 40791"
        ],
        [
            "854.122.7076"
        ],
        [
            "https://www.ross.biz/"
        ],
        [
            "Robert Snyder"
        ],
        [
            "rballard@example.com"
        ]
    ],
    "Moore-Parker": [
        [
            "915 Williams Mountain\nEast Christopherburgh, SD 87259"
        ],
        [
            "+1-426-449-8056x06328"
        ],
        [
            "http://stevens.com/"
        ],
        [
            "Charles Terry"
        ],
        [
            "morganmary@example.com"
        ]]}
print(x)


def _buyers_list() -> list:
    user_keys = list(x.keys())
    return user_keys


def _insert_buyer_info_excel(self):
    pass


def _update(data):
    buyer_info_combobox['values'] = data


def _check_key(event):
    value = buyer_info_combobox.get()
    # get data from la
    if value == "":
        data = _buyers_list()
    else:
        regex = fr'^{value}'
        data = [string for string in _buyers_list() if re.match(regex, string)]
        print(type(data))
    # update data in combobox
    _update(data)

root = tk.Tk()
buyer_info_combobox = ttk.Combobox(root)
buyer_info_combobox['values'] = _buyers_list()
buyer_info_combobox.bind("<<ComboboxSelected>>", _check_key)
buyer_info_combobox.pack()
root.mainloop()