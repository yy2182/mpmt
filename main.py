import sys
import commands

args = sys.argv
args.pop(0)

if len(args) == 0:
    commands.banner()
    exit()
else:
    print(args)
    match args[0].lower():
        case "help":
            commands.help()
        case "search":
            commands.help()
        case "configure":
            commands.configure()
        case "install":
            commands.install(name=args[1])