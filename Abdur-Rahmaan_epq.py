#This model shows the relationship between EOQ and EPQ, as well as how the daily production rate affects EPQ .
import math

annual_demand = 12000
setup_cost = 50
holding_cost = 2
daily_demand_rate = 40
daily_production_rate = 100000

def calculate_epq(demand, setup, hold_cost, d_rate, p_rate):
    return math.sqrt(
        (2 * demand * setup) /
        (hold_cost * (1 - d_rate / p_rate))
    )

epq = calculate_epq(
    annual_demand,
    setup_cost,
    holding_cost,
    daily_demand_rate,
    daily_production_rate
)

runs_per_year = annual_demand / epq
run_length_days = epq / daily_production_rate


max_inventory = epq * ( 1 - daily_demand_rate / daily_production_rate
)
   

print("EPQ RESULTS")
print("Optimal production quantity:", round(epq, 2))
print("Production runs per year:", round(runs_per_year, 2))
print("Length of each run (days):", round(run_length_days, 1))
print("Maximum inventory level:", round(max_inventory, 2))

#QUESTION 1.The  EPQ is now 904.53 units. Therefore, the EPQ decreases because the factory produces inventory faster,compared to demand thus increasing the portion of each batch accummalating as stock.

#QUESTION 2 The EPQ is now 774.75 units. The EOQ is 774.60. EOQ is similar to EPQ because when production is extremely fast, it is as if an entire order is received at once. Therefore, the EPQ approaches the EOQ.