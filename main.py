import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px

st.title('Stock Data Viewer')

# サポートされている有効な期間
valid_periods = ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']

# ユーザー入力を受け取る
ticker_symbol = st.text_input('Enter Ticker Symbol (e.g. AAPL, MSFT, GOOGL):', 'AAPL')
period = st.selectbox('Select Period:', valid_periods, index=valid_periods.index('1mo'))

# データを取得する
try:
    stock_data = yf.download(ticker_symbol, period=period)
    
    # 日付インデックスをリセットしてDataFrameのカラムにする
    stock_data.reset_index(inplace=True)

    if not stock_data.empty:
        st.subheader(f'Stock Data for {ticker_symbol}')
        st.write(stock_data)
        
        # 日付形式を適切に変換する
        stock_data['Date'] = pd.to_datetime(stock_data['Date'])
        stock_data['Date'] = stock_data['Date'].dt.strftime('%Y-%m-%d')
        
        # プロットを作成する
        fig = px.line(stock_data, x='Date', y='Close', title=f'{ticker_symbol} Closing Prices')
        st.plotly_chart(fig)
    else:
        st.write("No data found for the given ticker symbol and period.")
except Exception as e:
    st.write(f"An error occurred: {e}")
