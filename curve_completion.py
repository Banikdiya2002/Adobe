#Curve Completion (Basic)
#Simple Spline Interpolation for Gaps
from scipy.interpolate import splprep, splev

def complete_curve(XY, num_points=100):
    """Complete a curve by interpolating it with a spline."""
    tck, u = splprep([XY[:, 0], XY[:, 1]], s=0)
    u_new = np.linspace(u.min(), u.max(), num_points)
    x_new, y_new = splev(u_new, tck)
    return np.array([x_new, y_new]).T

# Example usage
for i, XYs in enumerate(path_XYs):
    for j, XY in enumerate(XYs):
        if not np.allclose(XY[0], XY[-1]):  # Detect gaps in the curve
            path_XYs[i][j] = complete_curve(XY)
plot(path_XYs)