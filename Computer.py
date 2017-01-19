from Process import Process
from ProcessTable import ProcessTable
from Registers import Registers
from CPU import CPU

class Computer:
    cpu = None
    process_table = None

    # def startPc(self):
    #     self.process_table = ProcessTable()
    #self.cpu = CPU(self.process_table.getRunningProcessRegisters())

    def  __init__(self):
        self.process_table = ProcessTable()
        self.cpu = CPU(self.process_table.getRunningProcessRegisters())

    def print(self):
        print()
        print()
        self.cpu.printRegisters()
        print()
        self.process_table.printProcess()
