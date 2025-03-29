import json
import os

"""
    The Product class manages information related to a product in the vegan product store inventory.

    Instance attributes:
    _name (str): Product name. Default: None.
    _quantity (int): Available quantity in stock. Default: None.
    _buy_price (float): Purchase price of the product. Default: None.
    _sell_price (float): Selling price of the product. Default: None.

    Methods:
    __init__(self, name=None, quantity=None, buy_price=None, sell_price=None):
    Constructor of the class. Initializes the product attributes.

    Parameters:
    name (str, optional): Product name. Default: None.
    quantity (int, optional): Available quantity in stock. Default: None.
    buy_price (float, optional): Purchase price of the product. Default: None.
    sell_price (float, optional): Selling price of the product. Default: None.
"""

class Product:

  def __init__(self, name=None, quantity=None, buy_price=None, sell_price=None):
    self._name = name
    self._quantity = quantity
    self._buy_price = buy_price
    self._sell_price = sell_price

  '''
  Reading private class attributes with get methods:

  get_name(self): returns the product name.
  get_get_quantity(self): returns the quantity of the selected product.
  get_get_buy_price(self): returns the purchase price of the selected product.
  get_get_sell_price(self): returns the selling price of the selected product.

  '''

  def get_name(self):
    return self._name

  def get_quantity(self):
    return self._quantity

  def get_buy_price(self):
    return self._buy_price

  def get_sell_price(self):
    return self._sell_price


"""
    The Register class manages the inventory operations register.
    It provides functionality to save and load data to/from a JSON file.

    Instance attributes:
    _warehouse_reg (dict): Dictionary representing the warehouse register, containing products and related information.
      If not specified, it is initialized as an empty dictionary.
    _filename (str): Name of the JSON file where the warehouse register is saved. Default: "warehouse_register.json".
    _profits (list): List of sales transactions for profit calculation. Initialized as an empty list.
    _costs (list): List of purchase transactions for cost calculation. Initialized as an empty list.

    Methods:
    __init__(self, warehouse_reg=None, filename="warehouse_register.json"):
    Constructor of the class. Initializes the register and loads data from the JSON file if available.

    Parameters:
      - warehouse_reg (dict, optional): Initial product register. If None, it is initialized as an empty dictionary.
      - filename (str, optional): Name of the JSON file for saving/loading the register. Default: "warehouse_register.json".

    open_warehouse_reg_json():
    Method called in the constructor to load the register from the JSON file, if it exists.
"""

class Register:
  def __init__(self, warehouse_reg=None, filename="warehouse_register.json"):
    if warehouse_reg is None:
      warehouse_reg = {}
    self._warehouse_reg = warehouse_reg
    self._filename = filename
    self.open_warehouse_reg_json()
    self._profits=[]
    self._costs=[]

  """
  Reading private class attributes with get method:
  get_warehouse_reg(self): returns the warehouse register.
  """

  def get_warehouse_reg(self):
    return self._warehouse_reg

  """
  def open_warehouse_reg_json(self):
  Method called in the constructor to load the register from the JSON file, if it exists.
  If the warehouse register exists, the file is loaded
  If the warehouse register does not exist, an empty dictionary is created and initialized.
  If the program reports an exception in case the JSON file is corrupted or unreadable, the exception is handled.
  In that case, an empty dictionary will be created and initialized.

  """

  def open_warehouse_reg_json(self):
    try:
      if os.path.exists(self._filename):
        with open(self._filename, "r") as json_file:
          self._warehouse_reg = json.load(json_file)
        print("\nThe warehouse contains already registered products\n")
      else:
        self._warehouse_reg = {}
        with open(self._filename, "w") as json_file:
            json.dump(self._warehouse_reg, json_file, indent=4)
            print("\nThe list of products in the warehouse is empty!\n")

    except json.JSONDecodeError:
      print("\nCannot open file, a new one will be created.\n")
      self._warehouse_reg = {}
      with open(self._filename, "w") as json_file:
        json.dump(self._warehouse_reg, json_file, indent=4)

  """
  def save_product_json(self):
  Method called by functions that manage warehouse operations to save purchases and sales of each product in the warehouse register.
  """

  def save_product_json(self):
      with open(self._filename, "w") as json_file:
        json.dump(self._warehouse_reg, json_file, indent=4)
  """
  add_product(self, product):

   Records the addition of a new product (and related information) to the warehouse or the increase of the quantity of an existing product following a purchase.

    Parameters:
    product (Product): object of the Product class, obtained from the input_add_product function and passed to this function to be added to the warehouse.

    Operation:
    Uses the `get` methods defined in the Product class to obtain product information.
    Checks if the product is already present in the warehouse.

    1. If the product is already present:
    The additional quantity is recorded in the `self._costs` list to maintain the order history.
    The warehouse register is updated with the newly purchased units.

    2. If the product is not present:
    The product is added to the warehouse register.
    The `self._costs` list is updated with the purchase of the new product.

  """

  def add_product(self, product):
      product_name = product.get_name()
      product_quantity = product.get_quantity()
      product_buy_price = product.get_buy_price()

      if product_name in self._warehouse_reg:
            additional_quantity = product_quantity - self._warehouse_reg[product_name]['quantity']
            if additional_quantity > 0:
                self._costs.append({
                    "product": product_name,
                    "quantity": additional_quantity,
                    "price": product_buy_price
                })
            self._warehouse_reg[product_name]['quantity'] += product.get_quantity()

      else:
            self._costs.append({
                "product": product_name,
                "quantity": product_quantity,
                "price": product_buy_price
            })

            self._warehouse_reg[product_name] = {
                'quantity': product.get_quantity(),
                'buy_price': product.get_buy_price(),
                'sell_price': product.get_sell_price()
            }

      self.save_product_json()
  """
  sell_product(self, product):

   Records the sale of a product by updating the quantity available in the warehouse.

    Parameters:
    product (Product): object of the Product class, obtained from the `input_sell_product` function,
                       representing the product to be sold.

    Operation:
    Checks that `product` is not None.
    Updates the quantity available in the warehouse.
    Saves the updated register in JSON format.
  """

  def sell_product(self, product):
      if product is None:
        return

      product_name = product.get_name()
      self._warehouse_reg[product_name]['quantity'] = product.get_quantity()
      self.save_product_json()

  """
  profits(self):

  Calculates the overall gross profit by accessing the cumulative list of all sales made.
  Gross profit is defined as the sum of revenues generated from the sale of each product, equal to selling price * quantity sold.
  """

  def profits(self):
        gross_profit = 0
        for item in self._profits:
            product_name = item["product"]
            product_quantity = item["quantity"]
            unit_price = item["price"]

            revenue = product_quantity * unit_price
            gross_profit += revenue

        print(f"Gross Profit: {gross_profit}\n")

  """
  costs(self):

  Calculates the overall costs by accessing the cumulative list of all purchases made.
  Total costs are defined as the sum of costs incurred for the purchase of each product, equal to purchase price * quantity purchased.
  Finally, it checks if profits from sales have also been recorded in self._profits and if so, calculates the net profit.
  Net profit is equal to the sum of all quantities sold and selling prices for each product (gross profit), minus total costs.
  """

  def costs (self):
      total_costs=0

      for item in self._costs:
            product_name = item["product"]
            product_quantity = item["quantity"]
            unit_price = item["price"]
            costs = product_quantity * unit_price
            total_costs += costs

      print(f"Total Costs: {total_costs}\n")

      if self._profits:
          net_profit = sum(item["quantity"] * item["price"] for item in self._profits) - total_costs
          print(f"Net Profit: {net_profit}\n")

  """
  transaction (self, transaction_items):

  Calculates the total amount sold in the single sales operation, reporting the sales data (product, quantity, price, and total sold) recorded inside the cycle.
  If a subsequent sales operation is carried out, the transaction list is reset, so that the transaction summary does not give a cumulative result of all sales operations.
  """

  def transaction (self, transaction_items):
    total_sold =0
    for item in transaction_items:
        product_name = item["product"]
        product_quantity = item ["quantity"]
        unit_price = item["price"]

        total_price = product_quantity*unit_price

        total_sold +=total_price

        print(f"Product: {product_name}, Quantity: {product_quantity}, Unit price: {unit_price}, Total price: {total_price}\n")
        print(f"Total sold: {total_sold}\n")
  """
  print_warehouse(self):
  Lists the products present in the warehouse register (if any) summarizing the product, quantity, and price of each.
  If there are no products in the warehouse, it provides a message informing that the warehouse is empty.

  """

  def print_warehouse(self):
      if not self._warehouse_reg:
          print("\nThe warehouse is empty.\n")
      else:
          print("\nPRODUCT QUANTITY PRICE\n")
          for product, data in self._warehouse_reg.items():
            quantity = data.get('quantity', 0)
            price = data.get('sell_price', 0)
            print(f"{product} {quantity} €{price}\n")

"""
Helper function to validate numeric input
Ensures the input is a valid number and optionally checks if it's positive

Parameters:
prompt (str): The message to display when requesting input
is_float (bool): Whether to accept floating point numbers
positive_only (bool): Whether to enforce positive values only

Returns:
float or int: The validated numeric value
"""
def validate_numeric_input(prompt, is_float=True, positive_only=True):
    while True:
        try:
            user_input = input(prompt).strip()
            if is_float:
                value = float(user_input)
            else:
                value = int(user_input)
                
            if positive_only and value <= 0:
                print("\nValue must be positive. Please try again.\n")
                continue
                
            return value
        except ValueError:
            print("\nInvalid input. Please enter a valid number.\n")

"""
Helper function to validate yes/no responses

Parameters:
prompt (str): The message to display when requesting input

Returns:
bool: True for 'yes', False for 'no'
"""
def validate_yes_no_input(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response == "yes" or response == "y":
            return True
        elif response == "no" or response == "n":
            return False
        else:
            print("\nInvalid response! Please enter 'yes' or 'no'.\n")

"""
    Manages user input to add a new product to the warehouse.

    This function asks the user to enter the necessary information for a new product (name, quantity, purchase price, and selling price) not present in the warehouse.
    If the product already exists, it only asks for the additional quantity if the selling price and purchase price are present in the register, otherwise it also asks to add this information.
    Handles input validation and displays appropriate error messages.

    Arguments:
    warehouse_reg (Register): The instance of the warehouse register.

    Result:
    Product: returns a new Product object with the information entered by the user.

    Exception handling:
    AssertionError: If the user's input is not valid.
    ValueError: If the numeric input is not valid.
"""

def input_add_product(warehouse_reg):
  while True:
    try:
        add_new_product = input("Product name: \n").strip().title()
        assert add_new_product != "", "Product name cannot be empty. Try again.\n"

        if add_new_product in warehouse_reg.get_warehouse_reg():
          print(f"\nProduct {add_new_product} already present in warehouse.\n")
          
          quantity_to_add = validate_numeric_input("Quantity: \n", is_float=False, positive_only=True)
          print(f"Quantity added to {add_new_product} equal to {quantity_to_add}.\n")

          existing_product = warehouse_reg.get_warehouse_reg()[add_new_product]

          if 'buy_price' not in existing_product or 'sell_price' not in existing_product:
                    print(f"The existing product {add_new_product} does not have a registered purchase or selling price.")
                    buy_price = validate_numeric_input("Purchase price: \n", is_float=True, positive_only=True)
                    sell_price = validate_numeric_input("Selling price: \n", is_float=True, positive_only=True)

                    existing_product['buy_price'] = buy_price
                    existing_product['sell_price'] = sell_price


          return Product(name=add_new_product,
                      quantity=existing_product['quantity'] + quantity_to_add,
                      buy_price=existing_product['buy_price'],
                      sell_price=existing_product['sell_price'])

          warehouse_reg._costs.append({"product": add_new_product, "quantity": quantity_to_add, "price": buy_price})

        else:
          buy_price = validate_numeric_input("Purchase price: \n", is_float=True, positive_only=True)
          sell_price = validate_numeric_input("Selling price: \n", is_float=True, positive_only=True)
          quantity = validate_numeric_input("Quantity: \n", is_float=False, positive_only=True)
          
          return Product(name=add_new_product, quantity=quantity,
                                  buy_price=buy_price, sell_price=sell_price)


    except AssertionError as e:
      print("\nAn error occurred:", e)

"""
    Manages user input to record the sale of a product.

    This function asks the user to enter the necessary information to sell a product present in the warehouse (name and quantity)
    If the product is not present in the warehouse, it reports this and asks the user to try again.
    If the product is present in the warehouse, it records the sale and asks the user if they want to continue by adding another product.
    When the user decides to end the sales process, a summary of the sale is displayed with information on the products sold and the total selling price.
    Handles input validation and displays appropriate error messages.

    Arguments:
    warehouse_reg (Register): The instance of the warehouse register.
    transaction: the list that records warehouse movements in the sales cycle to summarize the total sold at the end of the operation.

    Result:
    Product: returns a new Product object with the information entered by the user.

    Exception handling:
    AssertionError: If the user's input is not valid.
"""

def input_sell_product(warehouse_reg, transaction):
  while True:
    try:
      sell_product = input("Product name to sell: \n").strip().title()
      assert sell_product != "", "\nProduct name cannot be empty. Try again.\n"

      if not sell_product in warehouse_reg.get_warehouse_reg():
          print(f"Product {sell_product} not present in warehouse.\n")

          if validate_yes_no_input(f"Try with another product? [yes/no]\n"):
              continue
          else:
              return None

      else:
        existing_product = warehouse_reg.get_warehouse_reg()[sell_product]
        sell_price = existing_product['sell_price']
        
        quantity_to_sell = validate_numeric_input("Quantity: \n", is_float=False, positive_only=True)
        
        if quantity_to_sell > existing_product['quantity']:
          print(f"You are selling a quantity of {sell_product} not available in warehouse\n")
          return None
          
        existing_product['quantity'] -= quantity_to_sell
        print(f"Sale Registered\n {quantity_to_sell}X {sell_product}: {sell_price}.\n")
        warehouse_reg.save_product_json()

        transaction.append({"product":sell_product, "quantity":quantity_to_sell, "price":sell_price})
        warehouse_reg._profits.append({"product": sell_product, "quantity": quantity_to_sell, "price": sell_price})

        if validate_yes_no_input(f"Add another product? [yes/no]\n"):
           continue
        else:
          return Product(name=sell_product,
            quantity=existing_product['quantity'],
            buy_price=existing_product['buy_price'],
            sell_price=existing_product['sell_price'])

    except AssertionError as e:
      print("\nAn error occurred:", e)


"""
    Main function of the warehouse management program.

    Initializes the system, creates an instance of the warehouse register
    and manages the main program cycle, presenting a menu
    to the user and calling the appropriate functions based on the user's choices.

"""
def main():


  warehouse_reg = Register()
  profits=[]

  try:
      cmd = None
      while cmd!="exit":
        cmd = input("Hello! Choose which operation to perform:\n"
                  "1. add\n"
                  "2. list\n"
                  "3. sale\n"
                  "4. profits\n"
                  "5. help\n"
                  "6. exit\n").strip()


        assert cmd != "", "Enter the name of the chosen operation.\n"

        if cmd =="add":
          print("\nYou requested operation 1: Register a new product\n")
          new_product = input_add_product(warehouse_reg)
          warehouse_reg.add_product(new_product)

        elif cmd =="list":
          print("\nYou requested operation 2: List products in warehouse\n")
          warehouse_reg.print_warehouse()

        elif cmd =="sale":
          transaction= []
          print("\nYou requested operation 3: Register a sale\n")
          sell_product = input_sell_product(warehouse_reg, transaction)
          warehouse_reg.sell_product(sell_product)
          warehouse_reg.transaction(transaction)

        elif cmd =="profits":
          warehouse_reg.profits()
          warehouse_reg.costs()

        elif cmd =="help":
          print("1. add: register new products, with name, quantity, selling price and purchase price.\n"
                  "2. list: list all products present in the warehouse.\n"
                  "3. sale: register sales made for each product and display the receipt.\n"
                  "4. profits: show total gross and net profits accumulated.\n"
                  "5. help: display the menu with the description of commands\n"
                  "6. exit: terminate program execution.\n")

        elif cmd =="exit":
          print("bye bye\n")
        else:
          print("The command you entered is not valid, try again!\n")

  except AssertionError as e:
    print(e)

  print(f"End\n.")

main()
