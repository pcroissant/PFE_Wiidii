#IMPORTS

import json
import requests
import numpy as np
from tqdm import trange
import os

#NLPAUG IMPORTS
import nlpaug.augmenter.char as char_aug
import nlpaug.augmenter.word as naw

#LOAD DATASET
with open("dataset.json", "r") as dataset_file:
   dataset = json.load(dataset_file)


#PARAMS
NUMBER_OF_AUG = 2
dataset_aug = {}

#INITIALIZE AUGMENTERS
#key_aug = char_aug.KeyboardAug(lang="fr",aug_char_min=1, aug_char_max=2,aug_word_min=1,aug_word_max=2,model_path="keyboard/fr.json")
word_aug = naw.ContextualWordEmbsAug(model_path='camembert-base', action="substitute")
#word_aug = naw.ContextualWordEmbsAug(model_path='bert-base-multilingual-cased', action="substitute")

#DATA AUGMENTATION
for i in trange(len(dataset)):
    dataset_aug[i] = dataset[i]
    sentence = dataset[i].get("sentence")
    #keyboard_aug = key_aug.augment(sentence, n= NUMBER_OF_AUG) #param int n: Default is 1. Number of unique augmented output.
    wordswap_aug = augmented_text_word = word_aug.augment(sentence, n= NUMBER_OF_AUG)

    #dataset_aug[i]["keyboard_aug"] = keyboard_aug
    dataset_aug[i]["wordswap_aug"] = wordswap_aug


#SAVE AUGMENTED DATASET
with open("dataset_aug_typos_words.json", "w") as dataset_aug_file:
    json.dump(dataset, dataset_aug_file, ensure_ascii=False)