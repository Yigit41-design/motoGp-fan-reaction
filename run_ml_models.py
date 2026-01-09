"""
MotoGP ML Modellerini Çalıştır
Bu script notebook'u Python script olarak çalıştırır
"""
import json
import subprocess
import sys

def run_notebook_cells():
    """Notebook hücrelerini sırayla çalıştır"""
    
    # Notebook'u oku
    with open('ml_models_motogp.ipynb', 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    print("🚀 MotoGP ML Modelleri çalıştırılıyor...\n")
    
    # Her hücreyi çalıştır
    for i, cell in enumerate(notebook['cells']):
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            
            # Markdown hücrelerini atla
            if source.strip().startswith('#'):
                continue
            
            print(f"\n{'='*60}")
            print(f"Hücre {i+1} çalıştırılıyor...")
            print(f"{'='*60}\n")
            
            # Hücreyi çalıştır
            try:
                exec(source, globals())
            except Exception as e:
                print(f"❌ Hata: {e}")
                print("Devam ediliyor...\n")
                continue
    
    print("\n✅ Tüm hücreler çalıştırıldı!")

if __name__ == "__main__":
    run_notebook_cells()
