import phonenumbers
from phonenumbers import NumberParseException, PhoneNumberFormat
def normalize_phone_number(number, region='US'):
    try:
        # Parse the phone number
        parsed_number = phonenumbers.parse(number, region)
        
        # Format the phone number in E.164 format
        normalized_number = phonenumbers.format_number(parsed_number, PhoneNumberFormat.E164)
        return normalized_number
    except NumberParseException:
        return None
