#!/usr/bin/env python
# coding: utf-8
                              # 🚚 DELIVERY SCHEDULING OPTIMIZATION — LINEAR PROGRAMMING MODEL
# In[2]:


# Install PuLP if not installed
get_ipython().system('pip install pulp geopy')


# In[3]:


# === IMPORTS ===
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from geopy.distance import geodesic
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpBinary, PULP_CBC_CMD


# In[4]:


# === LOAD DATA ===
df = pd.read_csv("amazon_delivery.csv")


# In[5]:


# === PREPARE DATA ===
# Calculate distance (in km) between store and drop coordinates
df["Distance_km"] = df.apply(
    lambda row: geodesic(
        (row["Store_Latitude"], row["Store_Longitude"]),
        (row["Drop_Latitude"], row["Drop_Longitude"])
    ).km,
    axis=1
)


# In[6]:


# Select relevant columns
data = df[["Order_ID", "Distance_km", "Delivery_Time", "Vehicle"]].copy()
data = data.dropna()


# In[7]:


# Normalize the demand (Delivery_Time as proxy for workload)
data["Demand"] = data["Delivery_Time"] / data["Delivery_Time"].max() * 100


# In[8]:


# === MODEL PARAMETERS ===
vehicle_capacity = 500  # arbitrary workload capacity
vehicles = ["scooter", "motorcycle", "car"]
cost_per_km = {"scooter": 10, "motorcycle": 15, "car": 25}


# In[9]:


# === LINEAR PROGRAMMING MODEL ===
model = LpProblem("Amazon_Delivery_Optimization", LpMinimize)


# In[10]:


# Decision variable: 1 if vehicle v assigned to order i
x = LpVariable.dicts("x", ((i, v) for i in data.index for v in vehicles), cat=LpBinary)


# In[11]:


# Objective: minimize total cost (distance * cost per km)
model += lpSum(
    x[(i, v)] * data.loc[i, "Distance_km"] * cost_per_km[v]
    for i in data.index for v in vehicles
)


# In[12]:


# Each order must be assigned to exactly one vehicle
for i in data.index:
    model += lpSum(x[(i, v)] for v in vehicles) == 1


# In[13]:


# Capacity constraint for each vehicle type
for v in vehicles:
    model += lpSum(x[(i, v)] * data.loc[i, "Demand"] for i in data.index) <= vehicle_capacity


# In[14]:


# === SOLVE ===
model.solve(PULP_CBC_CMD(msg=False))


# In[15]:


# === RESULTS ===
assignments = []
for i in data.index:
    for v in vehicles:
        if x[(i, v)].value() == 1:
            assignments.append({
                "Order_ID": data.loc[i, "Order_ID"],
                "Vehicle": v,
                "Distance_km": round(data.loc[i, "Distance_km"], 2),
                "Demand": round(data.loc[i, "Demand"], 1),
            })

result_df = pd.DataFrame(assignments)
total_cost = sum(result_df["Distance_km"] * result_df["Vehicle"].map(cost_per_km))

print("\n✅ Optimal Delivery Assignments (first 10):")
print(result_df.head(10))
print(f"\n💰 Estimated Total Delivery Cost: ₹{total_cost:.2f}")


# In[16]:


# === VISUALIZE ===
plt.figure(figsize=(8, 5))
result_df.groupby("Vehicle")["Distance_km"].sum().plot(kind="bar", color=["skyblue", "salmon", "lightgreen"])
plt.title("Optimized Total Distance per Vehicle")
plt.ylabel("Distance (km)")
plt.xlabel("Vehicle Type")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

                                                           # --- THE END --- #