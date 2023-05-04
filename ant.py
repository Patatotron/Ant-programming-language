import os
import time
os.system('clear')
code = []
while True:
    try:
        line = input()
    except EOFError:
        break
    code.append(line)
os.system("clear")
variables = {}
output = []
def write_output():
    for x in range(len(output)):
        print(''.join(output[x]))
for x in range(len(code)):
    if str(code[x]).startswith("var "):
        code[x] = str(code[x]).replace("var ", '')
        code[x] = str(code[x]).replace(" ", '')
        code[x] = str(code[x]).split('=')
        var_value = str(code[x][1])
        variables[code[x][0]] = var_value
    elif str(code[x]).startswith("write"):
        code[x] = str(code[x]).replace("write(", '')
        code[x] = str(code[x]).replace(")", '')
        if code[x] in variables:
            output.append(variables[code[x]])
        else:
            output.append(code[x])
write_output()