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
        self.processes = {1: Process("init", "root", 0, Registers(self.random32BitHexValue(), self.random32BitHexValue(), self.random32BitHexValue(), self.random32BitHexValue(), self.random32BitHexValue(), self.random32BitHexValue()))}

    def random32BitHexValue(self):
        return randint(0x0, 0xFFFFFFFF)

    def randomPID(self):
        return randint(0, 5000)

    def getRunningProcessRegisters(self):
        for key, value in self.processes.items():
            if(value.status == 0):
                return value.registers

    def forkProcess(self):
        for key, value in self.processes.items():
            if (value.status == 0):
                new_process = Process(value.program, value.username, 1, value.registers)
                # http://stackoverflow.com/questions/1602934/check-if-a-given-key-already-exists-in-a-dictionary
                while True:
                    num = self.randomPID()
                    if num not in self.processes:
                        break
                self.processes[num] = new_process
                # need to break from outter loop to prevent exception
                break

    def printProcess(self):
        # http://stackoverflow.com/questions/18601688/python-prettytable-example
        table = prettytable.PrettyTable(["PID", "PROGRAM", "USER", "STATUS", "PC", "SP","R0", "R1", "R2", "R3"])
        for key, value in self.processes.items():
            table.add_row([str(key), value.program, value.username, str(value.status), ("0x" + str(format(value.registers.pc, '8X'))), ("0x" + str(format(value.registers.sp, '8X'))), ("0x" + str(format(value.registers.r0, '8X'))), ("0x" + str(format(value.registers.r1, '8X'))), ("0x" + str(format(value.registers.r2, '8X'))), ("0x" + str(format(value.registers.r3, '8X')))])
        print(table)


    def killProcess(self, pid):
        for key, value in self.processes.items():
            if value.status == 0:
                if (value.username == "root") or (value.username == self.processes[pid].username):
                    # http://stackoverflow.com/questions/11277432/how-to-remove-a-key-from-a-python-dictionary
                    self.processes.pop(pid, None)
                    break

    def execveProcess(self, program, user):
        for key, value in self.processes.items():
            if value.status == 0:
                value.program = program
                value.username = user
                value.registers = Registers(self.random32BitHexValue(), self.random32BitHexValue(), self.random32BitHexValue(), self.random32BitHexValue(), self.random32BitHexValue(), self.random32BitHexValue())
                break

    def blockProcess(self):
        for key, value in self.processes.items():
            if value.status == 0:
                value.status = 2
                keys = list(self.processes.keys())
                while True:
                    random_pid = keys[randint(0, len(keys) - 1)]
                    if self.processes[random_pid].status == 1:
                        self.processes[random_pid].status = 0
                        break
                break

    def unblockProcess(self, pid):
        for key, value in self.processes.items():
            if key == pid and value.status == 2:
                value.status = 1

    def yieldProcess(self):
        for key, value in self.processes.items():
            if value.status == 0:
                value.status = 1
                keys = list(self.processes.keys())
                while True:
                    random_pid = keys[randint(0, len(keys) - 1)]
                    if self.processes[random_pid].status == 1:
                        self.processes[random_pid].status = 0
                        break
                break

    def exitProcess(self):
        for key, value in self.processes.items():
            if value.status == 0:
                self.processes.pop(key, None)
                keys = list(self.processes.keys())
                while True:
                    random_pid = keys[randint(0, len(keys) - 1)]
                    if self.processes[random_pid].status == 1:
                        self.processes[random_pid].status = 0
                        break
                break