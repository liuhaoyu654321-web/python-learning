from parser import parse_json


def test_valid_json():
    content = '{"name": "Arlo", "age": 24}'

    result = parse_json(content)

    assert result == {
        "name": "Arlo",
        "age": 24
    }


def test_invalid_json():
    content = '{"name": "Arlo" "age": 24}'

    result = parse_json(content)

    assert result is None