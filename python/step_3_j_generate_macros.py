base_dir = "hmms/MFCC_0_D_A_T_Z/hmm.0"

with open("{}/vFloors".format(base_dir), mode="r") as file:
    data = file.read()

lines = data.split("\n")
lines.insert(0, "~o <MFCC_0_D_A_T_Z> <VecSize> 52")

with open("{}/macros".format(base_dir), mode="w") as file:
    file.write("\n".join(lines))
