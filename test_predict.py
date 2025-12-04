from app import predict
import sys

img_path = r"Food Classification dataset/pizza/001.jpg"
print(f"Testing image: {img_path}")
label, prob = predict(img_path)
print(f"Prediction: {label}, probability: {prob}")
