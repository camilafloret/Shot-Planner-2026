
import sys
import os
import numpy as np

# Add webapp to path
sys.path.append(os.path.join(os.getcwd(), 'webapp'))

import physics_engine
from numpy import radians

print("Testing Physics Engine with FRC 2026 constants...")
x = -3.0
y = 0.5
v = 8.0
angle = radians(60)

print(f"State: x={x}, y={y}, v={v}, angle=60deg")

# Test 1: Polar Zone
try:
    zone = physics_engine.get_ang_speed_space(x, y)
    print(f"Polar Zone Area: {zone['area']}")
    print(f"Angles count: {len(zone['angles'])}")
    print(f"Sample speeds: Lower={zone['lower_speeds'][0]:.4f}, Upper={zone['upper_speeds'][0]:.4f}")
except Exception as e:
    print(f"Polar Zone Failed: {e}")

# Test 2: Velocity Budget
try:
    v_min, v_max = physics_engine.get_velocity_budget(x, y, angle)
    print(f"Velocity Budget: Min={v_min}, Max={v_max}")
except Exception as e:
    print(f"Velocity Budget Failed: {e}")

# Test 3: Check Shot
try:
    res = physics_engine.check_shot(x, y, v, angle)
    print(f"Check Shot Result: {res}")
except Exception as e:
    print(f"Check Shot Failed: {e}")
