from folium.vector_layers import path_options
import jieba
import requests
import json
import joblib

from __Parameters import *


def participle(text_string):
    seg_list = jieba.cut(text_string)
    print(", ".join(seg_list))


def check_patient_location(patient_idx_info):
    for key, val in patient_idx_info.items():
        print('patient', key, '|', 'location', val[LOCATION_INFO_IDX])


def check_patient_lat_lon(patient_idx_lat_lon):
    for key, val in patient_idx_lat_lon.items():
        print('patient', key, '|', 'location', val)


def check_date_num(date_num):
    for key, val in date_num.items():
        print('data', key, '|', 'num', val)


# chinese
def parse_zhch(s):
    return str(str(s).encode('ascii', 'xmlcharrefreplace'))[2:-1]


def get_lat_lon(address):
    url = 'https://restapi.amap.com/v3/geocode/geo'
    params = {'key': KEY, 'address': address}
    res = requests.get(url, params)
    jd =  json.loads(res.text)
    try:
        lat_lon = jd['geocodes'][0]['location']
        return lat_lon
    except:
        return ''


def get_sick_time():
    pass


def get_min_val(set_idx):
    return min(set_idx)


def get_max_val(set_idx):
    return max(set_idx)


def modify_special_location(patient_idx_info):
    patient_idx_info['10'][2] = '藁城区小果庄村'
    patient_idx_info['14'][2] = '藁城区小果庄村在小果庄村'
    patient_idx_info['36'][2] = '平山县下槐镇庞家铺村藁城补胎店'
    patient_idx_info['43'][2] = '藁城区南桥寨村'
    patient_idx_info['45'][2] = '正定县'
    patient_idx_info['48'][2] = '藁城区增村镇刘家佐村'
    patient_idx_info['52'][2] = '山西省晋中市榆社县'
    patient_idx_info['55'][2] = '藁城区石家庄经济技术开发区'
    patient_idx_info['80'][2] = '藁城区增村镇小果庄村'
    patient_idx_info['83'][2] = '藁城区小果庄村'
    patient_idx_info['84'][2] = '新乐市天悦花园藁城区增村镇小果庄村'
    patient_idx_info['96'][2] = '藁城区增村镇牛家庄村藁城市'
    patient_idx_info['104'][2] = '藁城区增村镇刘家佐村'
    patient_idx_info['116'][2] = '藁城区增村镇小果庄村'
    patient_idx_info['127'][2] = '藁城区增村镇东姚村'
    patient_idx_info['168'][2] = '藁城区常安镇锁家寨村常安镇小常安村'
    patient_idx_info['176'][2] = '藁城区增村镇小果庄村'
    patient_idx_info['195'][2] = '藁城区增村镇北桥寨村'
    patient_idx_info['207'][2] = '藁城区增村镇南桥寨村正定县新城铺镇'
    patient_idx_info['210'][2] = '新乐市宝港上城小区新乐市信誉楼'
    patient_idx_info['213'][2] = '藁城区增村镇小果庄村'
    patient_idx_info['214'][2] = '藁城区增村镇小果庄村石家庄市'
    patient_idx_info['222'][2] = '藁城区增村镇刘家佐村'
    patient_idx_info['227'][2] = '藁城区增村镇南桥寨村'
    patient_idx_info['229'][2] = '藁城区南营镇南营村新乐市信誉楼'
    patient_idx_info['234'][2] = '裕华区晶彩苑小区'
    patient_idx_info['235'][2] = '藁城区增村镇杨马村'
    patient_idx_info['238'][2] = '藁城区增村镇南桥寨村'
    patient_idx_info['242'][2] = '新乐市桥东药材公司家属院'
    patient_idx_info['275'][2] = '藁城区增村镇小果庄村'
    patient_idx_info['278'][2] = '藁城区增村镇小果庄村'
    patient_idx_info['281'][2] = '裕华区晶彩苑小区'
    patient_idx_info['354'][2] = '裕华区赵村新区'
    patient_idx_info['370'][2] = '新华区中华北大街尚金苑小区'
    patient_idx_info['529'][2] = '高新区赵村新区小区'
    patient_idx_info['727'][2] = '藁城区增村镇小果庄村'
    patient_idx_info['779'][2] = '长安区普和小区北院'
    patient_idx_info['869'][2] = '藁城区增村镇小果庄村'


def modify_wrong_lat_lon(patient_idx_lat_lon):
    patient_idx_lat_lon['316'] = [39.846561, 116.36775]
    patient_idx_lat_lon['539'] = [38.014034, 114.618882]
    patient_idx_lat_lon['370'] = [38.09822, 114.478722]
    patient_idx_lat_lon['529'] = [39.604546, 116.224372]
    patient_idx_lat_lon['841'] = [38.057107, 114.405387]
    patient_idx_lat_lon['135'] = [38.049002, 114.537501]
    patient_idx_lat_lon['136'] = [38.049002, 114.537501]
    patient_idx_lat_lon['731'] = [38.038359, 114.56738]
    patient_idx_lat_lon['779'] = [38.095859, 114.52494]
    patient_idx_lat_lon['306'] = [38.070358, 114.526692]
    patient_idx_lat_lon['307'] = [38.070358, 114.526692]
    patient_idx_lat_lon['838'] = [38.118723, 114.440813]
    patient_idx_lat_lon['803'] = [38.050585, 114.614306]
    patient_idx_lat_lon['745'] = [38.038359, 114.56738]
    patient_idx_lat_lon['850'] = [38.095859, 114.52494]
    patient_idx_lat_lon['824'] = [38.095859, 114.52494]
    patient_idx_lat_lon['430'] = [38.050922, 114.55501]
    patient_idx_lat_lon['431'] = [38.050922, 114.55501]
    patient_idx_lat_lon['641'] = [38.09057, 114.519821]
    patient_idx_lat_lon['698'] = [38.060284, 114.553069]
    patient_idx_lat_lon['718'] = [38.078057, 114.580446]
    patient_idx_lat_lon['735'] = [38.128098, 114.516702]
    patient_idx_lat_lon['775'] = [38.073411, 114.53641]
    patient_idx_lat_lon['811'] = [38.080319, 114.573635]
    patient_idx_lat_lon['842'] = [38.050585, 114.614306]
    patient_idx_lat_lon['845'] = [38.093412, 114.502282]
    patient_idx_lat_lon['851'] = [38.095859, 114.52494]
    patient_idx_lat_lon.pop('744')
    patient_idx_lat_lon.pop('529')
    patient_idx_lat_lon.pop('316')



# if __name__ == '__main__':
#     x = joblib.load('./patient/patient_idx_info.pkl')
#     check_patient_location(x)
#     y = joblib.load('./patient/patient_idx_lat_lon.pkl')
#     check_patient_lat_lon(y)