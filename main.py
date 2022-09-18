def canonicalize_date(date_str):
    """
    Canonicalize a date string to the format YYYY-MM-DD.

    Args:
        date_str (str): A date string in the format yyyy-mm-dd or mm/dd/yyyy or MonthName   dd   yyyy.

    Returns:
        str: The date string in the format YYYY-MM-DD.
    """
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    date_list = date_str.split()
    if len(date_list) == 1:
        date_list = date_list[0].split("/")
    if len(date_list) == 1:
        date_list = date_list[0].split("-")
    if date_list[0] in months:
        day = date_list[1]
        year = date_list[2]
        month_num = 0
        for i in range(len(months)):
            if date_list[0] == months[i]:
                month_num = i + 1
        return "{:d}-{:d}-{:d}".format(int(year), int(month_num), int(day))
    if 0 < int(date_list[0]) < 13:
        month_num = date_list[0]
        day = date_list[1]
        year = date_list[2]
        return "{:d}-{:d}-{:d}".format(int(year), int(month_num), int(day))
    if len(date_list[0]) == 4:
        year = date_list[0]
        month_num = date_list[1]
        day = date_list[2]
        return "{:d}-{:d}-{:d}".format(int(year), int(month_num), int(day))
