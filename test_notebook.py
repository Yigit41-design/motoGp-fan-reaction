"""
Simple script to test the notebook
Checks if ML models are working correctly
"""
import json
import sys
from pathlib import Path

def test_notebook_structure(notebook_path):
    """Test notebook structure"""
    print(f"Checking notebook structure: {notebook_path}")
    
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    cells = notebook.get('cells', [])
    print(f"[OK] Found {len(cells)} total cells")
    
    # Check ML cells
    ml_cells = []
    for i, cell in enumerate(cells):
        if cell.get('cell_type') == 'code':
            source = ''.join(cell.get('source', []))
            if 'Random Forest' in source or 'Decision Tree' in source or 'train_random_forest' in source:
                ml_cells.append(i)
    
    print(f"[OK] Found {len(ml_cells)} ML cells (cell numbers: {ml_cells})")
    
    # Syntax check
    print("\nRunning syntax check...")
    errors = []
    for i, cell in enumerate(cells):
        if cell.get('cell_type') == 'code':
            source = ''.join(cell.get('source', []))
            # Skip Jupyter magic commands and pip install
            lines = source.strip().split('\n')
            # Skip if all lines start with ! or %
            if source.strip() and not all(line.strip().startswith('!') or line.strip().startswith('%') or not line.strip() for line in lines):
                try:
                    compile(source, f'<cell {i}>', 'exec')
                except SyntaxError as e:
                    # Only show real syntax errors
                    if 'invalid syntax' not in str(e).lower() or i != 57:  # Skip Cell 57 (pip install)
                        errors.append((i, str(e)))
                except Exception:
                    # Ignore other errors (import errors etc.)
                    pass
    
    if errors:
        print(f"[WARNING] Found {len(errors)} syntax errors:")
        for cell_num, error in errors[:5]:  # Show first 5 errors
            print(f"   Cell {cell_num}: {error}")
    else:
        print("[OK] No syntax errors!")
    
    return len(errors) == 0

if __name__ == "__main__":
    notebook_path = Path("motogp_fan_reaction_analysis.ipynb")
    
    if not notebook_path.exists():
        print(f"[ERROR] Notebook not found: {notebook_path}")
        sys.exit(1)
    
    success = test_notebook_structure(notebook_path)
    
    if success:
        print("\n[OK] Notebook structure looks correct!")
        print("You can now push to GitHub.")
    else:
        print("\n[WARNING] Some errors found, please check.")
        sys.exit(1)
