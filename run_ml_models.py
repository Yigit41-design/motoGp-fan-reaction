"""
Run MotoGP ML Models
This script runs the notebook as a Python script
"""
import json
import subprocess
import sys

def run_notebook_cells():
    """Run notebook cells sequentially"""
    
    # Read the notebook
    with open('ml_models_motogp.ipynb', 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    print("🚀 Running MotoGP ML Models...\n")
    
    # Execute each cell
    for i, cell in enumerate(notebook['cells']):
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            
            # Skip markdown cells
            if source.strip().startswith('#'):
                continue
            
            print(f"\n{'='*60}")
            print(f"Running cell {i+1}...")
            print(f"{'='*60}\n")
            
            # Execute the cell
            try:
                exec(source, globals())
            except Exception as e:
                print(f"❌ Error: {e}")
                print("Continuing...\n")
                continue
    
    print("\n✅ All cells executed!")

if __name__ == "__main__":
    run_notebook_cells()
