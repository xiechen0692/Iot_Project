from __future__ import division
from yolo.new_models import *
from utils.utils import *
from utils.datasets import *
import os
import sys
import time
import datetime
import argparse
import numpy as np
from PIL import Image
import random
import torch
from torch.utils.data import DataLoader
from torchvision import datasets
from torch.autograd import Variable
import scipy.misc as m
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.ticker import NullLocator

import pynvml
pynvml.nvmlInit()
handle = pynvml.nvmlDeviceGetHandleByIndex(0)
meminfo = pynvml.nvmlDeviceGetMemoryInfo(handle)



n_classes = 11
colors = [
    (random.randint(
        0, 255), random.randint(
            0, 255), random.randint(
                0, 255)) for _ in range(n_classes)]

##########################################################################


def label2color(colors, n_classes, seg):
    seg_color = np.zeros((seg.shape[0], seg.shape[1], 3))
    for c in range(n_classes):
        seg_color[:, :, 0] += ((seg == c) *
                               (colors[c][0])).astype('uint8')
        seg_color[:, :, 1] += ((seg == c) *
                               (colors[c][1])).astype('uint8')
        seg_color[:, :, 2] += ((seg == c) *
                               (colors[c][2])).astype('uint8')
    seg_color = seg_color.astype(np.uint8)
    return seg_color

# if __name__ == "__main__":
def dection_pic():
    parser = argparse.ArgumentParser()
    parser.add_argument("--image_folder", type=str, default="img_input", help="path to dataset")
    parser.add_argument("--model_def", type=str, default="yolo/yolov3_old.cfg", help="path to model definition file")
    parser.add_argument("--weights_path", type=str, default="yolo/yolov3.weights", help="path to weights file")
    parser.add_argument("--class_path", type=str, default="yolo/coco.names", help="path to class label file")
    parser.add_argument("--conf_thres", type=float, default=0.8, help="object confidence threshold")
    parser.add_argument("--nms_thres", type=float, default=0.5, help="iou thresshold for non-maximum suppression")
    parser.add_argument("--batch_size", type=int, default=1, help="size of the batches")
    parser.add_argument("--n_cpu", type=int, default=4, help="number of cpu threads to use during batch generation")
    parser.add_argument("--img_size", type=int, default=416, help="size of each image dimension")
    parser.add_argument("--checkpoint_model", type=str, help="path to checkpoint model")
    opt = parser.parse_args()
    print(opt)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    os.makedirs("output", exist_ok=True)

    # Set up model
    model = Darknet(opt.model_def, img_size=opt.img_size).to(device)
    # FCN_model = FCN8s(n_class=11).to(device)
    # FCN_model.load_state_dict(torch.load("checkpoints/FCNmodel_ckpt.pth"))

    if opt.weights_path.endswith(".weights"):
        # Load darknet weights
        model.load_darknet_weights(opt.weights_path)
    else:
        # Load checkpoint weights
        model.load_state_dict(torch.load(opt.weights_path))

    model.eval()  # Set in evaluation mode

    dataloader = DataLoader(
        ImageFolder(opt.image_folder, img_size=opt.img_size),
        batch_size=opt.batch_size,
        shuffle=False,
        num_workers=opt.n_cpu,
    )
    classes = load_classes(opt.class_path)  # Extracts class labels from file

    Tensor = torch.cuda.FloatTensor if torch.cuda.is_available() else torch.FloatTensor

    imgs = []  # Stores image paths
    img_detections = []  # Stores detections for each image index

    total_time = []
    print("\nPerforming object detection:")
    prev_time = time.time()
    for batch_i, (img_paths, input_imgs) in enumerate(dataloader):
        # Configure input
        input_imgs = Variable(input_imgs.type(Tensor))

        # Get detections
        with torch.no_grad():
            detections, x_beforeYOLOlayer= model(input_imgs)#
            ###
            # output = FCN_model(x_beforeYOLOlayer[0], x_beforeYOLOlayer[1], x_beforeYOLOlayer[2]).squeeze(0)
            # pr = output.data.cpu().numpy().transpose(1, 2, 0).argmax(axis=2)
            # out = label2color(colors, n_classes, pr)
            # m.imshow(out)
            ###
            detections = non_max_suppression(detections, opt.conf_thres, opt.nms_thres)
            print(len(detections))
        # Log progress
        current_time = time.time()
        inference_time = datetime.timedelta(seconds=current_time - prev_time)
        prev_time = current_time
        total_time.append(inference_time)
        print("\t+ Batch %d, Inference Time: %s" % (batch_i, inference_time))

        # Save image and detections
        imgs.extend(img_paths)
        img_detections.extend(detections)
    print("mean_time:",np.mean(np.array(total_time)))
    # Bounding-box colors
    cmap = plt.get_cmap("tab20b")
    colors = [cmap(i) for i in np.linspace(0, 1, 20)]
    colors2 = [cmap(i) for i in np.linspace(0, 1, 20)]
    colors3 = [cmap(i) for i in np.linspace(0, 1, 20)]
    colors4 = [cmap(i) for i in np.linspace(0, 1, 20)]
    colors5 = [cmap(i) for i in np.linspace(0, 1, 20)]
    colors = colors2 + colors3 + colors4 + colors5
    print(len(colors))
    print("\nSaving images:")
    # Iterate through images and save plot of detections
    object = []
    for img_i, (path, detections) in enumerate(zip(imgs, img_detections)):
        print("totalGPU:",meminfo.total % (1024 ** 2))  # 第二块显卡总的显存大小
        print("usedGPU:",meminfo.used % (1024 ** 2))  # 这里是字节bytes，所以要想得到以兆M为单位就需要除以1024**2
        print("availubleGPU:",meminfo.free % (1024 ** 2))  # 第二块显卡剩余显存大小
        print("(%d) Image: '%s'" % (img_i, path))
        # Create plot
        img = np.array(Image.open(path))
        plt.figure()
        fig, ax = plt.subplots(1)
        ax.imshow(img)
        # Draw bounding boxes and labels of detections
        if detections is not None:
            # Rescale boxes to original image
            # print("!!!!!!!!!!!!!!!!!!!!", detections.size())
            detections = rescale_boxes(detections, opt.img_size, img.shape[:2])
            unique_labels = detections[:, -1].cpu().unique()
            n_cls_preds = len(unique_labels)
            # print("colors:",len(colors))
            print("n_cls_preds:", n_cls_preds)
            bbox_colors = random.sample(colors, n_cls_preds)
            for x1, y1, x2, y2, conf, cls_conf, cls_pred in detections:
                object.append(classes[int(cls_pred)])
                print(int(cls_pred))
                print("\t+ Label: %s, Conf: %.5f" % (classes[int(cls_pred)], cls_conf.item()))

                box_w = x2 - x1
                box_h = y2 - y1

                color = bbox_colors[int(np.where(unique_labels == int(cls_pred))[0])]
                # Create a Rectangle patch
                bbox = patches.Rectangle((x1, y1), box_w, box_h, linewidth=2, edgecolor=color, facecolor="none")
                # Add the bbox to the plot
                ax.add_patch(bbox)
                # Add label
                plt.text(
                    x1,
                    y1,
                    s=classes[int(cls_pred)],
                    color="white",
                    verticalalignment="top",
                    bbox={"color": color, "pad": 0},
                )
        # Save generated image with detections
        # plt.axis("off")
        # plt.gca().xaxis.set_major_locator(NullLocator())
        # plt.gca().yaxis.set_major_locator(NullLocator())
        filename = path.split("/")[-1].split(".")[0]
        plt.savefig(f"img_output/{filename}.png", bbox_inches="tight", pad_inches=0.0)
        # plt.close()
    return object
