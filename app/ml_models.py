import numpy as np # type: ignore
from sklearn.ensemble import RandomForestRegressor # type: ignore
from sklearn.metrics import mean_absolute_error, r2_score # type: ignore
from xgboost import XGBRegressor # type: ignore
from sklearn.preprocessing import MinMaxScaler # type: ignore
from keras.models import Sequential # type: ignore
from keras.layers import LSTM, Dense # type: ignore


# ================= RANDOM FOREST =================
def random_forest_model(X, y):
    model = RandomForestRegressor(n_estimators=100)
    model.fit(X, y)
    predictions = model.predict(X)

    mae = mean_absolute_error(y, predictions)
    r2 = r2_score(y, predictions)

    return predictions, mae, r2


# ================= XGBOOST =================
def xgboost_model(X, y):
    model = XGBRegressor(objective="reg:squarederror")
    model.fit(X, y)
    predictions = model.predict(X)

    mae = mean_absolute_error(y, predictions)
    r2 = r2_score(y, predictions)

    return predictions, mae, r2


# ================= LSTM =================
def lstm_model(series):

    series = np.array(series).reshape(-1, 1)

    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(series)

    X = []
    y = []

    for i in range(3, len(scaled)):
        X.append(scaled[i-3:i])
        y.append(scaled[i])

    X = np.array(X)
    y = np.array(y)

    if len(X) == 0:
        return [], 0, 0

    model = Sequential()
    model.add(LSTM(50, input_shape=(3, 1)))
    model.add(Dense(1))
    model.compile(loss="mse", optimizer="adam")

    model.fit(X, y, epochs=5, verbose=0)

    predictions = model.predict(X)

    predictions = scaler.inverse_transform(predictions)
    actual = scaler.inverse_transform(y)

    mae = mean_absolute_error(actual, predictions)
    r2 = r2_score(actual, predictions)

    return predictions.flatten(), mae, r2