Energy Fuel Mix Optimisation

A full optimisation and emissions analysis project for a coal-based power plant, combining linear programming, environmental economics, and strategic decision modelling. This project explores how fuel choices, CO₂ pricing, and SO₂ control technologies impact profitability, compliance, and long-term operational strategy.
*Based on a Data from 2101

Project Overview
----------------

This project builds a complete optimisation model for selecting the most profitable fuel mix while meeting electricity demand and staying within strict CO₂ and SO₂ emission limits. It uses real-world factors such as fuel prices, calorific values, carbon content, sulphur levels, ROC incentives, and transmission charges.

Using Excel Solver and scenario modelling, the project analyses how the optimal strategy changes under different carbon prices and evaluates whether the plant should invest in a Flue Gas Desulphurisation (FGD) system.

Key Features
------------

-> Linear Programming Model

Monthly fuel mix optimisation across Stockpile, Russian, and Scottish coal

Peak, Off-Peak, and Weekend demand bands

Objective: maximise annual profit

Constraints: CO₂ cap, SO₂ limits, fuel availability, power demand


-> CO₂ Price Scenarios

Three carbon price levels modelled:

[1] 0 €/t → £22.66M profit

[2] 20 €/t → £14.85M profit (shift toward Scottish coal)

[3] 30 €/t → £3.13M profit (emissions fall by ~43%)

Shows strong sensitivity to carbon policy and major shifts in fuel choices.

-> SO₂ & FGD Investment Analysis

Comparison of two desulphurisation technologies:

Wet Limestone FGD → Annual NPV +£1.87M

Dry Sorbent Injection (DSI) → Annual NPV –£2.64M

Wet Limestone stays below the £10.64M sulphur penalty line, while DSI exceeds it.

-> Visualisations

[1] Includes charts illustrating:

[2] Cost vs benefit of FGD systems

[3] Net NPV comparison

[4] CO₂ emission vs profit trends

[5] Fuel mix changes across scenarios


-> Technologies Used

[1] Excel Solver

[2] Python (streamlit, matplotlib, pandas, numpy)

[3] Linear Programming formulation

[4] Energy & environmental analytics

[5] Scenario modelling


-> Results Summary

[1] Profit declines rapidly as CO₂ price rises

[2] Cleaner fuels become optimal under high carbon prices

[3] Wet Limestone FGD is financially justified

[4] DSI FGD is not viable under current costs




Created as part of a mathematical optimisation and energy analytics project.
-----------------------


📄 License

This project is licensed under the MIT License.
