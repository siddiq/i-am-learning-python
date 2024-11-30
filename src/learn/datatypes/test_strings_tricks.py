""" module """


def test_checktypes():
    """ checking """

    text = "123"
    assert text.isnumeric()
    assert text.isdigit()
    assert text.isalnum()
    assert not text.isalpha()

    text = "abc"
    assert text.isalnum()
    assert text.isalpha()
    assert not text.isnumeric()

    text = "abc123"
    assert text.isalnum()
    assert not text.isnumeric()
    assert not text.isalpha()

    text = "abc123@locslhost"
    assert not text.isnumeric()
    assert not text.isalnum()
    assert not text.isalpha()


def test_replace():
    """ replace """

    text = "<b>hello</b>"
    assert text.replace('<b>', '').replace('</b>', '') == 'hello'


def test_bytes():
    """ bytes """

    text = "hAllo world"
    text_bytes = b"hAllo world"

    assert text[0] == "h"
    assert text_bytes[0] == 104  # ascii of "h"

    assert text.encode("utf-8") == text_bytes
    assert text_bytes.decode("utf-8") == text
    assert text_bytes.decode("ascii") == text


def test_joining_and_splitting():
    """ joining and splitting """

    list1 = ["hello", "world"]
    assert " ".join(list1) == "hello world"
    assert "hello world".split(" ") == list1


def test_splitting():
    """ splitting """

    text = "This is an example sentence"
    arr = text.split(" ")
    assert arr == ["This", "is", "an", "example", "sentence"]
    assert len(arr) == 5
