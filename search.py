import os
import sys
from clrprint import clrprint, clrinput
from shutil import get_terminal_size as t_size
import time

def found_smth():
    global found
    found = True

def clear_line(withchar=' ', end=""):
    print(f"\r{t_size().columns * withchar}", end=end)

def is_binary(file_path):
    try:
        with open(file_path, 'rb') as f:
            for byte in f.read(1024):
                if byte > 127:
                    return True
        return False
    except:
        return True

def search_dir(directory, term):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            clear_line()
            relative_file_path = os.path.relpath(file_path, start=os.getcwd())
            print(f"\r{relative_file_path}", end="")
            if not is_binary(file_path):
                search_in_file(file_path, term)
            elif formatted_args[3] and term in str(relative_file_path):
                clear_line("-", "\n")
                clrprint(f"\rFound", term, "in", os.path.relpath(file_path, start=os.getcwd()), clr="w,y,w,g")
                samefile = True
                found_smth()

def search_in_cwd(term):
    for item in os.listdir(os.getcwd()):
        clear_line()
        print(f"\r{item}", end="")
        if os.path.isfile(item) and not is_binary(item):
            file_path = os.path.join(os.getcwd(), item)
            search_in_file(file_path, term)
        elif is_binary(item) and formatted_args[3] and term in str(item):
            clear_line("-", "\n")
            clrprint(f"\rFound", term, "in", item, clr="w,y,w,g")
            samefile = True
            found_smth()

def search_in_file(file_path, term):
    samefile = False
    if formatted_args[3] and term in str(file_path):
        clear_line("-", "\n")
        clrprint(f"\rFound", term, "in", os.path.relpath(file_path, start=os.getcwd()), clr="w,y,w,g")
        samefile = True
        found_smth()
    with open(file_path, 'r', errors='ignore') as f:
        for line_number, line in enumerate(f, start=1):
            if term in str(line):
                if not samefile:
                    clear_line("-", "\n")
                    clrprint(f"\rFound", term, "in", os.path.relpath(file_path, start=os.getcwd()), clr="w,y,w,g")
                    samefile = True
                    found_smth()
                clrprint(line_number, "\t:", line[:-1], clr="b,w,r")

def main():
    try:
        arg = sys.stdin.read().strip()
        listarg = [""]
        index = 0
        wait_until = -1
        is_flag = False 
        for i in range (len(arg)):
            if is_flag and arg[i] == " ":
                is_flag = False
                if listarg[index] != "":
                    index += 1
                    listarg.append("")
            elif arg[i] == "-" and not is_flag:
                is_flag = True
                index += 1
                listarg.append(arg[i])
            elif arg[i] == '"':
                index += 1
                listarg.append("")
            elif arg[i+1:i+3] == "--" and arg[i] == " ":
                pass
            else:
                listarg[index] += arg[i]
        listarg = list(filter(None, listarg))
        global formatted_args
        formatted_args = ["<term>", "<file>", False, False]
        for i in range(len(listarg)):
            is_flag = False
            if i == 0:
                formatted_args[0] = listarg[0].strip()
            if listarg[i] == "--in-file":
                is_flag = True
                try:
                    formatted_args[1] = listarg[i+1]
                except IndexError:
                    clrprint("FlagError:", "Expected more after `--in-file` but received", "None", clr="r,y,r")
                    exit(1)
            if listarg[i] == "--in-cwd":
                is_flag = True
                formatted_args[2] = True
            if listarg[i] == "--include-filename":
                is_flag = True
                formatted_args[3] = True
            if listarg[i] == "--help":
                is_flag = True
            if not is_flag and listarg[i][:2] == "--":
                clrprint("Skipping unknown flag", listarg[i], clr="y,b")
        
        if listarg[0] == "ECHO is on." or "--help" in arg:
            clrprint("\nUsage:", "search", "<term>", "[--in-file <file>] [--in-cwd] [--include-filename]", clr="w,g,b,r")
            clrprint("Tool to search for a given term in a directory/file and return its line number.", clr="w")
            clrprint("Always searches in current directory", "recursively", "unless specified", clr="y,b,r,w",end=".\n\n")
            clrprint("<term>\t\t\t",":", "Term you want to search for","(required)", clr="b,w,w,y")
            clrprint("--in-file <file>\t",":", "File that you want to search in.", clr="r,w,w")
            clrprint("--in-cwd\t\t",":", "Search without entering into sub-directories", clr="r,w,w")
            clrprint("--include-filename\t", ":", "Search includes file names", clr="r,w,w")
            exit(0)
        #exit(1)
        
        global found
        found = False
        if formatted_args[1] != "<file>" and formatted_args[2] == True:
            clrprint("FlagError:", "Received", "`--in-file`", "and", "`--in-cwd`", "simultaneously", clr="r,y,p,y,p,y")
            exit(1)
        
        print()
        
        if formatted_args[1] != "<file>":
            clrprint("Searching for", listarg[0], "in", listarg[2], clr="w,b,w,y")
        elif formatted_args[2] == True:
            clrprint("Searching for", listarg[0], "in", os.getcwd(), clr="w,b,w,y")
        else:
            clrprint("Searching for", listarg[0], clr="w,b")
        
        if formatted_args[1] != "<file>" and formatted_args[2] == False:
            if os.path.isfile(formatted_args[1]):
                search_in_file(formatted_args[1], formatted_args[0])
            else:
                clrprint("FileNotFoundError:", f"{os.getcwd()}{os.path.sep}{formatted_args[1]}", clr="r,b")
                exit(1)
        elif formatted_args[2] == True:
            search_in_cwd(formatted_args[0])
        else:
            search_dir(os.getcwd(), formatted_args[0])
        if not found:
            clear_line()
            clrprint("\nCouldn't find", formatted_args[0], clr="y,b")
        else:
            clear_line("-")
            print()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
