from Process import Process
from Registers import Registers
from random import randint
import prettytable

class ProcessTable:
    # http://stackoverflow.com/questions/8703496/hash-map-in-python
    processes = None
    running_pid = None
    latest_pid = None
    # http://stackoverflow.com/questions/8985806/python-constructors-and-init
    # http://stackoverflow.com/questions/625083/python-init-and-self-what-do-they-do
    def __init__(self):
        self.processes = {1: Process("init", "root", 0, Registers(self.random32BitHexValue(), self.random32BitHexValue(), self.random32BitHexValue(), self.random32BitHexValue(), self.random32BitHexValue(), self.random32BitHexValue()))}
        self.running_pid = 1
        self.latest_pid = self.running_pid

    def random32BitHexValue(self):
        return randint(0x0, 0xFFFFFFFF)

    def randomPID(self):
        self.latest_pid = self.latest_pid + 1
        return self.latest_pid

    def getRunningProcessRegisters(self):
        #need check for when exit command gets rid of all processes
        if self.running_pid != -1:
            return self.processes[self.running_pid].registers
        else:
            return None

    def forkProcess(self):
        new_process = Process(self.processes[self.running_pid].program, self.processes[self.running_pid].username, 1, self.processes[self.running_pid].registers)
        # http://stackoverflow.com/questions/1602934/check-if-a-given-key-already-exists-in-a-dictionary
        while True:
            num = self.randomPID()
            if num not in self.processes:
                break
        self.processes[num] = new_process

    def printProcess(self):
        print("Process Table")
        # http://stackoverflow.com/questions/18601688/python-prettytable-example
        table = prettytable.PrettyTable(["PID", "PROGRAM", "USER", "STATUS", "PC", "SP","R0", "R1", "R2", "R3"])
        if len(self.processes) > 0:
            for key, value in self.processes.items():
                table.add_row([str(key), value.program, value.username, str(value.status), ("0x" + str(format(value.registers.pc, '08X'))), ("0x" + str(format(value.registers.sp, '08X'))), ("0x" + str(format(value.registers.r0, '08X'))), ("0x" + str(format(value.registers.r1, '08X'))), ("0x" + str(format(value.registers.r2, '08X'))), ("0x" + str(format(value.registers.r3, '08X')))])
        print(table)

    def killProcess(self, pid):
        if (self.processes[self.running_pid].username == "root") or (self.processes[self.running_pid].username == self.processes[pid].username):
            # http://stackoverflow.com/questions/11277432/how-to-remove-a-key-from-a-python-dictionary
            self.processes.pop(pid, None)

    def execveProcess(self, program, user):
        if (self.processes[self.running_pid].username == "root") or (self.processes[self.running_pid].username == user):
            self.processes[self.running_pid].program = program
            self.processes[self.running_pid].username = user
            self.processes[self.running_pid].registers = Registers(self.random32BitHexValue(), self.random32BitHexValue(), self.random32BitHexValue(), self.random32BitHexValue(), self.random32BitHexValue(), self.random32BitHexValue())

    def blockProcess(self):
        self.processes[self.running_pid].status = 2
        keys = list(self.processes.keys())
        while True:
            random_pid = keys[randint(0, len(keys) - 1)]
            if self.processes[random_pid].status == 1:
                self.processes[random_pid].status = 0
                self.running_pid = random_pid
                break

    def unblockProcess(self, pid):
        if int(pid) in self.processes:
            if self.processes[int(pid)].status == 2:
                self.processes[int(pid)].status = 1

    def yieldProcess(self):
        keys = list(self.processes.keys())
        saved_pid = self.running_pid
        while True:
            random_pid = keys[randint(0, len(keys) - 1)]
            if self.processes[random_pid].status == 1:
                self.processes[random_pid].status = 0
                self.running_pid = random_pid
                break
        # need to be ran last to prevent loop choosing this process since we changed status = 1
        self.processes[saved_pid].status = 1

    def exitProcess(self):
            self.processes.pop(self.running_pid, None)
            if len(self.processes) > 0:
                keys = list(self.processes.keys())
                while True:
                    random_pid = keys[randint(0, len(keys) - 1)]
                    if self.processes[random_pid].status == 1:
                        self.processes[random_pid].status = 0
                        self.running_pid = random_pid
                        break
            else:
                self.running_pid = -1