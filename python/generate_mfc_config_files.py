audio_file_train_count = 10 # I don't want all of them
audio_file_test_count = 5 # I don't want all of them
nim = 13519156
audio_source_path = "data/audios/"
audio_mfcc_train_path = "mfcc/audios/"
audio_mfcc_test_path = "mfcc_test/audios/"
train_map_config_path = "config/wav_mfc_train_map.hcopy"
test_map_config_path = "config/wav_mfc_test_map.hcopy"
train_features_config_path = "config/train_features.txt"
test_features_config_path = "config/test_features.txt"

print("Audio file train count:", audio_file_train_count)
print("Audio file test count:", audio_file_test_count)
print("NIM:", nim)
print("Audio source path:", audio_source_path)
print("Audio MFCC train path:", audio_mfcc_train_path)
print("Audio MFCC test path:", audio_mfcc_test_path)
print("Train map config path:", train_map_config_path)
print("Test map config path:", test_map_config_path)
print("Train features config path:", train_features_config_path)
print("Test features config path:", test_features_config_path)

basename_template = str(nim) + "_{:0>3}"

map_lines = []
features_lines = []
for audio_num in range(1, audio_file_train_count + 1):
    basename = basename_template.format(audio_num)
    mfc_filepath = "{}{}.mfc".format(audio_mfcc_train_path, basename)
    map_lines.append(
        "{}\t{}".format(
            "{}{}.wav".format(audio_source_path, basename),
            mfc_filepath,
        )
    )
    features_lines.append(mfc_filepath)

with open(train_map_config_path, mode="w") as file:
    file.write("\n".join(map_lines))

print("Train map done.")

with open(train_features_config_path, mode="w") as file:
    file.write("\n".join(features_lines))

print("Train features done.")

map_lines = []
features_lines = []
for audio_num in range(audio_file_train_count + 1, audio_file_train_count + audio_file_test_count + 1):
    basename = basename_template.format(audio_num)
    mfc_filepath = "{}{}.mfc".format(audio_mfcc_test_path, basename)
    map_lines.append(
        "{}\t{}".format(
            "{}{}.wav".format(audio_source_path, basename),
            mfc_filepath,
        )
    )
    features_lines.append(mfc_filepath)

with open(test_map_config_path, mode="w") as file:
    file.write("\n".join(map_lines))

print("Test map done.")

with open(test_features_config_path, mode="w") as file:
    file.write("\n".join(features_lines))

print("Test features done.")
