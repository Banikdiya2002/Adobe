#Detecting and Regularizing Circles and Ellipses

from scipy.optimize import minimize

def fit_circle(XY):
    """Fit a circle to a set of points."""
    def calc_R(xc, yc):
        return np.sqrt((XY[:, 0] - xc) ** 2 + (XY[:, 1] - yc) ** 2)

    def f(c):
        Ri = calc_R(*c)
        return np.std(Ri)

    center_estimate = np.mean(XY, axis=0)
    center_optimized = minimize(f, center_estimate).x
    Ri = calc_R(*center_optimized)
    R = np.mean(Ri)
    return center_optimized, R

def is_circle(XY, tolerance=0.01):
    """Check if a set of points forms a circle."""
    center, radius = fit_circle(XY)
    Ri = np.sqrt((XY[:, 0] - center[0]) ** 2 + (XY[:, 1] - center[1]) ** 2)
    return np.allclose(Ri, radius, atol=tolerance)

def regularize_circle(XY):
    """Return the center and radius of the circle."""
    center, radius = fit_circle(XY)
    return center, radius

# Example usage
for i, XYs in enumerate(path_XYs):
    for j, XY in enumerate(XYs):
        if is_circle(XY):
            center, radius = regularize_circle(XY)
            print(f"Circle detected: Center = {center}, Radius = {radius}")