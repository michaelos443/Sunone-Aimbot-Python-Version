# Seaborn Export Module

## Overview
A new export module has been added to the seaborn library that allows users to easily save figures in multiple file formats with a single function call.

## Features
- `save_figure()`: Save matplotlib figures in various formats (PNG, PDF, SVG, JPEG, TIFF, etc.)
- `export_legend()`: Extract and save just the legend from a plot as a separate file
- Support for controlling resolution (DPI), transparency, and other export parameters

## Implementation Details
- Added new file: `seaborn/export.py`
- Updated `seaborn/__init__.py` to include the new module
- Added comprehensive examples in `examples/export_example.py`
- Added unit tests in `tests/test_export.py`

## Usage Examples

### Basic Usage
```python
import seaborn as sns
import matplotlib.pyplot as plt

# Create a simple plot
tips = sns.load_dataset("tips")
sns.scatterplot(data=tips, x="total_bill", y="tip")

# Save in multiple formats
sns.save_figure(formats=["png", "pdf", "svg"])
```

### Advanced Usage
```python
import seaborn as sns
import matplotlib.pyplot as plt

# Create a plot with a legend
tips = sns.load_dataset("tips")
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time")

# Get the legend
legend = plt.gca().get_legend()

# Export the main figure with high resolution
sns.save_figure(
    path="figures/tips_scatter",
    formats=["png", "jpg"],
    dpi=300
)

# Export just the legend
sns.export_legend(
    legend,
    path="figures/tips_legend",
    formats=["png", "pdf"]
)
```

## API Reference

### save_figure()
Save a matplotlib figure in one or multiple file formats.

```python
save_figure(
    fig=None,
    path="seaborn_plot",
    formats="png",
    dpi=300,
    quality=None,
    transparent=False,
    bbox_inches="tight",
    pad_inches=0.1,
    facecolor=None,
    **kwargs
)
```

**Parameters:**
- `fig`: The figure to save. If None, uses the current figure.
- `path`: The path where the figure should be saved, without file extension.
- `formats`: The file format(s) to save the figure in. Can be a single format or a list of formats.
- `dpi`: The resolution in dots per inch.
- `quality`: For JPEG format only, the image quality from 1 to 100.
- `transparent`: If True, the figure background will be transparent (for formats that support transparency).
- `bbox_inches`: Bounding box in inches. If 'tight', tries to figure out the tight bbox of the figure.
- `pad_inches`: Amount of padding when bbox_inches is 'tight'.
- `facecolor`: The figure facecolor.
- `**kwargs`: Additional keyword arguments passed to plt.savefig().

### export_legend()
Export only the legend of a plot to a separate file.

```python
export_legend(
    legend,
    path="legend",
    formats="png",
    **kwargs
)
```

**Parameters:**
- `legend`: The legend to export.
- `path`: The path where the legend should be saved, without file extension.
- `formats`: The file format(s) to save the legend in.
- `**kwargs`: Additional keyword arguments passed to save_figure().

## Status
- Pull request created and merged
- All tests passing
- Documentation needs to be added to the official seaborn documentation

## Related Links
- [Linear Issue: TES-20](https://linear.app/test-workspace-aug/issue/TES-20/seaborn-export-module-documentation)
- [GitHub Pull Request #1](https://github.com/michaelos443/seaborn/pull/1)

---
*Last updated: May 12, 2025*  
*Created by: Michael*
