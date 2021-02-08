#!/usr/bin/python

import argparse
import os
from random import shuffle

parser = argparse.ArgumentParser()

parser.add_argument('--train_folder', default='/home/jdlevy/Documents/UCSD/Senior/Quarter 2/DSC 180B/Image_Captioning_Explainer/data/raw/coco_data/train2017', type=str,
                    help='The folder path')
parser.add_argument('--val_folder', default='/home/jdlevy/Documents/UCSD/Senior/Quarter 2/DSC 180B/Image_Captioning_Explainer/data/raw/coco_data/val2017', type=str,
                    help='The folder path')
parser.add_argument('--train_filename', default='./data_flist/coco2017_train_shuffled.flist', type=str,
                    help='The output filename.')
parser.add_argument('--validation_filename', default='./data_flist/coco2017_validation_shuffled.flist', type=str,
                    help='The output filename.')
parser.add_argument('--is_shuffled', default='1', type=int,
                    help='Needed to shuffle')

if __name__ == "__main__":

    args = parser.parse_args()

    # get the list of directories
    # dirs = os.listdir(args.folder_path)
    # dirs_name_list = []

    # make 2 lists to save file paths
    # training_file_names = []
    # validation_file_names = []
    train_files = os.listdir(args.train_folder)
    training_file_names = [args.train_folder+'/'+fname for fname in train_files]

    val_files = os.listdir(args.val_folder)
    validation_file_names = [args.val_folder+'/'+fname for fname in val_files]

    # print all directory names

    # print all file paths
    for i in training_file_names:
        print(i)
    for i in validation_file_names:
        print(i)

    # This would print all the files and directories

    # shuffle file names if set
    if args.is_shuffled == 1:
        shuffle(training_file_names)
        shuffle(validation_file_names)

    # make output file if not existed
    if not os.path.exists(args.train_filename):
        os.mknod(args.train_filename)

    if not os.path.exists(args.validation_filename):
        os.mknod(args.validation_filename)

    # write to file
    fo = open(args.train_filename, "w")
    fo.write("\n".join(training_file_names))
    fo.close()

    fo = open(args.validation_filename, "w")
    fo.write("\n".join(validation_file_names))
    fo.close()

    # print process
    print("Written file is: ", args.train_filename, ", is_shuffle: ", args.is_shuffled)
