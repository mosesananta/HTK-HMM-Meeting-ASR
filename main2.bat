:: Tutorial - Step 3.l.2
mkdir hmms\hmm.5
mkdir hmms\hmm.6
mkdir hmms\hmm.7
HHEd -H hmms\hmm.4\macros -H hmms\hmm.4\hmmdefs -M hmms\hmm.5 config\sil.hed output\monophones1
HERest -C config\config_train.hcopy -I output\phones0.mlf -t 250.0 150.0 1000.0 -S config\train_features.txt -H hmms\hmm.5\macros -H hmms\hmm.5\hmmdefs -M hmms\hmm.6 output\monophones1
HERest -C config\config_train.hcopy -I output\phones0.mlf -t 250.0 150.0 1000.0 -S config\train_features.txt -H hmms\hmm.6\macros -H hmms\hmm.6\hmmdefs -M hmms\hmm.7 output\monophones1

:: Tutorial - Step 3.m
HVite -A -D -T 1 -l * -o SWT -b SENT-END -C config\config_train.hcopy -a -H hmms\hmm.7\macros -H hmms\hmm.7\hmmdefs -i output\aligned.mlf -m -t 250.0 150.0 1000.0 -y lab -I words.mlf -S config\train_features.txt output\dict output\monophones1 > log\HVite_log

mkdir hmms\hmm.8
mkdir hmms\hmm.9
HERest -C config\config_train.hcopy -I output\aligned.mlf -t 250.0 150.0 1000.0 -S config\train_features.txt -H hmms\hmm.7\macros -H hmms\hmm.7\hmmdefs -M hmms\hmm.8 output\monophones1
HERest -C config\config_train.hcopy -I output\aligned.mlf -t 250.0 150.0 1000.0 -S config\train_features.txt -H hmms\hmm.8\macros -H hmms\hmm.8\hmmdefs -M hmms\hmm.9 output\monophones1

:: HTKBook - 3.3.1
HLEd -n triphones1 -l * -i wintri.mlf mktri.led output\aligned.mlf

mkdir hmms\hmm.10
perl maketrihed.pl output\monophones1 triphones1
HHEd -B -H hmms\hmm.9\macros -H hmms\hmm.9\hmmdefs -M hmms\hmm.10 mktri.hed output\monophones1

mkdir hmms\hmm.11
mkdir hmms\hmm.12
HERest -B -C config\config_train.hcopy -I wintri.mlf -t 250.0 150.0 1000.0 -s stats -S config\train_features.txt -H hmms\hmm.10\macros -H hmms\hmm.10\hmmdefs -M hmms\hmm.11 triphones1

HERest -B -C config\config_train.hcopy -I wintri.mlf -t 250.0 150.0 1000.0 -s stats -S config\train_features.txt -H hmms\hmm.11\macros -H hmms\hmm.11\hmmdefs -M hmms\hmm.12 triphones1

:: HTKBook - 3.3.2
mkdir hmms\hmm.13

:: This where we stuck.
HHEd -B -H hmms\hmm.12\macros -H hmms\hmm.12\hmmdefs -M hmms\hmm.13 tree.hed triphones1 > log_file
