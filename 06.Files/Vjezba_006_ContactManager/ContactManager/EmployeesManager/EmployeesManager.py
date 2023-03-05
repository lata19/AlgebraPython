from FileManager import FileManager

class Employees:
    def __init__(self, first_name, last_name, oib, position):
        self.first_name = first_name
        self.last_name = last_name
        self.oib = oib
        self.position = position

    def convert_to_string(self, i):
        return f"{i}. Ime i prezime zaposlenika: {self.first_name} {self.last_name}\tOIB zaposlenika: {self.oib}\tRadno mjesto zaposlenika: {self.position}"

    def change_first_name(self, new_first_name):
        self.first_name = new_first_name

    def change_last_name(self, new_last_name):
        self.last_name = new_last_name

    def change_position(self, new_position):
        self.position = new_position

employees = {}


def create_employee(first_name, last_name, oib, position):
    employee = Employees(first_name, last_name, oib, position)
    employees[oib] = employee

def append_all_employees_to_file(file_path):
    i = 1
    file_writer = FileManager.openFilePathForAppending(file_path)
    for employee in employees.values():
        line = employee.convert_to_string(i)
        FileManager.writeLineWithFileWriter(file_writer, line)
        i += 1

    FileManager.closeFileConnection(file_writer)