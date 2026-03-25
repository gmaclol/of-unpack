import sys
import os

# Aggiungiamo la cartella pyxamstore al percorso per evitare errori di import
sys.path.append(os.path.join(os.getcwd(), "pyxamstore"))

import pyxamstore.explorer as explorer

def main():
    blob = "assemblies.blob"
    out = "DLL_ESTRATTE"
    
    if not os.path.exists(blob):
        print("File assemblies.blob non trovato!")
        return

    # Modifica "sporca" per far andare l'import relativo
    import pyxamstore.explorer as ex
    # Forziamo l'estrazione usando la funzione che abbiamo scoperto prima
    ex.unpack_store(blob, out)
    print("Estrazione completata con successo!")

if __name__ == "__main__":
    main()
