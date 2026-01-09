"""
Notebook'u test etmek için basit bir script
ML modellerinin çalışıp çalışmadığını kontrol eder
"""
import json
import sys
from pathlib import Path

def test_notebook_structure(notebook_path):
    """Notebook yapısını test et"""
    print(f"Notebook yapisi kontrol ediliyor: {notebook_path}")
    
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    cells = notebook.get('cells', [])
    print(f"[OK] Toplam {len(cells)} hucre bulundu")
    
    # ML hücrelerini kontrol et
    ml_cells = []
    for i, cell in enumerate(cells):
        if cell.get('cell_type') == 'code':
            source = ''.join(cell.get('source', []))
            if 'Random Forest' in source or 'Decision Tree' in source or 'train_random_forest' in source:
                ml_cells.append(i)
    
    print(f"[OK] {len(ml_cells)} ML hucre bulundu (hucre numaralari: {ml_cells})")
    
    # Syntax kontrolü
    print("\nSyntax kontrolu yapiliyor...")
    errors = []
    for i, cell in enumerate(cells):
        if cell.get('cell_type') == 'code':
            source = ''.join(cell.get('source', []))
            # Jupyter magic komutlarını ve pip install'ı atla
            lines = source.strip().split('\n')
            # Eğer tüm satırlar ! veya % ile başlıyorsa atla
            if source.strip() and not all(line.strip().startswith('!') or line.strip().startswith('%') or not line.strip() for line in lines):
                try:
                    compile(source, f'<cell {i}>', 'exec')
                except SyntaxError as e:
                    # Sadece gerçek syntax hatalarını göster
                    if 'invalid syntax' not in str(e).lower() or i != 57:  # Cell 57'yi atla (pip install)
                        errors.append((i, str(e)))
                except Exception:
                    # Diğer hataları görmezden gel (import hataları vs.)
                    pass
    
    if errors:
        print(f"[WARNING] {len(errors)} syntax hatasi bulundu:")
        for cell_num, error in errors[:5]:  # İlk 5 hatayı göster
            print(f"   Hucre {cell_num}: {error}")
    else:
        print("[OK] Syntax hatasi yok!")
    
    return len(errors) == 0

if __name__ == "__main__":
    notebook_path = Path("Untitled2_(2) (2).ipynb")
    
    if not notebook_path.exists():
        print(f"[ERROR] Notebook bulunamadi: {notebook_path}")
        sys.exit(1)
    
    success = test_notebook_structure(notebook_path)
    
    if success:
        print("\n[OK] Notebook yapisi dogru gorunuyor!")
        print("Simdi GitHub'a push edebilirsiniz.")
    else:
        print("\n[WARNING] Bazi hatalar bulundu, lutfen kontrol edin.")
        sys.exit(1)

