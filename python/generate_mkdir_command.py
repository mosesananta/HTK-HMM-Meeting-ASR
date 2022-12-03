template = r"mkdir hmms\<EXPERIMENT_NAME>\<HMM-FOLDER>"

experiment_name = "TR120K_W300K"
hmm_folder_func = lambda x: "hmm.{}".format(x)

commands = []

for i in range(0, 420 + 1):
    command = template
    command = command.replace("<EXPERIMENT_NAME>", experiment_name)
    command = command.replace("<HMM-FOLDER>", hmm_folder_func(i))
    commands.append(command)

with open("output2.txt", mode="w") as file:
    file.write("\n".join(commands))

print("Done. :D")