from Computer import Computer


def main():
    computer = Computer()

    while True:
        response = input("Enter a command -> fork, kill <pid>, execve <program> <user>, block, yield, exit, print, unblock <pid>, and quit: ")
        response = response.strip().split()

        if response[0] == "fork":
            computer.process_table.forkProcess()
        elif response[0] == "kill":
            computer.process_table.killPID(int(response[1]))
        elif response[0] == "execve":
            computer.process_table.execve(response[1], response[2])
            computer.cpu.registers = computer.process_table.getRunningProcessRegisters()
        elif response[0] == "block":
            computer.process_table.block()
            computer.cpu.registers = computer.process_table.getRunningProcessRegisters()
        elif response[0] == "yield":
            print("debug 5")
        elif response[0] == "exit":
            print("")
        elif response[0] == "print":
            computer.print()
        elif response[0] == "unblock":
            print("debug 8")
        elif response[0] == "unblock":
            print("debug 9")
        elif response[0] == "quit":
            break
        else:
            print("Unknow command")


if __name__ == '__main__':
    main()