from ultralytics import YOLO
from pathlib import Path
import cv2
model = YOLO('results/YOLOv8n (FT)/detect/train/weights/best.pt')

output_dir = Path('test')
output_dir.mkdir(parents=True, exist_ok=True)

results = model.predict(source='dataset/test/images', conf=0.4, save=False)

for i, result in enumerate(results):
    im = result.plot()
    save_path = output_dir / f"prediction_{i+1}.jpg"
    cv2.imwrite(str(save_path), im)

print(f"\nAll predictions saved to: {output_dir.resolve()}")
