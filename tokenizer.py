import tensorflow as tf

texts = ["It's sunny today."]

# Create vocabulary.
# num_words: max size of vocabulary.
tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=10, oov_token='<UNK>')
tokenizer.fit_on_texts(texts)

# Word-index dictionary.
ret1 = tokenizer.word_index
print(ret1)
# {'<UNK>': 1, "it's": 2, 'sunny': 3, 'today': 4}

# Index-word dictionary.
ret2 = tokenizer.index_word
print(ret2)
# {1: '<UNK>', 2: "it's", 3: 'sunny', 4: 'today'}

# Convert texts to sequence of ids.
ret3 = tokenizer.texts_to_sequences(texts)
print(ret3)
# [[2, 3, 4]]











