import math

def getDCG(rels):
    dcg = rels[0]
    i = 2
    for rel in rels[1:]:
        dcg = dcg + pow(2, rel) / math.log(i,2)
        i = i + 1
    return dcg

def getIDCG(rels):
    rels.sort()
    rels.reverse()
    return getDCG(rels)

def computing(scores):
    # scores = [4,2,4,2,2]
    dcg = getDCG(scores)
    # print(dcg)
    idcg = getIDCG(scores)
    # print(idcg)
    # print(dcg/idcg)
    return dcg/idcg