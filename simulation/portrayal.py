from simulation.agents import Predator, Prey


def agents_portrayal(agent):
    if agent is None:
        return

    portrayal = {}

    if type(agent) is Prey:
        portrayal["Shape"] = "circle"
        portrayal["scale"] = 0.9
        portrayal["Layer"] = 1
        portrayal["r"] = 0.8
        portrayal["Color"] = "#000000"
        portrayal["Filled"] = "true"

    elif type(agent) is Predator:
        portrayal["Shape"] = "circle"
        portrayal["scale"] = 0.9
        portrayal["Layer"] = 2
        portrayal["Color"] = "#00FF0F"
        portrayal["Filled"] = "true"
        portrayal["r"] = 0.8

    return portrayal
