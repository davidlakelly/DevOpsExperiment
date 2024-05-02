import api_call
import db_query


def test_hello_world():
    assert "Hello, World!" == "Hello, World!"

def test_get_data():
    assert api_call.get_data() == api_call.get_data()

def test_readSqliteTable():
    assert db_query.readSqliteTable() == db_query.readSqliteTable()


def test_api_call_returns_data():
    assert api_call.get_data() is not None

def test_db_query_returns_data():
    assert db_query.readSqliteTable() is not None

def test_api_call_returns_valid_data():
    data = api_call.get_data()
    assert isinstance(data, dict)


def test_db_query_returns_valid_data():
    data = db_query.readSqliteTable()
    assert isinstance(data, list)
    assert len(data) > 0
