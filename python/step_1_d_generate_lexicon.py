nims = [
    13519062,
    13519076, 
    13519088,
    # 13519100, (not a boyz)
    13519128,
    13519156,
    # 13519192, (not a boyz)
    13519196
]
lexicons_dir = "data/lexicons/"
merged_lexicon_path = "data/lexicon.lex"
ignored_lexicons_path = "data/ignored_lexicons.txt"

lines: list[str] = []
for nim in nims:
    filename = lexicons_dir + "{}.txt".format(nim)
    with open(filename, mode="r") as file:
        raw_data = file.read()

    file_lines = raw_data.split("\n")
    if file_lines[-1] != "": # Last line is not empty line
        lines += file_lines
    else:
        lines += file_lines[:-1]

lines = list(set(lines))

with open(ignored_lexicons_path, mode="r") as file:
    raw_data = file.read()

ignored_lexicons = raw_data.split("\n")
if ignored_lexicons[-1] == "": # Last line is empty
    ignored_lexicons = ignored_lexicons[:-1]

output_lines = []
for line in lines:
    if line != "":
        word = ""
        if "\t" in line:
            word = line.split("\t")[0]
        else:
            word = line.split(" ")[0]
        
        if not any([word == lexicon for lexicon in ignored_lexicons]):
            output_lines.append(line)

output_lines.sort()

output_lines.append("") # For new line

with open(merged_lexicon_path, mode="w") as file:
    file.write("\n".join(output_lines))
