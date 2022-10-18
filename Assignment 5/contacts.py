# Name: Trang Ngo
# Date: 10/12/2022
# File Purpose: Create contact module

import json

class Contacts:
    # self as a positional parameter, filename as keyword parameter
    def __init__(self, filename):
        # set a member variable equal to the filename
        self.filename = filename
        # set a member variable equal to an empty data dictionary.
        self.data = {}
        # open the filename and load the JSON decoded contents to the empty data dictionary
        try:
            with open(self.filename, 'r') as file:
                self.data = json.load(file)
        # filename does not exist
        except FileNotFoundError:
            pass
    
    # self as a positional parameter
    # id, first_name, last_name as keyword parameter
    def add_contact(self, id, first_name, last_name):
        # if the id exists in the data dictionary, return the string error.
        exists = id in self.data
        if exists: 
            return 'error'
        # set the id:[first_name, last_name] key:value pair to the data dictionary.
        self.data[id] = [first_name, last_name]
        # sort the data dictionary in ascending order by last name, and then by first name, ignoring case.
        self.sort_contacts()
        # write the contents of the data dictionary to the filename that was set to the member variable.
        self.write_data()
        # return the key:value pair that was added
        return self.data[id]

    # self as a positional parameter
    # id, first_name, last_name as keyword parameter
    def modify_contact(self, id, first_name, last_name):
        # if the id does not exists in the dictionary, return the string error.
        exists = id in self.data
        if not exists:
            return 'error'
        # set the id:[first_name, last_name'] key:value pair to the contact dictionary.
        self.data[id] = [first_name, last_name]
        # sort the data dictionary in ascending order by last name, and then by first name, ignoring case.
        self.sort_contacts()
        # write the contents of the data dictionary to the filename that was set to the member variable.
        self.write_data()
        # return the key:value pair that was modified.
        return self.data[id]

    # self as a positional parameter, id as a keyword parameter
    def delete_contact(self, id):
        # if the id does not exists in the dictionary, return the string error.
        exists = id in self.data
        if not exists:
            return 'error'
        # remove the key:value pair with the key equal to id.
        # pop: deletes the topmost element
        # push(a): inserts the element 'a' at the top
        exists = self.data.pop(id)
        # write the contents of the data dictionary to the filename that was set to the member variable.
        self.write_data()
        # return the key:value pair with the key equal to id.
        return exists
    
    def write_data(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f)
    
    def sort_contacts(self):
        list = []
        for key in self.data:
            list.append([key,self.data[key][0].upper(), self.data[key][1].upper(), self.data[key][0], self.data[key][1]])
        s = sorted(list,key = lambda x: (x[2], x[1]))
        # x[0] = key, x[2] = last name which we want to sort by first
        d = {}
        for item in s:
            id = item[0]
            first_name = item[3]
            last_name = item[4]
            d[id] = [first_name,last_name]
            self.data = d
            self.write_data()