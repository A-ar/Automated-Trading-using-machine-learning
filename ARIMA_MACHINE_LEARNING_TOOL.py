from datetime import date
import numpy as np
import datetime
from statsmodels.tsa.arima_model import ARIMA
from nsepy import get_history
import warnings
warnings.filterwarnings("ignore")
test = get_history(symbol='company_symbol', start=date.today() - datetime.timedelta(days=90), end=date.today())
test=test['Close'].values
best_aic = np.Inf
best_order = None
best_mdl = None
pq_rng = range(5) # [0,1,2,3]
d_rng = range(4) # [0,1]
for i in pq_rng:
    for d in d_rng:
        for j in pq_rng:
            try:
                tmp_mdl = ARIMA(test,order=(i,d,j)).fit(method='mle',trend='nc',disp=0)
                tmp_aic = tmp_mdl.aic
                if tmp_aic < best_aic :
                    best_aic = tmp_aic
                    best_order = (i, d, j)
                    best_mdl = tmp_mdl
            except: continue

value=best_mdl.forecast(steps=5)[0]
change=((value[4]-value[0])/value[0])*100
print(change)
