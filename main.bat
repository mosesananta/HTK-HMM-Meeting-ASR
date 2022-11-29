:: Tutorial - Step 1.d
py python/step_1_d_generate_lexicon.py

:: Tutorial - Step 1.e
py python/step_1_e_generate_wordlist.py

:: Tutorial - Step 2.b
py python/step_2_b_generate_train_test_config.py

:: Tutorial - Step 2.c
py python/step_2_c_generate_train_test_features.py

:: Tutorial - Step 2.d
mkdir hmms\hmm.0
mkdir hmms\hmm.1
mkdir hmms\hmm.2
mkdir hmms\hmm.3

:: Tutorial - Step 3.a
HParse data/grammar.txt output/wdnet.slf

:: Tutorial - Step 3.b
HDMan -m -w data\wordlist.txt -n output\monophones1 -l output\dlog output\dict data\lexicon.lex

:: Tutorial - Step 3.c
py python/step_3_c_modify_dict.py

:: Tutorial - Step 3.d
py python/step_3_d_modify_monophones1.py

:: Tutorial - Step 3.e
py python/step_3_e_generate_words_mlf.py
HLEd -l * -d output/dict -i output/phones0.mlf mkphones0.led words_train.mlf

:: Tutorial - Step 3.f
HCopy -T 1 -C config/config_feature.hcopy -S config/script_tr.hcopy

:: Tutorial - Step 3.g
HCompV -C config\config_train.hcopy -f 0.01 -m -S config\train_features.txt -M hmms\hmm.0 config\proto

:: Tutorial - Step 3.h
py python/step_3_h_generate_monophones0.py

:: Tutorial - Step 3.i
py python/step_3_i_generate_hmmdefs.py

:: Tutorial - Step 3.j
py python/step_3_j_generate_macros.py

:: Tutorial - Step 3.k
HERest -C config\config_train.hcopy -I output\phones0.mlf -t 250.0 150.0 1000.0 -S config\train_features.txt -H hmms\hmm.0\macros -H hmms\hmm.0\hmmdefs -M hmms\hmm.1 monophones0
HERest -C config\config_train.hcopy -I output\phones0.mlf -t 250.0 150.0 1000.0 -S config\train_features.txt -H hmms\hmm.1\macros -H hmms\hmm.1\hmmdefs -M hmms\hmm.2 monophones0
HERest -C config\config_train.hcopy -I output\phones0.mlf -t 250.0 150.0 1000.0 -S config\train_features.txt -H hmms\hmm.2\macros -H hmms\hmm.2\hmmdefs -M hmms\hmm.3 monophones0

:: Tutorial - Step 3.l dst.
echo Lanjutkan secara manual untuk step 3.l. Sudah capek. ._.
