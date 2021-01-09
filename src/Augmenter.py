import random
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

    # TODO: add BERT augmentation


# TODO: delete this test
# aug = Augmenter(force=1)
# sentence = "salut comment tu vas mon pote"
# keyaug_sentence = aug.augment_keyboard(sentence)
# letteraug_sentence = aug.augment_letter(sentence)
# letterdel_sentence = aug.delete_letter(sentence)
# letterswap_sentence = aug.swap_letter(sentence)
# print(
#     f"{sentence} -> sentence \n{keyaug_sentence} -> key_aug \n{letteraug_sentence} -> letter_aug \n{letterdel_sentence} -> letter_del\n{letterswap_sentence} -> letter_swap"
# )
