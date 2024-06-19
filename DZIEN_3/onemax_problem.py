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

#Ewaluacja
toolbox.register("evaluate",evalOneMax)

#opertor mutacji
toolbox.register("mutate",tools.mutFlipBit,indpb=0.05)

#operator selekcji
toolbox.register("select",tools.selTournament,tournsize=3)

