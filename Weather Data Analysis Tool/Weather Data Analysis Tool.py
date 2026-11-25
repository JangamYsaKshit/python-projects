# ==========================================
# Project: Weather Data Analysis Tool
# Pure Python Project
# ==========================================

# Database
Weather_Data = []

# Unique ID
unique_id = 0


# Main Menu
while True:
    print()
    print("======================================")
    print("       WEATHER DATA ANALYSIS TOOL")
    print("======================================")
    print("1. Add Weather Record")
    print("2. View All Weather Records")
    print("3. Search Weather Record")
    print("4. Update Weather Record")
    print("5. Delete Weather Record")
    print("6. Temperature Analysis")
    print("7. Rainfall Analysis")
    print("8. Monthly Weather Analysis")
    print("9. Overall Weather Statistics")
    print("10. Generate Weather Report")
    print("11. View Total Weather Records")
    print("12. Exit")
    print()

    try:
        user_menu_input = int(input("Enter Menu Choice: "))
    except ValueError:
        print("Invalid Menu Choice. Please Enter a Number.")
        continue

    # 1. Add Weather Record
    if user_menu_input == 1:
        print()
        print("--- Add Weather Record ---")

        while True:
            weather_date = input("Enter Date (DD-MM-YYYY): ").strip()

            if len(weather_date) == 10 and weather_date[2] == "-" and weather_date[5] == "-":
                date_parts = weather_date.split("-")

                if len(date_parts) == 3 and all(part.isdigit() for part in date_parts):
                    day = int(date_parts[0])
                    month = int(date_parts[1])
                    year = int(date_parts[2])

                    if 1 <= day <= 31 and 1 <= month <= 12 and year > 0:
                        break

            print("Invalid Date Format. Use DD-MM-YYYY.")

        while True:
            weather_city = input("Enter City Name: ").strip().title()

            if weather_city:
                break

            print("City Name Cannot Be Empty.")

        while True:
            try:
                weather_temperature = float(input("Enter Temperature: "))
                break
            except ValueError:
                print("Please Enter a Valid Number.")

        while True:
            try:
                weather_humidity = int(input("Enter Humidity (0-100): "))

                if 0 <= weather_humidity <= 100:
                    break

                print("Humidity Must Be Between 0 and 100.")

            except ValueError:
                print("Please Enter a Whole Number.")

        while True:
            try:
                weather_rainfall = float(input("Enter Rainfall (mm): "))

                if weather_rainfall >= 0:
                    break

                print("Rainfall Cannot Be Negative.")

            except ValueError:
                print("Please Enter a Valid Number.")

        unique_id += 1

        Weather_Data.append((
            unique_id,
            weather_date,
            weather_city,
            weather_temperature,
            weather_humidity,
            weather_rainfall
        ))

        print("Weather Record Added Successfully.")
        print("Record ID:", unique_id)

    # 2. View All Weather Records
    elif user_menu_input == 2:
        if len(Weather_Data) == 0:
            print("No Weather Data Available.")

        else:
            print()
            print("--- All Weather Records ---")

            for weather_record in Weather_Data:
                print(
                    "ID:", weather_record[0],
                    "| Date:", weather_record[1],
                    "| City:", weather_record[2],
                    "| Temperature:", weather_record[3], "°C",
                    "| Humidity:", weather_record[4], "%",
                    "| Rainfall:", weather_record[5], "mm"
                )

    # 3. Search Weather Record
    elif user_menu_input == 3:
        while True:
            print()
            print("--- Search Weather Record ---")
            print("1. Search By Record ID")
            print("2. Search By Date")
            print("3. Search By City")
            print("4. Return To Main Menu")

            try:
                search_menu = int(input("Enter Search Option: "))
            except ValueError:
                print("Please Enter a Number.")
                continue

            if search_menu == 4:
                break

            elif search_menu not in [1, 2, 3]:
                print("Invalid Search Option.")
                continue

            elif len(Weather_Data) == 0:
                print("No Weather Data Available.")
                continue

            matching_records = []

            if search_menu == 1:
                try:
                    search_id = int(input("Enter Record ID: "))
                except ValueError:
                    print("Invalid Record ID.")
                    continue

                for weather_record in Weather_Data:
                    if weather_record[0] == search_id:
                        matching_records.append(weather_record)

            elif search_menu == 2:
                search_date = input("Enter Date (DD-MM-YYYY): ").strip()

                for weather_record in Weather_Data:
                    if weather_record[1] == search_date:
                        matching_records.append(weather_record)

            elif search_menu == 3:
                search_city = input("Enter City Name: ").strip()

                for weather_record in Weather_Data:
                    if weather_record[2].casefold() == search_city.casefold():
                        matching_records.append(weather_record)

            if len(matching_records) == 0:
                print("No Matching Records Found.")

            else:
                print("--- Search Results ---")

                for weather_record in matching_records:
                    print(
                        "ID:", weather_record[0],
                        "| Date:", weather_record[1],
                        "| City:", weather_record[2],
                        "| Temperature:", weather_record[3], "°C",
                        "| Humidity:", weather_record[4], "%",
                        "| Rainfall:", weather_record[5], "mm"
                    )

    # 4. Update Weather Record
    elif user_menu_input == 4:
        if len(Weather_Data) == 0:
            print("No Weather Data Available.")

        else:
            try:
                search_id = int(input("Enter Record ID: "))
            except ValueError:
                print("Invalid Record ID.")
                continue

            record_found = False

            for record_index, weather_record in enumerate(Weather_Data):
                if weather_record[0] == search_id:
                    record_found = True
                    updated_record = list(weather_record)

                    while True:
                        print()
                        print("--- Update Weather Record ---")
                        print("1. Update Date")
                        print("2. Update City")
                        print("3. Update Temperature")
                        print("4. Update Humidity")
                        print("5. Update Rainfall")
                        print("6. Finish Updating")

                        try:
                            update_choice = int(input("Enter Option: "))
                        except ValueError:
                            print("Please Enter a Number.")
                            continue

                        if update_choice == 1:
                            new_date = input("Enter New Date (DD-MM-YYYY): ").strip()
                            updated_record[1] = new_date
                            print("Date Updated.")

                        elif update_choice == 2:
                            new_city = input("Enter New City: ").strip().title()

                            if new_city:
                                updated_record[2] = new_city
                                print("City Updated.")
                            else:
                                print("City Cannot Be Empty.")

                        elif update_choice == 3:
                            try:
                                updated_record[3] = float(input("Enter New Temperature: "))
                                print("Temperature Updated.")
                            except ValueError:
                                print("Invalid Temperature.")

                        elif update_choice == 4:
                            try:
                                new_humidity = int(input("Enter New Humidity: "))

                                if 0 <= new_humidity <= 100:
                                    updated_record[4] = new_humidity
                                    print("Humidity Updated.")
                                else:
                                    print("Humidity Must Be Between 0 and 100.")

                            except ValueError:
                                print("Invalid Humidity.")

                        elif update_choice == 5:
                            try:
                                new_rainfall = float(input("Enter New Rainfall: "))

                                if new_rainfall >= 0:
                                    updated_record[5] = new_rainfall
                                    print("Rainfall Updated.")
                                else:
                                    print("Rainfall Cannot Be Negative.")

                            except ValueError:
                                print("Invalid Rainfall.")

                        elif update_choice == 6:
                            break

                        else:
                            print("Invalid Option.")

                    Weather_Data[record_index] = tuple(updated_record)
                    print("Weather Record Updated Successfully.")
                    break

            if not record_found:
                print("Record ID Not Found.")

    # 5. Delete Weather Record
    elif user_menu_input == 5:
        if len(Weather_Data) == 0:
            print("No Weather Data Available.")

        else:
            try:
                search_id = int(input("Enter Record ID: "))
            except ValueError:
                print("Invalid Record ID.")
                continue

            record_found = False

            for weather_record in Weather_Data:
                if weather_record[0] == search_id:
                    record_found = True

                    print("Record Found:", weather_record)

                    confirmation = input("Confirm Delete (Yes/No): ").strip().title()

                    if confirmation == "Yes":
                        Weather_Data.remove(weather_record)
                        print("Record Deleted Successfully.")

                    else:
                        print("Delete Cancelled.")

                    break

            if not record_found:
                print("Record ID Not Found.")

    # 6. Temperature Analysis
    elif user_menu_input == 6:
        if len(Weather_Data) == 0:
            print("No Weather Data Available.")

        else:
            while True:
                print()
                print("--- Temperature Analysis ---")
                print("1. Average Temperature")
                print("2. Highest Temperature")
                print("3. Lowest Temperature")
                print("4. Temperature By City")
                print("5. Temperature By Date")
                print("6. Return To Main Menu")

                try:
                    analysis_choice = int(input("Enter Option: "))
                except ValueError:
                    print("Please Enter a Number.")
                    continue

                if analysis_choice == 6:
                    break

                elif analysis_choice == 1:
                    temperatures = [record[3] for record in Weather_Data]
                    print("Average Temperature:", round(sum(temperatures) / len(temperatures), 2), "°C")

                elif analysis_choice == 2:
                    highest = max(record[3] for record in Weather_Data)
                    print("Highest Temperature:", highest, "°C")

                    for record in Weather_Data:
                        if record[3] == highest:
                            print("City:", record[2], "| Date:", record[1])

                elif analysis_choice == 3:
                    lowest = min(record[3] for record in Weather_Data)
                    print("Lowest Temperature:", lowest, "°C")

                    for record in Weather_Data:
                        if record[3] == lowest:
                            print("City:", record[2], "| Date:", record[1])

                elif analysis_choice == 4:
                    search_city = input("Enter City Name: ").strip()
                    city_records = [
                        record for record in Weather_Data
                        if record[2].casefold() == search_city.casefold()
                    ]

                    if len(city_records) == 0:
                        print("City Not Found.")
                    else:
                        temperatures = [record[3] for record in city_records]
                        print("Average:", round(sum(temperatures) / len(temperatures), 2))
                        print("Highest:", max(temperatures))
                        print("Lowest:", min(temperatures))

                elif analysis_choice == 5:
                    search_date = input("Enter Date: ").strip()
                    date_records = [
                        record for record in Weather_Data
                        if record[1] == search_date
                    ]

                    if len(date_records) == 0:
                        print("Date Not Found.")
                    else:
                        for record in date_records:
                            print("City:", record[2], "| Temperature:", record[3], "°C")

                else:
                    print("Invalid Option.")

    # 7. Rainfall Analysis
    elif user_menu_input == 7:
        if len(Weather_Data) == 0:
            print("No Weather Data Available.")

        else:
            while True:
                print()
                print("--- Rainfall Analysis ---")
                print("1. Total Rainfall")
                print("2. Average Rainfall")
                print("3. Highest Rainfall")
                print("4. Rainiest Day")
                print("5. Count Rainy Records")
                print("6. Rainfall By City")
                print("7. Return To Main Menu")

                try:
                    rainfall_choice = int(input("Enter Option: "))
                except ValueError:
                    print("Please Enter a Number.")
                    continue

                if rainfall_choice == 7:
                    break

                elif rainfall_choice == 1:
                    total = sum(record[5] for record in Weather_Data)
                    print("Total Rainfall:", round(total, 2), "mm")

                elif rainfall_choice == 2:
                    average = sum(record[5] for record in Weather_Data) / len(Weather_Data)
                    print("Average Rainfall:", round(average, 2), "mm")

                elif rainfall_choice == 3:
                    highest = max(record[5] for record in Weather_Data)
                    print("Highest Rainfall:", highest, "mm")

                elif rainfall_choice == 4:
                    highest = max(record[5] for record in Weather_Data)

                    for record in Weather_Data:
                        if record[5] == highest:
                            print("Rainiest Day:", record[1], "| City:", record[2], "| Rainfall:", highest)

                elif rainfall_choice == 5:
                    rainy_records = sum(1 for record in Weather_Data if record[5] > 0)
                    print("Rainy Records:", rainy_records)

                elif rainfall_choice == 6:
                    search_city = input("Enter City Name: ").strip()

                    city_records = [
                        record for record in Weather_Data
                        if record[2].casefold() == search_city.casefold()
                    ]

                    if len(city_records) == 0:
                        print("City Not Found.")
                    else:
                        total = sum(record[5] for record in city_records)
                        average = total / len(city_records)

                        print("Total Rainfall:", round(total, 2), "mm")
                        print("Average Rainfall:", round(average, 2), "mm")

                else:
                    print("Invalid Option.")

    # 8. Monthly Weather Analysis
    elif user_menu_input == 8:
        if len(Weather_Data) == 0:
            print("No Weather Data Available.")

        else:
            monthly_data = {}

            for record in Weather_Data:
                date_parts = record[1].split("-")

                if len(date_parts) != 3:
                    continue

                month_key = date_parts[1] + "-" + date_parts[2]

                if month_key not in monthly_data:
                    monthly_data[month_key] = []

                monthly_data[month_key].append(record)

            print("--- Monthly Weather Analysis ---")

            for month, records in monthly_data.items():
                temperatures = [record[3] for record in records]
                rainfall = sum(record[5] for record in records)

                print()
                print("Month:", month)
                print("Total Records:", len(records))
                print("Average Temperature:", round(sum(temperatures) / len(temperatures), 2))
                print("Highest Temperature:", max(temperatures))
                print("Lowest Temperature:", min(temperatures))
                print("Total Rainfall:", round(rainfall, 2), "mm")

    # 9. Overall Weather Statistics
    elif user_menu_input == 9:
        if len(Weather_Data) == 0:
            print("No Weather Data Available.")

        else:
            temperatures = [record[3] for record in Weather_Data]
            humidity = [record[4] for record in Weather_Data]
            rainfall = [record[5] for record in Weather_Data]

            cities = set(record[2] for record in Weather_Data)

            print("--- Overall Weather Statistics ---")
            print("Total Records:", len(Weather_Data))
            print("Total Cities:", len(cities))
            print("Average Temperature:", round(sum(temperatures) / len(temperatures), 2))
            print("Highest Temperature:", max(temperatures))
            print("Lowest Temperature:", min(temperatures))
            print("Average Humidity:", round(sum(humidity) / len(humidity), 2), "%")
            print("Total Rainfall:", round(sum(rainfall), 2), "mm")
            print("Average Rainfall:", round(sum(rainfall) / len(rainfall), 2), "mm")

    # 10. Generate Weather Report
    elif user_menu_input == 10:
        if len(Weather_Data) == 0:
            print("No Weather Data Available.")

        else:
            temperatures = [record[3] for record in Weather_Data]
            rainfall = [record[5] for record in Weather_Data]

            print()
            print("========== WEATHER REPORT ==========")
            print("Total Records:", len(Weather_Data))
            print("Cities:", ", ".join(sorted(set(record[2] for record in Weather_Data))))
            print("Average Temperature:", round(sum(temperatures) / len(temperatures), 2), "°C")
            print("Highest Temperature:", max(temperatures), "°C")
            print("Lowest Temperature:", min(temperatures), "°C")
            print("Total Rainfall:", round(sum(rainfall), 2), "mm")
            print("Average Rainfall:", round(sum(rainfall) / len(rainfall), 2), "mm")
            print("====================================")

    # 11. View Total Weather Records
    elif user_menu_input == 11:
        print("Total Weather Records:", len(Weather_Data))

    # 12. Exit
    elif user_menu_input == 12:
        print("Thank You For Using Weather Data Analysis Tool.")
        break

    else:
        print("Invalid Menu Choice. Please Select Between 1 and 12.")
