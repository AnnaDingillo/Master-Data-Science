# Changelog — Vegan Shop Management Software

Questo file documenta le differenze tra le due versioni del software presenti in questa cartella:

- `Software di prodotti vegani` (versione iniziale, in italiano)
- `Vegan-shop-managment-software.py` (versione corretta, in inglese)

## [v2] — Versione corretta

### Bug corretto
- **Validazione numerica insufficiente**: la versione iniziale accettava prezzi (`buy_price`, `sell_price`) e quantità negative in fase di aggiunta prodotto, perché il controllo `except ValueError` intercetta solo errori di *formato* (es. testo non convertibile in numero), non errori *logici* (es. un numero negativo, sintatticamente valido ma privo di senso nel contesto di un magazzino).
- **Soluzione**: introdotta la funzione `validate_numeric_input()`, che dopo la conversione numerica controlla esplicitamente che il valore sia positivo (`value <= 0`), richiedendo un nuovo input in caso contrario.

### Refactoring
- Aggiunta la funzione helper `validate_yes_no_input()` per centralizzare la logica di conferma sì/no, prima duplicata in più punti di `input_sell_product()`.
- Tutta la validazione numerica (prezzi e quantità, sia in aggiunta prodotto che in vendita) è stata unificata tramite `validate_numeric_input()`, eliminando la duplicazione dei cicli `try/except` presenti nella versione iniziale.

### Traduzione
- Codice, commenti/docstring, messaggi a schermo e chiavi dei dizionari JSON tradotti dall'italiano all'inglese, per uniformità (es. `"prodotto"` → `"product"`, `"quantità"` → `"quantity"`, `"prezzo"` → `"price"`).
- I comandi del menù principale sono cambiati di conseguenza (`aggiungi`→`add`, `elenca`→`list`, `vendita`→`sale`, `profitti`→`profits`, `aiuto`→`help`, `chiudi`→`exit`). 

### Modifica aggiuntiva inserita nella validazione delle quantità inserite:
- Nella versione iniziale la quantità era validata con `.isdigit()`, che accetta lo zero (`"0".isdigit()` è `True`). La nuova funzione `validate_numeric_input()` usa `value <= 0`, quindi **ora anche lo zero viene rifiutato** come quantità o prezzo valido — comportamento non esplicitamente richiesto dal feedback originale.

