import numpy as np
from math import *



class KNN:
    """
    K Nearest Neighbours model
    Args:
        k_neigh: Number of neighbours to take for prediction
        weighted: Boolean flag to indicate if the nieghbours contribution
                  is weighted as an inverse of the distance measure
        p: Parameter of Minkowski distance
    """

    def __init__(self, k_neigh, weighted=False, p=2):

        self.weighted = weighted
        self.k_neigh = k_neigh
        self.p = p

    def fit(self, data, target):
        """
        Fit the model to the training dataset.
        Args:
            data: M x D Matrix( M data points with D attributes each)(float)
            target: Vector of length M (Target class for all the data points as int)
        Returns:
            The object itself
        """

        self.data = data
        self.target = target.astype(np.int64)

        return self

    def find_distance(self, x):
        """
        Find the Minkowski distance to all the points in the train dataset x
        Args:
            x: N x D Matrix (N inputs with D attributes each)(float)
        Returns:
            Distance between each input to every data point in the train dataset
            (N x M) Matrix (N Number of inputs, M number of samples in the train dataset)(float)
        """
        # TODO
        return_matrix = []
        for i in range(len(x)):
            temp = []
            for j in range(len(self.data)):
                p_raised_distance = 0
                for k in range(len(self.data[0])):
                    p_raised_distance += abs((x[i][k] - self.data[j][k])) ** self.p

                distance = p_raised_distance ** (1 / float(self.p))
                temp.append(distance)
            return_matrix.append(temp)

        return return_matrix


    def k_neighbours(self, x):
        """
        Find K nearest neighbours of each point in train dataset x
        Note that the point itself is not to be included in the set of k Nearest Neighbours
        Args:
            x: N x D Matrix( N inputs with D attributes each)(float)
        Returns:
            k nearest neighbours as a list of (neigh_dists, idx_of_neigh)
            neigh_dists -> N x k Matrix(float) - Dist of all input points to its k closest neighbours.
            idx_of_neigh -> N x k Matrix(int) - The (row index in the dataset) of the k closest neighbours of each input

            Note that each row of both neigh_dists and idx_of_neigh must be SORTED in increasing order of distance
        """
        # TODO
        final_neigh_dists = []
        final_idx_of_neigh = []
        k = self.k_neigh
        
        for distances in self.find_distance(x):

            sorted_distances = list(enumerate(distances))
            sorted_distances.sort(key=lambda l: l[1])
            
            idx_of_neigh = []
            neigh_dists = []


            for x in sorted_distances[0 : k]:

                idx_of_neigh.append(x[0])
                neigh_dists.append(x[1])

            final_idx_of_neigh.append(idx_of_neigh)
            final_neigh_dists.append(neigh_dists)
        

        return (final_neigh_dists, final_idx_of_neigh)

    def predict(self, x):
        """
        Predict the target value of the inputs.
        Args:
            x: N x D Matrix( N inputs with D attributes each)(float)
        Returns:
            pred: Vector of length N (Predicted target value for each input)(int)
        """
        # TODO
        neigh_dists, idx_of_neigh = self.k_neighbours(x)
        return_val = []
        val = []
        val.append(0)
        val.append(0)

        if self.weighted:
            dist_weight = 1 / np.array(neigh_dists)

        
        for weight, idxs in enumerate(idx_of_neigh):
            for index, idx in enumerate(idxs):
                if not self.target[idx]:
                    if not self.weighted:
                        val[1] += 1
                    else:
                        val[1] += dist_weight[weight][index]
                else:
                    if not self.weighted:
                        val[0] += 1
                    else:
                        val[0] += dist_weight[weight][index]

            if val[0] < val[1]:
                return_val.append(0)
            else:

                return_val.append(1)


        return np.array(return_val)

    def evaluate(self, x, y):
        """
        Evaluate Model on test data using 
            classification: accuracy metric
        Args:
            x: Test data (N x D) matrix(float)
            y: True target of test data(int)
        Returns:
            accuracy : (float.)
        """
        # TODO
        prediction = self.predict(x)
        truth_array = [0,0,0,0]

        for i, pred in enumerate(prediction):

            if pred == 1 and y[i] == 1:
                truth_array[0] += 1

            elif pred == 1 and y[i] == 0:
                truth_array[2] += 1

            elif pred == 0 and y[i] == 0:
                truth_array[1] += 1

            else:
                truth_array[3] += 1
        
        result = (truth_array[0] + truth_array[1]) / sum(truth_array)

        return result * 100
