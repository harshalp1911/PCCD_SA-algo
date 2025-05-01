# import pandas as pd
# from component import Component
# import numpy as np

# # def load_components(filename):
# #     df = pd.read_excel(filename)
# #     components = []
# #     for idx, row in df.iterrows():
# #         components.append(Component(
# #             name=row['Name'],
# #             volume=row['Volume'],
# #             material=row['Material'],
# #             index=idx
# #         ))
# #     return components
# def load_components(path):
#     import pandas as pd

#     df = pd.read_excel(path)
#     component_names = df.columns[2:]

#     volume_row = df.iloc[1, 2:]
#     width_row = df.iloc[2, 2:]
#     height_row = df.iloc[3, 2:]
#     material_row = df.iloc[4, 2:]

#     components = []
#     for name in component_names:
#         component = {
#             'name': name,
#             'volume': volume_row[name],
#             'width': width_row[name],
#             'height': height_row[name],
#             'material': material_row[name]
#         }
#         components.append(component)

#     return components


# def load_weight_matrix(filename):
#     df = pd.read_excel(filename, header=None)
#     return np.array(df.values)

import pandas as pd
from component import Component
import numpy as np

def load_components(path):
    df = pd.read_excel(path)
    component_names = df.columns[2:]

    volume_row = df.iloc[1, 2:]
    width_row = df.iloc[2, 2:]
    height_row = df.iloc[3, 2:]
    material_row = df.iloc[4, 2:]

    components = []
    # for idx, name in component_names:
    for idx, name in enumerate(component_names):
        component = Component(
            name=name,
            volume=volume_row[name],
            width=width_row[name],
            height=height_row[name],
            material=material_row[name],
            index=idx
        )
        components.append(component)

    return components

# def load_weight_matrix(filename):
#     df = pd.read_excel(filename, header=None)
#     return np.array(df.values)
def load_weight_matrix(filename):
    df = pd.read_excel(filename, header=None)
    return df.apply(pd.to_numeric, errors='coerce').fillna(0).values
