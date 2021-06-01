import joblib
import torch
import time
import numpy
import copy
import torch.utils.data as Data

from torchvision import transforms
from torch.optim import optimizer
from __Model import LSTM
from __Parameters import *
from __Visualization_tools import visualization_acc


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
train_data_x = []
train_data_y = []

for i in range(len(train_data) - LOOK_BACK):
    temp = train_data[i:(i + LOOK_BACK)]
    train_data_x.append(temp)
    train_data_y.append(train_data[i + LOOK_BACK])

train_data_x = numpy.array(train_data_x)
train_data_y = numpy.array(train_data_y)

train_size = int(len(train_data_x) * 0.9)
test_size = len(train_data_x) - train_size
train_x = train_data_x[:train_size]
train_y = train_data_y[:train_size]
test_x = train_data_x[train_size:]
test_y = train_data_y[train_size:]

train_x = torch.from_numpy(train_x.reshape(-1, 1, INPUT_FEATURE)).type(torch.float32)
train_y = torch.from_numpy(train_y.reshape(-1, 1, INPUT_FEATURE)).type(torch.float32)
test_x = torch.from_numpy(test_x.reshape(-1, 1, INPUT_FEATURE)).type(torch.float32)

rnn = LSTM(INPUT_FEATURE, HIDDEN_DIM)
optimizer = torch.optim.Adam(rnn.parameters(), lr=0.01)
criterion = torch.nn.MSELoss()

best_val_loss = float("inf")
best_model_wts = 0
for epoch in range(EPOCHS):
    out = rnn(train_x)
    loss = criterion(out, train_y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    if (loss.item() < best_val_loss):
        best_model_wts = copy.deepcopy(rnn.state_dict())
    if (epoch + 1) % 100 == 0:
        print("Epoch: {} | Loss: {:.5f}".format(epoch + 1, loss.item()))
        
rnn.load_state_dict(best_model_wts)
torch.save(rnn.state_dict(), './model_pkl/model.pkl')

rnn.eval()
new_train_data = torch.from_numpy(train_data.reshape(-1, 1, INPUT_FEATURE)).type(torch.float32)
pred_test = rnn(new_train_data).view(-1).data.numpy()
visualization_acc(pred_test, train_data)