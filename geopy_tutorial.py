from geopy.distance import geodesic

# Calculating Distance Between Two Locations

# Coordinates of two Locations
location1 = (18.521428, 73.8544541) # Pune 
location2 = (19.0785451, 72.878176) # Mumbai
distance = geodesic(location1, location2). kilometers
print("Distance betwen City :", distance, "km")