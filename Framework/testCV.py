import cv2


def show_image():
    # Read the image
    image = cv2.imread("/home/khushboo/Documents/GitHub/FYP/Framework/Aircrack-logo.png")

    # Check if the image was successfully loaded
    if image is not None:
        print("Image loaded successfully.")
        print("Image shape:", image.shape)
        print("Image data:\n", image)

        # Create a named window and display the image
        cv2.namedWindow("Photo", cv2.WINDOW_NORMAL)  # Use cv2.WINDOW_NORMAL for resizable window
        cv2.imshow("Photo", image)

        # Wait for a key press and display all windows
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Error: Unable to load the image.")
