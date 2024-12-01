"""
Serialize

"""

import json
import os


def test_json_serialize():
    """json"""

    obj1 = {"a": 1, "b": 2, "c": 3}
    json_str = json.dumps(obj1)

    obj2 = json.loads(json_str)
    assert obj1 == obj2

    print(json_str)


def test_load_from_file():
    """load from file"""

    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to the test.json file
    file_path = os.path.join(current_dir, "test.json")

    with open(file_path, "r", encoding="utf-8") as f:
        obj = json.load(f)

    assert obj["a"] == 1
    assert obj["b"] == 2
    assert obj["c"] == 3


def test_dump_to_file():
    """dump to file"""

    obj = {"a": 1, "b": 2, "c": 3}

    with open("test2.json", "w", encoding="utf-8") as f:
        json.dump(obj, f)

    with open("test2.json", "r", encoding="utf-8") as f:
        obj2 = json.load(f)

    assert obj == obj2

    os.unlink("test2.json")
