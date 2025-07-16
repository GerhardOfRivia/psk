#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from .chaos import Lorenz

import requests
import pandas as pd
from questdb.ingress import Sender


def main():
    model = Lorenz(num_points=50, init_point=(0, 0, 0), step=1)
    ndarray = model.get_coordinates()
    chaos_df = pd.DataFrame({
        "X": [x for x in ndarray[0]],
        "Y": [x for x in ndarray[1]],
        "Z": [x for x in ndarray[2]],
        "T": pd.to_datetime([x for x in ndarray[3]]),
    })

    conf = f"http::addr=localhost:9000;"
    with Sender.from_conf(conf) as sender:
        sender.dataframe(chaos_df, table_name="trek", at="T")

    resp = requests.get("http://localhost:9000/exp", {"query": "SELECT * FROM trek"})
    print(resp.text)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting gracefully...")
    except Exception as e:
        print(f"An error occurred: {e}")
