lexicon_path = "data/lexicon.lex"
wordlist_path = "data/wordlist.txt"

with open(lexicon_path, mode="r") as file:
    data = file.read()

lines = data.split("\n")
if lines[-1] == "": # Last line is empty line
    lines = lines[:-1]

output_lines = ["SENT-END","SENT-START"]
for line in lines:
    modified_line = line.replace("\t", " ")
    output_line = modified_line.split(" ")[0]
    output_lines.append(output_line)

output_lines.append("") # For newline at the end

with open(wordlist_path, mode="w") as file:
    file.write("\n".join(output_lines))

print("Done! :D")
