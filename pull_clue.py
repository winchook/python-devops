# coding=utf-8
"""
测试拉取一定时间段内线索
"""
import base64
import hashlib
import hmac
import json
import time
import logging
import requests
import math
import os
import sys
import time
import datetime

crm_server = 'https://feiyu.oceanengine.com'
pull_clues_api = '/crm/v2/openapi/pull-clues/'


class Signature(object):
    def __init__(self, signature_header=None, timestamp_header=None, timeout=None, token_header=None, digestmod=None):
        self.signature_header = signature_header or 'Signature'
        self.timestamp_header = timestamp_header or 'Timestamp'
        self.token_header = token_header or 'Access-Token'
        self.timeout = timeout or 300
        self.digestmod = digestmod or hashlib.sha256
        self.signature_key = b'TDJDMkNDVDlVTFY5'  # 签名密钥
        self.token = 'bc90c777149f0354fe520ae51ff27a045328567e'  # token
        #  签名函数，采用hmac的sha256对data进行加密签名，key为上面签名密钥，然后转成16进制，并对结果进行base64编码

    def generate_signature(self, data, key=None):
        data = data.encode('utf-8')
        key = key if key else self.signature_key
        signature = hmac.new(key, data, digestmod=self.digestmod).hexdigest()
        signature = base64.b64encode(signature.encode('utf-8'))
        return signature
    # 为了避免单次请求量过大，采用分页请求方式，需要设置每次请求的page和page_size,page_size默认是10条结果（最大可以设置100），返回


def crm_pull_clues(start_time, end_time, page=1, page_size=10):
    payload = {}
    payload["start_time"] = start_time
    payload["end_time"] = end_time
    payload["page"] = page
    payload["page_size"] = page_size
    timestamp = str(int(time.time()))
    sig = Signature()
    url = crm_server + pull_clues_api
    # 注意data拼成时间戳前有个空格
    data = sig.generate_signature('/crm/v2/openapi/pull-clues/?start_time=%s&end_time=%s %s' % (
        start_time, end_time, timestamp))
    # header总需要三个参数，Signature（即加密后生成的签名），Timestamp（时间戳），Access-Token（token）
    headers = {sig.signature_header: data, sig.timestamp_header: timestamp, sig.token_header: sig.token}
    headers.update({'Content-Type': 'application/json'})
    max_tries = 3  # 重试次数，可以根据具体情况设置
    # resp_data = None
    while max_tries > 0:
        try:
            resp = requests.get(url=url, params=payload, headers=headers)
            if resp.status_code == 200:
                res = json.loads(resp.content)  # 获取结果
                if res:
                    return res
        except Exception as e:
            logging.exception("error with %s" % str(e))
            resp_data = None
    max_tries -= 1
    return resp_data

def store_data(sql):
    os.system("/usr/local/mysql/bin/mysql -uroot -p'0sr5uSNR' -e \"%s\"" % sql)


if __name__ == '__main__':
    sql_prefix = 'insert into api_db.adv(adv_id, store_id, site_id, date, create_time, convert_status, module_id, clue_id, ad_plan_id, ad_plan_name, appname, form_remark, store_name, location, email, province_name, clue_source, weixin, adv_name, remark_dict, address, city_name, qq, remark, name, gender, age, telphone, clue_type, module_name, external_url)values'
    # store_data()
    if len(sys.argv) != 3:
        print("Usage:%s <start_time> <stop_time>" % sys.argv[0])
        exit(1)
    res = crm_pull_clues(sys.argv[1], sys.argv[2])
    count = res.get('count')
    if count:
        times = int(math.ceil(count / 10))
        for i in range(times):
            res = crm_pull_clues(sys.argv[1], sys.argv[2], i + 1)
            time.sleep(5)
            ret = []
            for item in res.get('data'):
                item = list(item.values())
                for j in item:
                    index = item.index(j)
                    if index == 4:
                        item[index] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(item[index])))
                    elif type(j) != str:
                        item[index] = str(j)
                    item[index] = "'%s'" % item[index]
                data = "(%s)" % ",".join(item)
                ret.append(data)
            ret = ",".join(ret)
            store_data(sql_prefix + ret)