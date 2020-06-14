# %E5%8C%97%E4%BA%AC = 北京

from bs4 import BeautifulSoup
import time
import numpy as np
import requests
import json
import csv
import io
import time
import pandas  as pd
import xlsxwriter

    
def getInData(url,direction):     
    mobility = []
    global matrixMobility

    headers = {
        'Accept': '*/*',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Referer':"https://heat.qq.com/qianxi/index_new.html"}
    response = requests.get(url=url, headers=headers) 
    jsonData = response.text
    jsonData = json.loads(jsonData)
    dataLen = len(jsonData['data'])
    for j in range(0,dataLen):
        cityName = jsonData['data'][j][0]
        popularScore = jsonData['data'][j][1]
        car=jsonData['data'][j][2]
        train=jsonData['data'][j][3]
        flight=jsonData['data'][j][4]
        mobility.append(date)
        mobility.append(cityName)
        mobility.append(popularScore)
        mobility.append(car)
        mobility.append(train)
        mobility.append(flight)
        mobility.append(direction)
        matrixMobility.append(mobility)
        mobility = []
        
    with open("腾讯迁入数据.csv", "w+", newline="",encoding='utf-8-sig') as csv_file:
        writer=csv.writer(csv_file)
        header=["日期","城市","热度 ","汽车","火车","飞机","流向"] 
        writer.writerow(header) 
        for i in range(len(matrixMobility)):
            writer.writerow(matrixMobility[i])

def getOutData(url,direction):     
    mobility = []
    global matrixMobility

    headers = {
        'Accept': '*/*',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'Referer':"https://heat.qq.com/qianxi/index_new.html"}
    response = requests.get(url=url, headers=headers) 
    jsonData = response.text
    jsonData = json.loads(jsonData)
    dataLen = len(jsonData['data'])
    for j in range(0,dataLen):
        cityName = jsonData['data'][j][0]
        popularScore = jsonData['data'][j][1]
        car=jsonData['data'][j][2]
        train=jsonData['data'][j][3]
        flight=jsonData['data'][j][4]
        mobility.append(date)
        mobility.append(cityName)
        mobility.append(popularScore)
        mobility.append(car)
        mobility.append(train)
        mobility.append(flight)
        mobility.append(direction)
        matrixMobility.append(mobility)
        mobility = []
        
    with open("腾讯迁出数据.csv", "w+", newline="",encoding='utf-8-sig') as csv_file:
        writer=csv.writer(csv_file)
        header=["日期","城市","热度 ","汽车","火车","飞机","流向"] 
        writer.writerow(header) 
        for i in range(len(matrixMobility)):
            writer.writerow(matrixMobility[i])        

    
if __name__ == "__main__":
    global matrixMobility     
    matrixMobility = []
    begin_date = '2019-05-13'
    end_date = '2019-06-09'
    dateList = [x.strftime('%Y-%m-%d') for x in list(pd.date_range(start=begin_date, end=end_date))]
    for date in dateList:
        url1 = 'https://heat.qq.com/api/getLbsMigrateDataByBeijing.php?city=%E5%8C%97%E4%BA%AC&direction=1&type=6&date={}'.format(date)
        print(url1)
        direction1 = "迁出"
        getInData(url1,direction1)
        
    for date in dateList:
        url2 = 'https://heat.qq.com/api/getLbsMigrateDataByBeijing.php?city=%E5%8C%97%E4%BA%AC&direction=0&type=6&date={}'.format(date)
        print(url2)
        direction2 = "迁入"
        getOutData(url2,direction2)        
        
    print("结束")
