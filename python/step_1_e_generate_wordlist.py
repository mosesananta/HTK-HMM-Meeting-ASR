lexicon_path = "data/lexicon.lex"
wordlist_path = "data/wordlist.txt"

with open(lexicon_path, mode="r") as file:
    data = file.read()

lines = data.split("\n")
if lines[-1] == "": # Last line is empty line
    lines = lines[:-1]

output_lines = ["SENT-END","SENT-START"]
output_lines += [line.split("\t")[0] for line in lines]
output_lines.append("") # For newline at the end

with open(wordlist_path, mode="w") as file:
    file.write("\n".join(output_lines))
