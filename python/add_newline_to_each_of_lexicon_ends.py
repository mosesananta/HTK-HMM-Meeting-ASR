nims = [13519062, 13519076, 13519088, 13519128, 13519156]
lexicons_dir = "data/lexicons/"

for nim in nims:
    filename = lexicons_dir + "{}.txt".format(nim)
    with open(filename, mode="r") as file:
        data = file.read()

    lines = data.split("\n")
    if lines[-1] != "": # Last line is not empty line
        lines.append("")
    
    print("Line:", lines[-1])

    with open(filename, mode="w") as file:
        file.write("\n".join(lines))
