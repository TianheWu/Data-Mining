import joblib
import re
from __Parameters import *
from __Data_process import modify_special_location, get_lat_lon, check_patient_location


# wrong_idx = [10, 36, 43, 48, 52, 55, 64, 80, 84, 90, 96, 104, 116,
# 127, 131, 134, 135, 136, 140, 172, 176, 195, 200, 207, 210, 213, 214, 227,
# 229, 235, 238, 242, 252, 253, 256, 258, 260, 267, 274, 275, 280, 281, 611,
# 727]
# wrong_key = list(map(str, wrong_idx))

patient_idx_info = {}
patient_idx_lat_lon = {}
patient_idx_locus = joblib.load('./patient/patient_idx_locus.pkl')

for key, val in patient_idx_locus.items():
    val = val.replace('。', '').replace('，', '。').replace('；', '。').replace('、', '。').replace(',', '。').replace('（', '').replace('“', '')
    val = val.split('。')
    if key not in patient_idx_info:
        patient_idx_info[key] = val[:3]

for key, val in patient_idx_info.items():
    is_include_digit = re.search(r'\d', val[LOCATION_INFO_IDX])
    if is_include_digit:
        val[LOCATION_INFO_IDX] = val[LOCATION_INFO_IDX][:is_include_digit.start()]
    val[LOCATION_INFO_IDX] = val[LOCATION_INFO_IDX].replace('现住', '').replace('人', '').replace('村民', '').replace('为', '').replace('第', '').replace('今日', '').replace('患者', '')
    temp_idx = val[LOCATION_INFO_IDX].find('在')
    if temp_idx != -1:
        val[LOCATION_INFO_IDX] = val[LOCATION_INFO_IDX][:temp_idx]
modify_special_location(patient_idx_info)
joblib.dump(patient_idx_info, './patient/' + 'patient_idx_info.pkl')

# check_patient_location(patient_idx_info)
for key, val in patient_idx_info.items():
    patient_lat_lon = get_lat_lon(val[LOCATION_INFO_IDX])
    if patient_lat_lon != '' and key not in patient_idx_lat_lon:
        lat_lon_list = patient_lat_lon.split(',', 1)
        lat_lon_list = list(map(float, lat_lon_list))
        lat_lon_list.reverse()
        patient_idx_lat_lon[key] = lat_lon_list
        print('patient', key, '|', 'location', lat_lon_list)
joblib.dump(patient_idx_lat_lon, './patient/' + 'patient_idx_lat_lon.pkl')

