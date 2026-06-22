# HolePlate 2D UMBridge server using Ferrite.jl

This file presents the black box FEM solver for Model Discovery problems serving the [statFEM-EUCLID](https://github.com/statFEM-EUCLID/HolePlate2D_discovery.jl) client. The selected interface is [UM-Bridge](https://um-bridge-benchmarks.readthedocs.io/en/docs/) for connecting the FEM solver [Ferrite.jl](https://ferrite-fem.github.io/Ferrite.jl/stable/) and the calibration client (statFEM-EUCLID). 

## HolePlate 2D example

This package refers to the 2D example presented in the GitHub repository [HolePlate2D_discovery.jl](https://github.com/statFEM-EUCLID/HolePlate2D_calibration.jl). The details can be found in the article [*Unsupervised Constitutive Model Discovery from Sparse and Noisy Data*](https://doi.org/10.1016/j.cma.2025.118722). 

The user can choose between different mesh file to validate the results. Each corresponding to a different mesh size. 

## Setup

You will need to [install Julia](https://julialang.org/install/).

Afterwards, clone this repository and load all dependencies through the julia package manager (**Pkg**)

```
cd HolePlate2D_serverDiscovery_Ferrite.jl
julia --project=. 
using Pkg
Pkg.instantiate()
```

### Initialize

In order to start the server, the user should: 
```
julia --project=. runserver.jl
```
in the terminal or;
```
include("runserver.jl")
```
inside the *julia REPL*

The model is served on the port: 
```
http://localhost:4232
```