# Vegan Shop Inventory Manager 🥦

This project is a simple inventory management software designed for a vegan product shop. It allows you to register new products, manage sales, view profits, and access a help menu.

## ✨ Key Features

- **add**: register new products with name, quantity, selling price, and purchase price.
- **list**: list all products in the inventory.
- **sale**: record sales and display a receipt.
- **profits**: show total gross and net profits.
- **help**: display the menu with all available commands.
- **close**: terminate the program.

## ⚙️ Requirements and Modules

The project uses only Python’s built-in modules:

- `json`: to load, save, and modify inventory data stored in a `.json` file.
- `os`: to check the existence of the inventory file when the program starts.

## 🧱 Code Structure

- **`Product` class**: represents a product with private attributes: `name`, `quantity`, `purchase_price`, `sale_price`.
- **`Register` class**: manages the full inventory, including the data file, profit and cost tracking, and operations.
- **Interactive functions**:
  - `input_add_product()`: allows the user to add a new product or update an existing one.
  - `input_sell_product()`: records a sale and updates the product quantity.

## 📦 Data Storage

All data is saved automatically in a .json file, so the inventory and financial data are persistent across sessions.

## 🚀 How to Use

Run the `main.py` file to start the program and follow the interactive menu:

```bash
python main.py

