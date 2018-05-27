import os
import pandas as pd
import matplotlib.pyplot as plt
# import code
# code.interact(local=dict(globals(), **locals()))

def plot_selected(data_frame, columns, start_index, end_index):
  data_frame = data_frame.ix[start_index: end_index, columns]
  plot_data(data_frame)

def symbol_to_path(symbol, base_dir='data'):
  return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
  data_frame = pd.DataFrame(index=dates)
  if 'SPY' not in symbols:
    symbols.insert(0, 'SPY')
  
  for symbol in symbols:
    data_frame_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date', parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
    data_frame_temp = data_frame_temp.rename(columns = {'Adj Close': symbol})
    data_frame = data_frame.join(data_frame_temp)
    if symbol == 'SPY':
      data_frame = data_frame.dropna(subset=['SPY'])
    
  return data_frame


def normalize_data(data_frame):
  return data_frame / data_frame.ix[0,:]
  

def plot_data(data_frame, title="Stock Prices"):
  axis = data_frame.plot(title=title, fontsize=2)
  axis.set_xlabel('Date')
  axis.set_ylabel('Price')
  plt.show()


def test_run():
  start_date = '2018-04-01'
  end_date = '2018-05-31'
  dates = pd.date_range(start=start_date, end=end_date)  
  symbols = ['RHT', 'CSV', 'MSFT']

  data_frame = get_data(symbols, dates)
#  print data_frame
  # data_frame = data_frame.ix['2018-04-20': '2018-04-30']
  # plot_data(data_frame)

  plot_selected(normalize_data(data_frame), ['SPY', 'RHT'], '2018-5-01', '2018-05-30')


if __name__ == "__main__":
  test_run()