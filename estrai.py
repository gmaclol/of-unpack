import sys
import os

# Colleghiamo la cartella
sys.path.append(os.path.join(os.getcwd(), "pyxamstore"))
import pyxamstore.explorer as ex

def inganno_totale():
    blob = "assemblies.blob"
    final_dir = "DLL_ESTRATTE"
    
    if not os.path.exists(blob):
        print("Errore: assemblies.blob non trovato!")
        return

    if not os.path.exists(final_dir):
        os.makedirs(final_dir)

    print("Inizio sventramento (Inganno del terminale in corso)...")
    
    # LA MAGIA È QUI:
    # Sovrascriviamo i comandi di sistema. 
    # Lo script penserà che stiamo eseguendo il tool da riga di comando.
    sys.argv = ["explorer.py", "unpack", blob, "--dir", final_dir]
    
    try:
        # Chiamiamo la funzione principale "nuda", come se avessimo premuto Invio nel terminale
        ex.main()
        print(f"--- SUCCESSO! File sparati in {final_dir} ---")
    except Exception as e:
        # Spesso questi tool lanciano un errore alla fine anche se hanno funzionato
        print(f"Esecuzione terminata. (Messaggio di sistema: {e})")

if __name__ == "__main__":
    inganno_totale()
