from nseta.common.log import default_logger, tracelog
import talib as ta

__all__ = ['ti']

class ti:

	def update_ti(self, df):
		try:
			df['RSI'] = self.get_rsi_df(df)
			df['MOM'] = self.get_mom_df(df)
			df[['Close','SMA(10)', 'SMA(50)']] = self.get_sma_df(df)
			df[['Close','EMA(9)']] = self.get_ema_df(df)
			df[['macd(12)','macdsignal(9)', 'macdhist(26)']] = self.get_macd_df(df)
		except Exception as e:
			default_logger().debug(e, exc_info=True)
		except SystemExit:
			pass
		return df

	def get_rsi_df(self, df):
		df['RSI'] = ta.RSI(df['Close'],14)
		return df['RSI']

	def get_mom_df(self, df):
		df['MOM'] = ta.MOM(df['Close'],2)
		return df['MOM']

	def get_dmi_df(self, df):
		df['DMI'] = ta.DX(df['High'],df['Low'],df['Close'],timeperiod=14)
		return df['DMI']

	def get_macd_df(self, df):
		df['macd'], df['macdsignal'], df['macdhist'] = ta.MACDEXT(df['Close'], fastperiod=12, fastmatype=0, slowperiod=26, slowmatype=0, signalperiod=9, signalmatype=0)
		return df[['macd','macdsignal', 'macdhist']]

	def get_sma_df(self, df):
		df['SMA(10)'] = ta.SMA(df['Close'],10)
		df['SMA(50)'] = ta.SMA(df['Close'],50)
		return df[['Close','SMA(10)', 'SMA(50)']]

	def get_ema_df(self, df):
		df['EMA(9)'] = ta.EMA(df['Close'], timeperiod = 9)
		return df[['Close','EMA(9)']]

	def get_adx_df(self, df):
		df['ADX'] = ta.ADX(df['High'],df['Low'], df['Close'], timeperiod=14)
		return df['ADX']

	def get_bbands_df(self, df):
		df['BBands-U'], df['BBands-M'], df['BBands-L'] = ta.BBANDS(df['Close'], timeperiod =20)
		return df[['Close','BBands-U','BBands-M','BBands-L']]

	def get_obv_df(self, df):
		df['OBV'] = ta.OBV(df['Close'], df['Volume'])
		return df['OBV']