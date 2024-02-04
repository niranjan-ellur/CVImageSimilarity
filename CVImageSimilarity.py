import os
import cv2
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim

def image_similarity(image1_path, image2_path):
    # Read images
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)

    # Convert images to grayscale
    gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Resize the smaller image to match the larger image
    if gray_image1.shape != gray_image2.shape:
        height, width = max(gray_image1.shape[0], gray_image2.shape[0]), max(gray_image1.shape[1], gray_image2.shape[1])
        gray_image1 = cv2.resize(gray_image1, (width, height))
        gray_image2 = cv2.resize(gray_image2, (width, height))

    # Compute Structural Similarity Index (SSI)
    similarity_index, _ = ssim(gray_image1, gray_image2, full=True)

    return similarity_index

def calculate_average_similarity(folder1, folder2, name):
    files1 = [file1 for file1 in os.listdir(folder1) if os.path.splitext(file1)[0] == name]
    files2 = [file2 for file2 in os.listdir(folder2) if file2.startswith(name.lower())]

    if not files1 or not files2:
        print(f"No images found for comparison with {name}")
        return None

    total_similarity = 0
    count = 0

    for file1 in files1:
        for file2 in files2:
            image1_path = os.path.join(folder1, file1)
            image2_path = os.path.join(folder2, file2)

            try:
                # Compare images and get similarity score
                similarity_score = image_similarity(image1_path, image2_path)

                # Display the pair of images being compared, their similarity score, and the images
                print(f"Comparing {file1} and {file2}: Similarity Score = {similarity_score:.2f}%")

                # Display images side by side
                fig, axes = plt.subplots(1, 2, figsize=(8, 4))
                axes[0].imshow(cv2.cvtColor(cv2.imread(image1_path), cv2.COLOR_BGR2RGB))
                axes[0].set_title('Image 1')
                axes[1].imshow(cv2.cvtColor(cv2.imread(image2_path), cv2.COLOR_BGR2RGB))
                axes[1].set_title('Image 2')
                plt.show(block=False)  # Display the images without blocking

                # Wait for a short duration (e.g., 1 second) to allow viewing
                plt.pause(1)

                # Close the current figures
                plt.close('all')

                # Accumulate similarity scores for average calculation
                total_similarity += similarity_score
                count += 1
            except Exception as e:
                print(f"Error comparing {file1} and {file2}: {e}")

    if count == 0:
        print(f"No valid comparisons found for {name}")
        return None

    # Calculate average similarity score
    average_similarity = total_similarity / count
    print(f"Average Similarity Score for {name}: {average_similarity:.2f}%")
    return average_similarity

def compare_folders(folder1, folder2):
    names1 = set(os.path.splitext(file1)[0] for file1 in os.listdir(folder1))
    
    for name in names1:
        calculate_average_similarity(folder1, folder2, name)

# Example usage:
folder1_path = r"D:\git hub upload\cv python\REFERENCE"  # Replace with the path to the first folder
folder2_path = r"D:\git hub upload\cv python\TEST" # Replace with the path to the first folder

compare_folders(folder1_path, folder2_path)
