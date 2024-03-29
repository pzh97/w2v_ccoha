# w2v_ccoha

1. Please go to https://drive.google.com/drive/folders/1OgsciwSfPR_LJAB_JTypmabBujiTUv1q?usp=sharing to download the corpora used in this project. This folder contains two corpora, which are two extracts from the *Corpus of Historical American English*. The period of `ccoha1.txt` spans from 1810 to 1860 while that of `ccoha2.txt` spans from 1960 to 2010. These two corpora have been cleaned (i.e. lemmatised, lowercased and punctuation-free). Therefore, it is unnecessary to perform any types of pre-processing. I personally did not remove the stop words either. Additionally, there is a `targets.txt` file contained in this folder, which incldes a list of words to be detected for lexical semantic change. The code that performs matrix alignment was ported from [quadrismegistus's page](https://gist.github.com/quadrismegistus/09a93e219a6ffc4f216fb85235535faf).

2. The output of `main.py` is a `.csv` file, which includes the cosine similarity of the same word from these two different corpora. The trained vectors of these two corpora will also be outputed in the `.npy` files.

3. The training process takes roughly *thirty minutes*. To run the `main.py`, please put `ccoha1.txt`, `ccoha2.txt` and `targets.txt` with the `main.py` in the same folder. **One Caveat**: the results may vary because each time you run the code, it trains the vectors from the scratch. 

4. The word frequency file should be run separately. It first POS-tags all the word in the corpora. Then, it will count the number of words. 

5. Statistical analysis is conducted by using the .R extension file.  
