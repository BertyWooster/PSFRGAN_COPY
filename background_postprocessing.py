import torch


def get_background_map(parse_map_onehot):
    back_map = parse_map_onehot[0, :1, :, :]
    back_map = torch.transpose(back_map, 0, 1)
    back_map = torch.transpose(back_map, 1, 2)
    return back_map


def set_background(img, back, map):
    img = img
    return img
