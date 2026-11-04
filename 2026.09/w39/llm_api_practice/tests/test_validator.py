from validator import validate


def test_valid_data():
    data = {
        "summary": "数据库连接失败",
        "category": "database",
        "urgent": True,
        "confidence": 0.95
    }

    result = validate(data)

    assert result is not None
    assert result.summary == "数据库连接失败"
    assert result.confidence == 0.95


def test_invalid_type():
    data = {
        "summary": "数据库连接失败",
        "category": "database",
        "urgent": True,
        "confidence": "高"
    }

    result = validate(data)

    assert result is None


def test_missing_field():
    data = {
        "summary": "数据库连接失败",
        "category": "database",
        "confidence": 0.95
    }

    result = validate(data)

    assert result is None