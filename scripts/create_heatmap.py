from pathlib import Path
import plotly.graph_objects as go
import plotly.io as pio
from IPython.display import Image

def create_heatmap(values, title='Predicted mutation effects', plot_interactive=True):
    # Create a directory to save the images
    images = Path('images')
    images.mkdir(parents=True, exist_ok=True)

    # Put 0 as midpoint for divergent colorscale
    midpoint = (0 - values.min().min()) / (values.max().max() - values.min().min())

    # Define custom colorscale for blue (negative) to red (positive)
    custom_colorscale = [[0, 'midnightblue'],
                         [midpoint, 'white'],
                         [1, 'red']]

    # Create heatmap trace
    heatmap_trace = go.Heatmap(
        x=values.columns,
        y=values.index,
        z=values,
        colorscale=custom_colorscale
    )

    # Create layout with equal aspect ratio
    layout = go.Layout(
        title=title,
        xaxis=dict(title='wildtype'),
        yaxis=dict(title='mutation', autorange='reversed')
    )

    # Create figure
    fig = go.Figure(data=[heatmap_trace], layout=layout)

    if plot_interactive:
        # Show the plot
        fig.show()
    else:
        # Save the plot as a PNG file
        image_path = images/f'{title}.png'
        pio.write_image(fig, image_path)

        # Display the saved PNG file
        display(Image(filename=image_path))