# 🦷 Bone Loss Detection in Dental X-rays using YOLOv8

**Internship Assignment Submission – Shankar Singh**  
**Deadline**: 19 July 2025


---

## 📁 1. Dataset Overview

- **Source**: [Roboflow Dataset](https://universe.roboflow.com/arshs-workspace414141/dadad-rvg/dataset/5)
- **Images**: 2,980 annotated dental radiographs
- **Format**: YOLOv8
- **Target Class**: `Bone Loss` (out of 9 total labels)
- **Preprocessing**: Auto-orientation, resize to 640x640 (also trained on 1024x1024)
- **Augmentation**:
  - Horizontal flip (50%)
  - HSV shift (hue: 0.015, saturation: 0.7, value: 0.4)
  - Rotation ±10°
  - Scale ±50%


---

## 🧠 2. Model Selection Rationale

YOLOv8 was selected due to:
- High accuracy with fast inference
- Real-time augmentation support
- Robust pre-trained weights
- Ease of fine-tuning on medical imaging tasks

### Trained Model Variants:
- 🧪 YOLOv8n (Nano)
- 🧪 YOLOv8n (Fine-Tuned)
- ⚡ YOLOv8s (Small)
- ⚙️ YOLOv8m (Medium)
- 🔁 YOLOv8m (1024x1024 Fine-Tuned)
- 🔁 YOLOv8m (Second Fine-Tuned)


---

## 📊 3. Model Performance Comparison

| Model Variant           | Params | GFLOPs | Precision | Recall | mAP@0.5 | mAP@0.5:0.95 | Inference | Best Epoch | Training Time |
|------------------------|--------|--------|-----------|--------|---------|--------------|-----------|-------------|----------------|
| YOLOv8n (Base)         | 3.0M   | 8.1    | 0.534     | 0.430  | 0.445   | 0.218        | ⚡ 2.8 ms  | 100         | 1.35 hr         |
| YOLOv8n (Fine-Tuned)   | 3.0M   | 8.1    | 0.504     | 0.456  | 0.451   | 0.223        | ⚡ 2.7 ms  | 50          | 0.66 hr         |
| YOLOv8s                | 11.1M  | 28.4   | 0.459     | 0.557  | 0.471   | 0.211        | ⚡ 5.3 ms  | 50          | ~0.9 hr         |
| YOLOv8m                | 25.8M  | 78.7   | 0.536     | 0.477  | 0.463   | 0.209        | 🐢 27.1 ms | 56          | ~1.5 hr         |
| YOLOv8m (1024 FT)      | 25.8M  | 78.7   | 0.440     | 0.428  | 0.420   | 0.203        | 🐌 70.0 ms | 12 (early)  | ~1.7 hr         |
| YOLOv8m (2nd FT)       | 25.8M  | 78.7   | 0.530     | 0.396  | 0.426   | 0.224        | 🐢 11.1 ms | 50          | ~1.4 hr         |


---

## 📈 4. Evaluation Metrics

- **Precision**: Measures how many predicted boxes are correct.
- **Recall**: Measures how many ground-truth boxes are found.
- **mAP@0.5**: Mean Average Precision at IoU threshold of 0.5.
- **mAP@0.5:0.95**: Generalization score across IoU thresholds.
- **Inference Time**: Time per image to make predictions.

> **Best All-Rounder:** YOLOv8m (2nd FT) — strong balance of metrics  
> **Best Recall:** YOLOv8s  
> **Best Speed:** YOLOv8n (Base)


---

## 🧪 5. Metric Limitations & Improvements

### 🔸 Lower Recall in YOLOv8m (2nd FT)
- Misses ~60% of actual positives — it's more conservative.
- ✅ **Fix**: Add more difficult examples and use recall-focused loss (e.g. Focal Loss).

### 🔸 mAP@0.5:0.95 < 0.25 in all models
- Indicates difficulty with precise localization (tight bounding boxes).
- ✅ **Fix**:
  - Use higher-res training (1024x1024 baseline)
  - Annotate cleaner/tighter bone loss boxes
  - Use test-time augmentation (TTA)

### 🔸 High Inference Time (YOLOv8m @ 27ms+)
- Slower for real-time or mobile deployment.
- ✅ **Fix**:
  - Use YOLOv8n or YOLOv8s
  - Apply quantization (INT8) or model pruning

---

## 🧾 6. Summary

- YOLOv8 family is highly effective for bone loss detection.
- All models successfully learned to localize bone loss with mAP@0.5 ~ 0.45
- Best generalization: YOLOv8m FT
- Best recall: YOLOv8s
- Best efficiency: YOLOv8n

🧠 Final models (`best.pt`) saved and validated with high-quality metrics and visualizations.

---

**Thank you for the opportunity!**
