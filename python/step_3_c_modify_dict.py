dict_path = "output/dict"
with open(dict_path, mode="r") as file:
    data = file.read()

lines = data.split("\n")

appended_lines = [
    "SENT-START [] sil",
    "SENT-END   [] sil",
    "silence       sil",
]

if lines[0] == appended_lines[0]:
    print("Warning: Step 3.c skipped")

else:
    output_lines = appended_lines + lines
    with open(dict_path, mode="w") as file:
        file.write("\n".join(output_lines))
