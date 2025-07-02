import statsmodels.api as sm

def fit_sarima(series, order, seasonal_order):
    model = sm.tsa.statespace.SARIMAX(series, order=order, seasonal_order=seasonal_order)
    return model.fit(disp=False)
