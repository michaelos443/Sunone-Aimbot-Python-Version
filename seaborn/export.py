"""Functions for exporting seaborn plots in various file formats."""
import os
import inspect
import matplotlib.pyplot as plt
from typing import Optional, Union, List, Tuple
import warnings

__all__ = ["save_figure"]


def save_figure(
    fig: Optional[plt.Figure] = None,
    path: str = "seaborn_plot",
    formats: Union[str, List[str]] = "png",
    dpi: int = 300,
    quality: Optional[int] = None,
    transparent: bool = False,
    bbox_inches: str = "tight",
    pad_inches: float = 0.1,
    facecolor: Optional[str] = None,
    **kwargs
) -> List[str]:
    """
    Save a matplotlib figure in one or multiple file formats.

    Parameters
    ----------
    fig : matplotlib.figure.Figure, optional
        The figure to save. If None, uses the current figure.
    path : str, optional
        The path where the figure should be saved, without file extension.
        Default is 'seaborn_plot'.
    formats : str or list of str, optional
        The file format(s) to save the figure in. Can be a single format or
        a list of formats. Supported formats include 'png', 'jpg', 'jpeg',
        'pdf', 'svg', 'eps', 'tif', 'tiff', etc. Default is 'png'.
    dpi : int, optional
        The resolution in dots per inch. Default is 300.
    quality : int, optional
        For JPEG format only, the image quality from 1 to 100. Default is None,
        which uses the default quality setting.
    transparent : bool, optional
        If True, the figure background will be transparent (for formats that
        support transparency). Default is False.
    bbox_inches : str, optional
        Bounding box in inches. If 'tight', tries to figure out the tight bbox
        of the figure. Default is 'tight'.
    pad_inches : float, optional
        Amount of padding when bbox_inches is 'tight'. Default is 0.1.
    facecolor : str, optional
        The figure facecolor. Default is None, which uses the current figure
        facecolor.
    **kwargs
        Additional keyword arguments passed to plt.savefig().

    Returns
    -------
    saved_paths : list of str
        List of paths where the figure was saved.

    Examples
    --------
    >>> import seaborn as sns
    >>> import matplotlib.pyplot as plt
    >>> # Create a simple plot
    >>> tips = sns.load_dataset("tips")
    >>> g = sns.scatterplot(data=tips, x="total_bill", y="tip")
    >>> # Save in multiple formats
    >>> sns.save_figure(formats=["png", "pdf", "svg"])
    >>> # Save with specific path and higher resolution
    >>> sns.save_figure(path="figures/my_plot", dpi=600, formats="tiff")
    """
    if fig is None:
        fig = plt.gcf()

    if isinstance(formats, str):
        formats = [formats]

    saved_paths = []

    for fmt in formats:
        fmt = fmt.lower().strip('.')

        # Handle jpg/jpeg consistency
        if fmt == 'jpg':
            fmt = 'jpeg'

        # Check if format is supported
        if fmt not in plt.gcf().canvas.get_supported_filetypes():
            warnings.warn(f"Format '{fmt}' is not supported by the current backend. "
                         f"Supported formats are: {plt.gcf().canvas.get_supported_filetypes().keys()}")
            continue

        # Create the full path with extension
        full_path = f"{path}.{fmt}"

        # Create directory if it doesn't exist
        directory = os.path.dirname(full_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        # Set format-specific parameters
        save_kwargs = kwargs.copy()
        save_kwargs.update({
            'dpi': dpi,
            'bbox_inches': bbox_inches,
            'pad_inches': pad_inches,
            'transparent': transparent,
        })

        if facecolor is not None:
            save_kwargs['facecolor'] = facecolor

        # Add quality for JPEG
        if fmt == 'jpeg' and quality is not None:
            if 1 <= quality <= 100:
                # Check if the backend supports the quality parameter
                try:
                    from matplotlib.backends.backend_agg import FigureCanvasAgg
                    if hasattr(FigureCanvasAgg, 'print_jpg') and 'quality' in inspect.signature(FigureCanvasAgg.print_jpg).parameters:
                        save_kwargs['quality'] = quality
                    else:
                        warnings.warn("The current matplotlib backend does not support the 'quality' parameter for JPEG. Using default quality.")
                except (ImportError, AttributeError):
                    warnings.warn("Could not determine if the current matplotlib backend supports the 'quality' parameter for JPEG. Using default quality.")
            else:
                warnings.warn("JPEG quality must be between 1 and 100. Using default quality.")

        # Save the figure
        fig.savefig(full_path, format=fmt, **save_kwargs)
        saved_paths.append(full_path)

    return saved_paths


def export_legend(
    legend,
    path: str = "legend",
    formats: Union[str, List[str]] = "png",
    **kwargs
) -> List[str]:
    """
    Export only the legend of a plot to a separate file.

    Parameters
    ----------
    legend : matplotlib.legend.Legend
        The legend to export.
    path : str, optional
        The path where the legend should be saved, without file extension.
        Default is 'legend'.
    formats : str or list of str, optional
        The file format(s) to save the legend in. Default is 'png'.
    **kwargs
        Additional keyword arguments passed to save_figure().

    Returns
    -------
    saved_paths : list of str
        List of paths where the legend was saved.

    Examples
    --------
    >>> import seaborn as sns
    >>> import matplotlib.pyplot as plt
    >>> # Create a plot with a legend
    >>> tips = sns.load_dataset("tips")
    >>> g = sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time")
    >>> # Get the legend
    >>> legend = plt.gca().get_legend()
    >>> # Export only the legend
    >>> sns.export_legend(legend, path="figures/time_legend")
    """
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.axis('off')

    # Add the legend to the new figure
    ax.legend(
        handles=legend.legend_handles if hasattr(legend, 'legend_handles') else legend.get_legend_handles_labels()[0],
        labels=[text.get_text() for text in legend.texts] if hasattr(legend, 'texts') else legend.get_legend_handles_labels()[1],
        title=legend.get_title().get_text() if legend.get_title() else None,
        frameon=legend.get_frame_on() if hasattr(legend, 'get_frame_on') else True,
        **{k: getattr(legend, f"get_{k}")() for k in ["framealpha", "edgecolor"]
           if hasattr(legend, f"get_{k}")}
    )

    # Save the figure with just the legend
    saved_paths = save_figure(fig=fig, path=path, formats=formats, **kwargs)
    plt.close(fig)

    return saved_paths
