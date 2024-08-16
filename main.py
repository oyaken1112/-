import yfinance as yf  # Yahoo Financeから株価情報を取得するための機能をインポート
import pandas as pd

def get_data(days, tickers):
    df = pd.DataFrame()
    
    for company in tickers:
        print(f"Fetching data for {company}...")  # デバッグメッセージ
        tkr = yf.Ticker(company)
        hist = tkr.history(period=f'{days}d')
        
        if hist.empty:
            print(f"No data found for {company}. Skipping...")
            continue
        
        # indexを日付のフォーマットに変更
        hist.index = hist.index.to_series().apply(lambda x: x.strftime('%d %B %Y'))
        
        hist["Name"] = company
        df = pd.concat([df, hist])
        print(f"Data for {company} added to the dataframe.")  # デバッグメッセージ
    
    return df

days = 30  # 取得する日数
tickers = ["AAPL", "MSFT", "GOOGL"]  # 企業のティッカーシンボル
df = get_data(days, tickers)  # リクエストする企業一覧すべてと変換するtickersを引数に株価取得

print(df.head())  # デバッグメッセージとして先頭の数行を表示
