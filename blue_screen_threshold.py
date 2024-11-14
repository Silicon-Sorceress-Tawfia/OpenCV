import matplotlib.pyplot as plt
import numpy as np
import cv2

# Load the image
image = cv2.imread('pizza.png')  # Replace with your image file path

# Check if the image was successfully loaded
if image is None:
    print("Error: Could not load the image. Check the file path or file integrity.")
else:
    # Convert the image to HSV color space
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the blue color range in HSV
    lower_blue = np.array([100, 150, 50])  # Lower range of blue
    upper_blue = np.array([140, 255, 255])  # Upper range of blue

    # Create a binary mask for blue color
    blue_mask = cv2.inRange(image_hsv, lower_blue, upper_blue)

    # Invert the mask to get the non-blue region
    mask_inverted = cv2.bitwise_not(blue_mask)

    # Extract the blue foreground
    foreground = cv2.bitwise_and(image, image, mask=blue_mask)

    # Extract the non-blue background
    background = cv2.bitwise_and(image, image, mask=mask_inverted)

    # Convert the images to RGB for display with Matplotlib
    foreground_rgb = cv2.cvtColor(foreground, cv2.COLOR_BGR2RGB)
    background_rgb = cv2.cvtColor(background, cv2.COLOR_BGR2RGB)

    # Display the results
    plt.figure(figsize=(12, 6))

    # Original Image
    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.axis('off')

    # Foreground (Blue Regions)
    plt.subplot(1, 3, 2)
    plt.imshow(foreground_rgb)
    plt.title("Foreground (Blue Regions)")
    plt.axis('off')

    # Background (Non-Blue Regions)
    plt.subplot(1, 3, 3)
    plt.imshow(background_rgb)
    plt.title("Background (Non-Blue Regions)")
    plt.axis('off')

    plt.show()

    # Optionally save the results
    cv2.imwrite('foreground_blue.png', foreground)
    cv2.imwrite('background_non_blue.png', background)





