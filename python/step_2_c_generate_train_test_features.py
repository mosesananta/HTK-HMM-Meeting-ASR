train_map_config_path = "config/script_tr.hcopy"
test_map_config_path = "config/script_te.hcopy"
train_features_config_path = "config/train_features.txt"
test_features_config_path = "config/test_features.txt"

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
