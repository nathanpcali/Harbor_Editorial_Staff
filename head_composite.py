#!/usr/bin/env python3
"""
Composite head from portrait onto desert motorcycle photo.
Uses OpenCV and MediaPipe for face detection and alignment.
"""

import cv2
import numpy as np
import os

# Source images
BASE_IMAGE = "/Users/natecali/.cursor/projects/Users-natecali-Documents-Cursor-team-management/assets/sundays-race-vintage-09-e6191dea-bdf2-4d5a-ae9f-7a8addc53e0b.png"
HEAD_IMAGE = "/Users/natecali/.cursor/projects/Users-natecali-Documents-Cursor-team-management/assets/IMG_2904_Original-4a238624-6c76-449b-ba23-b94c3109712d.png"
OUTPUT_PATH = "/Users/natecali/Desktop/desert-motorcycle-with-my-head.png"


def detect_face_opencv(image):
    """Detect face using OpenCV's DNN face detector."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Try Haar cascade as fallback (built-in, no extra files)
    cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(cascade_path)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(30, 30))
    
    if len(faces) > 0:
        # Return largest face
        faces = sorted(faces, key=lambda f: f[2] * f[3], reverse=True)
        x, y, w, h = faces[0]
        # Expand to include hair - add padding
        pad = int(max(w, h) * 0.4)
        x = max(0, x - pad)
        y = max(0, y - pad)
        w = min(image.shape[1] - x, w + 2 * pad)
        h = min(image.shape[0] - y, h + 2 * pad)
        return (x, y, w, h)
    return None


def extract_head_region(image, face_rect):
    """Extract head region with elliptical mask for blending."""
    x, y, w, h = face_rect
    head = image[y:y+h, x:x+w].copy()
    
    # Create elliptical mask (soft edges for blending)
    mask = np.zeros((h, w), dtype=np.float32)
    cv2.ellipse(mask, (w//2, h//2), (w//2, h//2), 0, 0, 360, 1.0, -1)
    
    # Soften mask edges
    mask = cv2.GaussianBlur(mask, (51, 51), 15)
    
    return head, mask, (x, y, w, h)


def color_match(source, target):
    """Match color statistics of source to target for better blending."""
    # Convert to LAB for better color matching
    source_lab = cv2.cvtColor(source, cv2.COLOR_BGR2LAB)
    target_lab = cv2.cvtColor(target, cv2.COLOR_BGR2LAB)
    
    s_mean, s_std = cv2.meanStdDev(source_lab)
    t_mean, t_std = cv2.meanStdDev(target_lab)
    
    # Flatten to (3,) for broadcasting
    s_mean = s_mean.flatten()
    s_std = s_std.flatten()
    t_mean = t_mean.flatten()
    t_std = t_std.flatten()
    
    # Avoid division by zero
    s_std = np.where(s_std == 0, 1, s_std)
    t_std = np.where(t_std == 0, 1, t_std)
    
    source_lab = source_lab.astype(np.float64)
    source_lab = (source_lab - s_mean) * (t_std / s_std) + t_mean
    source_lab = np.clip(source_lab, 0, 255).astype(np.uint8)
    
    return cv2.cvtColor(source_lab, cv2.COLOR_LAB2BGR)


def composite_heads():
    """Main compositing function."""
    print("Loading images...")
    base_img = cv2.imread(BASE_IMAGE)
    head_img = cv2.imread(HEAD_IMAGE)
    
    if base_img is None or head_img is None:
        print("Error: Could not load images")
        return False
    
    print("Detecting faces...")
    base_face = detect_face_opencv(base_img)
    head_face = detect_face_opencv(head_img)
    
    if base_face is None:
        print("Error: Could not detect face in base (motorcycle) image")
        return False
    if head_face is None:
        print("Error: Could not detect face in head (portrait) image")
        return False
    
    print("Extracting and compositing...")
    
    # Extract head from portrait
    head_region, head_mask, (hx, hy, hw, hh) = extract_head_region(head_img, head_face)
    
    # Get target region from base image
    bx, by, bw, bh = base_face
    target_region = base_img[by:by+bh, bx:bx+bw]
    
    # Resize head to match target size
    head_resized = cv2.resize(head_region, (bw, bh), interpolation=cv2.INTER_LANCZOS4)
    mask_resized = cv2.resize(head_mask, (bw, bh), interpolation=cv2.INTER_LINEAR)
    
    # Color match head to target lighting
    head_matched = color_match(head_resized, target_region)
    
    # Apply warm tint to match golden hour (slight orange)
    head_matched = cv2.convertScaleAbs(head_matched, alpha=1.0, beta=5)
    head_matched[:, :, 0] = np.clip(head_matched[:, :, 0] * 0.95, 0, 255).astype(np.uint8)
    head_matched[:, :, 1] = np.clip(head_matched[:, :, 1] * 1.05, 0, 255).astype(np.uint8)
    head_matched[:, :, 2] = np.clip(head_matched[:, :, 2] * 1.1, 0, 255).astype(np.uint8)
    
    # Blend using mask
    mask_3ch = cv2.merge([mask_resized, mask_resized, mask_resized])
    blended = (head_matched * mask_3ch + target_region * (1 - mask_3ch)).astype(np.uint8)
    
    # Place back into base image
    result = base_img.copy()
    result[by:by+bh, bx:bx+bw] = blended
    
    print(f"Saving to {OUTPUT_PATH}...")
    cv2.imwrite(OUTPUT_PATH, result)
    
    return True


if __name__ == "__main__":
    success = composite_heads()
    if success:
        print("Done! Image saved to your Desktop.")
    else:
        print("Compositing failed.")
