# Project 3: Bank Transaction & Fraud Monitoring System
# Project Goal:- 


# DB
Accounts = []
Transactions = []
Fraud_Alerts = []

# Generate Unique ID
unique_id = 0

# Menu
while True:
    print()
    print("========================================")
    print(" BANK TRANSACTION & FRAUD MONITORING")
    print("========================================")
    print()
    print("1.  Create Bank Account")
    print("2.  View All Accounts")
    print("3.  Search Account")
    print("4.  Update Account")
    print("5.  Delete Account")
    print()
    print("6.  Deposit Money")
    print("7.  Withdraw Money")
    print("8.  Check Account Balance")
    print("9.  Transfer Money")
    print()
    print("10. View All Transactions")
    print("11. Search Transaction")
    print("12. Filter Transactions by Account")
    print("13. Filter Transactions by Type")
    print("14. Sort Transactions")
    print()
    print("15. Detect Large Transactions")
    print("16. Detect Repeated Large Transactions")
    print("17. View Fraud Alerts")
    print("18. Review Fraud Alert")
    print()
    print("19. Account Statistics")
    print("20. Transaction Statistics")
    print("21. Fraud Statistics")
    print()
    print("22. Generate Bank Report")
    print("23. Exit")
    print()
    print("========================================")

    # User Menu Choice
    user_menu_choice = int(input("Enter Menu Option: "))

    # 1. Create Bank Account
    if user_menu_choice == 1:
        # Customer Name
        while True:
            customer_name = input("Enter Your Name: ").title()
            
            if len(customer_name) > 0:
                break
            print("Error, Invalid Name, Enter Again.")

        # Account Type
        while True:
            account_type = input("Enter Account Type (Savings | Current): ").title()

            if account_type == "Savings" or account_type == "Current":
                break
            print("Error, Invalid Account Type, Enter Again.")

        # Initial Deposit
        while True:
            initial_deposit = int(input("Enter Initial Deposit: "))

            if initial_deposit > 0:
                break
            print("Invalid Deposit, Enter Again.")

        unique_id += 1
        Accounts.append((unique_id, customer_name, account_type, initial_deposit))
        print("Details Added Successfully.")


    # 2. View All Accounts
    elif user_menu_choice == 2:

        # check if the list is empty.
        if len(Accounts) == 0:
            print("No Data Exist.")

        else:
            print("========== ALL BANK ACCOUNTS ==========")
            print()
            
            for view_accounts in Accounts:
                print(
                    " Account ID:", view_accounts[0],"\n",
                    "Account Name:", view_accounts[1],"\n",
                    "Account Type:", view_accounts[2],"\n",
                    "Balance: $", view_accounts[3], "\n",
                    "Account Status: Active", "\n",
                    "","\n",
                    "---------------------------------------"
                )
    
    # 3.  Search Account
    elif user_menu_choice == 3:

        # check if the list is empty.
        if len(Accounts) == 0:
            print("No Data Exist.")

        elif len(Accounts) >= 1:

            print()
            print("========== SEARCH BANK ACCOUNT ==========")
            # Ask for the Acoount Holder Name:
            search_account_name = str(input("Enter Account Holder Name: ")).title()

            for search_account in Accounts:
                if search_account[1] == search_account_name:
                    print()
                    print("Account Found!", "\n")
                    print(
                        " Account ID:", search_account[0],"\n",
                        "Account Name:", search_account[1],"\n",
                        "Account Type:", search_account[2],"\n",
                        "Balance: $", search_account[3], "\n",
                        "Account Status: Active", "\n"
                    )

        else:
            print("========== SEARCH BANK ACCOUNT ==========", "\n")
            print("Account Not Found.", "\n", "Enter Holder Name:", search_account_name, "\n")


    # 4.  Update Account
    elif user_menu_choice == 4:

        # check if the list is empty.
        if len(Accounts) == 0:
            print("No Data Exist")

        else:
            print("===== UPDATE ACCOUNT =====", "\n")
            # Ask for the Account Name.
            user_name_input = str(input("Enter Account Holder Name: ")).title()

            # Search for the account
            for search_user_name in Accounts:
                if search_account_name[1] == user_name_input:
                    print(
                        " Account ID:", search_account_name[0],"\n",
                        "Account Name:", search_account_name[1],"\n",
                        "Account Type:", search_account_name[2],"\n",
                        "Balance: $", search_account_name[3], "\n",
                        "Account Status: Active", "\n"
                    )

                    # update options
                    print("What would you like to update?", "\n")
                    print("1. Update Customer Name")
                    print("2. Update Account Type")
                    print("3. Update Account Status")
                    print("4. Back to Main Menu")

                    # which detail the user wants to update
                    update_choice = int(input("Enter Your Choice: "))

                    # 1. Update Customer Name
                    if update_choice == 1:
                        new_accout_holder_name = str(input("Enter New Customer Name: "))

                        if len(new_accout_holder_name) >= 1:
                            search_account_name[1] = new_accout_holder_name
                            print("\n", "Customer Name Updated Successfully!", "\n")
                            print("Updated Name: ", new_accout_holder_name)

                        else:
                            print("Error, Enter User Name Again.")
                    
                    # 2. Update Account Type
                    elif update_choice == 2:
                        new_account_type = str(input("Enter Account Type (Savings | Current): ")).title()

                        if new_account_type == "Savings" or new_account_type == "Current":
                            search_account_name[2] = new_account_type
                            print("\n", "Account Type Updated Successfully!", "\n")

                        else:
                            print("Error, Enter Account Name Again.")

                    # 3. Update Account Status
                    elif update_choice == 3:
                        pass

                    # 4. Back to Main Menu
                    elif update_choice == 4:
                        print("Back to Main Menu")
                        break

                    # Invalid Update Option
                    else:
                        print("Invalid Update Option")

    # 5 Exit
    elif user_menu_choice == 5:

        # # check if the list is empty.
        if len(Accounts) == 0:
            print("No bank accounts found")

        else:
            print("========== DELETE BANK ACCOUNT ==========", "\n")
            # Ask fir the Account Name
            delete_account_name = str(input("Enter Account Holder Name: ")).title()

            # Search for the account
            for search_account in Accounts:
                if search_account[1] == delete_account_name:
                    print("Account Found!")

                    print(
                        " Account ID:", search_account[0],"\n",
                        "Account Name:", search_account[1],"\n",
                        "Account Type:", search_account[2],"\n",
                        "Balance: $", search_account[3], "\n",
                        "Account Status: Active", "\n"
                    )

                    # check the account balance.
                    if search_account[3] <= 0:
                        print("Account cannot be deleted because it has a remaining balance.")

                    else:
                        print(
                            " Account ID:", search_account[0],"\n",
                            "Account Name:", search_account[1],"\n",
                            "Account Type:", search_account[2],"\n",
                            "Balance: $", search_account[3], "\n",
                            "Account Status: Active", "\n"
                        )

                        while True:
                            print("Are you sure you want to delete this account?", "\n")
                            print("1. Yes, Delete Account")
                            print("2. No, Cancel")
                            print("3. Exit")

                            # User's choice
                            users_delete_confirmaitons = int(input("Enter You'r Choice: "))

                            if users_delete_confirmaitons == 1:
                                Accounts.pop(search_account[0:])
                                print("Account Deleted Successfully.")

                            elif users_delete_confirmaitons == 2:
                                print("Account deletion cancelled.")

                            elif users_delete_confirmaitons == 3:
                                print("Return to the main menu.")
                                break
                            
                            else:
                                print("Invalid Delete Option Choice,")

    # 