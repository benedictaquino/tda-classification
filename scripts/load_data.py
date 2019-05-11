import struct
from pathlib import Path
import numpy as np


def read_mnist(data: str = 'train') -> (np.array, np.array):
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
    # get path to data directory relative to this script's location
    directory = Path(__file__).parent.parent / 'data'

    if data == 'train':  # load training set
        label_filepath = directory / 'train-labels-idx1-ubyte'
        image_filepath = directory / 'train-images-idx3-ubyte'
    elif data == 'test':  # load testing set
        label_filepath = directory / 't10k-labels-idx1-ubyte'
        image_filepath = directory / 't10k-images-idx3-ubyte'
    else:  # raise error
        raise ValueError('Invalid argument')

    with open(label_filepath, 'rb') as f:
        struct.unpack('>II', f.read(8))
        labels = np.fromfile(f, dtype=np.uint8)

    with open(image_filepath, 'rb') as f:
        _, _, rows, cols = struct.unpack('>IIII', f.read(16))
        images = np.fromfile(f, dtype=np.uint8)\
            .reshape(len(labels), rows, cols)

    return images, labels


if __name__ == '__main__':
    train_images, train_labels = read_mnist('train')
    test_images, test_labels = read_mnist('test')
