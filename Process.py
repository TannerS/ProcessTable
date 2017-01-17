class Process:
    program = None
    username = None
    status = None
    registers = None

    def __init__(self, program, username, status, registers):
        self.program = program
        self.username = username
        self.status = status
        self.registers = registers

    def getRegisters(self):
        return self.registers

    def getStatus(self):
        return self.status

    def getProgram(self):
        return self.program

    def getUserName(self):
        return self.username