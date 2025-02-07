def lr_schedule(epoch):
    """Learning Rate Schedule

    Learning rate is scheduled to be reduced after 80, 120, 160, 180 epochs.
    Called automatically every epoch as part of callbacks during training.

    # Arguments
        epoch (int): The number of epochs

    # Returns
        lr (float32): learning rate
    """
    lr = 1e-3
    if epoch > 180:
        lr *= 0.5e-3
    elif epoch > 160:
        lr *= 1e-3
    elif epoch > 120:
        lr *= 1e-2
    elif epoch > 80:
        lr *= 1e-1
    print('Learning rate: ', lr)
    return lr


def get_label(key):
    if key == 0:
        return 'airplane'
    elif key == 1:
        return 'automobile'
    elif key == 2:
        return 'bird'
    elif key == 3:
        return 'cat'
    elif key == 4:
        return 'deer'
    elif key == 5:
        return 'dog'
    elif key == 6:
        return 'frog'
    elif key == 7:
        return 'horse'
    elif key == 8:
        return 'ship'
    elif key == 9:
        return 'truck'
    else:
        return 'Invalid key'
