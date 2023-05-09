import os.path

filename = "Samplefile.txt"

if os.path.isfile(filename):
    with open(filename, "r") as f:
        contents = f.read()
        print(contents)
else:
        print("File does not exist.")

