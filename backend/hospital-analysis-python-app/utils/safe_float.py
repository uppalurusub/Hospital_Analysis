import pandas as pd
import numpy as np
import math


def safe_float(value):

    if pd.isna(value):
        return 0.0

    if value == np.inf:
        return 0.0

    if value == -np.inf:
        return 0.0

    return float(value)