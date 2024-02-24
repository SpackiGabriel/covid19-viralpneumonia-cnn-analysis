import matplotlib.pyplot as plt
import seaborn as sns

def plot_history(history):
    """
    Plots the training and validation loss, as well as the training and validation accuracy, over epochs.

    Parameters:
    - history: A Keras History object containing the training history.

    Returns:
    None
    """
    sns.set(style='whitegrid')

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)

    sns.lineplot(
        x = range(1, len(history.history['loss']) + 1),
        y = history.history['loss'],
        label = 'Training',
        color = 'skyblue'
    )

    sns.lineplot(
        x = range(1, len(history.history['val_loss']) + 1),
        y=history.history['val_loss'],
        label='Validation',
        color='orange'
    )

    plt.xlabel('Epoch')
    plt.ylabel('Loss')

    plt.title('Loss')
    plt.legend()


    plt.subplot(1, 2, 2)

    sns.lineplot(
        x = range(1, len(history.history['categorical_accuracy']) + 1),
        y = history.history['categorical_accuracy'],
        label='Training',
        color='skyblue'
    )

    sns.lineplot(
        x = range(1, len(history.history['val_categorical_accuracy']) + 1),
        y = history.history['val_categorical_accuracy'],
        label = 'Validation',
        color = 'orange'
    )

    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')

    plt.title('Accuracy')
    plt.legend()

    plt.tight_layout()
    plt.show()