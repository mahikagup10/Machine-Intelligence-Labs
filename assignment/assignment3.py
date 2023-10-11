import random
import numpy as np

class genetic_algorithm:
        
    def execute(pop_size,generations,threshold,X,y,network):
        class Agent:
            def __init__(self,network):
                class neural_network:
                    def __init__(self,network):
                        self.weights = []
                        self.activations = []
                        for layer in network:
                            if layer[0] != None:
                                input_size = layer[0]
                            else:
                                input_size = network[network.index(layer)-1][1]
                            output_size = layer[1]
                            activation = layer[2]
                            self.weights.append(np.random.randn(input_size,output_size))
                            self.activations.append(activation)
                    def propagate(self,data):
                        input_data = data
                        for i in range(len(self.weights)):
                            z = np.dot(input_data,self.weights[i])
                            a = self.activations[i](z)
                            input_data = a
                        yhat = a
                        return yhat
                self.neural_network = neural_network(network)
                self.fitness = 0
                def generate_agents(population, network):
                    return [Agent(network) for _ in range(population)]
                def fitness(agents,X,y):
                    for agent in agents:
                        yhat = agent.neural_network.propagate(X)
                        cost = (yhat - y)**2
                        agent.fitness = sum(cost)
                    return agents
                def selection(agents):
                    agents = sorted(agents, key=lambda agent: agent.fitness, reverse=False)
                    print('\n'.join(map(str, agents)))
                    agents = agents[:int(0.2 * len(agents))]
                    return agents
                def unflatten(flattened,shapes):
                    newarray = []
                    index = 0
                    for shape in shapes:
                        size = np.product(shape)
                        newarray.append(flattened[index : index + size].reshape(shape))
                        index += size
                    return newarray
                def crossover(agents,network,pop_size):
                    offspring = []
                    for _ in range((pop_size - len(agents)) // 2):
                        parent1 = random.choice(agents)
                        parent2 = random.choice(agents)
                        child1 = Agent(network)
                        child2 = Agent(network)
                        
                        shapes = [a.shape for a in parent1.neural_network.weights]
                        
                        genes1 = np.concatenate([a.flatten() for a in parent1.neural_network.weights])
                        genes2 = np.concatenate([a.flatten() for a in parent2.neural_network.weights])
                        
                        split = random.ragendint(0,len(genes1)-1)
                        child1_genes = np.asrray(genes1[0:split].tolist() + genes2[split:].tolist())
                        child2_genes = np.array(genes1[0:split].tolist() + genes2[split:].tolist())
                                
                        child1.neural_network.weights = unflatten(child1_genes,shapes)
                        child2.neural_network.weights = unflatten(child2_genes,shapes)
                                
                        offspring.append(child1)
                        offspring.append(child2)
                        agents.extend(offspring)
                        return agents