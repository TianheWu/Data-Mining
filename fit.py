import numpy
import joblib

from __Parameters import *
from __Data_process import polynomial_fitting
from __Visualization_tools import visualization_fit


date_num_sorted = joblib.load('./time_data/date_num_sorted.pkl')
x = numpy.arange(1, len(date_num_sorted) + 1)
y = numpy.empty([0, 1])
temp_sum = 0
for key, val in date_num_sorted.items():
    temp_sum += int(val)
    y = numpy.append(y, temp_sum)

x = x[numpy.newaxis, :]
y = y[:, numpy.newaxis]
y = numpy.concatenate((y, x.T), axis=1)
max_val = numpy.max(y[:, 0])
min_val = numpy.min(y[:, 0])
train_data = (y[:, 0] - min_val) / (max_val - min_val)
train_data = train_data[1:]
x = x[0][:-1]
print(len(x))
print(len(train_data))
res = polynomial_fitting(x, train_data)
pred_y = res(x)
visualization_fit(x, train_data, pred_y)
print(res)