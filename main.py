import yfinance as yf  # yahoo financeから株価情報を取得するための機能をインポート
import pandas as pd

def get_data(days, tickers):
    df = pd.DataFrame()
    
    for company in tickers:
        tkr = yf.Ticker(company)
        hist = tkr.history(period=f'{days}d')
        
        # indexを日付のフォーマットに変更
        hist.index = hist.index.to_series().apply(lambda x: x.strftime('%d %B %Y'))
        
        hist["Name"] = company
        df = pd.concat([df, hist])
    
    return df

days = 30  # 取得する日数
tickers = ["AAPL", "MSFT", "GOOGL"]  # 企業のティッカーシンボル
df = get_data(days, tickers)  # リクエストする企業一覧すべてと変換するtickersを引数に株価取得

print(df)
