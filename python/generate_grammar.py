# NEED FIXING BECAUSE SOMETIMES BAGIAN LEXICON NYA EX. d i k e t a h u i bocor , harusnya diketahui aja bukan tabnya
lexicon_path = "data/lexicon.lex"
grammar_path = "data/grammar.txt"

with open(lexicon_path, mode="r") as file:
    data = file.read()

lines = data.split("\n")
if lines[-1] == "": # Last line is empty line
    lines = lines[:-1]

output_lines = []
for line in lines:
    modified_line = line.replace("\t", " ")
    output_line = modified_line.split(" ")[0]
    output_lines.append(output_line)

with open(grammar_path, mode="w") as file:
    file.write('$word = ')
    file.write(' | '.join(output_lines))
    file.write(';\n( SENT-START <$word> SENT-END\n)')