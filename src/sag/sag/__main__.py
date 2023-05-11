#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from abc import ABC
import json
import logging
import pandas as pd
from pydantic import BaseModel, validator
import numpy as np
from typing import Any, Dict, Optional


class Data:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    @classmethod
    def load(cls, data: Any):
        df = pd.DataFrame.from_dict(data)
        return Data(df)

    def dump(self):
        return self.df.to_dict()

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def __modify_schema__(cls, field_schema):
        pass

    @classmethod
    def validate(cls, v):
        return v

    def __repr__(self):
        return f"{self.__class__.__name__}({self.df.size})"


class DataContainer(BaseModel, ABC):
    def head(self):
        raise NotImplementedError()

    @classmethod
    def validate(cls, v):
        if isinstance(v, Graph) or isinstance(v, Table):
            return v
        if isinstance(v, dict) and v.get("root") is not None:
            return Graph(**v)
        if isinstance(v, dict) and v.get("data") is not None:
            return Table(**v)
        raise TypeError(f"unknown data container: {v}")


class Table(DataContainer):
    name: Optional[str]
    data: Data

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {Data: lambda x: x.dump()}

    def head(self):
        return self.data.df.head()

    @validator("data")
    def convert_data(cls, v):
        if isinstance(v, Data):
            return v
        if isinstance(v, dict):
            return Data.load(v)
        raise TypeError("invalid data type")

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name})[{self.data.df.size}]"


class Graph(DataContainer):
    root: str

    def head(self):
        return self.root

    def __repr__(self):
        return f"{self.__class__.__name__}({self.root})"


class Structures(BaseModel):
    cache: Dict[str, DataContainer]

    class Config:
        json_encoders = {Data: lambda x: x.dump()}


def main():
    df = pd.DataFrame(np.random.randint(0, 100, size=(3, 3)), columns=list("ABC"))
    _data = Data(df)

    table = Table(data=_data)
    logging.info(table)
    table = table.json()
    logging.info(table)
    _table_json = json.loads(table)
    logging.info(_table_json)
    test_table = Table(**_table_json)
    logging.info(test_table)

    s = Structures(cache={"tab_1": Table(data=_data), "gra_1": Graph(root="cat")}).json()
    logging.info(s)
    s_json = json.loads(s)
    logging.info(s_json)
    s = Structures(**s_json)
    logging.info(s)


if __name__ == "__main__":
    main()
