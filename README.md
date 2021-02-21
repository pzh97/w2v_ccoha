# w2v_ccoha

Please go to https://drive.google.com/drive/folders/1OgsciwSfPR_LJAB_JTypmabBujiTUv1q?usp=sharing to download the corpora used in this project. This folder contains two corpora, which are two extracts from the Corpus of Historical American English. The period of ccoha1.txt spans from 1810 to 1860 while that of ccoha.txt spans from 1960 to 2010. These two corpora have been cleaned (i.e. lemmatised, lowercased and punctuation-free). Additionally, there is a targets.txt file contained in this folder, which incldes a list of words to be detected for lexical semantic change. 

The output of main.py is a .csv file, which includes the cosine similarity of the same word from these two different corpora. The trained vectors of these two corpora will also be outputed in the .npy files.

The training time is roughly three minutes. And the results may vary because each time you run the code, it trains the vectors from the scratch. If you want to the results (i.e. cosine similarity) to be consistent, please place a hashtag in the beginning of the code in line 8.

```
line 8: #w2v_model1.save(outpath)
```
