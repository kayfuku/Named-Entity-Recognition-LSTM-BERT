import logging
from gensim.models.word2vec import Word2Vec, Text8Corpus

# Enable logging.
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# Read data.
sentences = Text8Corpus('data/ja.text8')

# Train the model using Skip-gram.
model = Word2Vec(sentences, size=100, window=5, sg=1)
# Save the model.
model.save('models/model.bin')

####################################################
# Load the model.
model = Word2Vec.load('models/model.bin')

# 1. Get the word embedding.
ret1 = model.wv['猫']
print(ret1)
# [ 0.02126932  0.15553345  0.10472752  0.82008636  0.323413    0.42847344
#  -0.05886601 -0.03228    -0.49861073 -0.13823172  0.15907998 -0.2955121
#   0.15381564  0.02959213  0.45588103  0.04573615  0.10711562 -0.7498988
#   0.34765413  0.5668533   0.0082125   0.40620092  0.1419684  -0.15594704
#   0.2681074  -0.00587511 -0.17240909 -0.04313468  0.01801641 -0.08588244
#  -0.26890314 -0.58127177 -0.29637957  0.09391042  0.26176983 -0.09310274
#  -0.05240794  0.4360441   0.25374362  0.2856923  -0.09161343 -0.34498295
#   0.4329259   0.14602754  0.03789869 -0.16791926 -0.4877344   0.17858095
#   0.4094406  -0.0850195  -0.11097047 -0.22874318  0.20079853 -0.22009209
#  -0.56010604 -0.04158428 -0.03335527  0.4060119   0.31657434 -0.1612
#   0.08173443  0.2883147  -0.30228382 -0.7308256   0.16244555  0.33739495
#  -0.14550932 -0.02320065  0.1271792   0.43317288 -0.05100935  0.18821165
#  -0.14499703 -0.29236516  0.11985569 -0.6816047  -0.02462544  0.7209334
#   0.08087783 -0.03078242 -0.3001637   0.09602924  0.15235683  0.02264104
#  -0.04015381 -0.36455423 -0.5682253   0.35639977 -0.2645092   0.25024158
#   0.50275826  0.2397867   0.8356371   0.3348727   0.2646383   0.05557086
#  -0.0079511   0.03706888  0.08052761 -0.525195  ]

# Check length.
ret1_2 = model.wv['猫'].shape
print(ret1_2)
# (100,)


# 2. Get the similar words in top n.
ret2 = model.wv.most_similar('猫', topn=10)
print(ret2)
# [('野良猫', 0.7546266317367554), ('キツネ', 0.7544845342636108), ('ネコ', 0.7441849708557129), ('金魚', 0.7353794574737549), ('カナリア', 0.729904055595398), ('小鳥', 0.71142578125), ('ブタ', 0.7062164545059204), ('ネズミ', 0.7058307528495789), ('オオカミ', 0.7054729461669922), ('鼠', 0.7021951675415039)]


# 3. Analogy task
# ex. '日本' - '東京' + 'ロンドン'
ret3_1 = model.wv.most_similar(positive=['ロンドン', '日本'], negative=['東京'], topn=10)
print(ret3_1)
# [('イギリス', 0.7595683336257935), ('アメリカ', 0.7407962083816528), ('ヨーロッパ', 0.7204920053482056), ('カナダ', 0.7148586511611938), ('英国', 0.7120566368103027), ('オーストラリア', 0.6913736462593079), ('フランス', 0.6864825487136841), ('米国', 0.6713947057723999), ('アルゼンチン', 0.6597831845283508), ('ベルギー', 0.6553279161453247)]

ret3_2 = model.wv.most_similar(positive=['ワシントン', '日本'], negative=['東京'], topn=10)
print(ret3_2)
# [('アメリカ合衆国', 0.6575483083724976), ('アメリカ', 0.6495521664619446), ('米国', 0.626446545124054), ('ジョージア', 0.5866668224334717), ('合衆国', 0.5859478712081909), ('ペンシルベニア', 0.5834273099899292), ('ニューイングランド', 0.5741814970970154), ('アルゼンチン', 0.5693699717521667), ('南アフリカ', 0.5657532811164856), ('北米', 0.5657497048377991)]


# 4. Get the similarity between words.
ret4_1 = model.wv.similarity('猫', '犬') # 0.63878644
print(ret4_1)
ret4_2 = model.wv.similarity('猫', '車') # 0.08373636
print(ret4_2)
ret4_3 = model.wv.similarity('セダン', '車') # 0.7132833
print(ret4_3)





























