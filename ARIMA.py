from pyramid import auto_arima
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error,r2_score

def ARIMA_pred(data, forc_data):


    listp = forc_data.values

    stepwise_model = auto_arima(data, start_p=1, start_q=1,
                                max_p=3, max_q=3,
                                start_P=0, start_Q=0, max_P=3, max_Q=3,
                                error_action='ignore',
                                suppress_warnings=True,
                                stepwise=True)
    stepwise_model.fit(data)
    pr = stepwise_model.predict(n_periods=100)

    plt.plot(listp, color='red', label='Real Stock Price')
    plt.plot(pr, color='blue', label='Predicted Stock Price')
    plt.title(' Stock Price Prediction using ARIMA')
    plt.xlabel('Time')
    plt.ylabel('Stock Price')
    plt.legend()
    plt.show()
    print("For ARIMA The mean squared error is:")
    print(mean_squared_error(listp,pr))
    print("For ARIMA The R squared error is:")
    print(r2_score(listp,pr))
    plt.style.use('fivethirtyeight')
    plt.scatter(data, data - stepwise_model.predict_in_sample(data), color="green", s=10, label='Train data')
    plt.scatter(listp, listp - pr, color="blue", s=10, label='Test data')
    plt.hlines(y=0, xmin=0, xmax=250, linewidth=2)
    plt.legend(loc='upper right')
    plt.title("Residual errors for ARIMA")
    plt.show()

