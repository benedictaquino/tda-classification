import os
import struct
import numpy as np


def read(data: str = "train") -> (np.array, np.array):
    '''
    This function reads the MNIST training or testing dataset ubyte file to a
    numpy array

    Parameters
    ----------
    data : string designating train or test data sets
    Returns
    -------
    labels, images : a tuple of numpy arrays containing the training data
    '''
    if data == "train":
        label_filepath = "data/train-labels-idx1-ubyte"
        image_filepath = "data/train-images-idx3-ubyte"
    elif data == "test":
        label_filepath = "data/t10k-labels-idx1-ubyte"
        image_filepath = "data/t10k-images-idx3-ubyte"
    else:
        raise ValueError("Invalid argument")

    with open(label_filepath, "rb") as f:
        struct.unpack(">II", f.read(8))
        labels = np.fromfile(f, dtype=np.uint8)

    with open(image_filepath, "rb") as f:
        tmp1, tmp2, rows, cols = struct.unpack(">IIII", f.read(16))
        images = np.fromfile(f, dtype=np.uint8)\
            .reshape(len(labels), rows, cols)

    return images, labels


if __name__ == "__main__":
    try:
        # Load training and test data to numpy arrays
        train_images, train_labels = read("train")
        test_images, test_labels = read("test")
    except FileNotFoundError:  # change directory to base directory
        filepath = os.path.abspath(__file__)
        dname = os.path.abspath(os.curdir)
        os.chdir(
                os.path.abspath(
                    os.path.join(
                        filepath,
                        os.path.pardir,
                        os.path.pardir
                        )))

        train_labels, train_images = read("train")
        test_labels, test_images = read("test")

        os.chdir(dname)  # change back to current directory
