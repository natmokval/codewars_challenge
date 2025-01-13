# Befunge Interpreter
# https://www.codewars.com/kata/526c7b931666d07889000a3c/python
debug = True
from random import sample
def interpret(code):
    output = ""
    stack = []
    lines = []
    for i in code.splitlines():
        print(i)
        lines.append(i)
    pos_h = 0
    pos_v = 0
    dir_h = 1
    dir_v = 0
    str_mode = False
    while pos_h != -1:
        (pos_h, pos_v, dir_h, dir_v, stack, output, str_mode) = next_step(pos_h, pos_v, dir_h, dir_v, lines, stack, output, str_mode)
    return output

def next_step(pos_h, pos_v, dir_h, dir_v, lines, stack, output, str_mode):
    line = lines[pos_v]
    if debug:
        # print(f"Step: pos_h = {pos_h}, pos_v = {pos_v} ")
        print("stack = ", stack)
        print("Line: ", line)
        print("Command: ", line[pos_h])
        print("Output = ", output)
    if str_mode and line[pos_h] != "\"":
        stack.append(ord(line[pos_h]))
        return (pos_h+dir_h, pos_v+dir_v, dir_h, dir_v, stack, output, str_mode)
    if 47 < ord(line[pos_h]) < 58:
        stack.append(int(line[pos_h]))
    match line[pos_h]:
        case "+":
            stack = stack[:-2] + [stack[-2] + stack[-1]]
        case "-":
            stack = stack[:-2] + [stack[-2] - stack[-1]]
        case "*":
            stack = stack[:-2] + [stack[-2] * stack[-1]]
        case "/":
            stack = stack[:-2] + [int(round(stack[-2] / stack[-1])) if stack[-1] != 0 else 0]
        case "%":
            stack = stack[:-2] + [stack[-2] % stack[-1] if stack[-1] != 0 else 0]
        case "@":
            return (-1, -1, dir_h, dir_v, stack, output, str_mode)
        case "v":
            (dir_h, dir_v) = (0, 1)
        case ">":
            (dir_h, dir_v) = (1, 0)
        case "<":
            (dir_h, dir_v) = (-1, 0)
        case "^":
            (dir_h, dir_v) = (0, -1)
        case "\"":
            str_mode = not str_mode
        case ".":
            output += str(stack[-1])
            stack = stack[:-1]
        case ",":
            output += chr(stack[-1])
            stack = stack[:-1]
        case ":":
            if len(stack) == 0:
                stack.append(0)
            stack.append(stack[-1])
        case "_":
            (dir_h, dir_v) = (1, 0) if int(stack[-1]) == 0 else (-1, 0)
            stack = stack[:-1]
        case "|":
            (dir_h, dir_v) = (0, 1) if int(stack[-1]) == 0 else (0, -1)
            stack = stack[:-1]
        case "!":
            stack = stack[:-1] + [1 if stack[-1] == 0 else 0] 
        case "$":
            stack = stack[:-1]
        case "?":
            (dir_h, dir_v) = sample([(1, 0), (-1, 0), (0, 1), (0, -1)], 1)[0]
        case "#":
            (pos_h, pos_v) = (pos_h + dir_h, pos_v + dir_v)
        case "\\":
            if len(stack) == 1:
                stack = [0] + stack
            (stack[-2], stack[-1]) = (stack[-1], stack[-2])    
        case "p":
            (x, y) = (stack[-2], stack[-1])      
            tmp = list(lines[y])
            tmp[x] = chr(stack[-3])
            lines[y] = "".join(tmp)
            stack = stack[:-3]
        case "g":
            (x, y) = (stack[-2], stack[-1])  
            stack = stack[:-2]    
            stack += [ord(lines[y][x])]
        case "`":
            (b, a) = (stack[-2], stack[-1])  
            stack = stack[:-2]
            stack += [1] if b > a else [0]
    return (pos_h+dir_h, pos_v+dir_v, dir_h, dir_v, stack, output, str_mode)
        

# res = interpret('2>:3g" "-!v\\  g30          <\n |!`"&":+1_:.:03p>03g+:"&"`|\n @               ^  p3\\" ":<\n2 2345678901234567890123456789012345678')
# print(res)
