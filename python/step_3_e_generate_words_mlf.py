nims = [
    13519062,
    # 13519076, (sedang diperbaiki lexicon-nya)
    # 13519088, (sedang diperbaiki lexicon-nya)
    13519128,
    13519156,
]
transcripts_dir = "data/transcripts/"
script_tr_path = "config/script_tr.hcopy"
script_te_path = "config/script_te.hcopy"
output_filename = "words2.mlf"
valid_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "

with open(script_tr_path, mode="r") as file:
    raw_data = file.read()

train_lines = raw_data.split("\n")
if train_lines[-1] == "":
    train_lines = train_lines[:-1]
train_pairs = [str_pair.split("\t") for str_pair in train_lines]
train_map = {wav_path: mfc_path for wav_path, mfc_path in train_pairs}

with open(script_te_path, mode="r") as file:
    raw_data = file.read()

test_lines = raw_data.split("\n")
if test_lines[-1] == "":
    test_lines = test_lines[:-1]
test_pairs = [str_pair.split("\t") for str_pair in test_lines]
test_map = {wav_path: mfc_path for wav_path, mfc_path in test_pairs}

transcripts: dict[str, str] = {}
for nim in nims:
    transcript_path = "{}{}.txt".format(transcripts_dir, nim)
    with open(transcript_path, mode="r") as file:
        raw_data = file.read()

    transcript_lines = raw_data.split("\n")
    if transcript_lines[-1] == "":
        transcript_lines = transcript_lines[:-1]
    if "\t" in transcript_lines[0]:
        transcript_pairs = [str_pair.split("\t") for str_pair in transcript_lines]
    else:
        words_list = [line.split(" ") for line in transcript_lines]
        transcript_pairs = [[ws[0], " ".join(ws[1:])] for ws in words_list]

    #print(transcript_pairs)
    transcripts = transcripts | {path.replace(" ", ""): content for path, content in transcript_pairs}

print(transcripts['13519128_059.wav'])
lines = ["#!MLF!#"]
for wav_filename, mfc_filename in test_pairs:
    lab_filename = mfc_filename.replace(".mfc", ".lab")
    lines.append("\"{}\"".format(lab_filename))

    transcript_filename = wav_filename.split("/")[-1]
    sentence = transcripts[transcript_filename]
    clean_sentence = "".join([char.lower() if char in valid_chars else " " for char in sentence])
    for word in clean_sentence.split(" "):
        if word != "":
            lines.append(word)

    lines.append(".")

lines.append("") # For newline

with open(output_filename, mode="w") as file:
    file.write("\n".join(lines))