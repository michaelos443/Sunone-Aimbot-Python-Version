"""
Example script demonstrating the use of seaborn's export functionality.
"""
import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Import export functions directly
from seaborn.export import save_figure, export_legend

# Set the style
sns.set_theme(style="whitegrid")

# Create a directory for our exported figures if it doesn't exist
os.makedirs("exported_figures", exist_ok=True)

# Example 1: Simple line plot with multiple export formats
def example_line_plot():
    print("Creating and exporting a line plot...")

    # Generate some data
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Create a simple line plot
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, linewidth=2.5)
    plt.title("Sine Wave", fontsize=16)
    plt.xlabel("X", fontsize=14)
    plt.ylabel("sin(x)", fontsize=14)

    # Export in multiple formats
    paths = save_figure(
        path="exported_figures/sine_wave",
        formats=["png", "pdf", "svg"],
        dpi=300
    )

    print(f"Line plot exported to: {paths}")
    plt.close()

# Example 2: Scatter plot with hue and legend export
def example_scatter_plot():
    print("Creating and exporting a scatter plot with legend...")

    # Load the tips dataset
    tips = sns.load_dataset("tips")

    # Create a scatter plot
    plt.figure(figsize=(10, 8))
    scatter = sns.scatterplot(
        data=tips,
        x="total_bill",
        y="tip",
        hue="time",
        size="size",
        sizes=(20, 200),
        palette="viridis"
    )

    plt.title("Tips vs Total Bill by Time of Day", fontsize=16)
    plt.xlabel("Total Bill ($)", fontsize=14)
    plt.ylabel("Tip ($)", fontsize=14)

    # Get the legend
    legend = plt.gca().get_legend()

    # Export the main figure
    paths = save_figure(
        path="exported_figures/tips_scatter",
        formats=["png", "jpg"],
        dpi=300
        # Note: quality parameter removed as it might not be supported by all backends
    )

    # Export just the legend
    legend_paths = export_legend(
        legend,
        path="exported_figures/tips_legend",
        formats=["png", "pdf"]
    )

    print(f"Scatter plot exported to: {paths}")
    print(f"Legend exported to: {legend_paths}")
    plt.close()

# Example 3: Simple barplot visualization
def example_barplot():
    print("Creating and exporting a barplot...")

    # Create some sample data
    categories = ['A', 'B', 'C', 'D', 'E']
    values = [5, 7, 3, 8, 4]

    # Create a barplot
    plt.figure(figsize=(10, 6))
    barplot = sns.barplot(x=categories, y=values)

    plt.title("Sample Barplot", fontsize=16)
    plt.xlabel("Categories", fontsize=14)
    plt.ylabel("Values", fontsize=14)

    # Export with transparent background
    paths = save_figure(
        path="exported_figures/sample_barplot",
        formats=["png", "tiff"],
        dpi=300,
        transparent=True
    )

    print(f"Barplot exported to: {paths}")
    plt.close()

# Example 4: Multiple plots in a grid
def example_grid_plot():
    print("Creating and exporting a grid of plots...")

    # Load the iris dataset
    iris = sns.load_dataset("iris")

    # Create a pairplot
    pairplot = sns.pairplot(
        iris,
        hue="species",
        height=2.5,
        corner=True
    )

    # Export the pairplot
    paths = save_figure(
        fig=pairplot.fig,
        path="exported_figures/iris_pairplot",
        formats=["png", "pdf"],
        dpi=300
    )

    print(f"Pairplot exported to: {paths}")
    plt.close()

if __name__ == "__main__":
    print("Running seaborn export examples...")

    # Run all examples
    example_line_plot()
    example_scatter_plot()
    example_barplot()
    example_grid_plot()

    print("\nAll examples completed. Check the 'exported_figures' directory for the results.")
