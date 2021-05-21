# Introduction
This repo contains a sample code to show how to create a Flask API server by deploying our remote sensing imagery cloud removal PyTorch model that is trained on RICE dataset.
# Usage
1. Download the pretrained model.
- For RCIE1 (thin cloud dataset): [model_thin.pth](https://j8rd-my.sharepoint.com/:u:/g/personal/25_t_skings_club/EVw8ftEDszJBrT403aVmmCwBZFPOrNZuYb1pSVyU7MAQzg?e=aatrhv)
- For RCIE2 (thick cloud dateset): [model_thick.path](https://j8rd-my.sharepoint.com/:u:/g/personal/25_t_skings_club/ER8pK0UJrApDjuc0k7kiYi0BXCZZKi9_9MErXmhYk8SJWg?e=qtb8IX)
2. Place the model on root dir.
3. Run `app.py`.
# Tips
There are many images used for test in `test_thin` and `test_thick` folder.