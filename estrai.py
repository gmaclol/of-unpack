import sys
import os
import shutil

# Aggiungiamo il percorso corretto
sys.path.append(os.path.join(os.getcwd(), "pyxamstore"))
import pyxamstore.explorer as ex

def main():
    blob = "assemblies.blob"
    # Cartella dove vogliamo le DLL per l'upload
    final_dir = "DLL_ESTRATTE"
    
    if not os.path.exists(blob):
        print("File assemblies.blob non trovato!")
        return

    print("Inizio sventramento del blob...")
    try:
        # Usiamo SOLO il blob come vuole la funzione
        ex.unpack_store(blob)
        
        # Dato che unpack_store crea una cartella di default (di solito 'out' o 'assemblies')
        # cerchiamo dove sono finiti i file e li mettiamo in DLL_ESTRATTE
        if not os.path.exists(final_dir):
            os.makedirs(final_dir)
            
        # Cerchiamo i file .dll estratti e li spostiamo
        source_dir = "out" if os.path.exists("out") else "assemblies"
        if os.path.exists(source_dir):
            for f in os.listdir(source_dir):
                shutil.move(os.path.join(source_dir, f), os.path.join(final_dir, f))
            print(f"SUCCESSO! File spostati in {final_dir}")
        else:
            print("Estratti, ma non trovo la cartella di output (out o assemblies)!")
            
    except Exception as e:
        print(f"Errore: {e}")

if __name__ == "__main__":
    main()
