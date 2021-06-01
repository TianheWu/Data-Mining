import torch
import torch.nn.functional as F


class Regression(torch.nn.Module):

    def __init__(self, n_feature, n_hidden, n_output):
        super(Regression, self).__init__()
        self.hidden = torch.nn.Linear(n_feature, n_hidden)
        self.out = torch.nn.Linear(n_hidden, n_output)

    def forward(self, x):
        x = F.sigmoid(self.hidden(x))
        x = self.out(x)
        return x;


class LSTM(torch.nn.Module):

    def __init__(self, input_dim, hidden_dim, output_dim=1, layer_dim=2):
        super(LSTM, self).__init__()
        self.hidden_dim = hidden_dim
        self.layer_dim = layer_dim
        self.lstm = torch.nn.LSTM(input_dim, hidden_dim, layer_dim)
        self.fc1 = torch.nn.Linear(hidden_dim, output_dim)
    
    def forward(self, x):
        x, h_n = self.lstm(x, None)
        s, b, h = x.shape
        x = x.view(s * b, h)
        x = self.fc1(x)
        x = x.view(s, b, -1)
        return x
        

