base_dir = "hmms/baseline/hmm.0"
monophones0_path = "monophones0"

with open("{}/proto".format(base_dir), mode="r") as file:
    data = file.read()

lines = data.split("\n")
selected_lines = lines[3:] # Starts from fourth line to the end
# We ignore the empty line for now. If error exists, you should check this part.

with open(monophones0_path, mode="r") as file:
    data = file.read()

phones = data.split("\n")
if phones[-1] == "":
    phones = phones[:-1]

output_lines = lines[:3]
for phone in phones:
    output_lines.append(selected_lines[0].replace("proto", phone))
    for line in selected_lines[1:]:
        output_lines.append(line)

output_filename = "{}/hmmdefs".format(base_dir)
with open(output_filename, mode="w") as file:
    file.write("\n".join(output_lines))
