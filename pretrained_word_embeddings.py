import gensim

# Read pre-trained word embeddings.
# model = gensim.models.KeyedVectors.load_word2vec_format('data/cc.ja.300.vec.gz', binary=False)
model = gensim.models.KeyedVectors.load_word2vec_format('data/cc.en.300.vec.gz', binary=False)


# Use it.
# ret1 = model.wv['猫']
ret1 = model.wv['King']
print(ret1)
# King
# [-0.0892  0.0395  0.0448 -0.0021  0.0367  0.0526 -0.1426 -0.0045 -0.0738
#  -0.0062 -0.0702 -0.11   -0.2031  0.0226 -0.1347  0.0482  0.0522 -0.0148
#  ...
#  -0.0258 -0.0461 -0.0376 -0.0542  0.1013 -0.0501  0.0817  0.1088 -0.156
#   0.1637 -0.0274  0.0441]
ret2 = model.wv['Queen']
print(ret2)
ret3 = model.wv['Man']
print(ret3)
ret4 = model.wv['Woman']
print(ret4)




# 猫
# [-2.618e-01 -7.520e-02 -1.930e-02  2.088e-01 -3.005e-01  1.936e-01
#  -1.561e-01 -3.540e-02  1.220e-01  2.718e-01  7.460e-02  1.356e-01
#   ...
#  -1.062e-01  3.230e-02 -2.380e-02  1.860e-02 -2.750e-02 -1.900e-01]

# ret2 = model.most_similar('猫', topn=10)
# print(ret2)
# [('ネコ', 0.8059154748916626), ('ねこ', 0.7272597551345825), ('子猫', 0.720253586769104), ('仔猫', 0.706268846988678), ('ニャンコ', 0.7058037519454956), ('野良猫', 0.7030350565910339), ('犬', 0.6505385637283325), ('ミケ', 0.6356303691864014), ('野良ねこ', 0.6340526342391968), ('飼猫', 0.6265145540237427)]



#
# # Evaluate the word embeddings model.
# from gensim.test.utils import datapath
#
# # Only for English language data.
# # 1. human-judged
# ret1 = model.evaluate_word_pairs(datapath('wordsim353.tsv'))
# # 2. analogy task
# ret2 = model.accuracy(datapath('questions-words.txt'))




