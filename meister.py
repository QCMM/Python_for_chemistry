#!/usr/bin/env python


import numpy as np


def compute_area_polygon(x, y):
    """Compute the surface area of a polygon.
    
    Parameters
    ----------
    x : np.array
        X-coordinates of the polygon's corners.
    y : np.array
        Y-coordinates of the polygon's corners.
    
    Returns
    -------
    area : type of x and y
        The surface area of the polygon.

    Raises
    ------
    TypeError
        When x and y do not have the same length.

    """
    # Shoelace algorithm, Meister, 1769
    if len(x) != len(y):
        raise TypeError("Arguments x and y must have the same length.")
    if len(x) < 2:
        return 0.0
    else:
        return abs( x[-1]*y[0] + np.dot(x[:-1], y[1:])
                   -x[0]*y[-1] - np.dot(x[1:], y[:-1]))/2


def check_single(x, y, area):
    np.testing.assert_almost_equal(compute_area_polygon(x, y), area)

def check_variants(x, y, area):
    x = np.asarray(x)
    y = np.asarray(y)
    check_single(x, y, area)
    check_single(x[::-1], y[::-1], area)
    check_single(x + 0.3, y - 0.5478, area)
    check_single(-2*x, 0.8*y, 1.6*area)
    xp = np.cos(0.3)*x - np.sin(0.3)*y
    yp = np.sin(0.3)*x + np.cos(0.3)*y
    check_single(xp, yp, area)

def test_compute_area_polygon():        
    # Simple geometries
    check_single([0, 0, 1, 1], [0, 1, 1, 0], 1.0)
    check_single([0.0, 0.0, 2.0], [0.0, 1.0, 1.0], 1.0)
    check_single([-0.5, 2.5, 1.0, 0.0], [0.0, 0.0, 0.5, 0.5], 1.0)
    
    # Corner cases: flat, coinciding points, too short vectors
    check_single([0.0, 2.0, -1.0], [0.0, 2.0, -1.0], 0.0)
    check_single([0.0, 0.0, 2.0, 2.0], [0.0, 1.0, 1.0, 1.0], 1.0)
    check_single([], [], 0.0)
    check_single([1], [2], 0.0)
    check_single([2.0, 1.0], [0.0, 0.0], 0.0)
