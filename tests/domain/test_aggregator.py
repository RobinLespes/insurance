import pandas as pd

from insurance.domain.aggregator import aggregate

def test_aggregator():

    df = pd.DataFrame({"sex": ["male", "male", "female"], "charge": [1, 1, 1]})
    res = aggregate(df)

    assert res[res["sex"]=="male"]["charge"].values[0] == 1