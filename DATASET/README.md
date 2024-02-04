Dataset Description

 Overview

The dataset used for image comparison consists of images organized in two folders: a reference folder (`REFERENCE`) and a test folder (`TEST`). Each folder contains a collection of images with varying content and quality.

Dataset Structure

Reference Folder (`REFERENCE`): This folder serves as the baseline for comparison. It contains a set of images that will be compared against corresponding images in the test folder.

Test Folder (`TEST`): This folder contains images that will be compared against the reference images. Image pairs are identified based on the unique names of the images.

Image Naming Convention

Images in both the reference and test folders follow a naming convention to facilitate pairing for comparison. The script extracts the base name of the images, removing the file extension, to identify matching pairs.

Example


REFERENCE/
|-- image1_reference.jpg
|-- image2_reference.jpg
|-- ...

TEST/
|-- image1_test.jpg
|-- image2_test.jpg
|-- ...
