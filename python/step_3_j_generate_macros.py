from const import EXPERIMENT, TARGETKIND, VECSIZE

base_dir = f"hmms/{EXPERIMENT}/hmm.0"

with open("{}/vFloors".format(base_dir), mode="r") as file:
    data = file.read()

lines = data.split("\n")
lines.insert(0, f"~o <{TARGETKIND}> <VecSize> {VECSIZE}")

with open("{}/macros".format(base_dir), mode="w") as file:
    file.write("\n".join(lines))
