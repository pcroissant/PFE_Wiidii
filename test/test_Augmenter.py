import pytest
from src.Augmenter import Augmenter

class TestAugmenter(object):    
    def test_augment_keyboard(self):
        aug1 = Augmenter(1)
        aug2 = Augmenter(2)
        sentence = "Sylvanus le roi du NLP"
        augmented_sentence1 = aug1.augment_keyboard(sentence)
        augmented_sentence2 = aug2.augment_keyboard(sentence)
        
        assert len(augmented_sentence1) == len(sentence)
        assert len(augmented_sentence2) == len(sentence)
        assert augmented_sentence1 != sentence
        assert augmented_sentence2 != sentence
        # assert augmented_sentence1 != augmented_sentence2
    
    def test_augment_letter(self):
        aug1 = Augmenter(1)
        aug2 = Augmenter(2)
        sentence = "Sylvanus le roi du NLP"
        augmented_sentence1 = aug1.augment_letter(sentence)
        augmented_sentence2 = aug2.augment_letter(sentence)
        
        assert len(augmented_sentence1) == len(sentence)+1
        assert len(augmented_sentence2) == len(sentence)+2
        assert augmented_sentence1 != sentence
        assert augmented_sentence2 != sentence
        assert augmented_sentence1 != augmented_sentence2
    
    def test_delete_letter(self):
        aug1 = Augmenter(1)
        aug2 = Augmenter(2)
        sentence = "Sylvanus le roi du NLP"
        augmented_sentence1 = aug1.delete_letter(sentence)
        augmented_sentence2 = aug2.delete_letter(sentence)
        
        assert len(augmented_sentence1) == len(sentence)-1
        assert len(augmented_sentence2) == len(sentence)-2
        assert augmented_sentence1 != sentence
        assert augmented_sentence2 != sentence
        assert augmented_sentence1 != augmented_sentence2
        
        sentence = "?"
        augmented_sentence2 = aug2.delete_letter(sentence)
        
        assert len(augmented_sentence2) != 0
    
    def test_swap_letter(self):
        aug1 = Augmenter(1)
        aug2 = Augmenter(2)
        sentence = "Sylvanus le roi du NLP"
        augmented_sentence1 = aug1.swap_letter(sentence)
        augmented_sentence2 = aug2.swap_letter(sentence)
        
        assert len(augmented_sentence1) == len(sentence)
        assert len(augmented_sentence2) == len(sentence)
    
    # def test_augment_bert(self):
    #     aug1 = Augmenter(1)
    #     aug2 = Augmenter(2)
    #     sentence = "Sylvanus le roi du NLP"
    #     augmented_sentence1 = aug1.augment_bert(sentence)
    #     augmented_sentence2 = aug2.augment_bert(sentence)
    
    #     # assert len(augmented_sentence1) == len(sentence)
    #     # assert augmented_sentence1 != sentence
    #     # assert len(augmented_sentence2) == len(sentence)
    #     # assert augmented_sentence2 != sentence
    #     # assert augmented_sentence1 != augmented_sentence2