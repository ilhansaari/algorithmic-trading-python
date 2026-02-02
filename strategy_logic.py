# Project: Crypto Trading Bot Strategy
# Author: İlhan Sarı
# Status: Development Phase

import pandas as pd
# import talib as ta (Will be added later)

class TradingStrategy:
    def __init__(self, symbol, timeframe):
        self.symbol = symbol
        self.timeframe = timeframe
        self.rsi_period = 14
        self.stop_loss = 0.02 # %2 Stop Loss

    def check_signal(self, data):
        """
        Main logic to determine Buy/Sell signals based on RSI and MACD
        """
        current_rsi = data['rsi'].iloc[-1]
        
        # BUY LOGIC: RSI Oversold (<30)
        if current_rsi < 30:
            print(f"BUY SIGNAL DETECTED for {self.symbol}")
            return "BUY"
            
        # SELL LOGIC: RSI Overbought (>70)
        elif current_rsi > 70:
            print(f"SELL SIGNAL DETECTED for {self.symbol}")
            return "SELL"
            
        else:
            return "HOLD"

# TODO: Connect to Binance API
# TODO: Add MACD filter
