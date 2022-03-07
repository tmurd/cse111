from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase, get_adjective
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

        # Get a random number between 2 and 10 inclusive.
        quantity = random.randint(2, 11)

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(quantity)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    # 1. Test the single verb.

    single_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_noun function which
        # should return a single noun.
        word = get_noun(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_nouns

    # 2. Test the plural verbs.

    plural_nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Get a random number between 2 and 10 inclusive.
        quantity = random.randint(2, 11)

        # Call the get_noun function which
        # should return a plural noun.
        word = get_noun(quantity)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_nouns

def test_get_verb():
    # 1. Test the past tense verb.

    past_verb = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Get a random number between 1 and 10 inclusive.
        quantity = random.randint(1, 11)

        # Get "past" tense to test.
        tense = "past"

        # Call the get_verb function which
        # should return a past verb.
        word = get_verb(quantity, tense)

        # Verify that the word returned from get_verb
        # is one of the words in the past_verb list.
        assert word in past_verb

    # 2. Test the single, present tense verb.

    single_present_verb = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Use quantity '1' to test single_present_verb
        quantity = 1

        # Get "present" tense to test.
        tense = "present"

        # Call the get_verb function which
        # should return a single, present tense verb.
        word = get_verb(quantity, tense)

        # Verify that the word returned from get_verb
        # is one of the words in the single_present_verb list.
        assert word in single_present_verb

    # 3. Test the plural, present tense verb.

    plural_present_verb = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Get a random number between 2 and 10 inclusive.
        quantity = random.randint(2, 11)

        # Get a "present" tense to test.
        tense = "present"

        # Call the get_verb function which
        # should return a single, present tense verb.
        word = get_verb(quantity, tense)

        # Verify that the word returned from get_verb
        # is one of the words in the plural_present_verb list.
        assert word in plural_present_verb

    # 4. Test the future tense verb.

    future_verb = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Get a random number between 1 and 10 inclusive.
        quantity = random.randint(1, 11)

        # Get "future" tense to test.
        tense = "future"

        # Call the get_verb function which
        # should return a future verb.
        word = get_verb(quantity, tense)

        # Verify that the word returned from get_verb
        # is one of the words in the future_verb list.
        assert word in future_verb

def test_get_preposition():
    # 1. Test the preposition words.

    preposition_words = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(8):

        # Call the get_preposition function which
        # should return a preposition.
        word = get_preposition()

        # Verify that the word returned from get_prepositon
        # is one of the words in the prepositon list.
        assert word in preposition_words

def test_get_prepositional_phrase():

    # Get a random number between 1 and 10 inclusive.
    quantity = random.randint(1, 11)

    # Call get_prepostional_phrase function
    phrase = get_prepositional_phrase(quantity)

    # Split the phrase at each space (" ")
    words = phrase.split(" ")

    # Make sure there are 3 words in the phrase
    assert len(words) == 3

    # Import possible prepositions
    prepositions = ["about", "above", "across", "after", "along",
    "around", "at", "before", "behind", "below",
    "beyond", "by", "despite", "except", "for",
    "from", "in", "into", "near", "of",
    "off", "on", "onto", "out", "over",
    "past", "to", "under", "with", "without"]

    # Import possible determiners based on singular or plural
    if quantity == 1:
        determiners = ["a", "one", "the"]
    else:
        determiners = ["two", "some", "many", "the"]

    # Import possible nouns based on singular or plural
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    
    # Make sure correct type of word shows up in the correct place in the phrase
    assert words[0] in prepositions
    assert words[1] in determiners
    assert words[2] in nouns

def test_get_adjective():
    # 1. Test the adjective words.

    adjective_words = ["weird", "funny", "blue", "humorous",
            "jolly", "cute", "pretty", "ugly", "smart",
            "intresting", "awkward", "playful", "dirty"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(8):

        # Call the get_adjective function which
        # should return a adjective.
        word = get_adjective()

        # Verify that the word returned from get_adjective
        # is one of the words in the adjective list.
        assert word in adjective_words



# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])