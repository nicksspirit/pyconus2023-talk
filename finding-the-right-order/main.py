import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Input Variables
order_input = ctrl.Antecedent(np.arange(0, 3500, 150), "order_throughput")
pay_input = ctrl.Antecedent(np.arange(-365, 60, 1), "pay_turnaround")

# Output Variable
fin_ouput = ctrl.Consequent(np.arange(0, 100, 10), "financial")

# Defining triangular membership functions
order_input["poor"] = fuzz.trimf(order_input.universe, [0, 0, 1750])
order_input["average"] = fuzz.trimf(order_input.universe, [1200, 1750, 2250])
order_input["good"] = fuzz.trimf(order_input.universe, [1750, 3500, 3500])

# Plot membership function for order_throughput
order_input.view()

pay_input["poor"] = fuzz.trimf(pay_input.universe, [-365, -365, -120])
pay_input["average"] = fuzz.trimf(pay_input.universe, [-120, -30, -10])
pay_input["good"] = fuzz.trimf(pay_input.universe, [-30, 0, 60])

# Plot membership function for pay_turnaround
pay_input.view()

fin_ouput["poor"] = fuzz.trimf(fin_ouput.universe, [0, 0, 50])
fin_ouput["average"] = fuzz.trimf(fin_ouput.universe, [0, 50, 100])
fin_ouput["good"] = fuzz.trimf(fin_ouput.universe, [50, 100, 100])

# Plot membership function for financial
fin_ouput.view()

# Create Rules
rule1 = ctrl.Rule(order_input["poor"] | pay_input["poor"], fin_ouput["poor"])
rule2 = ctrl.Rule(order_input["average"] | pay_input["average"], fin_ouput["average"])
rule3 = ctrl.Rule(order_input["good"] | pay_input["good"], fin_ouput["good"])

# Create Fuzzy Logic System
fin_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
financials = ctrl.ControlSystemSimulation(fin_ctrl)

# Provide some input to our fuzzy logix system.
# Try to change the input and see what happens
financials.input["order_throughput"] = 2600.94
financials.input["pay_turnaround"] = 10

financials.compute()

# Let's output the score our fuzzy logic system gave the financial factor.
print("Score for Financials: ", round(financials.output["financial"], 2))

fin_ouput.view(sim=financials)
plt.show()
