# Read the input file
with open('controls.ini', 'r') as file:
    lines = file.readlines()

new_lines = []

for line in lines:
    line = line.strip()
    
    # If it's a P1NumButtons line, multiply the value by 3
    if line.startswith('P1NumButtons='):
        key, value = line.split('=')
        new_value = int(value) * 3
        new_lines.append(f"{key}={new_value}")
    else:
        # Keep all other lines as they are
        new_lines.append(line)

# Write the output file
with open('controls_updated.ini', 'w') as file:
    file.write('\n'.join(new_lines))