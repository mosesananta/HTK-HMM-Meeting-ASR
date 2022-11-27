Keterangan berkas `feature_extraction.hcopy`:
`SOURCERATE`: Periode sampel asal dalam satuan 100 ns (sekitar 1 / sample-rate(16000))
`TARGETKIND`: `0`: power, `D`: delta, `A`: accel
-   Mengapa bisa accel?
`TARGETRATE`: Satuannya 100 ns.
`WINDOWSIZE`: Satuannya 100 ns.
`NUMCHAINS`: Ukuran filterbank.

Keterangan berkas `model_train.hcopy`:
Itu sebenarnya hampir sama dengan `feature_extraction.hcopy`. Perbedaannya terdapat pada dua baris pertama dalam berkas `feature_extraction.hcopy` yang tidak ada pada `model_train.hcopy`.