import jieba
import requests
import json

from __Parameters import *


def participle(text_string):
    seg_list = jieba.cut(text_string)
    print(", ".join(seg_list))


def check_patient_location(patient_idx_info):
    for key, val in patient_idx_info.items():
        print('patient', key, '|', 'location', val[LOCATION_INFO_IDX])


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


def modify_special_location(patient_idx_info):
    patient_idx_info['10'][2] = '藁城区小果庄村'
    patient_idx_info['14'][2] = '藁城区小果庄村在小果庄村'
    patient_idx_info['36'][2] = '平山县下槐镇庞家铺村藁城补胎店'
    patient_idx_info['43'][2] = '藁城区南桥寨村'
    patient_idx_info['45'][2] = '正定县'
    patient_idx_info['48'][2] = '藁城区增村镇刘家佐村'
    patient_idx_info['52'][2] = '行唐县滨河小区居民山西省晋中市榆社县'
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
    patient_idx_info['275'][2] = '城区增村镇小果庄村'
    patient_idx_info['278'][2] = '藁城区增村镇小果庄村'
    patient_idx_info['281'][2] = '裕华区晶彩苑小区'
    patient_idx_info['354'][2] = '裕华区赵村新区'
    patient_idx_info['727'][2] = '藁城区增村镇小果庄村'
    patient_idx_info['869'][2] = '藁城区增村镇小果庄村'
