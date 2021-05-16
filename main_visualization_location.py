import joblib
import folium
from __Data_process import parse_zhch


patient_idx_lat_lon = joblib.load('./patient/patient_idx_lat_lon.pkl')
for key, val in patient_idx_lat_lon.items():
    print(key, val)

# map_covid = folium.Map(
#     location = [37.8957, 114.9042],
#     zoom_start = 4
# )
# map_covid.save('map.html')
