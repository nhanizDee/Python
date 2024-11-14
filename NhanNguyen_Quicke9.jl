#=
NhanNguyen_Quicke9:
- Julia version: 
- Author: nhanf
- Date: 2024-11-14
=#
using JuMP
using GLPK

# Define the model with GLPK solver
model = Model(GLPK.Optimizer)

# Define variables
@variable(model, x1 >= 0)  # Number of batches of Product 1
@variable(model, x2 >= 0)  # Number of batches of Product 2

# Objective function: Maximize profit
@objective(model, Max, 3000 * x1 + 5000 * x2)

# Constraints
@constraint(model, 1 * x1 + 0 * x2 <= 4)   # Plant 1 constraint
@constraint(model, 0 * x1 + 2 * x2 <= 12)  # Plant 2 constraint
@constraint(model, 3 * x1 + 2 * x2 <= 18)  # Plant 3 constraint

# Solve the model
optimize!(model)

# Display results
println("Optimal number of batches for Product 1: ", value(x1))
println("Optimal number of batches for Product 2: ", value(x2))
println("Maximum profit: $", objective_value(model))
