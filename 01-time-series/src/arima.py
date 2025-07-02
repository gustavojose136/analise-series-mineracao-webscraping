import statsmodels.api as sm

def fit_arima(series, order):
    model = sm.tsa.ARIMA(series, order=order)
    return model.fit()
