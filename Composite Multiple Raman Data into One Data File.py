from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import os
plt.rcParams["figure.dpi"] = 1200

all_data = []

angles = []

files_names = []

raman_shift = []

folder_path = Path(r'C:\Users\mairz\Desktop\Research\Dr. Gamini Research\Data\Angle Resolved Polarized Raman\Black Phousphorus\BlackPhosphorus_4_23_2023\Parallel')

folder_content = os.listdir(folder_path)

for i in folder_content:

    if i.endswith(".txt"):
        files_names.append(os.path.splitext(i)[0])

        angles.append(float(os.path.splitext(i)[0]))

files_names.sort(key=float)

angles.sort()

#######################################################

for idx, file_name in enumerate(files_names):

    with open(os.path.join(folder_path, (file_name + ".txt"))) as f:

        content = f.read()

    lines = content.split('\n')

    second_column = []

    for line in lines:

        columns = line.split('\t')

        if len(columns) == 2:

            if idx == 0:

                raman_shift.append(float(columns[0]))

                second_column.append(float(columns[1]))

            else:
                second_column.append(float(columns[1]))

    all_data.append(second_column)

#############################################################################
f = dict(zip(angles, all_data))

raw_data = pd.DataFrame(f)
raw_data.insert(0, "Raman Shift", raman_shift)
print(raw_data)
raw_data.to_csv(r"C:\Users\mairz\Desktop\Research\Dr. Gamini Research\Data\Angle Resolved Polarized Raman\Black Phousphorus\BlackPhosphorus_4_23_2023\RawData\ParallelDataNEW.txt", sep="\t", index=False)
