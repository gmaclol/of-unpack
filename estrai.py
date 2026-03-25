import sys
import os
import shutil

# Percorso per pyxamstore
sys.path.append(os.path.join(os.getcwd(), "pyxamstore"))
import pyxamstore.explorer as ex

def main():
    blob = "assemblies.blob"
    final_dir = "DLL_ESTRATTE"
    
    if not os.path.exists(blob):
        print(f"Errore: {blob} non trovato!")
        return

    print("Tentativo finale: forzatura posizionale dei parametri...")
    try:
        # Passiamo i parametri senza nomi, solo i valori nell'ordine: 
        # [files], arch, force
        # Dalla lista di prima: unpack_store(file) o do_unpack(args, arch, force)
        
        # Proviamo il comando più pulito possibile per questa versione
        ex.do_unpack([blob], None, True)
        
        if not os.path.exists(final_dir):
            os.makedirs(final_dir)
            
        # Cerchiamo le DLL ovunque siano finite
        trovati = 0
        for root, dirs, files in os.walk("."):
            for f in files:
                if f.endswith(".dll") and "DLL_ESTRATTE" not in root:
                    # Copiamo invece di spostare per sicurezza
                    shutil.copy2(os.path.join(root, f), os.path.join(final_dir, f))
                    trovati += 1
        
        if trovati > 0:
            print(f"SUCCESSO! Trovate {trovati} DLL.")
        else:
            print("Esecuzione terminata, ma nessuna DLL rilevata.")
            
    except Exception as e:
        print(f"Errore: {e}")

if __name__ == "__main__":
    main()
