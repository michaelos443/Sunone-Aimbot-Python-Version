# Seaborn Export Module Documentation

## Overview
A new export module has been added to the seaborn library that allows users to easily save figures in multiple file formats with a single function call. This module simplifies the process of exporting visualizations for publications, presentations, or web content.

## Features
* **Multi-format export** - Save figures in various formats (PNG, PDF, SVG, JPEG, TIFF, etc.)
* **Legend extraction** - Extract and save just the legend from a plot as a separate file
* **High-resolution support** - Control resolution (DPI) for high-quality exports
* **Batch processing** - Save in multiple formats with one command
* **Transparency control** - Save with transparent backgrounds for better integration

## Implementation Details
* Added new file: `seaborn/export.py`
* Updated `seaborn/__init__.py` to include the new module
* Added comprehensive examples in `examples/export_example.py`
* Added unit tests in `tests/test_export.py`

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

## Status and Links
* Pull request created and merged: [GitHub Pull Request #1](https://github.com/michaelos443/seaborn/pull/1)
* All tests passing
* Documentation available on:
  * [Confluence](https://test-team-e43poqe8.atlassian.net/wiki/spaces/SD/pages/9961473/Seaborn+Export+Module+Documentation)
  * [Linear Issue TES-20](https://linear.app/test-workspace-aug/issue/TES-20/seaborn-export-module-documentation)

## Next Steps
1. Add documentation to the official seaborn documentation
2. Create user guides and tutorials
3. Gather feedback from users
4. Consider additional export features based on feedback

---

**Issue Type**: Task  
**Priority**: Medium  
**Labels**: documentation, seaborn, export-module  
**Assignee**: Unassigned  
**Reporter**: Michael Osei
