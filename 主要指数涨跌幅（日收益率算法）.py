# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 11:04:19 2025

@author: zhurun
"""

import akshare as ak

startDate = "20250101"
endDate = "20250331"

index = ak.index_zh_a_hist(symbol="000016", period="daily", start_date=startDate, end_date=endDate)
index['涨跌幅'] = index['涨跌幅'].apply(lambda x:1+x/100)
result  = index['涨跌幅'].prod()-1
print('上证50涨跌幅：'+str(round(result*100,2))+"%")

index = ak.index_zh_a_hist(symbol="000300", period="daily", start_date=startDate, end_date=endDate)
index['涨跌幅'] = index['涨跌幅'].apply(lambda x:1+x/100)
result  = index['涨跌幅'].prod()-1
print('沪深300涨跌幅：'+str(round(result*100,2))+"%")

index = ak.index_zh_a_hist(symbol="000905", period="daily", start_date=startDate, end_date=endDate)
index['涨跌幅'] = index['涨跌幅'].apply(lambda x:1+x/100)
result  = index['涨跌幅'].prod()-1
print('中证500涨跌幅：'+str(round(result*100,2))+"%")

index = ak.index_zh_a_hist(symbol="000852", period="daily", start_date=startDate, end_date=endDate)
index['涨跌幅'] = index['涨跌幅'].apply(lambda x:1+x/100)
result  = index['涨跌幅'].prod()-1
print('中证1000涨跌幅：'+str(round(result*100,2))+"%")

index = ak.index_zh_a_hist(symbol="399006", period="daily", start_date=startDate, end_date=endDate)
index['涨跌幅'] = index['涨跌幅'].apply(lambda x:1+x/100)
result  = index['涨跌幅'].prod()-1
print('创业板指涨跌幅：'+str(round(result*100,2))+"%")

index = ak.index_zh_a_hist(symbol="000688", period="daily", start_date=startDate, end_date=endDate)
index['涨跌幅'] = index['涨跌幅'].apply(lambda x:1+x/100)
result  = index['涨跌幅'].prod()-1
print('科创50涨跌幅：'+str(round(result*100,2))+"%")

index = ak.index_zh_a_hist(symbol="899050", period="daily", start_date=startDate, end_date=endDate)
index['涨跌幅'] = index['涨跌幅'].apply(lambda x:1+x/100)
result  = index['涨跌幅'].prod()-1
print('北证50涨跌幅：'+str(round(result*100,2))+"%")