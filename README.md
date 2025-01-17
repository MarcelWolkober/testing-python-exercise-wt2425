# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

```bash
python -m pytest
========================================== test session starts ===========================================
platform win32 -- Python 3.13.1, pytest-8.3.4, pluggy-1.5.0
rootdir: C:\Users\marce\Desktop\Uni\SSE\Repos\testing-python-exercise-wt2425
collected 5 items                                                                                         

tests\integration\test_diffusion2d.py ..                                                            [ 40%] 
tests\unit\test_diffusion2d_functions.py FFF                                                        [100%]

================================================ FAILURES ================================================ 
_________________________________________ test_initialize_domain _________________________________________ 

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        w, h, dx, dy = 2.0, 3.0, 0.5, 0.5
        expected_nx = 4  # int(2.0 / 0.5)
        expected_ny = 6  # int(3.0 / 0.5)

        solver.initialize_domain(w, h, dx, dy)

>       assert solver.nx == expected_nx
E       assert 6 == 4
E        +  where 6 = <diffusion2d.SolveDiffusion2D object at 0x00000244B3B6FED0>.nx

tests\unit\test_diffusion2d_functions.py:19: AssertionError
__________________________________ test_initialize_physical_parameters ___________________________________ 

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_physical_parameters
        """
        solver = SolveDiffusion2D()
        d, T_cold, T_hot = 1.0, 250.0, 300.0
        solver.dx = 0.5
        solver.dy = 0.25
        expected_dt = 0.025 #(0.5**2 * 0.25**2) / (2 * 1.0 * (0.5**2 + 0.25**2))

        solver.initialize_physical_parameters(d, T_cold, T_hot)

        assert solver.D == d
        assert solver.T_cold == T_cold
        assert solver.T_hot == T_hot
>       assert solver.dt == expected_dt
E       assert 0.0625 == 0.025
E        +  where 0.0625 = <diffusion2d.SolveDiffusion2D object at 0x00000244B55A8770>.dt

tests\unit\test_diffusion2d_functions.py:37: AssertionError
------------------------------------------ Captured stdout call ------------------------------------------ 
dt = 0.0625
_______________________________________ test_set_initial_condition _______________________________________ 

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.set_initial_condition
        """
        solver = SolveDiffusion2D()
        solver.nx, solver.ny = 4, 4
        solver.dx, solver.dy = 1.0, 2.0
        solver.T_cold = 25.0
        solver.T_hot = 30.0
        expected_u = np.array([
            [25.0, 25.0, 25.0, 25.0],
            [25.0, 25.0, 25.0, 25.0],
            [25.0, 25.0, 25.0, 25.0],
            [25.0, 25.0, 25.0, 25.0]
        ])

        u = solver.set_initial_condition()

>       assert np.array_equal(u, expected_u)
E       assert False
E        +  where False = <function array_equal at 0x00000244913A68F0>(array([[30., 30., 30., 30.],\n       [30., 30., 30., 30.],\n       [30., 30., 30., 30.],\n       [30., 30., 30., 30.]]), array([[25., 25., 25., 25.],\n       [25., 25., 25., 25.],\n       [25., 25., 25., 25.],\n       [25., 25., 25., 25.]]))
E        +    where <function array_equal at 0x00000244913A68F0> = np.array_equal

tests\unit\test_diffusion2d_functions.py:57: AssertionError
======================================== short test summary info ========================================= 
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - assert 6 == 4
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters - assert 0.0625 == 0.025
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition - assert False
====================================== 3 failed, 2 passed in 0.56s =======================================
```

### unittest log


```bash
python -m unittest tests/unit/test_diffusion2d_functions.py
Fdt = 0.0625
FF
======================================================================
FAIL: test_initialize_domain (tests.unit.test_diffusion2d_functions.TestDiffusion2D.test_initialize_domain)
Check function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\marce\Desktop\Uni\SSE\Repos\testing-python-exercise-wt2425\tests\unit\test_diffusion2d_functions.py", line 25, in test_initialize_domain
    self.assertEqual(self.solver.nx, expected_nx)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 6 != 4

======================================================================
FAIL: test_initialize_physical_parameters (tests.unit.test_diffusion2d_functions.TestDiffusion2D.test_initialize_physical_parameters)
Checks function SolveDiffusion2D.initialize_physical_parameters
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\marce\Desktop\Uni\SSE\Repos\testing-python-exercise-wt2425\tests\unit\test_diffusion2d_functions.py", line 42, in test_initialize_physical_parameters
    self.assertEqual(self.solver.dt, expected_dt)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 0.0625 != 0.025

======================================================================
FAIL: test_set_initial_condition (tests.unit.test_diffusion2d_functions.TestDiffusion2D.test_set_initial_condition)        
Checks function SolveDiffusion2D.set_initial_condition
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\marce\Desktop\Uni\SSE\Repos\testing-python-exercise-wt2425\tests\unit\test_diffusion2d_functions.py", line 61, in test_set_initial_condition
    np.testing.assert_array_equal(u, expected_u)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^
  File "C:\Users\marce\Desktop\Uni\SSE\Repos\testing-python-exercise-wt2425\venv\Lib\site-packages\numpy\_utils\__init__.py", line 85, in wrapper
    return fun(*args, **kwargs)
  File "C:\Users\marce\Desktop\Uni\SSE\Repos\testing-python-exercise-wt2425\venv\Lib\site-packages\numpy\testing\_private\utils.py", line 1020, in assert_array_equal
    assert_array_compare(operator.__eq__, actual, desired, err_msg=err_msg,
    ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                         verbose=verbose, header='Arrays are not equal',
                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                         strict=strict)
                         ^^^^^^^^^^^^^^
  File "C:\Users\marce\Desktop\Uni\SSE\Repos\testing-python-exercise-wt2425\venv\Lib\site-packages\numpy\testing\_private\utils.py", line 884, in assert_array_compare
    raise AssertionError(msg)
AssertionError:
Arrays are not equal

Mismatched elements: 16 / 16 (100%)
Max absolute difference among violations: 5.
Max relative difference among violations: 0.2
 ACTUAL: array([[30., 30., 30., 30.],
       [30., 30., 30., 30.],
       [30., 30., 30., 30.],
       [30., 30., 30., 30.]])
 DESIRED: array([[25., 25., 25., 25.],
       [25., 25., 25., 25.],
       [25., 25., 25., 25.],
       [25., 25., 25., 25.]])

----------------------------------------------------------------------
Ran 3 tests in 0.064s

FAILED (failures=3)
```

### integration test log

```bash
pytest tests/integration/test_diffusion2d.py
============================================================ test session starts ============================================================
platform win32 -- Python 3.13.1, pytest-8.3.4, pluggy-1.5.0
rootdir: C:\Users\marce\Desktop\Uni\SSE\Repos\testing-python-exercise-wt2425
collected 2 items                                                                                                                            

tests\integration\test_diffusion2d.py FF                                                                                               [100%]

================================================================= FAILURES ================================================================== 
____________________________________________________ test_initialize_physical_parameters ____________________________________________________ 

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

>       assert solver.dt == expected_dt
E       assert 0.0625 == 0.025
E        +  where 0.0625 = <diffusion2d.SolveDiffusion2D object at 0x000001E755336270>.dt

tests\integration\test_diffusion2d.py:24: AssertionError
----------------------------------------------------------- Captured stdout call ------------------------------------------------------------ 
dt = 0.0625
________________________________________________________ test_set_initial_condition _________________________________________________________ 

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

>       np.testing.assert_array_equal(u, expected_u)

tests\integration\test_diffusion2d.py:44:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

args = (array([[30., 30., 30., 30.],
       [30., 30., 30., 30.],
       [30., 30., 30., 30.],
       [30., 30., 30., 30.]]), array([[25., 25., 25., 25.],
       [25., 25., 25., 25.],
       [25., 25., 25., 25.],
       [25., 25., 25., 25.]]))
kwargs = {}, old_name = 'y', new_name = 'desired'

    @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        for old_name, new_name in zip(old_names, new_names):
            if old_name in kwargs:
                if dep_version:
                    end_version = dep_version.split('.')
                    end_version[1] = str(int(end_version[1]) + 2)
                    end_version = '.'.join(end_version)
                    msg = (f"Use of keyword argument `{old_name}` is "
                           f"deprecated and replaced by `{new_name}`. "
                           f"Support for `{old_name}` will be removed "
                           f"in NumPy {end_version}.")
                    warnings.warn(msg, DeprecationWarning, stacklevel=2)
                if new_name in kwargs:
                    msg = (f"{fun.__name__}() got multiple values for "
                           f"argument now known as `{new_name}`")
                    raise TypeError(msg)
                kwargs[new_name] = kwargs.pop(old_name)
>       return fun(*args, **kwargs)
E       AssertionError: 
E       Arrays are not equal
E       
E       Mismatched elements: 16 / 16 (100%)
E       Max absolute difference among violations: 5.
E       Max relative difference among violations: 0.2
E        ACTUAL: array([[30., 30., 30., 30.],
E              [30., 30., 30., 30.],
E              [30., 30., 30., 30.],
E              [30., 30., 30., 30.]])
E        DESIRED: array([[25., 25., 25., 25.],
E              [25., 25., 25., 25.],
E              [25., 25., 25., 25.],
E              [25., 25., 25., 25.]])

venv\Lib\site-packages\numpy\_utils\__init__.py:85: AssertionError
----------------------------------------------------------- Captured stdout call ------------------------------------------------------------ 
dt = 0.25
========================================================== short test summary info ========================================================== 
FAILED tests/integration/test_diffusion2d.py::test_initialize_physical_parameters - assert 0.0625 == 0.025
FAILED tests/integration/test_diffusion2d.py::test_set_initial_condition - AssertionError:
============================================================= 2 failed in 0.57s =============================================================
```

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
