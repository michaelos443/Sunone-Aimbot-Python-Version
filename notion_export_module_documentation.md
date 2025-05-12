# 📊 Seaborn Export Module

## Overview
A new export module has been added to the seaborn library that allows users to easily save figures in multiple file formats with a single function call. This module simplifies the process of exporting visualizations for publications, presentations, or web content.

## Key Features
- 💾 **Multi-format export** - Save figures in various formats (PNG, PDF, SVG, JPEG, TIFF, etc.)
- 🏷️ **Legend extraction** - Extract and save just the legend from a plot as a separate file
- 🔍 **High-resolution support** - Control resolution (DPI) for high-quality exports
- 🔄 **Batch processing** - Save in multiple formats with one command
- 🖼️ **Transparency control** - Save with transparent backgrounds for better integration

## Implementation Details
The module consists of the following components:

| Component | Description |
|-----------|-------------|
| `seaborn/export.py` | Main module file containing export functionality |
| `seaborn/__init__.py` | Updated to include the new module |
| `examples/export_example.py` | Comprehensive examples demonstrating usage |
| `tests/test_export.py` | Unit tests ensuring functionality works correctly |

## Code Examples

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

**Function Signature:**
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

| Parameter | Type | Description |
|-----------|------|-------------|
| `fig` | `matplotlib.figure.Figure` | The figure to save. If None, uses the current figure. |
| `path` | `str` | The path where the figure should be saved, without file extension. |
| `formats` | `str` or `list` | The file format(s) to save the figure in. Can be a single format or a list of formats. |
| `dpi` | `int` | The resolution in dots per inch. |
| `quality` | `int` | For JPEG format only, the image quality from 1 to 100. |
| `transparent` | `bool` | If True, the figure background will be transparent (for formats that support transparency). |
| `bbox_inches` | `str` | Bounding box in inches. If 'tight', tries to figure out the tight bbox of the figure. |
| `pad_inches` | `float` | Amount of padding when bbox_inches is 'tight'. |
| `facecolor` | `str` | The figure facecolor. |
| `**kwargs` | | Additional keyword arguments passed to plt.savefig(). |

**Returns:**
- `List[str]`: List of paths where the figure was saved.

### export_legend()
Export only the legend of a plot to a separate file.

**Function Signature:**
```python
export_legend(
    legend,
    path="legend",
    formats="png",
    **kwargs
)
```

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `legend` | `matplotlib.legend.Legend` | The legend to export. |
| `path` | `str` | The path where the legend should be saved, without file extension. |
| `formats` | `str` or `list` | The file format(s) to save the legend in. |
| `**kwargs` | | Additional keyword arguments passed to save_figure(). |

**Returns:**
- `List[str]`: List of paths where the legend was saved.

## Use Cases

1. **Academic Publications**
   - Export high-resolution figures in formats required by journals (TIFF, EPS, etc.)
   - Extract legends for custom placement in multi-panel figures

2. **Web Content**
   - Save visualizations with transparent backgrounds for web integration
   - Generate both raster (PNG) and vector (SVG) formats for different use cases

3. **Presentations**
   - Create high-quality exports for presentations
   - Save in multiple formats to accommodate different presentation software

4. **Reports**
   - Batch export multiple visualizations in consistent formats
   - Ensure consistent resolution and quality across all figures

## Status and Links
- ✅ Pull request created and merged
- ✅ All tests passing
- 📝 Documentation available on:
  - [Confluence](https://test-team-e43poqe8.atlassian.net/wiki/spaces/SD/pages/9961473/Seaborn+Export+Module+Documentation)
  - [Linear Issue TES-20](https://linear.app/test-workspace-aug/issue/TES-20/seaborn-export-module-documentation)
  - [GitHub Pull Request #1](https://github.com/michaelos443/seaborn/pull/1)

## Next Steps
- [ ] Add documentation to the official seaborn documentation
- [ ] Create user guides and tutorials
- [ ] Gather feedback from users
- [ ] Consider additional export features based on feedback
