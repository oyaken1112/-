import streamlit as st
import yfinance as yf
import pandas as pd

def get_data(days, tickers):
    df = pd.DataFrame()
    for company in tickers.keys():
        tkr = yf.Ticker(tickers[company])
        hist = tkr.history(period='1mo')  # 正しい期間を使用
        hist.index = pd.to_datetime(hist.index).strftime('%d %B %Y')  # 修正
        hist = hist[['Close']]  # データを終値だけ抽出
        hist.columns = [company]  # データのカラムをyf.Tickerのリクエストした会社名に変更
        hist = hist.T  # 欲しい情報が逆なので、転置する
        hist.index.name = 'Name'  # インデックスの名前を変更
        df = pd.concat([df, hist])  # データを結合
    return df

st.title('株価可視化アプリ')
st.sidebar.write('株価可視化のためのツールです。')

tickers = {
    'apple': 'AAPL',
    'microsoft': 'MSFT',
    'google': 'GOOGL'
}

days = st.sidebar.slider(
    '日数',
    1, 30, 20
)

try:
    df = get_data(days, tickers)
    st.write(df)
except Exception as e:
    st.error(f"Error: {e}")
