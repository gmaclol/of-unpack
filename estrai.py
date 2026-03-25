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

    print("Inizio sventramento del blob (Configurazione forzata)...")
    try:
        # do_unpack vuole: args, in_dir, in_arch, force
        # Gli passiamo: il file, la cartella corrente, nessuna architettura specifica, True per il force
        ex.do_unpack([blob], in_dir=".", in_arch=None, force=True)
        
        if not os.path.exists(final_dir):
            os.makedirs(final_dir)
            
        # Spostiamo tutto quello che finisce con .dll nella cartella finale
        trovati = 0
        # Il tool potrebbe estrarre in 'out' o nella root
        for root, dirs, files in os.walk("."):
            for f in files:
                if f.endswith(".dll") and "DLL_ESTRATTE" not in root:
                    shutil.move(os.path.join(root, f), os.path.join(final_dir, f))
                    trovati += 1
        
        if trovati > 0:
            print(f"SUCCESSO! Estratte {trovati} DLL in {final_dir}")
        else:
            print("Nessuna DLL trovata dopo l'esecuzione.")
            
    except Exception as e:
        print(f"Errore tecnico finale: {e}")

if __name__ == "__main__":
    main()
