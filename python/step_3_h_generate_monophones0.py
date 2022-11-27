monophones0_path = "monophones0"
monophones1_path = "output/monophones1"

with open(monophones1_path, mode="r") as file:
    data = file.read()

lines = data.split("\n")
output_lines = [line for line in lines if line != "sp"]

with open(monophones0_path, mode="w") as file:
    file.write("\n".join(output_lines))
