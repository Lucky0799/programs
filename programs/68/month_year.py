import calendar

def generate_calendar(year, month):
    # Create a TextCalendar instance
    cal = calendar.TextCalendar()

    # Generate the calendar for the specified month and year
    calendar_output = cal.formatmonth(year, month)

    return calendar_output

if __name__ == "__main__":
    # Input: Year and Month
    year = int(input("Enter the year: "))
    month = int(input("Enter the month (1-12): "))

    # Validate input
    if 1 <= month <= 12:
        # Generate and print the calendar
        calendar_result = generate_calendar(year, month)
        print(f"\nCalendar for {calendar.month_name[month]} {year}:\n")
        print(calendar_result)
    else:
        print("Invalid month. Please enter a month between 1 and 12.")
