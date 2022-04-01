import phonenumbers
from phonenumbers import timezone,geocoder,carrier
phone=input("your number in stating contry code : ")
number=phonenumbers.parse(phone)
time=timezone.time_zones_for_number(number)
cari=carrier.name_for_number(number, "en")
reditered=geocoder.description_for_number(number,"en")

print(number)
print(time)
print(cari)
print(reditered)