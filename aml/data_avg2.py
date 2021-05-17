from azureml.core import Run
import argparse
import os
# Import numpy
import numpy as np

# Get the experiment run context
run = Run.get_context()


# Get the temperature list from the data file
with open('datafile.txt') as fp:
  data = fp.read()

# Remove brackets from the list
data = data.strip('[')
data = data.strip(']')

# Split the values by comma and convert to int
temps = data.split(',')
temps = [int(i) for i in temps]

# Make the list an array
tempArray = np.array(temps)

# Average the values
avg = np.average(tempArray)

# Write the average out to a file
file2 = open('average.txt', 'w')
file2.writelines(str(avg))