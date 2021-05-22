import torch
import cv2
import numpy as np
from model import Generator

def cloud_remove(cloud_cover, org_img='inp.png', sr_img='out.png'):
    # configuration
    folder_in = './static/img/upload/'
    foler_out = './static/img/result/'
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = Generator(0)
    model.load_state_dict(torch.load(f'model_{cloud_cover[0].lower()+cloud_cover[1:]}.pth'))
    model.to(device)

    # read
    img = cv2.imread(folder_in+org_img, cv2.IMREAD_COLOR)
    img = cv2.resize(img, (256, 256))
    img = img.astype(np.float32) / 255.
    img = (torch.from_numpy(np.transpose(img[:, :, [2, 1, 0]], (2, 0, 1))).float()-0.5)/0.5
    img = img.unsqueeze(0).to(device)
    
    # inference
    with torch.no_grad():
        output = model(img)
    
    # save
    output = (output.data.squeeze().float().cpu().numpy()*0.5+0.5)*255
    output = np.transpose(output[[2, 1, 0], :, :], (1, 2, 0)).astype(np.uint8)
    cv2.imwrite(foler_out+sr_img, output)