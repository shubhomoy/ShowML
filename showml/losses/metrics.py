import numpy as np
from showml.losses import MeanSquareError, BinaryCrossEntropy
from showml.losses.loss_functions import CrossEntropy


def r2_score(y: np.ndarray, z: np.ndarray) -> float:
    """
    Calculate the r^2 (coefficient of determination) score of the model
    param y: The true values
    param z: The predicted values
    return: The r^2 score
    """
    rss = np.sum(np.square(y - z))
    tss = np.sum(np.square(y - np.mean(y)))
    r_2 = 1 - (rss / tss)
    return r_2


def accuracy(y: np.ndarray, z: np.ndarray) -> float:
    """
    Compute the classification accuracy of the model
    param y: The true labels
    param z: The predicted labels
    return: The classification accuracy of the model
    """
    if y.ndim == 1:
        # y and z are not one hot encoded
        true_class = y
        predicted_class = [1 if i > 0.5 else 0 for i in z]
    else:
        # y and z are one hot encoded
        true_class = np.argmax(y, axis=1)
        predicted_class = np.argmax(z, axis=1)

    return np.sum(true_class == predicted_class) / len(true_class)


def mean_square_error(y: np.ndarray, z: np.ndarray) -> float:
    return MeanSquareError().objective(y, z)


def binary_cross_entropy(y: np.ndarray, z: np.ndarray) -> float:
    return BinaryCrossEntropy().objective(y, z)


def cross_entropy(y: np.ndarray, z: np.ndarray) -> float:
    return CrossEntropy().objective(y, z)
