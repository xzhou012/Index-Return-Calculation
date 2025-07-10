import akshare as ak
import pandas as pd

# 设置默认参数
index_code = 'sh000300'  # 沪深300
start_date = '2023-01-30'
end_date = '2025-06-17'

# 获取指数数据
try:
    df = ak.stock_zh_index_daily(symbol=index_code)
    # 转换日期格式
    df['date'] = pd.to_datetime(df['date'])
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]
    
    # 保存为Excel
    output_file = f'{index_code}.xlsx'
    df.to_excel(output_file, 
               index=False,
               engine='openpyxl')
    print(f"数据已保存到 {output_file}")
    
except Exception as e:
    print(f"获取数据失败: {e}")
