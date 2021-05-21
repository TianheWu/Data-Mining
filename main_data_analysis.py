import numpy
import joblib

from __Parameters import *
from __Visualization_tools import visualization_kmeans
from __Data_process import get_min_val, get_max_val
from sklearn.cluster import KMeans


patient_idx_lat_lon = joblib.load('./patient/patient_idx_lat_lon.pkl')
lat_lon_info = numpy.empty([0, 2])
patient_idx_type = {}
patient_type_idx = {0:[], 1:[], 2:[], 3:[], 4:[]}
patient_type_min_idx = {0:0, 1:0, 2:0, 3:0, 4:0}
patient_type_max_idx = {0:0, 1:0, 2:0, 3:0, 4:0}

for key, val in patient_idx_lat_lon.items():
    temp_lat_lon = numpy.array(val).reshape(1, 2)
    lat_lon_info = numpy.concatenate((lat_lon_info, temp_lat_lon), axis=0)

k_means = KMeans(n_clusters=5, random_state=None).fit(lat_lon_info)
y_pred = k_means.predict(lat_lon_info)
visualization_kmeans(lat_lon_info, y_pred, k_means)
centers = k_means.cluster_centers_
labels = k_means.labels_

index_label = 0
for key in patient_idx_lat_lon.keys():
    if key not in patient_idx_type:
        patient_idx_type[key] = labels[index_label]
        patient_type_idx[labels[index_label]].append(key)
        index_label += 1
joblib.dump(patient_idx_type, './patient/patient_idx_type.pkl')
joblib.dump(patient_type_idx, './patient/patient_type_idx.pkl')

for key, val in patient_type_idx.items():
    patient_type_idx[key] = list(map(int, val))
    temp_min_val = get_min_val(patient_type_idx[key])
    temp_max_val = get_max_val(patient_type_idx[key])
    patient_type_min_idx[key] = str(temp_min_val)
    patient_type_max_idx[key] = str(temp_max_val)
    patient_type_idx[key] = list(map(str, val))

joblib.dump(patient_type_min_idx, './location/patient_type_min_idx.pkl')
joblib.dump(patient_type_max_idx, './location/patient_type_max_idx.pkl')
joblib.dump(centers, './location/centers.pkl')


