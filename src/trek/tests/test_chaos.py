import datetime
import math
import pandas as pd
from trek.chaos import Lorenz


# filepath: /psk/src/trek/tests/test_chaos.py

def test_attractor_default():
    result = Lorenz.attractor(0, 1, -1)
    assert isinstance(result, tuple)
    assert len(result) == 3
    assert math.isclose(result[0], 10)
    assert math.isclose(result[1], -1)
    assert math.isclose(result[2], 2.6666666666666665)


def test_attractor_default_xyz():
    x, y, z = Lorenz.attractor(0, 1, -1)
    assert math.isclose(x, 10)
    assert math.isclose(y, -1)
    assert math.isclose(z, 2.6666666666666665)


def test_get_coordinates_shape():
    model = Lorenz(num_points=10, init_point=(0.1, 0, -0.1))
    result_df = model.get_coordinates()
    assert result_df.shape == (10, 3)
    expected_df = pd.DataFrame(
        [[0.1, 0, -0.1]],
        columns=["x", "y", "z"]
    )
    diff = result_df.iloc[[0]].compare(expected_df.iloc[[0]])
    assert diff.empty


def test_update_attributes():
    model = Lorenz(num_points=5, step=2)
    model.update_attributes(num_points=10, step=5)
    assert model.num_points == 10
    assert model.step == 5


def test_custom_parameters():
    x, y, z = 1, 2, 3
    sigma, beta, rho = 14, 2.5, 30
    result = Lorenz.attractor(x, y, z, sigma=sigma, beta=beta, rho=rho)
    assert math.isclose(result[0], sigma * (y - x))
    assert math.isclose(result[1], rho * x - y - x * z)
    assert math.isclose(result[2], x * y - beta * z)
