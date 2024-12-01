""" module """


def test_creating():
    """creating"""

    text = "hello world"
    text2 = "hello world'"
    multiline = """hello
    world"""
    text3 = r"hello\nworld"  # regex
    text4 = b"hello world"  # bytes

    text5 = "  hello world  "

    assert text == "hello world"
    assert text2 == "hello world'"
    assert multiline == "hello\n    world"
    assert text3 == "hello\\nworld"
    assert text4 == b"hello world"
    assert text5.strip() == "hello world"


def test_string_cases():
    """case"""

    text = "hello world"

    assert text == "hello world"
    assert text.replace("h", "4") == "4ello world"
    assert text.title() == "Hello World"
    assert text.capitalize() == "Hello world"
    assert text.swapcase() == "HELLO WORLD"
    assert text.swapcase().swapcase() == text

    assert "h" in text
    assert "z" not in text


def test_search_and_replace():
    """search and replace"""

    text = "hello world"

    assert text.startswith("hello")
    assert text.endswith("world")
    assert text.find("world") == 6
    assert text.find("z") == -1
    assert text.count("l") == 3
    assert text.replace("world", "universe") == "hello universe"
    assert text.split(" ") == ["hello", "world"]
    list1 = text.split(" ")
    assert ",".join(list1) == "hello,world"


def test_fstring():
    """f string"""

    colmus = "name"
    table = "customers"
    assert f"select {colmus} from {table}" == "select name from customers"


def test_formatting():
    """formatting"""

    assert (
        "select {} from {}".format("first_name", "users")
        == "select first_name from users"
    )
