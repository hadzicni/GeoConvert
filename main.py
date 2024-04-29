from geopy.geocoders import Nominatim

def address_to_coordinates(address):
    geolocator = Nominatim(user_agent="geo_coder")
    location = geolocator.geocode(address)
    if location:
        latitude = location.latitude
        longitude = location.longitude
        print(f"Die Koordinaten für die Adresse '{address}' sind: {latitude}, {longitude}")
    else:
        print("Die Adresse konnte nicht geocodiert werden.")

def coordinates_to_address(latitude, longitude):
    geolocator = Nominatim(user_agent="geo_coder")
    location = geolocator.reverse((latitude, longitude))
    if location:
        address = location.address
        print(f"Die Adresse für die Koordinaten '{latitude}, {longitude}' ist: {address}")
    else:
        print("Die Koordinaten konnten nicht geocodiert werden.")

if __name__ == "__main__":
    print("Geocodierungstool")
    print("1. Adresse zu Koordinaten")
    print("2. Koordinaten zu Adresse")
    choice = input("Bitte wähle eine Option (1/2): ")
    
    if choice == "1":
        address = input("Bitte gib die Adresse ein: ")
        address_to_coordinates(address)
    elif choice == "2":
        latitude = float(input("Bitte gib die Breitengrad-Koordinate ein: "))
        longitude = float(input("Bitte gib die Längengrad-Koordinate ein: "))
        coordinates_to_address(latitude, longitude)
    else:
        print("Ungültige Option.")
