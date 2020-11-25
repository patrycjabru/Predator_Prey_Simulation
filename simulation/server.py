from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid

from simulation.portrayal import agents_portrayal
from simulation.model import PPModel

canvas_element = CanvasGrid(agents_portrayal, 80, 80, 800, 800)

model_params = dict(height=80, width=80)

server = ModularServer(
    PPModel, [canvas_element], "Predator-Prey Simulation", model_params
)
server.port = 8521
