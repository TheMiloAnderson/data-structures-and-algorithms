from repeated_word.repeated_word import first_repeated_word
import pytest


def test_repeated_word():
    string = 'It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn\'t know what I was doing in New York'
    assert first_repeated_word(string) == 'summer'


def test_empty_string():
    string = ''
    assert first_repeated_word(string) is None


def test_no_repeated_words():
    string = 'It was a queer, sultry summer'
    assert first_repeated_word(string) is None
