import numpy as np


class HMM:
    """
    HMM model class
    Args:
        A: State transition matrix
        states: list of states
        emissions: list of observations
        B: Emmision probabilites
    """

    def __init__(self, A, states, emissions, pi, B):
        self.A = A
        self.B = B
        self.states = states
        self.emissions = emissions
        self.pi = pi
        self.N = len(states)
        self.M = len(emissions)
        self.make_states_dict()

    def make_states_dict(self):
        """
        Make dictionary mapping between states and indexes
        """
        self.states_dict = dict(zip(self.states, list(range(self.N))))
        self.emissions_dict = dict(
            zip(self.emissions, list(range(self.M))))

    def viterbi_algorithm(self, seq):
        """
        Function implementing the Viterbi algorithm
        Args:
            seq: Observation sequence (list of observations. must be in the emmissions dict)
        Returns:
            nu: Porbability of the hidden state at time t given an obeservation sequence
            hidden_states_sequence: Most likely state sequence 
        """
        #s = [self.emissions_dict[i] for i in seq]
        s = []
        for i in seq:
            s.append(self.emissions_dict[i])
        obs_len = len(s)

        v = np.zeros((self.N, obs_len))
        E = np.zeros((self.N, obs_len-1)).astype(np.int32)
        v[:, 0] = np.multiply(self.pi, self.B[:, s[0]])

        # Compute D and E in a nested loop
        for n in range(1, obs_len):
            for i in range(self.N):
                temp_product = np.multiply(self.A[:, i], v[:, n-1])
                v[i, n] = np.max(temp_product) * self.B[i, s[n]]
                E[i, n-1] = np.argmax(temp_product)

        # Backtracking
        opt = np.zeros(obs_len).astype(np.int32)
        opt[-1] = np.argmax(v[:, -1])
        for n in range(obs_len-2, -1, -1):
            opt[n] = E[int(opt[n+1]), n]
        result = []
        for i in opt:
            for j in self.states_dict:
                if i == self.states_dict[j]:
                    result.append(j)
        return result

