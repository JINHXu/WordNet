#!/usr/bin/env/python3

import unittest

from wordnet import WordNet


class TestWordNet(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.wn = WordNet("data/synsets.txt", "data/hypernyms.txt")

    def test_size(self):
        self.assertEqual(len(self.wn), 82115)

    def test_synsets(self):
        bank_synsets = self.wn.get_synsets("bank")
        self.assertEqual(len(bank_synsets), 10)

    def test_iter(self):
        all_syns = set()
        for syn in self.wn:
            all_syns.add(syn)
        self.assertEqual(len(all_syns), 82115)

    def test_paths_to_root_count(self):
        dog_synsets = self.wn.get_synsets("dog")

        domestic_dog = next(
            syn for syn in dog_synsets if "domestic_dog" in syn.name)

        paths = self.wn.paths_to_root(domestic_dog)

        self.assertEqual(len(paths), 2)

    def test_paths_to_root_length(self):
        cat_synsets = self.wn.get_synsets("cat")

        domestic_cat = next(
            syn for syn in cat_synsets if "true_cat" in syn.name)

        paths = self.wn.paths_to_root(domestic_cat)

        self.assertEqual(len(paths), 1)
        self.assertEqual(len(paths[0]), 13)

    def test_lowest_common_hypernym(self):
        dog_synsets = self.wn.get_synsets("dog")
        domestic_dog = next(
            syn for syn in dog_synsets if "domestic_dog" in syn.name)

        cat_synsets = self.wn.get_synsets("cat")
        domestic_cat = next(
            syn for syn in cat_synsets if "true_cat" in syn.name)

        hyp = self.wn.lowest_common_hypernyms(domestic_dog, domestic_cat)

        self.assertEqual(len(hyp), 1)

        # [27618] carnivore: a terrestrial or aquatic flesh-eating mammal
        self.assertEqual(len(hyp), 1)
        self.assertEqual(next(iter(hyp)).index, 27618)

    def test_distance(self):
        dog_synsets = self.wn.get_synsets("dog")
        domestic_dog = next(
            syn for syn in dog_synsets if "domestic_dog" in syn.name)

        cat_synsets = self.wn.get_synsets("cat")
        domestic_cat = next(
            syn for syn in cat_synsets if "true_cat" in syn.name)

        distance = self.wn.distance(domestic_dog, domestic_cat)
        self.assertEqual(distance, 4)


"""

    def test_lch_similarity(self):
        dog_synsets = self.wn.get_synsets("dog")
        domestic_dog = next(syn for syn in dog_synsets if "domestic_dog" in syn.name)
        
        cat_synsets = self.wn.get_synsets("cat")
        domestic_cat = next(syn for syn in cat_synsets if "true_cat" in syn.name)

        lch_similarity = self.wn.lch_similarity(domestic_dog, domestic_cat)

        self.assertAlmostEqual(lch_similarity, 2.028148247)                
    
    def test_noun_lowest_common_hypernyms(self):
        lowest_common_hypernyms = self.wn.noun_lowest_common_hypernyms("dog", "horse")

        #[61107] placental placental_mammal eutherian eutherian_mammal: mammals having a placenta; all mammals except monotremes and marsupials
        self.assertEqual(len(lowest_common_hypernyms), 1)
        self.assertEqual(next(iter(lowest_common_hypernyms)).index, 61107)
"""
