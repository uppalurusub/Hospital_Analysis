# utils/json_sanitizer.py

import math
import numpy as np
import pandas as pd


def sanitize_json(obj):

    if isinstance(obj, dict):
        return {
            k: sanitize_json(v)
            for k, v in obj.items()
        }

    if isinstance(obj, list):
        return [
            sanitize_json(x)
            for x in obj
        ]

    if isinstance(obj, np.integer):
        return int(obj)

    if isinstance(obj, np.floating):
        obj = float(obj)

    if isinstance(obj, float):

        if math.isnan(obj):
            return None

        if math.isinf(obj):
            return None

        return obj

    if pd.isna(obj):
        return None

    return obj