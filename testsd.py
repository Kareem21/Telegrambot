import requests
import json
import base64
from datetime import datetime
import os

url = "https://7tkca9ef130k7q-3001.proxy.runpod.net/sdapi/v1/txt2img"

# customization - 20 curated options shower/etc/standing/etc
payload = {
    "prompt": "a beautiful blonde 25 year old naked woman, raw , nsfw, (naked:1) with legs spread, sexy, nude , sitting on sofa, girl next door , messy hair, film grain, retro, Porta 160 color, shot on ARRI ALEXA 65, sharp focus on subject, Fujifilm XT-3",
    "negative_prompt": "blurry, clothes, distorted, weird body parts",
    "sampler_name": "Euler",
    "model_type" : "amIReal_V45",
    "num_inference_steps": 20,
    "model_type": "sdxl-v1",
    "scheduler_type": "dpmpp-2m-karras",
    "cfg_scale": 7,
    "height": 1024,
    "width": 1024,
     "batch_size": 1,
    "restore_faces": True,
    "inpaint_full_res": True,
    "seed": -1, 
    "n_iter": 2,
    "enable_hr": False,
    "hr_scale": 2,
    "denoising_strength": 0.7,
    "hr_second_pass_steps": 10,
}

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    images = json.loads(response.content)["images"]
    script_dir = os.path.dirname(os.path.abspath(__file__))

    for i, image_data in enumerate(images):
        decoded_base64_content = base64.b64decode(image_data)

        # Save the image with a timestamp and index as the filename
        filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{i}.jpeg"
        file_path = os.path.join(script_dir, filename)

        with open(file_path, "wb") as f:
            f.write(decoded_base64_content)
        print(f"Image saved as {file_path}")
else:
    print(f"Error: {response.status_code} - {response.text}")