import random
import nlpaug.augmenter.word as word_aug
import nlpaug.augmenter.char as char_aug
import os


class Augmenter(object):
    def __init__(self, force: int):
        self.force = force
        self.key_aug = char_aug.KeyboardAug(
            lang="fr",
            aug_char_min=1,
            aug_char_max=1,
            aug_word_min=self.force,
            aug_word_max=self.force,
            include_upper_case=True,
            model_path="keyboard/fr-mobile.json",
        )
        self.swap_aug = char_aug.RandomCharAug(
            action="swap",
            aug_char_min=1,
            aug_char_max=1,
            aug_word_min=self.force,
            aug_word_max=self.force,
        )
        self.bert_aug = word_aug.ContextualWordEmbsAug(
            model_path="camembert-base",
            action="substitute",
            aug_max=1,
        )

    def augment_keyboard(self, sentence: str):
        """Augment a given sentence by simulating keyboard typing mistakes.

        Args:
            sentence (str): Sentence to augment

        Returns:
            [str]: Augmented sentence
        """
        return self.key_aug.augment(sentence, n=1)

    def augment_letter(self, sentence: str):
        """Augment a given sentence by doubling letters.

        Args:
            sentence (str): Sentence to augment

        Returns:
            [str]: Augmented sentence
        """
        augmented_sentence = sentence
        for i in range(self.force):
            index = self._get_letter_index(augmented_sentence)
            augmented_sentence = f"{augmented_sentence[:index]}{augmented_sentence[index]}{augmented_sentence[index:]}"
        return augmented_sentence

    def delete_letter(self, sentence: str):
        """Augment a given sentence by deleting letters.

        Args:
            sentence (str): Sentence to augment

        Returns:
            [str]: Augmented sentence
        """
        augmented_sentence = sentence
        for i in range(self.force):
            if len(augmented_sentence) <= 1:
                break
            index = self._get_letter_index(augmented_sentence)
            augmented_sentence = (
                f"{augmented_sentence[:index]}{augmented_sentence[index+1:]}"
            )
        return augmented_sentence

    def swap_letter(self, sentence: str):
        """Augment a given sentence by swapping adjacent letters.

        Args:
            sentence (str): Sentence to augment

        Returns:
            [str]: Augmented sentence
        """
        return self.swap_aug.augment(sentence, n=1)

    def augment_bert(self, sentence: str):
        """Augment a given sentence by changing words by synonyms.

        Args:
            sentence (str): Sentence to augment

        Returns:
            [str]: Augmented sentence
        """
        augmented_sentence = sentence
        for i in range(self.force):
            augmented_sentence = self.bert_aug.augment(augmented_sentence, n=1)
        return augmented_sentence

    def _get_letter_index(self, sentence: str):
        """Get a random index for a sentence augmentation, making sur it's not a space.
        Args:
            sentence (str): Sentence where to find the letter to augment.

        Returns:
            [int]: Index of the letter to augment.
        """
        index = random.randint(0, len(sentence) - 1)
        while sentence[index] == " ":
            index = random.randint(0, len(sentence) - 1)
        return index