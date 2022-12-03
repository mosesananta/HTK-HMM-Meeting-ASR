template_1 = r"HERest -C config\<EXPERIMENT_NAME>\config_train.hcopy -I output\<EXPERIMENT_NAME>\<MLF_NAME> -t 250.0 150.0 1000.0 -S config\<EXPERIMENT_NAME>\train_features.txt -H hmms\<EXPERIMENT_NAME>\<CURR-HMM-FOLDER>\macros -H hmms\<EXPERIMENT_NAME>\<CURR-HMM-FOLDER>\hmmdefs -M hmms\<EXPERIMENT_NAME>\<NEXT-HMM-FOLDER> <PHONE_NAME>"

template_2 = r"HERest -B -C config\<EXPERIMENT_NAME>\config_train.hcopy -I output\<EXPERIMENT_NAME>\<MLF_NAME> -t 250.0 150.0 1000.0 -s output\<EXPERIMENT_NAME>\stats -S config\<EXPERIMENT_NAME>\train_features.txt -H hmms\<EXPERIMENT_NAME>\<CURR-HMM-FOLDER>\macros -H hmms\<EXPERIMENT_NAME>\<CURR-HMM-FOLDER>\hmmdefs -M hmms\<EXPERIMENT_NAME>\<NEXT-HMM-FOLDER> <PHONE_NAME>"

template_3 = r"HERest -B -C config\<EXPERIMENT_NAME>\config_train.hcopy -I output\<EXPERIMENT_NAME>\<MLF_NAME> -t 250.0 150.0 1000.0 -S config\<EXPERIMENT_NAME>\train_features.txt -H hmms\<EXPERIMENT_NAME>\<CURR-HMM-FOLDER>\macros -H hmms\<EXPERIMENT_NAME>\<CURR-HMM-FOLDER>\hmmdefs -M hmms\<EXPERIMENT_NAME>\<NEXT-HMM-FOLDER> <PHONE_NAME>"

experiment_name = "TR120K_W300K"
phone_name = r"output/<EXPERIMENT_NAME>/tiedlist".replace("<EXPERIMENT_NAME>", experiment_name)
mlf_name = "wintri.mlf"
hmm_folder_func = lambda x: "hmm.{}".format(x)

commands = []

for i in range(350, 420):
    command = template_3
    command = command.replace("<EXPERIMENT_NAME>", experiment_name)
    command = command.replace("<PHONE_NAME>", phone_name)
    command = command.replace("<MLF_NAME>", mlf_name)
    command = command.replace("<CURR-HMM-FOLDER>", hmm_folder_func(i))
    command = command.replace("<NEXT-HMM-FOLDER>", hmm_folder_func(i+1))
    commands.append(command)

with open("output.txt", mode="w") as file:
    file.write("\n".join(commands))

print("Done. :D")