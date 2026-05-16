import re

def extract_patterns(text):

    email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

    phone_pattern = r'\b\d{10}\b'

    date_pattern = r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b'

    emails = re.findall(email_pattern, text)

    phones = re.findall(phone_pattern, text)

    dates = re.findall(date_pattern, text)

    return {
        "emails": emails,
        "phones": phones,
        "dates": dates
    }