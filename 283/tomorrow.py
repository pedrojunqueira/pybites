from datetime import datetime, timedelta, date

def tomorrow(reference:datetime=None)->date:
    if not reference:
        reference = date.today()
    return reference + timedelta(days=1)