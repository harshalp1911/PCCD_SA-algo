# util.py
import pandas as pd
from component import Component

def load_components(path):
    """
    Expects an Excel laid out like:
      Row 0: display names (e.g. Pedal, Pins, …)
      Row 1: codes (C1, C2, …)
      Row 2: volumes
      Row 3: widths
      Row 4: heights
      Row 5: material
    """
    df = pd.read_excel(path, header=None)
    codes     = df.iloc[1, 2:].tolist()
    volumes   = df.iloc[2, 2:].tolist()
    widths    = df.iloc[3, 2:].tolist()
    heights   = df.iloc[4, 2:].tolist()
    materials = df.iloc[5, 2:].tolist()

    components = []
    for idx, code in enumerate(codes):
        volume = float(volumes[idx])
        width  = float(widths[idx])
        height = float(heights[idx])
        material = str(materials[idx])
        comp = Component(
            name=code,
            volume=volume,
            width=width,
            height=height,
            material=material,
            index=idx
        )
        components.append(comp)

    return components

def load_weight_matrix(path):
    """
    Reads the square compatibility matrix from Excel,
    coercing non-numeric cells (headers) to zero.
    """
    df = pd.read_excel(path, header=None)
    mat = df.apply(pd.to_numeric, errors='coerce').fillna(0)
    return mat.values
