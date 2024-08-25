import os
import sys
import subprocess
from pathlib import Path

try:
    from rich import print
except:
    pass  

# NOTE: change this
VAULTS_DIR = Path(r"D:\KELREY'S\Personal Vaults")

def create_output_directory(base_dir, notebook_name):
    # NOTE: Create a new folder named after the notebook in the base directory
    vaults_dir = VAULTS_DIR / base_dir / "JupyterNB" 
    output_dir = os.path.join(str(vaults_dir), notebook_name)
    os.makedirs(output_dir, exist_ok=True)
    return output_dir

def main(input_notebook, base_output_dir):
    # Extract notebook name without extension
    notebook_name = os.path.splitext(os.path.basename(input_notebook))[0]

    # Create output directory
    output_dir = create_output_directory(base_output_dir, notebook_name)
    # Construct the nbconvert command
    nbconvert_command_md = [
        'jupyter', 'nbconvert',
        '--to', 'markdown',
        input_notebook,
        '--output-dir', output_dir
    ]
    
    nbconvert_command_pdf = [
        'jupyter', 'nbconvert',
        '--to', 'pdf',
        input_notebook,
        '--output-dir', output_dir
    ]

    # Execute the command
    subprocess.run(nbconvert_command_md, check=True)
    subprocess.run(nbconvert_command_pdf, check=True)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python convert_notebook.py <input_notebook> <fault folders ex: '8 - Works' >")
        sys.exit(1)

    input_notebook = sys.argv[1]
    base_output_dir = sys.argv[2]

    # NOTE: i set the `base_output_dir` to only takes the main folder in my obsidian vault
    acceptable_base_dirs = [x.name for x in VAULTS_DIR.iterdir() if x.is_dir()]
    if base_output_dir not in acceptable_base_dirs:
        print(f"\n===>{base_output_dir}<===  not in: ", acceptable_base_dirs, sep="\t\n")
        sys.exit(1)
         
    main(input_notebook, base_output_dir)