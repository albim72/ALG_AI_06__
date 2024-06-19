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

def main():
    random.seed(64)
    #utworzenie populacji
    pop = toolbox.population(n=300)
    
    #CXPB - prawdopodobieństwo z który dwa osobniki zostaną reprodukowane
    #MUTPB - prawdopodobieństwo mutacji osobnika
    
    CXPB, MUTPB = 0.5,0.2
    
    print("Zaczynamy ewolucję....")
    
    #ewaluacja populacji wejściowej
    fitness = list(map(toolbox.evaluate,pop))
    for ind,fit in zip(pop,fitness):
        ind.fitness.values = fit
        
    print(f" Ewaluacji poddano {len(pop)} osobników")
    
    

