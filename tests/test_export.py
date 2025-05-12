"""Tests for export functionality."""
import os
import pytest
import matplotlib.pyplot as plt
import numpy as np
import tempfile
import shutil

import seaborn as sns
from seaborn.export import save_figure, export_legend


class TestExport:
    """Test the export functionality."""

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        """Create a temporary directory for test files and clean up after tests."""
        self.temp_dir = tempfile.mkdtemp()
        yield
        plt.close("all")
        shutil.rmtree(self.temp_dir)

    def test_save_figure_single_format(self):
        """Test saving a figure in a single format."""
        # Create a simple plot
        plt.figure()
        plt.plot([1, 2, 3], [1, 2, 3])

        # Save in PNG format
        path = os.path.join(self.temp_dir, "test_plot")
        saved_paths = save_figure(path=path, formats="png")

        # Check that the file was created
        assert len(saved_paths) == 1
        assert os.path.exists(saved_paths[0])
        assert saved_paths[0].endswith(".png")

    def test_save_figure_multiple_formats(self):
        """Test saving a figure in multiple formats."""
        # Create a simple plot
        plt.figure()
        plt.plot([1, 2, 3], [1, 2, 3])

        # Save in multiple formats
        path = os.path.join(self.temp_dir, "test_plot")
        formats = ["png", "pdf", "svg"]
        saved_paths = save_figure(path=path, formats=formats)

        # Check that all files were created
        assert len(saved_paths) == len(formats)
        for p, fmt in zip(saved_paths, formats):
            assert os.path.exists(p)
            assert p.endswith(f".{fmt}")

    def test_save_figure_with_directory_creation(self):
        """Test saving a figure with automatic directory creation."""
        # Create a simple plot
        plt.figure()
        plt.plot([1, 2, 3], [1, 2, 3])

        # Save in a subdirectory that doesn't exist yet
        path = os.path.join(self.temp_dir, "subdir", "test_plot")
        saved_paths = save_figure(path=path, formats="png")

        # Check that the directory and file were created
        assert os.path.exists(os.path.dirname(saved_paths[0]))
        assert os.path.exists(saved_paths[0])

    def test_export_legend(self):
        """Test exporting just the legend."""
        # Create a plot with a legend
        plt.figure()
        for i in range(3):
            plt.plot([1, 2, 3], [i, i+1, i+2], label=f"Line {i+1}")
        legend = plt.legend()

        # Export the legend
        path = os.path.join(self.temp_dir, "test_legend")
        saved_paths = export_legend(legend, path=path, formats="png")

        # Check that the file was created
        assert len(saved_paths) == 1
        assert os.path.exists(saved_paths[0])
        assert saved_paths[0].endswith(".png")

    def test_save_figure_jpg_format(self):
        """Test saving a figure in JPEG format."""
        # Create a simple plot
        plt.figure()
        plt.plot([1, 2, 3], [1, 2, 3])

        # Save as JPEG
        path = os.path.join(self.temp_dir, "test_plot")
        saved_paths = save_figure(path=path, formats="jpg")

        # Check that the file was created
        assert len(saved_paths) == 1
        assert os.path.exists(saved_paths[0])
        assert saved_paths[0].endswith(".jpeg")  # Note: jpg is converted to jpeg

    def test_save_figure_with_transparent_background(self):
        """Test saving a figure with transparent background."""
        # Create a simple plot
        plt.figure()
        plt.plot([1, 2, 3], [1, 2, 3])

        # Save with transparent background
        path = os.path.join(self.temp_dir, "test_plot")
        saved_paths = save_figure(path=path, formats="png", transparent=True)

        # Check that the file was created
        assert len(saved_paths) == 1
        assert os.path.exists(saved_paths[0])
