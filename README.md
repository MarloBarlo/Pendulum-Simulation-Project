# **Pendulum Simulation Project**

## Overview

This project features two implementations of a **pendulum simulation**:

1. A **real-time animated simulation** using **Pygame**, which visually demonstrates pendulum motion through physics-based modeling.
2. A **mathematically-driven animation** using **Matplotlib** and **SciPy**, showcasing a driven pendulum system modeled with differential equations.

These tools together provide a practical way to explore classical mechanics, numerical integration, and real-time visualization.

---

## Features

### 🔴 Pygame Simulation
- Simulates multiple pendulums with varying lengths and colors.
- Real-time rendering of swinging pendulums based on gravity and angular motion.
- Includes simple physics: angular velocity, acceleration, and damping.
- Uses OOP to define each pendulum as an instance of a class.

### 🔵 Matplotlib Simulation
- Models a **driven pendulum** using a system of differential equations.
- Simulates the effects of a vertically oscillating pivot (parametric excitation).
- Visualized with **Matplotlib animation**.
- Uses `scipy.integrate.odeint` for solving the system numerically.

---

## Getting Started

### 🔧 Requirements
Install the required libraries using pip:

```bash
pip install pygame matplotlib scipy numpy
```

### ▶️ Running the Simulations

#### 1. **Pygame Pendulum Simulation**
Run the Pygame script:
```bash
python pendulum_pygame.py
```

#### 2. **Matplotlib Driven Pendulum**
Run the Matplotlib script:
```bash
python driven_pendulum.py
```
It will generate an animation of the driven pendulum using `matplotlib.animation`.

---

## How It Works

### 📌 Pygame Version
Each `Pendulum` object calculates its position using:
- Angular acceleration:  
  \[
  \alpha = -\frac{g}{l} \sin(\theta)
  \]
- Position updated frame-by-frame, and visualized as a line and circle.

### 📌 Matplotlib Version
The driven pendulum is modeled by solving the second-order ODE:
\[
\frac{d^2\theta}{dt^2} = (1 - \alpha \omega^2 \cos(\omega t)) \sin(\theta)
\]
Where:
- `alpha` controls amplitude of pivot oscillation.
- `omega` is the oscillation frequency.

---

## Visual Output

- **Pygame**: A smooth animation with multiple pendulums swinging at different rates.
- **Matplotlib**: A clean animated plot showing how the driven pendulum moves in response to parametric excitation.

---
