Dapatkan monofon:
`HDMan -m -w data\wordlist.txt -n output\monophones1 -l output\dlog output\dict data\lexicons\13519156.txt`

Jika ada eror seperti ini:
```
  ERROR [+8050]  ReadDict: Phone or outsym expected in word yang
  ERROR [+1413]  ReadNextWord: ReadDictWord failed
 FATAL ERROR - Terminating program HDMan
```

tambahkan _newline_ pada leksikon.

---

Dapatkan MFCC:
`HCopy -T 1 -C config/feature_extraction.hcopy -S config/wav_mfc_train_map.hcopy`

Dapatkan proto:
`HCompV -C config\model_train.hcopy -f 0.01 -m -S config\train_features.txt -M hmms\hmm.0 config\proto`

Dapatkan hmm1:
`HERest -C config\model_train.hcopy -I output\phones0.mlf -t 250.0 150.0 1000.0 -S config\train_features.txt -H hmms\hmm.0\macros -H hmms\hmm.0\hmmdefs -M hmms\hmm.1 output\monophones0`

Kalau `HHEd` sudah dilakukan, lanjut pakai `HERest`.

Kita pakai monophones1 untuk HERest. (22/11/2022)