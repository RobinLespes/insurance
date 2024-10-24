import numpy as np


def aggregate(df):
    res = df.groupby("sex", as_index=False).agg({"charge": np.mean})
    return res
