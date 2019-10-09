import sys
import os

arg = sys.argv

lang = [
        "java",
        "js",
        "py"
]

print("GitHub Reposistory: https://github.com/rkgold/CC")

if len(arg) == 2:
    
    if lang.__contains__(arg[1].split(".")[len(arg[1].split("."))-1]):
        ext = arg[1].split(".")[len(arg[1].split("."))-1]
        if ext == lang[0]:
            os.system("jdk\\bin\\javac "+arg[1])
            os.system("jdk\\bin\\java "+arg[1])
        elif ext == lang[1]:
            os.system("nodejs\\node "+arg[1])
        elif ext == lang[2]:
            os.system("python "+arg[1])
        else:
            print("The file format "+ext+" is not supported...")
elif len(arg) == 2:
    if lang.__contains__(arg[1]):
        fn = input("Enter filename: ")
        if arg[1] == lang[0]:
            os.system("javac "+fn+"."+arg[1])
            os.system("java "+fn)
        elif arg[1] == lang[1]:
            os.system("node "+fn+"."+arg[1])
        elif arg[1] == lang[2]:
            os.system("python "+fn+"."+arg[1])
        else:
            print("The file format "+arg[1]+" is not supported...")
elif len(arg) == 1:
    print("Usage: cc -lang -fn")