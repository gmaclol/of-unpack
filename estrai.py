import sys
import os
import shutil

# Colleghiamo la cartella
sys.path.append(os.path.join(os.getcwd(), "pyxamstore"))
import pyxamstore.explorer as ex

def estrazione_finale():
    blob = "assemblies.blob"
    final_dir = "DLL_ESTRATTE"
    
    if not os.path.exists(blob):
        print(f"Errore: {blob} non trovato!")
        return

    if not os.path.exists(final_dir):
        os.makedirs(final_dir)

    print("Sventramento finale (Parametri perfetti)...")
    
    try:
        # LA VERA MAGIA: Niente liste [], niente nomi strani.
        # Solo i 3 valori esatti che la funzione pretende: (file, architettura, force)
        ex.do_unpack(blob, None, True)
        
        # Raccogliamo i frutti
        trovati = 0
        for root, dirs, files in os.walk("."):
            for f in files:
                if f.endswith(".dll") and final_dir not in root:
                    # Copiamo le DLL nella cartella finale
                    shutil.copy2(os.path.join(root, f), os.path.join(final_dir, f))
                    trovati += 1
                    
        if trovati > 0:
            print(f"--- VITTORIA! Trovate {trovati} DLL e messe in {final_dir} ---")
        else:
            print("Nessuna DLL estratta. Il blob potrebbe essere vuoto o corrotto.")
            
    except Exception as e:
        print(f"Errore tecnico: {e}")

if __name__ == "__main__":
    estrazione_finale()
