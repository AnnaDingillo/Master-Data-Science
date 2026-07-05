# Contenuto della cartella:

1. "**Anna Dingillo_software di prodotti vegani.ipynb**": il file colab inviato per correzione al coach.
2. il feedback del coach
3. "**Vegan-shop-managment-software.py**": il file con le correzioni pronto per l'utilizzo, indicazioni a seguire (Ita + Eng).
4. Changelog.md: il file con il confronto tra le due versioni del codice.
5. il certificato che attesta il superamento del corso.


# Software di Gestione Negozio Vegano (ITA)

Questo progetto è un semplice software di gestione magazzino pensato per un negozio di prodotti vegani. Permette di registrare nuovi prodotti, gestire le vendite, visualizzare i profitti e accedere a un menù di aiuto.

## Funzionalità Principali

- **aggiungi**: registra nuovi prodotti indicando nome, quantità, prezzo di vendita e prezzo di acquisto.
- **elenca**: elenca tutti i prodotti presenti in magazzino.
- **vendita**: registra le vendite e mostra uno scontrino.
- **profitti**: mostra i profitti lordi e netti totali.
- **aiuto**: mostra il menù con tutti i comandi disponibili.
- **chiudi**: termina il programma.

## Requisiti e Moduli

Il progetto utilizza esclusivamente moduli integrati di Python:

- `json`: per caricare, salvare e modificare i dati di magazzino contenuti in un file `.json`.
- `os`: per verificare l'esistenza del file di magazzino all'avvio del programma.

## Struttura del Codice

- **classe `Product`**: rappresenta un prodotto con attributi privati: `name`, `quantity`, `purchase_price`, `sale_price`.
- **classe `Register`**: gestisce l'intero magazzino, incluso il file dei dati, il tracciamento di profitti e costi, e le operazioni.
- **Funzioni interattive**:
  - `input_add_product()`: permette all'utente di aggiungere un nuovo prodotto o aggiornarne uno esistente.
  - `input_sell_product()`: registra una vendita e aggiorna la quantità del prodotto.

## Salvataggio dei Dati

Tutti i dati vengono salvati automaticamente in un file .json, così magazzino e dati finanziari sono persistenti tra una sessione e l'altra.

## Come Usarlo

Esegui il file `main.py` per avviare il programma e segui il menù interattivo:

```bash
python main.py
```

# Vegan Shop Management Software (ENG)

This project is a simple inventory management software designed for a vegan product shop. It allows you to register new products, manage sales, view profits, and access a help menu.

## Key Features

- **add**: register new products with name, quantity, selling price, and purchase price.
- **list**: list all products in the inventory.
- **sale**: record sales and display a receipt.
- **profits**: show total gross and net profits.
- **help**: display the menu with all available commands.
- **close**: terminate the program.

## Requirements and Modules

The project uses only Python’s built-in modules:

- `json`: to load, save, and modify inventory data stored in a `.json` file.
- `os`: to check the existence of the inventory file when the program starts.

## Code Structure

- **`Product` class**: represents a product with private attributes: `name`, `quantity`, `purchase_price`, `sale_price`.
- **`Register` class**: manages the full inventory, including the data file, profit and cost tracking, and operations.
- **Interactive functions**:
  - `input_add_product()`: allows the user to add a new product or update an existing one.
  - `input_sell_product()`: records a sale and updates the product quantity.

## Data Storage

All data is saved automatically in a .json file, so the inventory and financial data are persistent across sessions.

## How to Use

Run the `main.py` file to start the program and follow the interactive menu:

```bash
python main.py

