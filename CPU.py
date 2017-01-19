import prettytable

class CPU:
    registers = None

    def __init__(self, registers):
        self.registers = registers


    def printRegisters(self):
        print("CPU")
        # http://stackoverflow.com/questions/18601688/python-prettytable-example
        table = prettytable.PrettyTable(["PC", "SP","R0", "R1", "R2", "R3"])
        if self.registers != None:
            table.add_row([("0x" + str(format(self.registers.pc, '08X'))), ("0x" + str(format(self.registers.sp, '08X'))), ("0x" + str(format(self.registers.r0, '08X'))), ("0x" + str(format(self.registers.r1, '08X'))), ("0x" + str(format(self.registers.r2, '08X'))), ("0x" + str(format(self.registers.r3, '08X')))])
        print(table)

