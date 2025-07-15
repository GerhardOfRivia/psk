import folium
import math


def destination_point(lat1_deg, lon1_deg, distance_km, bearing_deg, r=6371.0):
    lat1 = math.radians(lat1_deg)
    lon1 = math.radians(lon1_deg)
    bearing = math.radians(bearing_deg)
    d_div_r = distance_km / r

    lat2 = math.asin(
        math.sin(lat1) * math.cos(d_div_r) +
        math.cos(lat1) * math.sin(d_div_r) * math.cos(bearing),
    )

    lon2 = lon1 + math.atan2(
        math.sin(bearing) * math.sin(d_div_r) * math.cos(lat1),
        math.cos(d_div_r) - math.sin(lat1) * math.sin(lat2),
    )

    return math.degrees(lat2), math.degrees(lon2)


def generate_circle(center_lat, center_lon, radius_km=200, total_points=360):
    lat_lon_list = []
    for angle in range(total_points+1):
        lat_lon = destination_point(center_lat, center_lon, radius_km, angle)
        lat_lon_list.append(lat_lon)
    return lat_lon_list


def main():
    center_lat = 37.6865
    center_lon = -71.8260

    lat_long_circle = generate_circle(center_lat, center_lon)

    # Create a folium map centered on the circle
    m = folium.Map(location=[center_lat, center_lon], zoom_start=15)
    # Add the circle path as a PolyLine
    folium.PolyLine(lat_long_circle, color='blue', weight=3).add_to(m)
    # Add a marker for the center
    folium.Marker([center_lat, center_lon], tooltip="Center").add_to(m)

    # Save the map to an HTML file
    m.save("circle_map.html")
    print("Map saved to circle_map.html")


if __name__ == "__main__":
    main()
