# pyPulseCounter
---
Simple command-line tool for counting rising edges in a time-voltage excel-spreadsheet.
Output is:
|Time|Voltage|delta time|velocity|

Input arguments:
+ input_file (required): Path to excel-spreadsheet
+ -o --output-file (optional): Path to output-file
+ -t --threshold (optional): Voltage-level for logic level 'high'
+ -r --reflector (optional): Reflector length
+ -p --plot (optional): Save plot of input and the counted rising edges as png-file
