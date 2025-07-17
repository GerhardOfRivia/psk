import pytest
import gooop.proto.person_pb2 as person_pb2


def test_person_fields():
    person = person_pb2.Person()
    person.name = "Bob"
    person.id = 42
    person.email = "bob@example.com"
    assert person.name == "Bob"
    assert person.id == 42
    assert person.email == "bob@example.com"


def test_person_serialization_deserialization():
    person = person_pb2.Person(name="Carol", id=7, email="carol@example.com")
    data = person.SerializeToString()
    new_person = person_pb2.Person()
    new_person.ParseFromString(data)
    assert new_person.name == "Carol"
    assert new_person.id == 7
    assert new_person.email == "carol@example.com"


def test_person_default_values():
    person = person_pb2.Person()
    assert person.name == ""
    assert person.id == 0
    assert person.email == ""
