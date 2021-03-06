# --------------------------------------------------------
# Fast R-CNN
# Copyright (c) 2015 Microsoft
# Licensed under The MIT License [see LICENSE for details]
# Written by Ross Girshick
# --------------------------------------------------------

"""Factory method for easily getting imdbs by name."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# print('1\n')
__sets = {}
from .pascal_voc import pascal_voc
# from lib.datasets.coco import coco
#from lib.datasets.DIY_pascal_voc import DIY_pascal_voc

import numpy as np

# Set up voc_<year>_<split>
for year in ['2007', '2012']:
    for split in ['train', 'val', 'trainval', 'test']:
        name = 'voc_{}_{}'.format(year, split)
        __sets[name] = (lambda split=split, year=year: pascal_voc(split, year))
# print('2')

# # Set up coco_2014_<split>
# for year in ['2014']:
#     for split in ['train', 'val', 'minival', 'valminusminival', 'trainval']:
#         name = 'coco_{}_{}'.format(year, split)
#         __sets[name] = (lambda split=split, year=year: coco(split, year))
#
# # Set up coco_2015_<split>
# for year in ['2015']:
#     for split in ['test', 'test-dev']:
#         name = 'coco_{}_{}'.format(year, split)
#         __sets[name] = (lambda split=split, year=year: coco(split, year))

for year in ['2018']:
    for split in ['trainval']:
        name = 'DIY_dataset'
        __sets[name] = (lambda split=split, year=year: DIY_pascal_voc(split, year))

# print('3\n')

def get_imdb(name):
    """Get an imdb (image database) by name."""
    print('sets', __sets)
    if name not in __sets:
        raise KeyError('Unknown dataset: {}'.format(name))
    return __sets[name]()


def list_imdbs():
    """List all registered imdbs."""
    return list(__sets.keys())