# Bar 1D UMBridge server using KratosMultiphysics

This file presents the black box FEM solver for UQ quantification problems serving the [statFEM.jl](https://github.com/jpthiele/statFEM.jl) client. The selected interface is [UM-Bridge](https://um-bridge-benchmarks.readthedocs.io/en/docs/) for connecting the FEM solver ([Kratos](https://github.com/KratosMultiphysics/Kratos)) and the UQ server. 

## Bar 1D example

This package refers to a simple 1D example involving a Bar under an uniaxial tension test. The detailed example can be found in the article [*Inferring displacement fields from sparse measurements using the statistical finite element method*](https://doi.org/10.1016/j.ymssp.2023.110574)

## Initial setup
As introduced, the two additional package required by the server are: 
* the FEM solver **KratosMultiPhysics**; 
* the interface **UM-Bridge**. 

For the installation instruction of *Kratos* the user is reffered to [Install.md](https://github.com/KratosMultiphysics/Kratos/blob/master/INSTALL.md), knowing that the following applications needs to be installed: 

* [StructuralMechanicsApplication](https://github.com/KratosMultiphysics/Kratos/tree/master/applications/StructuralMechanicsApplication);
 * [ConstitutiveLawApplication](https://github.com/KratosMultiphysics/Kratos/tree/master/applications/ConstitutiveLawsApplication)
 * [LinearSolversApplication](https://github.com/KratosMultiphysics/Kratos/tree/master/LinearSolversApplication)
 * [SystemIdentificationApplication](https://github.com/KratosMultiphysics/Kratos/tree/master/applications/SystemIdentificationApplication)
 * [OptimizationApplication](https://github.com/KratosMultiphysics/Kratos/tree/master/applications/OptimizationApplication)

## Run the server
In order to start the server, run the following command on the main folder: 
```
python3 runserver.py
```

The model is served on the port: 
```
http://localhost:4242
```
