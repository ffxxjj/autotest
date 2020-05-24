#_*_ coding:utf-8 _*_
import pytest
import requests
import json
BASE_URL="http://httpbin.org/"
#BASE_URL="192.168.9.11:9000"
IP_URL = "/ip"
LOCAL_IP ="112.44.18.213"
POST_TEST_URL = "/post"
class Test_httpbin():
    def test_get_ip(self):
        url = BASE_URL + IP_URL
        print(url)
        r = requests.get(url)
        print(r.headers)
        print(r.text)
       # response_data = r.json()
        response_data = json.loads(r.text)
        print(response_data)
        assert 200 == r.status_code
        assert  LOCAL_IP == response_data["origin"]

    def test_post_method(self):
        url = BASE_URL + POST_TEST_URL
        post_data = {"name":"xzh","pwd":"1999777"}
        r = requests.post(url,data=post_data)
        print(r.headers)
        print(r.text)
        response_data = r.json()
        assert 200 == r.status_code
        assert post_data["name"] == response_data["form"]["name"]
        assert post_data["pwd"] == response_data["form"]["pwd"]
