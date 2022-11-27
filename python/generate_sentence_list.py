# DEPRECATED

nim = 13519156
input_filename = "data/transcripts/{}.txt".format(nim)
with open(input_filename, mode="r") as file:
    data = file.read()

source_sentence_pairs = [x.split("\t") for x in data.split("\n")[:15]] # No need to take it all
sentences = [pair[1] for pair in source_sentence_pairs]
sources = [pair[0] for pair in source_sentence_pairs]

word_sequences = []
for sentence in sentences:
    clean_sentence = "".join([char.lower() if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" else " " for char in sentence])
    word_candidates = clean_sentence.split(" ")
    words = [x for x in word_candidates if x != ""]
    word_sequences.append(words)

output_lines = [" ".join(sequence) for sequence in word_sequences]
output_lines.append("") # Newline

output_filename = "data/sentlist.txt"
with open(output_filename, mode="w") as file:
    file.write("\n".join(output_lines))
