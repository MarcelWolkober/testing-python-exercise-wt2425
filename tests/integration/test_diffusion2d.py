"""
Integration tests for functions in class SolveDiffusion2D
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))) #With out this my test will not be found

from diffusion2d import SolveDiffusion2D
import numpy as np

def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_physical_parameters
    """
    solver = SolveDiffusion2D()
    w, h, dx, dy = 2.0, 3.0, 0.5, 0.25
    d, T_cold, T_hot = 1.0, 250.0, 300.0
    expected_dt = 0.025  # (0.5**2 * 0.25**2) / (2 * 1.0 * (0.5**2 + 0.25**2))
    
    solver.initialize_domain(w, h, dx, dy)
    solver.initialize_physical_parameters(d, T_cold, T_hot)
    
    assert solver.dt == expected_dt

def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.set_initial_condition
    """
    solver = SolveDiffusion2D()
    w, h, dx, dy = 4.0, 4.0, 1.0, 1.0
    d, T_cold, T_hot = 1.0, 25.0, 30.0
    expected_u = np.array([
        [25.0, 25.0, 25.0, 25.0],
        [25.0, 25.0, 25.0, 25.0],
        [25.0, 25.0, 25.0, 25.0],
        [25.0, 25.0, 25.0, 25.0]
    ])
    
    solver.initialize_domain(w, h, dx, dy)
    solver.initialize_physical_parameters(d, T_cold, T_hot)
    u = solver.set_initial_condition()
    
    np.testing.assert_array_equal(u, expected_u)
