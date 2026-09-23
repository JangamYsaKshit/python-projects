# Project: Personal Finance Analytics Engine
# Goal: The application manages a collection of financial transactions and converts them into useful financial information.


# DATA
Transaction_Data = []


# 1. Add Transaction 
def add_transaction():
    Transaction_id = int(input("Enter Transaction ID:"))

    # check whether ID already exists
    if Transaction_id not in Transaction_Data and Transaction_id > 0:
        Transaction_date = input("Enter Transactions Date (YYYY-MM-DD) Format:")
        Transaction_description = input("Enter Transactions Description:")
        Transaction_category = input("Enter Transactions Category:")
        Transaction_type = input("Enter Transactions Type, (Income/Expense):").upper()
        Transaction_amont = int(input("Enter Transactions Amount:"))

        if Transaction_amont <= 0:
            print("Error")

        else:
            Transaction_Data.append([Transaction_id, Transaction_date, Transaction_description, Transaction_category, Transaction_type, Transaction_amont])
            print("Transaction Added.")

    else:
        print("Error, ID already exists")

    print()


# 2. view transactions
def view_transactions():

    if len(Transaction_Data) == 0:
        print("No Transactions")

    else:
        for view in Transaction_Data:
                Transaction_id = view[0]
                Transaction_date = view[1]
                Transaction_description = view[2]
                Transaction_category = view[3]
                Transaction_type = view[4]
                Transaction_amont = view[5]

                print("ID:", Transaction_id,
                  "| Transaction Date:", Transaction_date,
                  "| Transaction Desctiption:", Transaction_description,
                  "| Transaction Category:", Transaction_category,
                  "| Transaction Type:", Transaction_type,
                  "| Transaction Amount:", Transaction_amont
                  )                    
    print() 


# 3. Search Transaction
def search_transaction():
    transaction_id = int(input("Enter Transaction ID: "))

    for search in Transaction_Data:
        if transaction_id == search[0]:
            transaction_id = search[0]
            transaction_date = search[1]
            transaction_description = search[2]
            transaction_category = search[3]
            transaction_type = search[4]
            transaction_amount = search[5]

            print("ID:", transaction_id,
                  "| Transaction Date:", transaction_date,
                  "| Transaction Desctiption:", transaction_description,
                  "| Transaction Category:", transaction_category,
                  "| Transaction Type:", transaction_type,
                  "| Transaction Amount:", transaction_amount
                )
            break

    else:
        print("Transactoin Not Found")


# 4. Financial Summary
def financial_summary():
    if len(Transaction_Data) != 0:
        total_income = 0
        total_expenses = 0

        for summary in Transaction_Data:
                transaction_id = summary[0]
                transaction_date = summary[1]
                transaction_description = summary[2]
                transaction_category = summary[3]
                transaction_type = summary[4]

                if summary[4] == "INCOME":
                    total_income = total_income + summary[5]

                elif summary[4] == "EXPENSE":
                    total_expenses = total_expenses + summary[5]

                transaction_amount = summary[5]

        print("Financial Summary")
        print(total_income)
        print(total_expenses)

        Balance = total_income - total_expenses
        print("Balance =", Balance)

    else:
        print("Error")


# 5. Expense Analysis
def expenses_analysis():
    total_expenses = 0
    expense_count = 0
    highest_expenses = 0
    lowest_expenses = 0

    for analysis in Transaction_Data:
        transaction_id = analysis[0]
        transaction_date = analysis[1]
        transaction_description = analysis[2]
        transaction_category = analysis[3]
        transaction_type = analysis[4]
        if analysis[4] == "Expense":
            total_expenses = total_expenses + analysis[5]
            expense_count += 1


            # For Highest Expenses
            if expense_count == 1:
                highest_expenses = analysis[5]

            else:
                if analysis[5] > highest_expenses:
                    highest_expenses = analysis[5]

            # For Lowest Expenses
            if expense_count == 1:
                lowest_expenses = analysis[5]

            else:
                if analysis[5] < lowest_expenses:
                    lowest_expenses = analysis[5]

        
    Total_expense = total_expenses
    Number_of_expense = expense_count
    average_expense = Total_expense / Number_of_expense
    transaction_amount = analysis[5]

    print("Expenses Analysis")
    print("-----------------")
    print("Total Expenses:",total_expenses)
    print()
    print("Highest Expenses:",highest_expenses)
    print("Lowest Expenses:",lowest_expenses)
    print()
    print("Average Expenses:",average_expense)


# 6. Category Analysis
def category_analysis():
    category_totals = {}
    if len(Transaction_Data) == 0:
        print("No Transactions")

    else:
        total_category = 0
        for category in Transaction_Data:
            if category[4] != "EXPENSE":
                print("")

            else:
                transaction_category = category[3]
                transaction_amount = category[5]
                if transaction_category in category_totals:
                    category_totals[category[3]] = category_totals[category[3]] + category[5]

                else:
                    category_totals[category[3]] = category[5]

    print("Category Analysis")
    for viewcategory, viewamount in category_totals.items():
        print("Category:",viewcategory,"| Amount", viewamount)


# 7.  Monthly Analysis
def monthly_analysis():
    monthly_structure = {}
    if len(Transaction_Data) == 0:
        print("No Transactions")

    else:
        for monthly in Transaction_Data:
            transaction_date = monthly[1][:7]
            transaction_amount = monthly[5]
            if transaction_date in monthly_structure:
                monthly_structure[monthly[1][:7]] = monthly_structure[monthly[1][:7]] + monthly[5]

            else:
                monthly_structure[monthly[1][:7]] = monthly[5]

    print("Monthly Analysis")
    for viewmonth, viewamount in monthly_structure.items():
        print("Month:",viewmonth,"| Amount:",viewamount)


# 8. Spending Statistics
def spending_statistics():
    if len(Transaction_Data) == 0:
        print("No Transaction")

    else:
        total_expenses = 0
        expense_count = 0
        highest_expense = 0
        lowest_expense = 0

        for spending in Transaction_Data:
            if spending[4] == "Expense":
                total_expenses = total_expenses + spending[5]
                expense_count += 1

                # First Expenses
                if expense_count == 1:
                    highest_expense = spending[5]
                    lowest_expense = spending[5]

                else:
                    if spending[5] > highest_expense:
                        highest_expense = spending[5]

                    if spending[5] < lowest_expense:
                        lowest_expense = spending[5]

        if expense_count == 0:
            print("No Expenses")

        else:
            average_expenses = total_expenses / expense_count

    print("Spending Statistice")
    print("-------------------")
    print("Total Expenses:",total_expenses)
    print("Number Of Expenses:",expense_count)
    print("Highest Expenses:",highest_expense)
    print("Lowest Expenses:",lowest_expense)
    print("Average Expenses:",average_expenses)


# 9. Financial Report
def financial_report():
    if len(Transaction_Data) == 0:
        print("No Transactions")

    else:
        financial_month = input("Enter Month | (Example:- 2026-08): ")

        monthly_income = 0
        monthly_expenses = 0
        income_count = 0
        expenses_count = 0

        for financial in Transaction_Data:
            if financial_month == financial[1][:7]:
                if financial[4] == "Income":
                    monthly_income = monthly_income + financial[5]
                    income_count += 1

                elif financial[4] == "Expense":
                    monthly_expenses = monthly_expenses + financial[5]
                    expenses_count += 1

        # AFTER the loop
        if income_count + expenses_count == 0:
            print("No Transaction Found For This Month!")

        else:
            total_balance = monthly_income - monthly_expenses

            print("Monthly Analysis")
            print("----------------")
            print("Total Income:", monthly_income)
            print("Total Expenses:", monthly_expenses)
            print("Balance:", total_balance)


# Menu
while True:

    print()
    print("====== Menu ======")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Search Transaction")
    print("4. Financial Summary")
    print("5. Expense Analysis ")
    print("6. Category Analysis")
    print("7. Monthly Analysis")
    print("8. Spending Statistics")
    print("9. Financial Report ")
    print("10. Exit")
    print("")

    user_menu = int(input("Enter Number:"))

    if user_menu == 1:
        add_transaction()

    elif user_menu == 2:
        view_transactions()

    elif user_menu == 3:
        search_transaction()

    elif user_menu == 4:
        financial_summary()

    elif user_menu == 5:
        expenses_analysis()

    elif user_menu == 6:
        category_analysis()

    elif user_menu == 7:
        monthly_analysis()

    elif user_menu == 8:
        spending_statistics()

    elif user_menu == 9:
        financial_report()

    elif user_menu == 10:
        print("Exit")
        break

    else:
        print("Invalid Menu Choice!")
