# Name: Trang Ngo
# Date: 11/9/2022
# File Purpose: Inventory Module

import json

class Inventory:
    def __init__(self, filename):
        self.filename = filename
        self.data = {}
        try:
            with open(self.filename, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            pass
    
    # Write the updated dictionary to the filename provided in the __init__ function.
    # Return an integer value of 100 for a successful add.
    def write_data(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f)

    def add_item(self,barcode,description):
        # The isinstance() function returns True if the specified object is of the specified type, otherwise False.
        if not isinstance(barcode, str) or not len(barcode) == 6 or not barcode[:2] == 'BC' or not barcode[2:].isdigit():
            return 109 
        if barcode in self.data:
            return 101
        # update at barcode element in self.data where 0 represents description
        # element 0 known as description
        self.data[barcode] = [description, 0]
        self.write_data()
        return 100
    
    def modify_description(self, barcode, description):
        if barcode not in self.data:
            return 102
        self.data[barcode] = [description, self.data[barcode][1]]
        self.write_data()
        return 100
    
    def add_qty(self, barcode, qty):
        if barcode not in self.data:
            return 102
        if type(qty) != int:
           return 108
        self.data[barcode][1] += qty
        self.write_data()
        return 100
    
    def remove_qty(self,barcode,qty):
        if barcode not in self.data:
            return 102
        if type(qty) != int:
            return 108
        if qty > self.data[barcode][1]:
            return 103
        self.data[barcode][1] -= qty
        self.write_data()
        return 100

    def get_inventory(self):
        # allow 8 characters for the barcode, 20 characters for the description, and 5 characters for the quantity
        display = ""
        for key in self.data:
            display += f'{key:<8}{self.data[key][0]:<20}{self.data[key][1]:5}\n'
        return display