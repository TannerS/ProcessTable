class CPU:
    registers = None

    def __init__(self, registers):
        self.registers = registers


    def printRegisters(self):
        print("PC = " + "0x" + str(format(self.registers.pc, '8X')), end=" ")
        print("SP = " + "0x" + str(format(self.registers.sp, '8X')))
        print(" ")
        print("R0 = " + "0x" + str(format(self.registers.r0, '8X')), end=" ")
        print("R1 = " + "0x" + str(format(self.registers.r1, '8X')))
        print(" ")
        print("R2 = " + "0x" + str(format(self.registers.r2, '8X')), end=" ")
        print("R3 = " + "0x" + str(format(self.registers.r3, '8X')))
        print(" ")
