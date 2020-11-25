from mesa import Model
from mesa.space import MultiGrid

from simulation.agents import Prey, Predator
from simulation.schedule import RandomActivationByBreed


class PPModel(Model):

    height = 80
    width = 80

    initial_preys = 100
    initial_predators = 50

    def __init__(self, height=80, width=80, initial_preys=100,
                 initial_predators=50):

        super().__init__()
        self.height = height
        self.width = width
        self.initial_preys = initial_preys
        self.initial_predators = initial_predators

        self.schedule = RandomActivationByBreed(self)
        self.grid = MultiGrid(self.height, self.width, torus=True)

        # Create preys:
        for i in range(self.initial_preys):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            prey = Prey(self.next_id(), (x, y), self, True)
            self.grid.place_agent(prey, (x, y))
            self.schedule.add(prey)

        # Create predators
        for i in range(self.initial_predators):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            predator = Predator(self.next_id(), (x, y), self, True)
            self.grid.place_agent(predator, (x, y))
            self.schedule.add(predator)

        self.running = True

    def step(self):
        self.schedule.step()

    def run_model(self, step_count: int = 200):

        for i in range(step_count):
            self.step()
