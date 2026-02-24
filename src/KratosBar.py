import numpy as np
import KratosMultiphysics
import KratosMultiphysics.OptimizationApplication as KratosOA
from KratosMultiphysics.StructuralMechanicsApplication.structural_mechanics_analysis import StructuralMechanicsAnalysis


''' This class embedeeds the FEM solver. It takes as input the vector comprehending elasticity modulus samples and it gives as an output
    the displacement at the last node of the bar.

    The number of nodes are given as input
'''

class CustomAnalysisStage(StructuralMechanicsAnalysis):
    def Reset(self) -> None:
        self.continue_running = True

class Kratos:
    def __init__(self, project_parameters: KratosMultiphysics.Parameters) -> None:
        self.model = KratosMultiphysics.Model()
        self.analysis = CustomAnalysisStage(self.model, project_parameters)

    def Initialize(self) -> None:
        self.analysis.Initialize()

    ### Solution of the FEM problem
    def solution(self, youngs_modulus: float) -> np.ndarray:
        model_part: KratosMultiphysics.ModelPart = self.analysis._GetSolver().GetComputingModelPart()

        # this creates seperate properties per each element.
        KratosOA.OptimizationUtils.CreateEntitySpecificPropertiesForContainer(model_part, model_part.Elements, False)

        # assign the Youngs modulus
        e_exp = KratosMultiphysics.Expression.ElementExpression(model_part)
        KratosMultiphysics.Expression.LiteralExpressionIO.SetData(e_exp, youngs_modulus * 1e9)
        KratosOA.PropertiesVariableExpressionIO.Write(e_exp, KratosMultiphysics.YOUNG_MODULUS)

        # run the simulation
        self.analysis.Reset()
        self.analysis.time = self.analysis.project_parameters["problem_data"]["start_time"].GetDouble()
        model_part.ProcessInfo.SetValue(KratosMultiphysics.STEP, 0)
        model_part.ProcessInfo.SetValue(KratosMultiphysics.TIME, 0)
        model_part.ProcessInfo.SetValue(KratosMultiphysics.DELTA_TIME, 0)

        

        self.analysis.RunSolutionLoop()
        self.analysis.RunSolutionLoop()

        # extract the displacements numpy vector
        u_exp = KratosMultiphysics.Expression.NodalExpression(model_part)
        KratosMultiphysics.Expression.VariableExpressionIO.Read(u_exp, KratosMultiphysics.DISPLACEMENT_X, is_historical=True)

        return u_exp.Evaluate() # matrix [n, 3]

    def GetNumberOfNodes(self) -> int:
        return self.analysis._GetSolver().GetComputingModelPart().NumberOfNodes()

    def Finalize(self) -> None:
        self.analysis.Finalize()
