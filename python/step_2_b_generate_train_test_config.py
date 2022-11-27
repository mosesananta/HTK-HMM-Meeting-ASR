import os
import random

random.seed(120) # For reproducibility

nims = [
    13519062,
    # 13519076, (sedang diperbaiki lexicon-nya)
    # 13519088, (sedang diperbaiki lexicon-nya)
    13519128,
    13519156,
]
audio_list_dir = "data/audios/"
audio_mfcc_train_dir = "mfcc/"
audio_mfcc_test_dir = "mfcc_test/"
train_map_config_path = "config/script_tr.hcopy"
test_map_config_path = "config/script_te.hcopy"
ignored_audio_filename_list_path = "data/ignored_audios.txt"

audio_filename_list = []
str_nims = [str(nim) for nim in nims]
for filename in os.listdir(audio_list_dir):
    if any([filename.startswith(str_nim) for str_nim in str_nims]):
        audio_path = os.path.join(audio_list_dir, filename)
        audio_filename_list.append(filename)
    # else: filename with unregistered NIM will be skipped

with open(ignored_audio_filename_list_path, mode="r") as file:
    raw_data = file.read()

ignored_audio_filename_list = raw_data.split("\n")
if ignored_audio_filename_list[-1] == "": # Last line is empty
    ignored_audio_filename_list = ignored_audio_filename_list[:-1]

audio_filename_list = list(filter(
    lambda x: x not in ignored_audio_filename_list,
    audio_filename_list
))

train_proportion = 0.8
split_index = round(len(audio_filename_list) * train_proportion)

random.shuffle(audio_filename_list)
train_audio_filename_list = audio_filename_list[:split_index]
test_audio_filename_list = audio_filename_list[split_index:]
train_audio_filename_list.sort()
test_audio_filename_list.sort()

map_lines = []
#features_lines = []
for filename in train_audio_filename_list:
    basename = filename.split(".")[0]
    mfc_filepath = "{}{}.mfc".format(audio_mfcc_train_dir, basename)
    map_lines.append(
        "{}\t{}".format(
            "{}{}.wav".format(audio_list_dir, basename),
            mfc_filepath,
        )
    )
    #features_lines.append(mfc_filepath)

with open(train_map_config_path, mode="w") as file:
    file.write("\n".join(map_lines))

# with open(train_features_config_path, mode="w") as file:
#     file.write("\n".join(features_lines))

map_lines = []
# features_lines = []

for filename in test_audio_filename_list:
    basename = filename.split(".")[0]
    mfc_filepath = "{}{}.mfc".format(audio_mfcc_test_dir, basename)
    map_lines.append(
        "{}\t{}".format(
            "{}{}.wav".format(audio_list_dir, basename),
            mfc_filepath,
        )
    )
    #features_lines.append(mfc_filepath)

with open(test_map_config_path, mode="w") as file:
    file.write("\n".join(map_lines))

# with open(test_features_config_path, mode="w") as file:
#     file.write("\n".join(features_lines))
