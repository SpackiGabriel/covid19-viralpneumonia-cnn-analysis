import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import platform
import os

from sklearn.metrics import confusion_matrix, recall_score, f1_score


def clear_console():
    """
    Clears the console/terminal.

    Returns:
    None
    """
    os.system('cls' if platform.system() == 'Windows' else 'clear')


def get_true_and_predicted_classes(model, dataset):
    """
    Returns the true classes and predicted classes for a given model and dataset.

    Parameters:
    model (tf.keras.Model): The trained model.
    dataset (tf.data.Dataset): The dataset containing images and labels.

    Returns:
    true_classes (np.ndarray): An array of true classes.
    predicted_classes (np.ndarray): An array of predicted classes.
    """
    true_classes = []
    predicted_classes = []

    for images, labels in dataset:
        true_classes.extend(np.argmax(labels.numpy(), axis=1))
        predicted_classes.extend(np.argmax(model.predict(images), axis=1))

    return np.array(true_classes), np.array(predicted_classes)

def get_confusion_matrix(true_classes, predicted_classes):
    """
    Calculate the confusion matrix for a classification task.

    Args:
        true_classes (array-like): The true class labels.
        predicted_classes (array-like): The predicted class labels.

    Returns:
        array-like: The confusion matrix.
    """
    return confusion_matrix(true_classes, predicted_classes)

def get_recall(true_classes, predicted_classes):
    """
    Calculate the recall score for a classification model.

    Parameters:
    true_classes (array-like): The true class labels.
    predicted_classes (array-like): The predicted class labels.

    Returns:
    float: The recall score.

    """
    return recall_score(true_classes, predicted_classes, average=None)


def get_f1_score(true_classes, predicted_classes):
    """
    Calculate the F1 score for a given set of true classes and predicted classes.

    Parameters:
    true_classes (array-like): The true classes.
    predicted_classes (array-like): The predicted classes.

    Returns:
    float: The F1 score.

    """
    return f1_score(true_classes, predicted_classes, average='macro')


def get_accuracy_and_loss(model, dataset):
    """
    Returns the accuracy and loss of a given model on a dataset.

    Args:
        model (object): The trained model to be evaluated.
        dataset (object): The dataset to evaluate the model on.

    Returns:
        accuracy (float): The accuracy of the model on the dataset.
        loss (float): The loss of the model on the dataset.
    """
    loss, accuracy = model.evaluate(dataset, verbose=0)
    return accuracy, loss


def plot_confusion_matrix(conf_matrix, dataset):
    """
    Plots the confusion matrix using a heatmap.

    Args:
        conf_matrix (numpy.ndarray): The confusion matrix.
        dataset (Dataset): The dataset object containing class names.

    Returns:
        None
    """
    plt.figure(figsize=(8, 6))
    sns.set(font_scale=1.2)
    sns.heatmap(
        conf_matrix,
        annot=True,
        cbar=False,
        fmt='d',
        cmap="Blues",
        xticklabels=dataset.class_names,
        yticklabels=dataset.class_names
    )

    plt.title('Confusion Matrix')
    plt.show()


def plot_recall(recall, dataset):
    """
    Plots the recall score as a bar chart.

    Args:
        recall (array-like): The recall score values.
        dataset (Dataset): The dataset object containing class names.

    Returns:
        None
    """
    plt.figure(figsize=(8, 6))
    sns.barplot(x=dataset.class_names, y=recall)
    plt.title('Recall Score')
    plt.show()
    
    for index, value in enumerate(recall):
        print(f"{dataset.class_names[index]}: {value:.4f}")

def plot_f1_score(f1_score):
    """
    Plots the F1 score as a bar chart.

    Args:
        f1_score (float): The F1 score.

    Returns:
        None
    """
    plt.figure(figsize=(8, 6))
    sns.barplot(x=['F1 Score'], y=[f1_score])
    plt.title('F1 Score')
    plt.show()

    print(f"F1-Score: {f1_score:.4f}")


def plot_accuracy_and_loss(accuracy, loss):
    """
    Plots the final accuracy and loss of a model on a bar chart.

    Args:
        accuracy (float): The accuracy of the model on the dataset.
        loss (float): The loss of the model on the dataset.

    Returns:
        None
    """
    plt.figure(figsize=(8, 6))
    sns.barplot(x=['Accuracy', 'Loss'], y=[accuracy, loss])
    plt.title('Accuracy and Loss')
    plt.show()

    print(f"Accuracy: {accuracy:.4f} | Loss: {loss:.4f}")


def evaluate_model(model, dataset):
    """
    Evaluates the performance of a given model on a dataset.

    Args:
        model (object): The trained model to be evaluated.
        dataset (object): The dataset to evaluate the model on.

    Returns:
        None
    """
    true_classes, predicted_classes = get_true_and_predicted_classes(model, dataset)
    
    clear_console()

    conf_matrix = get_confusion_matrix(true_classes, predicted_classes)
    recall = get_recall(true_classes, predicted_classes)
    f1 = get_f1_score(true_classes, predicted_classes)
    accuracy, loss = get_accuracy_and_loss(model, dataset)

    plot_confusion_matrix(conf_matrix, dataset)
    plot_recall(recall, dataset)
    plot_f1_score(f1)
    plot_accuracy_and_loss(accuracy, loss)