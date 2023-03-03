import argparse, os;folder, filees = [], [];parser = argparse.ArgumentParser();parser.add_argument("file", nargs="?");args = parser.parse_args()
if args.file==None: args.file = os.getcwd();args.file = args.file.replace("\\", "/");files = os.listdir(f"{args.file}")
if len(files)!=0: [folder.append(file) if os.path.isdir(file) else filees.append(file) for file in files];[print(file) for file in folder];[print(file) for file in filees]
if len(files)==0: print("This folder is empty")