import matplotlib.pyplot as plt
from pyFTS.partitioners import Grid
from pyFTS.models import chen
from sklearn.metrics import mean_squared_error,r2_score

def FTS(train, test):
    # Universe of Discourse Partitioner
    partitioner = Grid.GridPartitioner(data=train, npart=75)

    # Create an empty model using the Chen(1996) method
    model = chen.ConventionalFTS(partitioner=partitioner)

    # The training procedure is performed by the method fit
    model.fit(train)

    # The forecasting procedure is performed by the method predict
    forecasts = model.predict(test)

    # Plot
    plt.plot(test, color='red', label='Real Stock Price')
    plt.plot(forecasts, color='blue', label='Predicted Stock Price')
    plt.title(' Stock Price Prediction using fuzzy logic')
    plt.xlabel('Time')
    plt.ylabel('Stock Price')
    plt.legend()
    plt.show()
    print("For Fuzzy time series The mean squared error is:")
    print(mean_squared_error(test,forecasts))
    print("For fuzzy time series The R squared error is:")
    print(r2_score(test,forecasts))
    plt.style.use('fivethirtyeight')
    plt.scatter(train, train - model.predict(train), color="green", s=10, label='Train data')
    plt.scatter(test, test - forecasts, color="blue", s=10, label='Test data')
    plt.hlines(y=0, xmin=0, xmax=250, linewidth=2)
    plt.legend(loc='upper right')
    plt.title("Residual errors for FTS")
    plt.show()