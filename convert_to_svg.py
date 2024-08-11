#Converting to SVG with Bézier Curves
def polyline_to_svg_bezier(XY, svg_path, color="black"):
    dwg = svgwrite.Drawing(svg_path, profile='tiny')
    path_data = [("M", (XY[0, 0], XY[0, 1]))]

    for i in range(1, len(XY)-1, 2):
        # Assume points are in pairs for the Bézier curve
        if i+2 < len(XY):
            path_data.append(("C", (XY[i, 0], XY[i, 1], XY[i+1, 0], XY[i+1, 1], XY[i+2, 0], XY[i+2, 1])))

    dwg.add(dwg.path(d=path_data, stroke=color, fill='none', stroke_width=2))
    dwg.save()

# Example usage
svg_path = 'output.svg'
for i, XYs in enumerate(path_XYs):
    for XY in XYs:
        polyline_to_svg_bezier(XY, f'output_{i}.svg')