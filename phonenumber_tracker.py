import phonenumbers
from phonenumbers import carrier, geocoder, timezone
print ('\n')
number = input('Enter phone number: ')
print ('Phone number details: \n')

phone_number = phonenumbers.parse(number)

print(f"Location: {geocoder.country_name_for_number(phone_number, 'en')}")
print(f"Carrier: {carrier.name_for_number(phone_number, 'en')}")
print(f"Time Zone: {timezone.time_zones_for_number(phone_number)}")
