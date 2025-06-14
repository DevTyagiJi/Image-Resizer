import cv2

# Load the image
image = cv2.imread("RANDOM.jpg", cv2.IMREAD_UNCHANGED)

# Check if image is loaded successfully
if image is None:
    print("Error: Image not found or could not be loaded.")
    exit()

# Get original dimensions
original_height, original_width = image.shape[:2]

# Calculate new dimensions (50%)
new_width = int(original_width * 0.5)
new_height = int(original_height * 0.5)

# Resize the image
resized_image = cv2.resize(image, (new_width, new_height))

# Save the resized image
cv2.imwrite("resized_image.jpg", resized_image)

# Display (optional)
cv2.imshow("Resized Image", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
