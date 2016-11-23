# -*- coding: UTF-8 -*-
from svm import *
from svmutil import *

y, x = svm_read_problem('F:/python/traindata.txt')
m = svm_train(y, x, '-s 0 -t 2 -b 1')
p_labels, p_acc, p_vals = svm_predict(y, x, m, '-b 1')
print("plabels")
print(p_labels)
print("p_acc")
print(p_acc)
print("pvals")
print(pvals)
print("end")