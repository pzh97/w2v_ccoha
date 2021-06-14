#pos-tag the whole corpora
import nltk
def get_pos(text='And now for something completely different'):
    text=" ".join([i.split("_")[0] for i in text.split(" ") ])
    words = nltk.word_tokenize(text)
    # print(words)
    word_tag = nltk.pos_tag(words)
    return " ".join([i[0]+"_"+i[1] for i in word_tag])
get_pos()

#train word embeddings with pos taggers
def train_w2v(path,outpath):
    data=[i.strip() for i in open(path)]
    data=[get_pos(i.strip()) for i in data]
    data=[i.split(" ") for i in data]
    import gensim
    w2v_model1 = gensim.models.Word2Vec(data, size=300, window=8, iter=10, min_count=0, negative=20)
    word_vectors1 = w2v_model1.wv
    w2v_model1.save(outpath)
    w2v_model1=gensim.models.Word2Vec.load(outpath)
    return w2v_model1

w2v1=train_w2v("ccoha1.txt","w2v1")
w2v2=train_w2v("ccoha2.txt","w2v2")

#get all the words in the corpora
import pandas as pd
df=pd.DataFrame()
df["w2v1"]=w2v1.wv.index2word
df.to_csv("res1.csv",header=True,index=False,encoding="utf-8-sig")
df=pd.DataFrame()
df["w2v2"]=w2v2.wv.index2word
df.to_csv("res2.csv",header=True,index=False,encoding="utf-8-sig")
# word=[i.strip().split("_")[0] for i in open("targets.txt")]
word=[i.strip() for i in open("targets.txt")]
d_word={}
for i in word:
    d_word[i]=0


#get frequency
def frequency(path,d_word,outpath):
    import copy
    tmpd_word=copy.deepcopy(d_word)
    data=[i.strip() for i in open(path)]
    data=[get_pos(i.strip()) for i in data]
    data=[i.split(" ") for i in data]
    for i in data:
        for j in i:
            if j in tmpd_word:
                tmpd_word[j]+=1
    tmpd_word=sorted(tmpd_word.items(),key=lambda x:x[1],reverse=True)
    with open(outpath,"w",encoding="utf-8") as w:
        for i in tmpd_word:
               w.write(str(i[0])+" "+str(i[1])+"\n")
    
frequency("ccoha1.txt",d_word,"cipin1.txt")

frequency("ccoha2.txt",d_word,"cipin2.txt")



