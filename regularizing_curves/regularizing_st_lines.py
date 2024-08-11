#Regularizing Curves
#Detecting and Regularizing Straight Lines

def is_straight_line(XY, tolerance=0.01):
    """Check if a set of points lies on a straight line."""
    x, y = XY[:, 0], XY[:, 1]
    A = np.vstack([x, np.ones(len(x))]).T
    m, c = np.linalg.lstsq(A, y, rcond=None)[0]  # Slope and intercept
    line_y = m * x + c
    return np.allclose(y, line_y, atol=tolerance)

def regularize_straight_line(XY):
    """Return the two endpoints of the line."""
    return np.array([XY[0], XY[-1]])

# Example usage
for i, XYs in enumerate(path_XYs):
    for j, XY in enumerate(XYs):
        if is_straight_line(XY):
            path_XYs[i][j] = regularize_straight_line(XY)
plot(path_XYs)