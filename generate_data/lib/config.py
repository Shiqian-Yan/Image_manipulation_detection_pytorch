
import os.path as osp

import argparse

parser = argparse.ArgumentParser(description='YsqNet')
parser.add_argument('--rootDir', default=osp.abspath(osp.join(osp.dirname(__file__))), type=str,
                    help='choose the dir of dataset')
parser.add_argument('--dataDir', default='/home/stu4/user/ysq/voc2007',
                    type=str, help='choose the dataDir')

parser.add_argument('--saveDir', default='/home/stu4/user/ysq/DIY_2007',
                    type=str, help='choose the saveDir')

parser.add_argument('--imdb', default='voc_2007_train',
                    type=str, help='train or test')


parser.add_argument('--number', default=5011,
                    type=int, help='the number of images')

args = parser.parse_args()
