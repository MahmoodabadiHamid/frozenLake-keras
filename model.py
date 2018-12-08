


class Actor():
    def __init__(self, state_size, action_size):
        super(Actor, self).__init__()
        import torch.nn as nn
        self.state_size = state_size
        self.action_size = action_size
        self.linear1 = nn.Linear(self.state_size, 164)
        self.linear2 = nn.Linear(164, 150)
        self.linear3 = nn.Linear(150, self.action_size)

    def forward(self, state):
        output = F.relu(self.linear1(state))
        output = F.relu(self.linear2(output))
        output = self.linear3(output)
        distribution = Categorical(F.softmax(output, dim=-1))
        return distribution



class Critic():
    def __init__(self, state_size, action_size):
        super(Critic, self).__init__()
        import torch.nn as nn
        self.state_size = state_size
        self.action_size = action_size
        self.linear1 = nn.Linear(self.state_size, 164)
        self.linear2 = nn.Linear(164, 150)
        self.linear3 = nn.Linear(150, 1)

    def forward(self, state):
        output = F.relu(self.linear1(state))
        output = F.relu(self.linear2(output))
        value = self.linear3(output)
        return value
























