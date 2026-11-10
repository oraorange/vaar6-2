# GIF Thumbnail API — Variant 6

Practical assignment 2, stage 1. Converts the first frame of a GIF file to a PNG thumbnail while preserving the aspect ratio.

## Setup

```bash
python -m venv .venv
python -m pip install -r requirements.txt
```

## Usage

```bash
python -m src.cli examples/sample1.gif --size 128
python -m src.cli examples/sample2.gif --size 64
python -m src.cli examples/sample3.gif --size 32
```

Use `--output output/custom.png` to choose a target path. Successful execution prints the output path to stdout; errors are printed to stderr with a nonzero exit code.

## Tests

```bash
python -m pytest -q
```

## Configuration

`--size`: maximum thumbnail width and height in pixels (default 128). `--output`: output PNG path (default `output/<input_stem>.png`).

Stages 2 and 3 will add FastAPI, an XML API, Hypothesis state-machine tests, and SQLite.
