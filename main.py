#perform tokenisation and define a training function. 
def train_w2v(path,outpath):
    data=[i.strip() for i in open(path)]
    data=[i.split(" ") for i in data]
    import gensim
    w2v_model1 = gensim.models.Word2Vec(data, size=128, iter=10, min_count=0)
    word_vectors1 = w2v_model1.wv
    w2v_model1.save(outpath)
    w2v_model1=gensim.models.Word2Vec.load(outpath)
    return w2v_model1
w2v1=train_w2v("ccoha1.txt","w2v1")
w2v2=train_w2v("ccoha2.txt","w2v2")

#compute the cosine similarity of target words. 
import numpy as np
t1  = np.array([-0.4,0.8,0.5,-0.2,0.3])
t2  = np.array([-0.5,0.4,-0.2,0.7,-0.1])
def cos_sim(a, b):
    a_norm = np.linalg.norm(a)
    b_norm = np.linalg.norm(b)
    cos = np.dot(a,b)/(a_norm * b_norm)
    return abs(cos)
cos_sim(t1,t2)
targets=[i.strip() for i in open("targets.txt")]
sim=[]
for i in targets:
    sim.append(cos_sim(w2v1[i],w2v2[i]))

#create a csv file that stores the cosine similarity of the target words 
import pandas as pd
df=pd.DataFrame()
df["targets"]=targets
df["sim"]=sim
df.to_csv("targets.csv", header=True, encoding="utf-8-sig")
