import joblib

from __Data_process import participle, check_date_num


date_num = {}
date_num_sorted = {}
patient_idx_locus = joblib.load('./patient/patient_idx_locus.pkl')

included_info_list = []
for key, val in patient_idx_locus.items():
    val = val.replace('。', '').replace('，', '。').replace('；', '。').replace('、', '。').replace(',', '。').replace('（', '').replace('“', '').replace(';', '')
    val = val.split('。')
    for info in val:
        if '呈阳性' in info:
            # print(info)
            idx_special_word = info.find('呈')
            if idx_special_word - 13 >= 0:
                info = info[idx_special_word - 6:idx_special_word + 1]
            else:
                info = info[:idx_special_word + 1]
            idx_month = info.find('月')
            idx_day = info.find('日')
            if idx_month != -1 and idx_day != -1:
                date = info[idx_month - 1] + '-'                    
                j = 1
                temp_char = info[idx_day - j]
                day_string = ''
                while temp_char.isdigit():
                    day_string += temp_char
                    j += 1
                    temp_char = info[idx_day - j]
                day_string = day_string[::-1]
                if len(day_string) == 1:
                    day_string = '0' + day_string
                date += day_string
                if date not in date_num:
                    date_num[date] = 1
                else:
                     date_num[date] += 1
date_num['1-13'] += 1
date_num.pop(' -13')
temp_list = sorted(date_num.items(), key=lambda e:e[0], reverse=False)
for _tuple in temp_list:
    date_num_sorted[_tuple[0]] = _tuple[1]

joblib.dump(date_num_sorted, './time_data/date_num_sorted.pkl')


