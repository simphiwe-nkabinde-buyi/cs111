from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["two", "some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners


def test_get_noun():

    single_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    for _ in range(len(single_nouns)):
        noun = get_noun(1)
        assert noun in single_nouns

    plural_nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    for _ in range(len(plural_nouns)):
        noun = get_noun(2)
        assert noun in plural_nouns

def test_get_verb():

    past_verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    for _ in range(len(past_verbs)):
        verb = get_verb(1, 'past')
        assert verb in past_verbs

    single_present_verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(len(single_present_verbs)):
        verb = get_verb(1, 'present')
        assert verb in single_present_verbs

    plural_present_verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    for _ in range(len(plural_present_verbs)):
        verb = get_verb(2, 'present')
        assert verb in plural_present_verbs

    future_verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    for _ in range(len(future_verbs)):
        verb = get_verb(2, 'future')
        assert verb in future_verbs

def test_get_preposition():
    prepositions = [
        "about", "above", "across", "after", "along", "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"
    ]

    for _ in range(len(prepositions)):
        preposition = get_preposition()
        assert preposition in prepositions

def test_get_prepositional_phrase():

    prepos_phrase = get_prepositional_phrase(1)
    phrase_words_list = prepos_phrase.split()
    assert len(phrase_words_list) == 3

    # 1. test prepostion
    prepositions = [
        "about", "above", "across", "after", "along", "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"
    ]

    for _ in range(len(prepositions)):
        preposition = phrase_words_list[0]
        assert preposition in prepositions

    #2. test determiner
    determiners = ["a", "one", "the", "two", "some", "many", "the"]
    for _ in range(len(determiners)):
        determiner = phrase_words_list[1]
        assert determiner in determiners
    
    #3. test noun
    nouns = [
        "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman", "birds", 
        "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"
    ]
    for _ in range(len(nouns)):
        noun = phrase_words_list[2]
        assert noun in nouns


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])