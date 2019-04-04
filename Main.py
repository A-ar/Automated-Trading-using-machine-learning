import pandas as pd
from datetime import date
import datetime
import warnings
from nsepy import get_history
import ARIMA
import Profit_loss_scraper
import RNN
import FTS
warnings.filterwarnings("ignore")
print("enter the company name:")
inp = input()

def list_to_dt(x,start):
    x=pd.DataFrame(x)
    datelist = pd.date_range(start, periods=len(x)).tolist()
    y=pd.DataFrame({'Date':datelist})
    y=y.join(x)
    y.set_index("Date", inplace=True)
    return y

sym = Profit_loss_scraper.pl_statement(inp)
data = get_history(symbol=sym, start=date.today() - datetime.timedelta(days=1600), end=date.today()- datetime.timedelta(days=100))
forc_data = get_history(symbol=sym, start=date.today() - datetime.timedelta(days=300), end=date.today())
data=data['Close']
forc_data=forc_data['Close']
data = data[len(data) - 900:]
forc_data = forc_data[len(forc_data) - 100:]
ARIMA.ARIMA_pred(data,forc_data)
FTS.FTS(data.values,forc_data.values)
RNN.RNN(data,forc_data)








