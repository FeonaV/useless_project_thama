import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("🌸 Petal Counter")
st.write("Upload a flower image, and I'll try to count the petals.")

uploaded_file = st.file_uploader("Choose a flower image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read image
    image = Image.open(uploaded_file).convert("RGB")
    image_np = np.array(image)
    img = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

    # Convert to gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.GaussianBlur(gray, (5,5), 0)

    # Threshold
    _, thresh = cv2.threshold(gray_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    if np.mean(gray) > 150:  # invert if background is white
        thresh = cv2.bitwise_not(thresh)

    # Morphological cleaning
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7,7))
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

    # Distance transform for petal centers
    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    _, sure_fg = cv2.threshold(dist_transform, 0.35 * dist_transform.max(), 255, 0)
    sure_fg = np.uint8(sure_fg)

    # Markers for watershed
    _, markers = cv2.connectedComponents(sure_fg)
    markers = markers + 1
    unknown = cv2.subtract(cv2.dilate(opening, kernel, iterations=3), sure_fg)
    markers[unknown == 255] = 0

    markers = cv2.watershed(img, markers)

    # Count petals
    unique_labels = np.unique(markers)
    petal_count = 0
    for lbl in unique_labels:
        if lbl <= 1:  # background/boundary
            continue
        mask = np.uint8(markers == lbl)
        if cv2.countNonZero(mask) > 500:
            petal_count += 1

    st.image(image, caption=f"Estimated Petals: {petal_count}", use_column_width=True)
    st.success(f"🌼 Estimated Petal Count: {petal_count}")