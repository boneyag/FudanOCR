config = {
    'exp_name': '【0605】Test',
    'epoch': 500,
    'lr': 1.0,
    'mode': 'strokelet',  # character / strokelet
    'batch': 32,
    'val_frequency': 1,
    'test_only': False,
    'resume': '',
    'train_dataset': './data/mydata/train_1000',
    'test_dataset': './data/mydata/test_1000',
    'weight_decay': False,
    'schedule_frequency': 1000000,
    'image_size': 32,
    'update_gallery_feature': 100,
    'distance_coeff': 1,
    'encoder': 'resnet',  # resnet / densenet / vgg
    'decoder': 'transformer',  # gru / transformer / ctc
    'alphabet': 3755,
    'stn': False,
    'constrain': False,
}