# NEED FIXING BECAUSE SOMETIMES BAGIAN LEXICON NYA EX. d i k e t a h u i bocor , harusnya diketahui aja bukan tabnya
lexicon_path = "data/lexicon.lex"
grammar_path = "data/grammar_fixed.txt"

with open(lexicon_path, mode="r") as file:
    data = file.read()

lines = data.split("\n")
if lines[-1] == "": # Last line is empty line
    lines = lines[:-1]

output_lines = []
output_lines += [line.split("\t")[0] for line in lines]



with open(grammar_path, mode="w") as file:
    file.write('$word = ')
    file.write(' | '.join(output_lines))
    file.write(';\n( SENT-START <$word> SENT-END\n)')