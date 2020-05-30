#!/usr/bin/python
"""
commandline utility tool for processing time/velocity data and extracting rising and falling edges.
Input args:
-o --output-file
-t --threshold
-r --reflector-length
-p --plot
"""

import argparse
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(
    description="Tool for processing time/voltage data from excel-files")
parser.add_argument(
    "input_file", type=argparse.FileType('rb'), default=sys.stdin)
parser.add_argument(
    "--output_file", "-o", type=argparse.FileType('w'), default=sys.stdout, required=False)
parser.add_argument("--threshold", "-t", type=float, default=3.0)
parser.add_argument("--reflector", "-r", type=float,
                    default=0.05, required=False)
parser.add_argument("--plot", "-p", required=False, action="store_true")

args = parser.parse_args()

df = pd.read_excel(args.input_file)

voltage_array = df["velocity"][1:].to_numpy()
time_array = df["Time"][1:].to_numpy()

rising_edges_index = np.flatnonzero(
    (voltage_array[:-1] <= args.threshold) & (voltage_array[1:] >= args.threshold)) + 1

time_differences = np.diff(time_array[rising_edges_index])
time_differences = np.append(time_differences, np.nan)

k_value = 3.6 * args.reflector
velocity = k_value / time_differences

output_dataframe = pd.DataFrame(
    {"Time": time_array[rising_edges_index], "Voltage": voltage_array[rising_edges_index],
     "Delta time": time_differences, "Velocity": velocity})

output_dataframe.to_csv(args.output_file, sep='\t', index=False)

if args.plot:
    output_plot = plt.figure()
    plt.plot(time_array, voltage_array)
    plt.plot(time_array[rising_edges_index],
             voltage_array[rising_edges_index], 'rx')
    output_plot.savefig("test.png")
