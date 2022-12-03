MFCC_HYPERPARAMETER=["MFCC_0_D_A_Z", "MFCC_D_A_E_Z", "MFCC_0_D_Z", "MFCC_0_D_A_T_Z", "MFCC_D_A_Z"]
experiment_name = "baseline"
train_map_config_path = f"config/{experiment_name}/script_tr.hcopy"
test_map_config_path = f"config/{experiment_name}/script_te.hcopy"
train_features_config_path = f"config/{experiment_name}/train_features.txt"
test_features_config_path = f"config/{experiment_name}/test_features.txt"

with open(train_map_config_path, mode="r") as file:
    raw_data = file.read()

lines = [line.split("\t")[1] for line in raw_data.split("\n")]
with open(train_features_config_path, mode="w") as file:
    file.write("\n".join(lines))

with open(test_map_config_path, mode="r") as file:
    raw_data = file.read()

lines = [line.split("\t")[1] for line in raw_data.split("\n")]
with open(test_features_config_path, mode="w") as file:
    file.write("\n".join(lines))
