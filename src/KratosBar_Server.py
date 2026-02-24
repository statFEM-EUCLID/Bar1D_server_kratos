import numpy as np 
import umbridge
import KratosMultiphysics
from src.KratosBar import Kratos
import os
class BarModel(umbridge.Model):

    def __init__(self):
        super().__init__("Bar1D.FEM")
        
        path_sm = os.path.dirname(os.path.abspath(__file__))
        path_par = os.path.join(path_sm, 'Bar1D/ProjectParameters.json')
        
        with open(path_par, "r") as file_input:
            parameters = KratosMultiphysics.Parameters(file_input.read())    

        self.kratos = Kratos(parameters)
        self.kratos.Initialize()

    def get_input_sizes(self, config):
        return [1]

    def get_output_sizes(self, config):
        # n_nodes = self.kratos.GetNumberOfNodes(self)
        return [50]

    def __call__(self, parameters, config):

        E = np.array(parameters[0], dtype=float)
        posterior = self.kratos.solution(E)

        return [posterior.astype(float).tolist()]

    def supports_evaluate(self):
        return True