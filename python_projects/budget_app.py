'''

Budget App

Complete the Category class. It should be able to instantiate objects based on different budget categories like food, clothing, and entertainment. When objects are created, they are passed in the name of the category. The class should have an instance variable called ledger that is a list. The class should also contain the following methods:

    - A deposit method that accepts an amount and description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.
    - A withdraw method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method should return True if the withdrawal took place, and False otherwise.
    - A get_balance method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
    - A transfer method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.
    - A check_funds method that accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method.

When the budget object is printed it should display:

    - A title line of 30 characters where the name of the category is centered in a line of * characters.
    - A list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, then the amount. The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
    - A line displaying the category total.

Here is an example usage:

food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
print(food)

And here is an example of the output:

*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96

Besides the Category class, create a function (outside of the class) called create_spend_chart that takes a list of categories as an argument. It should return a string that is a bar chart.

The chart should show the percentage spent in each category passed in to the function. The percentage spent should be calculated only with withdrawals and not with deposits. Down the left side of the chart should be labels 0 - 100. The "bars" in the bar chart should be made out of the "o" character. The height of each bar should be rounded down to the nearest 10. The horizontal line below the bars should go two spaces past the final bar. Each category name should be written vertically below the bar. There should be a title at the top that says "Percentage spent by category".

This function will be tested with up to four categories.

Look at the example output below very closely and make sure the spacing of the output matches the example exactly.

Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     


TEST CASES

-The deposit method should create a specific object in the ledger instance variable.
-Calling the deposit method with no description should create a blank description.
-The withdraw method should create a specific object in the ledger instance variable.
-Calling the withdraw method with no description should create a blank description.
-The withdraw method should return True if the withdrawal took place.
-Calling food.deposit(900, "deposit") and food.withdraw(45.67, "milk, cereal, eggs, bacon, bread") should return a balance of 854.33.
-Calling the transfer method on a category object should create a specific ledger item in that category object.
-The transfer method should return True if the transfer took place.
-Calling transfer on a category object should reduce the balance in the category object.
-The transfer method should increase the balance of the category object passed as its argument.
-The transfer method should create a specific ledger item in the category object passed as its argument.
-The check_funds method should return False if the amount passed to the method is greater than the category balance.
-The check_funds method should return True if the amount passed to the method is not greater than the category balance.
-The withdraw method should return False if the withdrawal didn't take place.
-The transfer method should return False if the transfer didn't take place.
-Printing a Category instance should give a different string representation of the object.
-create_spend_chart should print a different chart representation. Check that all spacing is exact.

'''


class Category:

    instances = []

    def __init__(self, category):
        self.category = category
        Category.instances.append(self)
        self.ledger = []

    def __str__(self):
        line_length = 30
        text_length = len(self.category)
        asterisks_length = (line_length - text_length) // 2
        title_line = '*' * asterisks_length + self.category + '*' * asterisks_length
        # If the length of the text is odd, add an additional asterisk to the end
        if text_length % 2 != 0:
            title_line += '*'

        title_line += '\n'

        transactions_lines = ''
        for transaction in self.ledger:
            description = transaction['description']
            amount = "{:.2f}".format(transaction['amount'])
            amount_length = len(amount)
            description_length = len(description)
            if 30 - amount_length + 1 > description_length:
                no_of_space = 30 - (amount_length + description_length)
                transaction_line = description + ' ' * no_of_space + amount
            else:
                no_of_space = 1
                description_length_truncated = 30 - amount_length
                transaction_line = description[0:description_length_truncated-1] + \
                    ' ' * no_of_space + amount

            transactions_lines += transaction_line + '\n'

        total_line = 'Total: ' + "{:.2f}".format(self.get_balance())

        return title_line + transactions_lines + total_line

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append(
                {"amount": amount * (-1), "description": description})
            return True
        else:
            return False

    def get_balance(self):
        return sum(transaction['amount'] for transaction in self.ledger)

    def transfer(self, amount, destination_category):
        if self.check_funds(amount):
            if isinstance(destination_category, Category):
                self.withdraw(amount, 'Transfer to ' +
                              destination_category.category)
                destination_category.deposit(
                    amount, 'Transfer from ' + self.category)
                return True
        return False

    def check_funds(self, amount):
        if amount > sum(transaction['amount']
                        for transaction in self.ledger):
            return False
        else:
            return True

    @classmethod
    def get_instances(cls):
        return cls.instances


def create_spend_chart(categories):
    needed_instances = []

    all_instances = Category.get_instances()

    for category in categories:
        if category in all_instances:
            needed_instances.append(category)

    spend_data = []

    for instance in needed_instances:
        category = instance.category
        ledger = instance.ledger
        withdrawals = 0
        for transaction in ledger:
            if transaction['amount'] < 0:
                withdrawals += transaction['amount'] * -1
        spend_data.append({category: withdrawals})

    categories_list = []
    spend_data_per_category = []

    for item in spend_data:
        for cat, spend in item.items():
            categories_list.append(cat)

            spend_data_per_category.append(spend)

    total_withdrawals = sum(spend_data_per_category)
    spend_percentages = [(x / total_withdrawals) *
                         100 for x in spend_data_per_category]

    # Determine the maximum length of category name
    max_category_length = max(len(category) for category in categories_list)

    # Build the histogram string
    histogram_lines = []
    histogram_lines.append("Percentage spent by category")
    for i in range(100, -10, -10):
        line = "{:>3}| ".format(i)
        for percentage in spend_percentages:
            if percentage >= i:
                line += "o  "
            else:
                line += "   "
        histogram_lines.append(line)
    histogram_lines.append("    ----------")

    # Build the categories string
    categories_lines = []
    for i in range(max_category_length):
        category_line = "     "
        for category in categories_list:
            if i < len(category):
                category_line += category[i] + "  "
            else:
                category_line += "   "
        categories_lines.append(category_line)

    # Concatenate all lines into a single string
    result = "\n".join(histogram_lines + categories_lines)

    return result


food = Category("Food")
food.deposit(900, "deposit")
entertainment = Category("Entertainment")
entertainment.deposit(900, "deposit")
business = Category("Business")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

print(create_spend_chart([food, entertainment, business]))

# print(food.ledger)
