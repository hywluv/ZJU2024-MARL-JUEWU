REGISTRY = {}

from .rnn_agent import RNNAgent
REGISTRY["rnn"] = RNNAgent

from .n_rnn_agent import NRNNAgent
REGISTRY["n_rnn"] = NRNNAgent