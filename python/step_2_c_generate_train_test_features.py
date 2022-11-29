MFCC_HYPERPARAMETER=["MFCC_0_D_A_Z", "MFCC_D_A_E_Z", "MFCC_0_D_Z", "MFCC_0_D_A_T_Z", "MFCC_D_A_Z"]
curr_mfcc = MFCC_HYPERPARAMETER[0]
train_map_config_path = f"config/script_tr_{curr_mfcc}.hcopy"
test_map_config_path = f"config/script_te_{curr_mfcc}.hcopy"
train_features_config_path = f"config/train_features_{curr_mfcc}.txt"
test_features_config_path = f"config/test_features_{curr_mfcc}.txt"

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
