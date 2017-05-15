import data_utils

'''
print(data_utils.basic_tokenizer(b"COc1 ccc c ( N C(EO) OC (C) (C) C)c1 I"))
print("=========================")
print(data_utils.simple_tokenizer(b"COc1 ccc c ( N C(EO) OC (C) (C) C)c1 I"))
'''


data_utils.prepare_data_test("./Vocabulary", "./Corpus/sourceCorpusSegmented.txt", "./Corpus/targetCorpusSegmented.txt", "./Corpus/devSourceCorpusSegmented.txt", "./Corpus/devTargetCorpusSegmented.txt", 40000, 40000)
