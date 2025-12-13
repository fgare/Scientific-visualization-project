import re

def estrai_delta_elbo(input_file, output_file):
    # Pattern regex per cercare 'deltaELBO=' seguito da numeri e punti
    # Spiegazione pattern:
    # deltaELBO=  -> cerca letteralmente questa stringa
    # ([\d\.]+)   -> cattura una sequenza di cifre (\d) e punti (\.)
    pattern = r"deltaELBO=([\d\.]+)"

    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                # Cerca il pattern nella riga corrente
                match = re.search(pattern, line)
                
                # Se il pattern viene trovato, scrivi il valore nel nuovo file
                if match:
                    valore = match.group(1)
                    outfile.write(f"{valore}\n")
        
        print(f"Operazione completata! I dati sono stati salvati in '{output_file}'.")

    except FileNotFoundError:
        print(f"Errore: Il file '{input_file}' non è stato trovato.")
    except Exception as e:
        print(f"Si è verificato un errore: {e}")

# --- Configurazione dei file ---
file_di_input = r"C:\Users\Federico\Documents\GitHub\Scientific-visualization-project\training_output.txt"
file_di_output = r"C:\Users\Federico\Documents\GitHub\Scientific-visualization-project\elbo_values.txt"

# Esecuzione della funzione
estrai_delta_elbo(file_di_input, file_di_output)