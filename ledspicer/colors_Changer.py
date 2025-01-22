# Read the input file
with open('colors.ini', 'r') as file:
    lines = file.readlines()

new_lines = []
current_game = None

for line in lines:
    line = line.strip()
    
    # If it's a game title line (in brackets), keep as is
    if line.startswith('[') and line.endswith(']'):
        current_game = line
        new_lines.append(line)
        continue
        
    # Skip empty lines
    if not line:
        new_lines.append(line)
        continue
        
    # Process button/control configuration lines
    if '=' in line:
        key, value = line.split('=')
        # Add three entries with _1, _2, _3 suffixes
        new_lines.append(f"{key}_1={value}")
        new_lines.append(f"{key}_2={value}")
        new_lines.append(f"{key}_3={value}")

# Write the output file
with open('colors_expanded.ini', 'w') as file:
    file.write('\n'.join(new_lines))