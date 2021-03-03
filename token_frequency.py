import nltk

#define a function that tokenises corpora
def tokenise(corpus):
	with open(corpus) as myfile:
		data = myfile.read().replace('\n', ' ')
	corpus = data.split(' ')
	return corpus

#define a function that counts the token numbers of corpora
def count(data):
    data = tokenise(data)
    fdist1 = nltk.FreqDist(data)
    return print(fdist1.N())
count('ccoha1.txt')
count('ccoha2.txt')

#define a function that counts the token frequencies of a list of target words
def countvoc(corpus, targets):
    corpus = tokenise(corpus)
    fdist1 = nltk.FreqDist(corpus)
    targets=[i.strip() for i in open("targets.txt")]
    freq=[]
    for i in targets:
        freq.append(fdist1[i])
    return freq
print(countvoc('ccoha1.txt', 'targets.txt'))
print(countvoc('ccoha2.txt', 'targets.txt'))
