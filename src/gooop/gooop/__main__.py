#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import gooop.proto.person_pb2 as person_pb2


def main():
    # Create a new Person message
    person = person_pb2.Person()
    person.name = "Alice"
    person.id = 123
    person.email = "alice@example.com"

    # Serialize to string
    data = person.SerializeToString()

    # Deserialize from string
    person2 = person_pb2.Person()
    person2.ParseFromString(data)

    print(person2)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting gracefully...")
    except Exception as e:
        print(f"An error occurred: {e}")
