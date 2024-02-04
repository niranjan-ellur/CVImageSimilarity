# CVImageSimilarity


## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Usage](#usage)
- [Example](#example)
- [License](#license)

## Introduction

The script compares images in two folders and calculates the average structural similarity index for each pair. It displays the images being compared, their similarity score, and the average similarity score for each unique image name.

## Requirements

Ensure you have the following dependencies installed:

- Python 3.x
- OpenCV (`pip install opencv-python`)
- Matplotlib (`pip install matplotlib`)
- scikit-image (`pip install scikit-image`)

## Usage

1. Clone the repository:

    ```bash
    git clone (https://github.com/niranjan-ellur/CVImageSimilarity.git)
    cd CVImageSimilarity
    ```

2. Run the script:

    ```bash
    python CVImageSimilarity.py
    ```

3. Follow the prompts to enter the paths to the two folders containing images.

## Example

```python
# Example usage:
folder1_path = r"path/to/first/folder"
folder2_path = r"path/to/second/folder"

compare_folders(folder1_path, folder2_path)
