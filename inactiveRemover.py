currMem = "members.txt"
exMem = "inactive.txt"


def inactiveRmvr(currMem, exMem):
    with open (currMem,"r+") as writeFile:
        with open (exMem,"a+") as appendFile:
            writeFile.seek(0)
            members = writeFile.readlines()
            header = members [0]
            members.pop(0)

            inactive = [member for member in members if ("no" in member)]

            writeFile.seek(0)
            writeFile.write(header)
            for member in members:
                if (member in inactive):
                    appendFile.write(member)
                else:
                    writeFile.write(member)
            writeFile.truncate()

inactiveRmvr(currMem, exMem)

currMem = "members.txt"
exMem = "inactive.txt"

headers = "Membership No Date Joined Active \n"

with open(currMem,"r") as readFile:
    print("Active Members: \n\n")
    print(readFile.read())

with open(exMem,"r") as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())