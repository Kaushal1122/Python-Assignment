
import boto3
import pytest
from botocore.exceptions import ClientError
from moto import mock_aws

from src.boto3_example import DynamodBExample


@mock_aws
def test_create_dynamo_table():
    """
    Implement the test logic here for testing create_dynamo_table method.
    """
    example = DynamodBExample()
    example.create_movies_table()

    dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
    table = dynamodb.Table("Movies")
    table.load()

    assert table.table_status == "ACTIVE"
    assert table.key_schema == [
        {"AttributeName": "year", "KeyType": "HASH"},
        {"AttributeName": "title", "KeyType": "RANGE"},
    ]


@mock_aws
def test_add_dynamo_record_table():
    """
    Implement the test logic here for testing add_dynamo_record_table method.
    """
    example = DynamodBExample()
    example.create_movies_table()

    item = {
        "year": 2020,
        "title": "Test Movie",
        "info": {"rating": 8},
    }

    example.add_dynamo_record("Movies", item)

    dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
    response = dynamodb.Table("Movies").get_item(
        Key={"year": 2020, "title": "Test Movie"}
    )

    assert response["Item"] == item


@mock_aws
def test_add_dynamo_record_table_failure():
    """
    Implement the test logic here to test add_dynamo_record_table failures.
    """
    example = DynamodBExample()

    with pytest.raises(ClientError):
        example.add_dynamo_record(
            "MissingMovies",
            {"year": 2020, "title": "Test Movie"},
        )
