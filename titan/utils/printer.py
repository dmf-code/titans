from prettytable import PrettyTable
from titan.abstracts.singleton import Singleton


class Printer(metaclass=Singleton):
    table = None

    def init(self, title=None):
        if not title:
           title = ["ID", "operator"]
        self.table = PrettyTable(title)

    def add_row(self, row):
        self.table.add_row(row)

    def output(self):
        print(self.table)
        self.table = None
