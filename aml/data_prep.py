# Create a series of temperature values
data = [49,60,77,32,55,90,28,60,83,75,62,18,85,72,58,67,42,33,98,70]

# Write the list to a file
file1 = open('datafile.txt', 'w')
file1.writelines(str(data))