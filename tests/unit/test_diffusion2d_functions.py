"""
Tests for functions in class SolveDiffusion2D
"""

import unittest
from unittest import TestCase
from diffusion2d import SolveDiffusion2D
import numpy as np

class TestDiffusion2D(TestCase):

    def setUp(self):
        self.solver = SolveDiffusion2D()

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        w, h, dx, dy = 2.0, 3.0, 0.5, 0.5
        expected_nx = 4  # int(2.0 / 0.5)
        expected_ny = 6  # int(3.0 / 0.5)
        
        self.solver.initialize_domain(w, h, dx, dy)
        
        self.assertEqual(self.solver.nx, expected_nx)
        self.assertEqual(self.solver.ny, expected_ny)

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_physical_parameters
        """
        d, T_cold, T_hot = 1.0, 250.0, 300.0
        self.solver.dx = 0.5
        self.solver.dy = 0.25
        expected_dt = 0.025  # (0.5**2 * 0.25**2) / (2 * 1.0 * (0.5**2 + 0.25**2))
        
        self.solver.initialize_physical_parameters(d, T_cold, T_hot)
        
        self.assertEqual(self.solver.D, d)
        self.assertEqual(self.solver.T_cold, T_cold)
        self.assertEqual(self.solver.T_hot, T_hot)
        self.assertEqual(self.solver.dt, expected_dt)

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.set_initial_condition
        """
        self.solver.nx, self.solver.ny = 4, 4
        self.solver.dx, self.solver.dy = 1.0, 1.0
        self.solver.T_cold = 25.0
        self.solver.T_hot = 30.0
        expected_u = np.array([
            [25.0, 25.0, 25.0, 25.0],
            [25.0, 25.0, 25.0, 25.0],
            [25.0, 25.0, 25.0, 25.0],
            [25.0, 25.0, 25.0, 25.0]
        ])
        
        u = self.solver.set_initial_condition()
        
        np.testing.assert_array_equal(u, expected_u)

if __name__ == '__main__':
    unittest.main()
