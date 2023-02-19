from FileManager import FileManager

class Organization:
    def __init__(self, name, adress, oib):
        self.name = name
        self.adress = adress
        self.oib = oib

    def print_organization(self):
        print(f"Naziv: {self.name}\tAdresa: {self.adress}\tOIB: {self.oib}")

    def convert_to_string(self):
        return f"Naziv: {self.name}\tAdresa: {self.adress}\tOIB: {self.oib}"
    
    def change_name(self, new_name):
        self.name = new_name
    
    def change_adress(self, new_adress):
        self.adress = new_adress
    
organizations = {}

def create_organization(name, adress, oib):
    organization = Organization(name, adress, oib)
    organizations[oib] = organization

def write_all_organization_to_file(file_path):
    file_writer = FileManager.openFilePathForWriting(file_path)
    for organization in organizations.values():
        line = organization.convert_to_string()
        FileManager.writeLineWithFileWriter(file_writer, line)

    FileManager.closeFileConnection(file_writer)