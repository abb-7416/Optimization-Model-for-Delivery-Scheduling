**🚚 Delivery Scheduling Optimization — Operations Research Project**
**🎓 PGDM — AI & Data Science
🧭 Domain: Operations Research (Optimization Model)
📖 Project Overview**

This project applies Linear Programming (LP) using Python (PuLP) to optimize delivery scheduling for an e-commerce logistics dataset.
The goal is to minimize total delivery cost while considering vehicle capacity constraints and varying delivery demands.

**🎯 Objective**

Develop a delivery optimization model that:

Minimizes total transportation cost

Assigns each delivery to an optimal vehicle

Respects delivery load capacity per vehicle

**🧰 Tools & Libraries**

Python

PuLP — Linear Programming solver

Geopy — Calculate distances from coordinates

Matplotlib — Visualization

**🧱 Methodology**
**Step 1 — Data Preparation**

Dataset: amazon_delivery.csv (from Kaggle)
Columns used:

Order_ID — Unique delivery identifier

Store_Latitude, Store_Longitude — Store coordinates

Drop_Latitude, Drop_Longitude — Delivery coordinates

Delivery_Time — Time taken for each delivery

Vehicle — Type of vehicle used

**Step 2 — Derived Feature**

Distance_km: Computed using geographic coordinates (Haversine/Geodesic method)

Demand: Normalized workload measure from Delivery_Time

<img width="1696" height="1066" alt="image" src="https://github.com/user-attachments/assets/9e5e927c-32f6-4dd9-b30e-b072d599a8a0" />


**🧮 Results**

Optimal vehicle assignments for each delivery

Total minimized cost of deliveries

Balanced workload across vehicles

**Visualization:**
Bar chart comparing total distance covered per vehicle.

**📦 Deliverables**
File	Description
delivery_optimization.ipynb	Jupyter Notebook with full code
data.csv	Cleaned dataset for analysis
README.md	Project documentation
**🧠 Learning Outcome**

Understand linear programming formulation

Apply optimization in logistics

Explore real-world constraint modeling using Python tools

**📊 Example Output**
**✅ Optimal Delivery Assignments (first 10):**
       Order_ID      Vehicle  Distance_km  Demand
0  ialx566343618     scooter        2.83     80.0
1  akqg208421122  motorcycle        9.13    100.0
...

💰 Estimated Total Delivery Cost: ₹4325.50
****🧩 Future Enhancements****

Include traffic and weather impact

Predict demand using Machine Learning

Integrate real-time GPS data
