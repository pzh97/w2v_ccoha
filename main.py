import gensim
import numpy as np
import pandas as pd

#define a training function
def train_w2v(path,outpath):
    data=[i.strip() for i in open(path)]
    data=[i.split(" ") for i in data]
    w2v_model1 = gensim.models.Word2Vec(data, size=300, window = 8, iter=10, min_count=0, negative = 20)
    word_vectors1 = w2v_model1.wv
    w2v_model1.save(outpath)
    w2v_model1=gensim.models.Word2Vec.load(outpath)
    return w2v_model1
w2v1=train_w2v("ccoha1.txt","w2v1")
w2v2=train_w2v("ccoha2.txt","w2v2")

#perform orthogonal procrustes to align matrices
def smart_procrustes_align_gensim(base_embed, other_embed, words=None):
    
    base_embed.init_sims()
    other_embed.init_sims()

    # make sure vocabulary and indices are aligned
    in_base_embed, in_other_embed = intersection_align_gensim(base_embed, other_embed, words=words)

    # get the embedding matrices
    base_vecs = in_base_embed.wv.syn0norm
    other_vecs = in_other_embed.wv.syn0norm

    # just a matrix dot product with numpy
    m = other_vecs.T.dot(base_vecs) 
    # SVD method from numpy
    u, _, v = np.linalg.svd(m)
    # another matrix operation
    ortho = u.dot(v) 
    # Replace original array with modified one
    # i.e. multiplying the embedding matrix (syn0norm)by "ortho"
    other_embed.wv.syn0norm = other_embed.wv.syn0 = (other_embed.wv.syn0norm).dot(ortho)
    return other_embed
    
def intersection_align_gensim(m1,m2, words=None):
    # Get the vocab for each model
    vocab_m1 = set(m1.wv.vocab.keys())
    vocab_m2 = set(m2.wv.vocab.keys())

    # Find the common vocabulary
    common_vocab = vocab_m1&vocab_m2
    if words: common_vocab&=set(words)

    # If no alignment necessary because vocab is identical...
    if not vocab_m1-common_vocab and not vocab_m2-common_vocab:
        return (m1,m2)

    # Otherwise sort by frequency (summed for both)
    common_vocab = list(common_vocab)
    common_vocab.sort(key=lambda w: m1.wv.vocab[w].count + m2.wv.vocab[w].count,reverse=True)

    # Then for each model...
    for m in [m1,m2]:
        # Replace old syn0norm array with new one (with common vocab)
        indices = [m.wv.vocab[w].index for w in common_vocab]
        old_arr = m.wv.syn0norm
        new_arr = np.array([old_arr[index] for index in indices])
        m.wv.syn0norm = m.wv.syn0 = new_arr

        # Replace old vocab dictionary with new one (with common vocab)
        # and old index2word with new one
        m.wv.index2word = common_vocab
        old_vocab = m.wv.vocab
        new_vocab = {}
        for new_index,word in enumerate(common_vocab):
            old_vocab_obj=old_vocab[word]
            new_vocab[word] = gensim.models.word2vec.Vocab(index=new_index, count=old_vocab_obj.count)
        m.wv.vocab = new_vocab
     return (m1,m2)

from gensim.models import Word2Vec
model_1 = Word2Vec.load("w2v1")
model_2 = Word2Vec.load("w2v2")
smart_procrustes_align_gensim(model_1, model_2, words=None)

#compute the cosine similarity of target words
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
    sim.append(cos_sim(model_1[i], model_2[i]))

#create a csv file that stores the cosine similarity of the target words 
df=pd.DataFrame()
df["targets"]=targets
df["sim"]=sim
df.to_csv("targets.csv", header=True, encoding="utf-8-sig")
