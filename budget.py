class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.budget = 0
        self.withdraws = 0

    def deposit(self, amount, description = ""):
        self.amount = amount
        self.ledger.append({"amount": self.amount, "description": description})
        self.budget += amount

    def withdraw(self, amount, description = ""):
      if self.check_funds(amount) == True:
        self.ledger.append({"amount": -1 * amount , "description": description})
        self.budget -= amount
        self.withdraws += amount
        return True
      else:
        return False

    def get_balance(self):
        return self.budget

    def check_funds(self, amount):
        if self.budget >= amount:
          # print("TRUE")
          return True
        else:
          # print("FALSE")
          return False


    def transfer(self, amount, category):
        category.deposit(amount, "Transfer from " + str(self.name))
        return self.withdraw(amount, "Transfer to " + str(category.name))
        
  
    def __str__(self):

        title = self.name.center(30, "*") + "\n"
        transactions = ""
        for transaction in self.ledger:
      
          if len(transaction['description']) < 23:
              spaces = (30 - len(str(transaction['description']) + format(transaction['amount'], '.2f'))) * " "
              transactions += str(transaction['description']) + spaces + format(transaction['amount'], '.2f') + "\n"
          else:
              transactions += str(transaction['description'])[0:23] + (7 - len(format(transaction['amount'], '.2f'))) * " " + format(transaction['amount'], '.2f') + "\n"
          
        total = "Total: " + str(self.budget)   
        balance = title + transactions + total 

        return balance

      
def create_spend_chart(categories):
  
    # Calculing the percentages from each category
  
    total_expenses = 0
    strings = []
  
    for category in categories:
        total_expenses += category.withdraws
        strings.append(category.name)       # Create a list with the names of each category


    pct_category = []

    for category in categories:
        pct_category.append(round(category.withdraws/total_expenses * 100, 0))
      
    # print(pct_category)
    rounded = []
    for pct in pct_category:
        if pct < 10:
            rounded.append(0)
        elif (pct % 10) / 10 > 0.5:
            rounded.append((pct // 10 + 1) * 10 )
        else:
            rounded.append((pct // 10) * 10 )

      
    # print(rounded)

    
    # Starts the string
    title = "Percentage spent by category\n"

    percentages = ["100| ", " 90| ", " 80| ", " 70| ", " 60| ", 
                   " 50| ", " 40| ", " 30| ", " 20| ", " 10| ", 
                   "  0| "]


    expenses = ""
    counter = 110

    ## Graphs the points ans spaces
    
    for percentage in percentages:
      
        counter = counter - 10
        expenses += percentage 

        for value in rounded:
          if counter > value:
            expenses += "   "
          else:
            expenses += "o  "
            
        expenses += "\n"

    # Graphs the lines for the report
    line = (" "* 4) + "-" + ("---"* len(rounded)) + "\n"

    # Graph the word below each percentage
    ## Finds the longest word in the string list
    longest = 0
    for text in strings:
      if len(text) > longest:
        longest = len(text)
        
    ## Normalize each word to get the same len to all the categogies
    for i in range(len(strings)):
      strings[i] = strings[i] + " " * (longest - len(strings[i]))

      
    ## Prints each letter.
    bottom = ""
    
    for i in range(len(strings[0])):
      bottom += "    "
      for text in strings:
        bottom += " " + text[i] + " "
    
      bottom += " \n"
      
    bottom = bottom.rstrip() + "  "
  
    return title + expenses + line + bottom

    
