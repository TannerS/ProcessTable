from Process import Process
from Registers import Registers
from random import randint
import prettytable

class ProcessTable:
    # http://stackoverflow.com/questions/8703496/hash-map-in-python
    processes = None

    # http://stackoverflow.com/questions/8985806/python-constructors-and-init
    # http://stackoverflow.com/questions/625083/python-init-and-self-what-do-they-do
    def __init__(self):
        self.processes = {"1": Process("init", "root", 0, Registers(self.random32BitHexValue(), self.random32BitHexValue(), self.random32BitHexValue(), self.random32BitHexValue(), self.random32BitHexValue(), self.random32BitHexValue()))}

    def random32BitHexValue(self):
        return randint(0x0, 0xFFFFFFFF)

    def getRunningProcessRegisters(self):
        for key, value in self.processes.items():
            if(value.status == 0):
                return value.registers

    def printTable(self):
        # stackoverflow.com/questions/10623727/python-spacing-and-aligning-strings
        table = prettytable.PrettyTable(["PID", "PROGRAM", "USER", "STATUS", "PC", "SP","R0", "R1", "R2", "R3"])
        #print(("PID {0:12} PROGRAM {0:12} USER {0:12} STATUS {0:12} PC {0:12} SP {0:12} R0 {0:12} R1 {0:12} R2 {0:12} R3").format("","","","","","","","",""))
        for key, value in self.processes.items():
            table.add_row([str(key), value.program, value.username, str(value.status), ("0x" + str(format(value.registers.pc, '8X'))), ("0x" + str(format(value.registers.sp, '8X'))), ("0x" + str(format(value.registers.r0, '8X'))), ("0x" + str(format(value.registers.r1, '8X'))), ("0x" + str(format(value.registers.r2, '8X'))), ("0x" + str(format(value.registers.r3, '8X')))])
        print(table)

