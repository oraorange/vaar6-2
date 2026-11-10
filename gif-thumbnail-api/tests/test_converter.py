"""Tests for GIF thumbnail conversion."""

import pytest
from PIL import Image

from src.converter import create_thumbnail


@pytest.mark.parametrize("size", [32, 64, 128])
def test_thumbnail(tmp_path, size):
    """Generate thumbnails of three different sizes."""
    source = tmp_path / "input.gif"
    target = tmp_path / "output.png"
    Image.new("RGB", (320, 160), "red").save(source, "GIF")
    assert create_thumbnail(source, target, size) == target
    with Image.open(target) as result:
        assert result.format == "PNG"
        assert result.size == (size, size // 2)


def test_missing_file(tmp_path):
    """Reject a missing GIF file."""
    with pytest.raises(FileNotFoundError):
        create_thumbnail(tmp_path / "missing.gif", tmp_path / "out.png")


def test_invalid_size(tmp_path):
    """Reject a non-positive thumbnail size."""
    with pytest.raises(ValueError):
        create_thumbnail(tmp_path / "input.gif", tmp_path / "out.png", 0)
