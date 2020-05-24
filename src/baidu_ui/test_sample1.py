import pytest;
from selenium import webdriver
from time import sleep,ctime;##ctime 将时间转化为字符串
import xlrd;
import os
Excel_dir="E:\移动测试\demo1\data\pytest.xlsx"
class Test_baidu_serach():
   def test_answer(self):
       driver=webdriver.Chrome();
       #打开网页
       driver.get('http://www.baidu.com');
       #打开测试文件
       excle_file=xlrd.open_workbook(Excel_dir)
       #获取第一个列表
       sheet=excle_file.sheet_by_index(0)
       #获取第一列信息,行为.row_values,起始都为0
       cols=sheet.col_values(0);
       print(cols);
       for query in cols:
           driver.find_element_by_id("kw").clear()
           driver.find_element_by_id("kw").send_keys(str(query))
           driver.find_element_by_id("su").click()
           sleep(2)
       driver.quit()
   def test_one(self):
       print("88888888")
       assert 1==5
   def test_two(x):
       return x+1
       assert test_two(3)==5

