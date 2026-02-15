from datetime import datetime, timedelta

def getPastDateFromDays(days):
    # Calculate dates
    today = datetime.now()
    days_ago = today - timedelta(days)
    # Format dates for API (YYYY-MM-DD)
    return days_ago.strftime("%Y-%m-%d")

