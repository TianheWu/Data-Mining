import joblib
import folium
from matplotlib.pyplot import flag
import numpy

from __Parameters import *
from __Visualization_tools import add_point, add_circle, add_line, color_select, get_type_icon_color
from folium import plugins


map_covid = folium.Map(
    location = [CHOOSED_LAT, CHOOSED_LON],
    zoom_start = 13
)
incidents = plugins.MarkerCluster().add_to(map_covid)

patient_idx_lat_lon = joblib.load('./patient/patient_idx_lat_lon.pkl')
patient_idx_type = joblib.load('./patient/patient_idx_type.pkl')
patient_type_idx = joblib.load('./patient/patient_type_idx.pkl')

patient_type_max_idx = joblib.load('./location/patient_type_max_idx.pkl')
patient_type_min_idx = joblib.load('./location/patient_type_min_idx.pkl')
location_centers = joblib.load('./location/centers.pkl')

idx_condition = numpy.zeros(DATA_IDX_NUM + 1)
for key, val in patient_type_max_idx.items():
    idx_condition[int(val)] = TYPE_MAX_VAL
for key, val in patient_type_min_idx.items():
    idx_condition[int(val)] = TYPE_MIN_VAL

# draw point and circle
in_color = BASIC_COLOR
for key, val in patient_idx_lat_lon.items():
    int_key = int(key)
    extremum_color = ''
    flag_extremum = False

    # last patient in cluster
    if idx_condition[int_key] == TYPE_MAX_VAL:
        extremum_color = 'red'
        flag_extremum = True
    # first patient in cluster
    elif idx_condition[int_key] == TYPE_MIN_VAL:
        extremum_color = 'pink'
        flag_extremum = True

    circle_color = get_type_icon_color(patient_idx_type[key])
    add_circle([val[LAT_IDX], val[LON_IDX]], int(key), circle_color, 10, companent=incidents)
    # point_color = get_type_icon_color(patient_idx_type[key])
    if flag_extremum:
        add_point([val[LAT_IDX], val[LON_IDX]], int(key), extremum_color, companent=map_covid)
    # in_color = color_select(in_color)

for center in location_centers:
    center = list(center)
    add_circle(center, 0, 'blue', 200, companent=map_covid)



# draw line
# for key, val in patient_type_idx.items():
#     patient_type_idx[key] = list(map(int, val))
#     patient_type_idx[key].sort()
#     patient_type_idx[key] = list(map(str, patient_type_idx[key]))

# print(patient_type_idx)

# for key, val in patient_type_idx.items():
#     locations = numpy.empty([0, 2])
#     for i in val:
#         temp_location = numpy.array(patient_idx_lat_lon[str(i)]).reshape(1, 2)
#         locations = numpy.concatenate((locations, temp_location), axis=0)
#     add_line(locations, 'red', map_covid)

map_covid.add_child(incidents)
map_covid.save('./figure/map_covid_2.html')