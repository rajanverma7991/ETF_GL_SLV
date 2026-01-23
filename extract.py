import nbformat

# STEP 1: load executed notebook
nb = nbformat.read("executed.ipynb", as_version=4)

# STEP 2: find last cell output (can customize)
final_output = ""
for cell in reversed(nb['cells']):
    if cell['cell_type'] == 'code' and 'outputs' in cell:
        for out in cell['outputs']:
            if out.get('text'):
                final_output = out['text']
                break
    if final_output:
        break

# STEP 3: save to output/ folder
with open("output/result.txt", "w") as f:
    f.write(final_output.strip())

print("Saved:", final_output)
