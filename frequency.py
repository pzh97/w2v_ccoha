#pos-tag the whole corpora
import nltk
def get_pos(text='And now for something completely different'):
    text=" ".join([i.split("_")[0] for i in text.split(" ") ])
    words = nltk.word_tokenize(text)
    # print(words)
    word_tag = nltk.pos_tag(words)
    return " ".join([i[0]+"_"+i[1] for i in word_tag])
get_pos()

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
    
frequency("ccoha1.txt",d_word,"frequency1.txt")
frequency("ccoha2.txt",d_word,"frequency2.txt")
