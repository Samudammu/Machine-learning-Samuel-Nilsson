import os
import torch
from torchvision.models import resnet18, ResNet18_Weights
from torchvision import transforms
from PIL import Image
import matplotlib.pyplot as plt
from torchcam.methods import GradCAM
from torchcam.utils import overlay_mask

# Modell + labels
weights = ResNet18_Weights.DEFAULT
model = resnet18(weights=weights)
model.eval()

categories = weights.meta["categories"]

cam_extractor = GradCAM(model, target_layer="layer4")

# Transform
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

# Base path
BASE_DIR = os.path.dirname(__file__)

RESULT_DIR = os.path.join(BASE_DIR, "..", "results")

# CAM funktion
def run(image_path, name):
    img = Image.open(image_path).convert("RGB")

    input_tensor = transform(img).unsqueeze(0)

    output = model(input_tensor)

    pred_class = output.argmax().item()
    pred_name = categories[pred_class]

    print("\n========================")
    print("Image:", name)
    print("Prediction:", pred_name)

    activation_map = cam_extractor(pred_class, output)[0]

    cam = activation_map.squeeze().detach().cpu().numpy()
    cam = (cam - cam.min()) / (cam.max() - cam.min() + 1e-8)
    cam = (cam * 255).astype("uint8")

    cam_img = Image.fromarray(cam)

    result = overlay_mask(img, cam_img, alpha=0.5)

    plt.imshow(result)
    plt.axis("off")
    plt.title(pred_name)

    # spara varje bild separat
    save_path = os.path.join(RESULT_DIR, f"{name}_cam.png")
    plt.savefig(save_path)

    print("Saved to:", save_path)

    plt.show()

    print("Top-5 predictions:")
    values, indices = torch.topk(output, 5)

    for v, i in zip(values[0], indices[0]):
        print(categories[i.item()], float(v))

# visualiserning
images = [
    "boat.jpg",
    "boat_neg.jpg",
    "chair.jpg",
    "chair_neg.jpg",
    "flower.jpg",
    "flower_neg.jpg"
]

for img_name in images:
    image_path = os.path.join(BASE_DIR, "..", "images", img_name)
    run(image_path, img_name.replace(".jpg", ""))