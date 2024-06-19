import random

from deap import base
from deap import creator
from deap import tools


creator.create("FitnessMax",base.Fitness,weights=(1.0,))
creator.create("Individual",list,fitness=creator.FitnessMax)

toolbox = base.Toolbox()

#Generator atrybutu
toolbox.register("attr_bools",random.randint,0,1)

#generator osobnika
toolbox.register("individual",tools.initRepeat,creator.Individual,toolbox.attr_bools,100)

#generator populacji
toolbox.register("population",tools.initRepeat,list,toolbox.individual)

#funkcja przystosowania
def evalOneMax(individual):
    return sum(individual)
