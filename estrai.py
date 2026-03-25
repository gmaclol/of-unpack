import sys
import os
import shutil

# Aggiungiamo il percorso per le dipendenze
sys.path.append(os.path.join(os.getcwd(), "pyxamstore"))
import pyxamstore.explorer as ex

def main():
    blob = "assemblies.blob"
    final_dir = "DLL_ESTRATTE"
    
    if not os.path.exists(blob):
        print(f"Errore: {blob} non trovato!")
        return

    print("Inizio sventramento del blob...")
    try:
        # Passiamo il file dentro una lista [] per evitare l'errore delle lettere separate
        # E usiamo do_unpack che è la funzione di basso livello più sicura
        ex.do_unpack([blob])
        
        if not os.path.exists(final_dir):
            os.makedirs(final_dir)
            
        # Il tool di solito estrae in una cartella chiamata 'out'
        source = "out"
        if os.path.exists(source):
            for f in os.listdir(source):
                shutil.move(os.path.join(source, f), os.path.join(final_dir, f))
            print(f"SUCCESSO! File pronti in {final_dir}")
        else:
            # Se non ha creato 'out', cerchiamo file .dll sparsi nella cartella corrente
            for f in os.listdir('.'):
                if f.endswith('.dll'):
                    shutil.move(f, os.path.join(final_dir, f))
            print("Controllo completato.")
            
    except Exception as e:
        print(f"Errore tecnico: {e}")

if __name__ == "__main__":
    main()
