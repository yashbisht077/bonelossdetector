import os

BASE_DIR = "dataset"
SUBSETS = ["train", "valid", "test"]

for subset in SUBSETS:
    label_dir = os.path.join(BASE_DIR, subset, "labels")
    image_dir = os.path.join(BASE_DIR, subset, "images")

    for label_file in os.listdir(label_dir):
        if not label_file.endswith(".txt"):
            continue

        label_path = os.path.join(label_dir, label_file)
        with open(label_path, "r") as f:
            lines = f.readlines()

        bone_loss_lines = [line for line in lines if line.startswith("0 ")]

        if bone_loss_lines:
            with open(label_path, "w") as f:
                f.writelines(bone_loss_lines)
        else:
            os.remove(label_path)
            image_name = label_file.replace(".txt", ".jpg")
            image_path = os.path.join(image_dir, image_name)
            if os.path.exists(image_path):
                os.remove(image_path)

print("Filtering complete — only Bone Loss images retained.")