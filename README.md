# pyPulseCounter
---
Simple command-line tool for counting rising edges in a time-voltage excel-spreadsheet.
Output is (default to stdout):
+ Time (timestamp of each rising edge)
+ Voltage (voltage of each timestamp)
+ Time delta (difference between each timestamp)
+ Velocity (calculated velocity)

Input arguments:
+ input_file (required): Path to excel-spreadsheet
+ -o --output-file (optional): Path to output-file
+ -t --threshold (optional): Voltage-level for logic level 'high'
+ -r --reflector (optional): Reflector length
+ -p --plot (optional): Save plot of input and the counted rising edges as png-file
