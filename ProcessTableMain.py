from Computer import Computer


def main():
    computer = Computer()

    while True:
        response = input("Enter a command -> fork, kill <pid>, execve <program> <user>, block, yield, exit, print, unblock <pid>, and quit: ")
        response = response.strip().split()

        if len(response) > 0:
            if response[0] == "fork":
                computer.process_table.forkProcess()
            elif response[0] == "kill":
                computer.process_table.killProcess(int(response[1]))
            elif response[0] == "execve":
                computer.process_table.execveProcess(response[1], response[2])
                computer.cpu.registers = computer.process_table.getRunningProcessRegisters()
            elif response[0] == "block":
                computer.process_table.blockProcess()
                computer.cpu.registers = computer.process_table.getRunningProcessRegisters()
            elif response[0] == "yield":
                computer.process_table.yieldProcess()
                computer.cpu.registers = computer.process_table.getRunningProcessRegisters()
            elif response[0] == "exit":
                computer.process_table.exitProcess()
                computer.cpu.registers = computer.process_table.getRunningProcessRegisters()
            elif response[0] == "print":
                computer.print()
            elif response[0] == "unblock":
                computer.process_table.unblockProcess(response[1])
            elif response[0] == "quit":
                break
            else:
                print("Unknow command")


if __name__ == '__main__':
    main()