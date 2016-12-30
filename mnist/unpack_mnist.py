#coding:utf-8

import cPickle, gzip, numpy
from scipy.misc import imsave
import os

f = gzip.open('mnist.pkl.gz', 'rb')
train_set, valid_set, test_set = cPickle.load(f) 
# train_set包含50000条数据，它是一个tuple，
# 元素0是图片像素数据的集合，范围为0~1；元素1是标签数据，数据范围0~9；
# valid_set包含10000条数据
# test_set包含10000条数据
f.close()

# convert both train and test to png as images
# 其中test_set前3000条
x = numpy.concatenate((train_set[0]*255,valid_set[0]*255,test_set[0][:3000,:]*255))
for i in range(20):
  imsave('mnist_batch_'+`i`+'.png', x[3000*i:3000*(i+1),:])
imsave('mnist_batch_'+`20`+'.png', x[60000:,:]) # test set

# dump the labels
# 这里label数组的size=70000
L = 'var labels=' + `list(numpy.concatenate((train_set[1],valid_set[1],test_set[1])))` + ';\n'
open('mnist_labels.js', 'w').write(L)

