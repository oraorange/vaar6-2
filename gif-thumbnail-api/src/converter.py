"""Convert the first GIF frame into a PNG thumbnail."""

from pathlib import Path

from PIL import Image, UnidentifiedImageError


DEFAULT_SIZE = 128


def create_thumbnail(source: Path, target: Path, size: int = DEFAULT_SIZE) -> Path:
    """Create a proportionally resized PNG from the first GIF frame."""
    if size <= 0:
        raise ValueError("Thumbnail size must be positive")
    if not source.is_file():
        raise FileNotFoundError(source)
    with Image.open(source) as image:
        if image.format != "GIF":
            raise ValueError("Input file must be a GIF")
        image.seek(0)
        frame = image.convert("RGBA")
        frame.thumbnail((size, size), Image.Resampling.LANCZOS)
        target.parent.mkdir(parents=True, exist_ok=True)
        frame.save(target, format="PNG")
    return target
