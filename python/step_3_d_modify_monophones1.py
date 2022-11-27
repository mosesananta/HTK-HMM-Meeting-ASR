monophones_file_path = "output/monophones1"
with open(monophones_file_path, mode="r") as file:
    data = file.read()

lines = data.split("\n")

appended_lines = [
    "sil",
    "sp",
]

if lines[0] == appended_lines[0]:
    print("Warning: Step 3.d skipped")

else:
    output_lines = appended_lines + lines
    with open(monophones_file_path, mode="w") as file:
        file.write("\n".join(output_lines))
