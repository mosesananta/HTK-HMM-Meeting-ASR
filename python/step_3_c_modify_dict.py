dict_path = "output/dict"
with open(dict_path, mode="r") as file:
    data = file.read()

lines = data.strip().split("\n")

appended_lines = [
    "SENT-END   [] sil",
    "SENT-START [] sil",
]

if lines[0] == appended_lines[0]:
    print("Warning: Step 3.c skipped")

else:
    lines.append("silence         sil")
    lines.sort()

    output_lines = appended_lines + lines
    output_lines.append("\n") # For new line

    with open(dict_path, mode="w") as file:
        file.write("\n".join(output_lines))
