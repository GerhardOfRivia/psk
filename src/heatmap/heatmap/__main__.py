# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# coding: utf-8

import logging
import numpy as np
import cv2
import matplotlib.pyplot as plt


logger = logging.getLogger()


def generate_heatmap(given, k1, k3, k5):
    fig = plt.figure(figsize=(15, 10))
    ax = plt.subplot(2, 2, 1)
    ax.set_title("")
    img = ax.imshow(given, cmap="gray", interpolation="nearest")
    ax = plt.subplot(2, 2, 2)
    ax.set_title("Disparity Size 1")
    img = ax.imshow(k1, cmap="jet", interpolation="nearest")
    plt.colorbar(img)
    ax = plt.subplot(2, 2, 3)
    ax.set_title("Disparity Size 3")
    img = ax.imshow(k3, cmap="jet", interpolation="nearest")
    plt.colorbar(img)
    ax = plt.subplot(2, 2, 4)
    ax.set_title("Disparity Size 5")
    img = ax.imshow(k5, cmap="jet", interpolation="nearest")
    plt.colorbar(img)
    fig.tight_layout()
    plt.savefig("{}.png".format(__title__), format='png')


def main():
    # Read images
    img = cv2.imread("img.png", cv2.IMREAD_UNCHANGED)

    # Perform disparitySSD three times for window sizes 1, 3, and 5
    k1 = (leftImg, rightImg, 1)
    k3 = disparitySSD(leftImg, rightImg, 3)
    k5 = disparitySSD(leftImg, rightImg, 5)

    # Generate graphs
    generate_heatmap(builtInImg, k1, k3, k5)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    except Exception as err:
        logger.exception(err)
