import csv

# Read the input file
with open('systems_ledspicer.csv', 'r') as file:
    content = file.readlines()

# Process the header line
header = content[0].strip().split(';')
new_header = [header[0]]  # Keep first column (system) as is

# Create new header with _1, _2, _3 suffixes for all columns except the first
for column in header[1:]:  # Start from second column
    if column:  # Skip empty columns
        new_header.extend([f"{column}_1", f"{column}_2", f"{column}_3"])

# Process the data lines
new_lines = [';'.join(new_header)]
for line in content[1:]:
    if line.strip():  # Skip empty lines
        values = line.strip().split(';')
        new_values = [values[0]]  # Keep the system name as is
        for value in values[1:]:  # Start from second column
            if value:  # If value exists, repeat it 3 times
                new_values.extend([value] * 3)  # Repeat the value 3 times
            else:  # If empty, add 3 empty values
                new_values.extend([''] * 3)
        new_lines.append(';'.join(new_values))

# Write the output file
with open('systems_ledspicer_expanded.csv', 'w', newline='') as file:
    file.write('\n'.join(new_lines))