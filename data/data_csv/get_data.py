#!/usr/bin/python
# -*- coding: utf-8 -*-

import shlex
import subprocess
import re
import datetime
import json
# import sys

# reload(sys)
# sys.setdefaultencoding('utf8')

START = 2000001
END = 2074719
# END = 2000005

def check_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%d/%m/%Y')
        return True
    except ValueError:
        return False

def new_json():
    json_array = {
        "sbd": -1,
        "ho": "",
        "ten_lot": "",
        "ten": "",
        "dd": -1,
        "mm": -1,
        "yyyy": -1,
        "Toan": -1,
        "Ngu_Van": -1,
        "KHXH": -1,
        "KHTN": -1,
        "Lich_Su": -1,
        "Dia_Ly": -1,
        "GDCD": -1,
        "Sinh_Hoc": -1,
        "Vat_Ly": -1,
        "Hoa_Hoc": -1,
        "Tieng_Anh": -1
    }
    return json_array

def get_date_index(array):
    date_index = -1
    for index, element in enumerate(array):
        if check_date(element):
            date_index = index
            break
    if date_index == -1:
        for index, element in enumerate(array):
            temp_array = element.split('/')
            if len(temp_array) == 3:
                date_index = index
                break
    return date_index

def get_grade_array(array, first_index):
    return array[first_index + 1:len(array) - 1]

def convert_vietnamese(in_put):
    out_put = in_put
    out_put = re.sub("&#39;", "'", out_put)
    out_put = re.sub("&#192;", "À", out_put)
    out_put = re.sub("&#193;", "Á", out_put)
    out_put = re.sub("&#194;", "Â", out_put)
    out_put = re.sub("&#195;", "Ã", out_put)
    out_put = re.sub("&#200;", "È", out_put)
    out_put = re.sub("&#201;", "É", out_put)
    out_put = re.sub("&#202;", "Ê", out_put)
    out_put = re.sub("&#204;", "Ì", out_put)
    out_put = re.sub("&#205;", "Í", out_put)
    out_put = re.sub("&#208;", "Ð", out_put)
    out_put = re.sub("&#210;", "Ò", out_put)
    out_put = re.sub("&#211;", "Ó", out_put)
    out_put = re.sub("&#212;", "Ô", out_put)
    out_put = re.sub("&#213;", "Õ", out_put)
    out_put = re.sub("&#217;", "Ù", out_put)
    out_put = re.sub("&#218;", "Ú", out_put)
    out_put = re.sub("&#221;", "Ý", out_put)
    return out_put

def parse_json(array):
    date_index = get_date_index(array)
    grade_array = get_grade_array(array, date_index)

    json_data = new_json()

    date_array = array[date_index].split('/')
    
    day = date_array[0]
    month = date_array[1]
    year = date_array[2]

    ho = convert_vietnamese(array[1])
    ten_lot = convert_vietnamese(" ".join(array[2 : date_index-1]))
    ten = convert_vietnamese(array[date_index - 1])
    json_data['ho'] = ho
    json_data['ten_lot'] = ten_lot
    json_data['ten'] = ten
    json_data['sbd'] = array[0]
    json_data['dd'] = day
    json_data['mm'] = month
    json_data['yyyy'] = year
    
    for index, element in enumerate(grade_array):
        if index % 2 == 0:
            if element == "Vat_Ly":
                json_data['Vat_Ly'] = grade_array[index + 1]
            elif element == "Dia_Ly":
                json_data['Dia_Ly'] = grade_array[index + 1]
            elif element == "KHTN":
                json_data['KHTN'] = grade_array[index + 1]
            elif element == "GDCD":
                json_data['GDCD'] = grade_array[index + 1]
            elif element == "Ngu_Van":
                json_data['Ngu_Van'] = grade_array[index + 1]
            elif element == "Hoa_Hoc":
                json_data['Hoa_Hoc'] = grade_array[index + 1]
            elif element == "Toan":
                json_data['Toan'] = grade_array[index + 1]
            elif element == "KHXH":
                json_data['KHXH'] = grade_array[index + 1]
            elif element == "Sinh_Hoc":
                json_data['Sinh_Hoc'] = grade_array[index + 1]
            elif element == "Lich_Su":
                json_data['Lich_Su'] = grade_array[index + 1]
            elif element == "Tieng_Anh":
                json_data['Tieng_Anh'] = grade_array[index + 1]
    
    return json_data

def create_csv(a):
    array_csv = ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"]
    data = json.loads(a)
    for key, value in data.items():
        if key == "sbd":
            array_csv[0] = str(value)
        if key == "ho":
            array_csv[1] = str(value)
        if key == "ten_lot":
            array_csv[2] = str(value)
        if key == "ten":
            array_csv[3] = str(value)
        if key == "dd":
            array_csv[4] = str(value)
        if key == "mm":
            array_csv[5] = str(value)
        if key == "yyyy":
            array_csv[6] = str(value)
        if key == "Vat_Ly":
            array_csv[7] = str(value)
        if key == "Dia_Ly":
            array_csv[8] = str(value)
        if key == "KHTN":
            array_csv[9] = str(value)
        if key == "GDCD":
            array_csv[10] = str(value)
        if key == "Ngu_Van":
            array_csv[11] = str(value)
        if key == "Hoa_Hoc":
            array_csv[12] = str(value)
        if key == "Toan":
            array_csv[13] = str(value)
        if key == "KHXH":
            array_csv[14] = str(value)
        if key == "Sinh_Hoc":
            array_csv[15] = str(value)
        if key == "Lich_Su":
            array_csv[16] = str(value)
        if key == "Tieng_Anh":
            array_csv[17] = str(value)

    return ",".join(array_csv)
    
############### MAIN ###############
file = open("diemthidhqg2020_test.csv", "w")
file.write('sbd,ho,lot,ten,dd,mm,yyyy,vat_ly,dia_ly,khtn,gdcd,ngu_van,hoa_hoc,toan_hoc,khxh,sinh_hoc,lich_su,tieng_anh\n')
file.close()

for count in range(START, END):
    print(str((((count-2000000)*100)/(END-2000000))) + "% => 0" + str(count))
    command = 'curl -F "SoBaoDanh=0' + str(count) + '" diemthi.hcm.edu.vn/Home/Show'
    result = subprocess.check_output(shlex.split(command))
    x = re.search("Color: red ; font-size: x-large", result)
    if x:
        print("Not found")
    else:
        result = re.sub('<[^>]+>', '', result)
        result = re.sub('[\t\n\r]', '', result)
        result = re.sub(' +', ' ', result)
        result = result[157:]
        result = result.replace('To&#225;n', 'Toan')
        result = result.replace('Ng\xe1\xbb\xaf v\xc4\x83n', 'Ngu_Van')
        result = result.replace('L\xe1\xbb\x8bch s\xe1\xbb\xad', 'Lich_Su')
        result = result.replace('\xc4\x90\xe1\xbb\x8ba l&#237;', 'Dia_Ly')
        result = result.replace('Sinh h\xe1\xbb\x8dc', 'Sinh_Hoc')
        result = result.replace('V\xe1\xba\xadt l&#237;', 'Vat_Ly')
        result = result.replace('H&#243;a h\xe1\xbb\x8dc', 'Hoa_Hoc')
        result = result.replace('Ti\xe1\xba\xbfng Anh', 'Tieng_Anh')
        result = result.replace('Ti\xe1\xba\xbfng Nh\xe1\xba\xadt', 'Tieng_Anh')
        result = '0' + str(count) + ' ' + result
        result = result.replace(':', '')

        array = result.split(' ')
        file = open("diemthidhqg2020_test.csv", "a")
        file.write(str(create_csv(json.dumps(parse_json(array)))) + '\n')
        # file.write(str(json.dumps(parse_json(array))) + '\n')
        file.close()
print("DOWNLOAD SUCCESS!!!!")
