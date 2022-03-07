from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_makes_full_name():
    assert make_full_name("Anna", "Harrison") == "Harrison; Anna"
    assert make_full_name("Eva", "Hamill-Thomas") == "Hamill-Thomas; Eva"
    assert make_full_name("T", "DJ") == "DJ; T"
    assert make_full_name("", "")  == "; "

def test_extract_family_name():
    assert extract_family_name("Harrison; Anna") == "Harrison"
    assert extract_family_name("Hamill-Thomas; Eva") == "Hamill-Thomas"
    assert extract_family_name("T; DJ") == "T"
    assert extract_family_name("; ")  == ""

def test_extract_given_name():
    assert extract_given_name("Harrison; Anna") == "Anna"
    assert extract_given_name("Hamill-Thomas; Eva") == "Eva"
    assert extract_given_name("T; DJ") == "DJ"
    assert extract_given_name("; ")  == ""

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])