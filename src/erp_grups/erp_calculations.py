
class ErpCodeCalculator:
    def __init__(self):
        self.erp_codes = {
            "PRF": ["Steel Profiles (Beams / Columns / Piles)", None],
            "PLT": ["Steel Plates (CS / AS)", None],
            "HSS": ["Hollow Structural Sections", None],
            "PCSW": ["PC Stands and Wires", None],
            "NGL": ["Angles (Equal and Unequal)", None],
            "CFC": ["Steel Sheets Cut From Coils (CS / AS / SS)", None],
            "CHS": ["Tubular Products (API / EN / DIN)", None],
            "SWP": ["SAW Pipes", None],
            "SMP": ["Seamless Heavy Wall Tubes", None],
            "FTG": ["Pipe Fittings", None],
            "VLV": ["Valves", None],
            "BNN": ["Bolts and Nuts", None],
            "SWR": ["Steel Wires / Ropes", None],
            "ALP": ["Aluminum Products", None],
            "CNA": ["Chemicals and Additives", None],
            "CPS": ["Consumables for Steel (Zinc / Electrodes / Steel Shots)", None],
            "UGR": ["UPS, Generator, Regulators", None],
            "GICS": ["Galvanized Steel Coils and Sheets", None],
            "PTRN": ["Expanded Sheets / Tear and Chequered", None],
            "RWA": ["Rails and Accessories", None],
            "GTS": ["Geotechnical Systems", None],
            "PPS": ["Post and Pretensioning Systems", None],
            "FBM": ["Bars (Flat, Square, Hexagonal, Round, Rectangular) Mill", None],
            "DRB": ["Deformed Reinforcing Bars", None],
            "PMP": ["Pumps (Injection)", None],
            "SSPS": ["Stainless Steel Plates / Sheets", None],
            "CLP": ["Cladded Plates", None],
            "HLE": ["Heavy Lifting Equipment", None],
            "MSC": ["Miscellaneous - Not Listed", None]
        }
        self.dimension1 = 2000
        self.dimension2 = 3500
        self.dimension3 = 4000
        self.length = 10
    def _erp_code_abbreviation(self):
        return list(self.erp_codes.keys())
    def calculate_PRF(self):
        pass


    def calculate_PLT(self):
        return (self.dimension1 * self.dimension2 * self.length) * 7.85 / 1_000_000

    def calculate_HSS(self):
        return self.length * (abs((abs((self.dimension1 * self.dimension2)) - abs(self.dimension1 - (2 * self.dimension3))) * (
                abs(self.dimension2 - (2 * self.dimension3)))) * 7.85) / 1_000_000

    def calculate_PCSW(self):
        pass

    def calculate_NGL(self):
        pass

    def calculate_CFC(self):
        pass

    def calculate_CHS(self):
        return self.dimension2 * (self.dimension1 - self.dimension2) / 40, 55 * self.length

    def calculate_SWP(self):
        pass

    def calculate_SMP(self):
        pass

    def calculate_FTG(self):
        pass

    def calculate_VLV(self):
        pass

    def calculate_BNN(self):
        pass

    def calculate_SWR(self):
        pass

    def calculate_ALP(self):
        pass

    def calculate_CNA(self):
        pass

    def calculate_CPS(self):
        pass

    def calculate_UGR(self):
        pass

    def calculate_GICS(self):
        pass

    def calculate_PTRN(self):
        pass

    def calculate_RWA(self):
        pass

    def calculate_GTS(self):
        pass

    def calculate_PPS(self):
        pass

    def calculate_FBM(self):
        pass

    def calculate_DRB(self):
        pass

    def calculate_PMP(self):
        pass

    def calculate_SSPS(self):
        pass

    def calculate_CLP(self):
        pass

    def calculate_HLE(self):
        pass

    def calculate_MSC(self):
        pass

