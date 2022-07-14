import os
from http.cookiejar import _str2time

os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

import tensorflow as tf

node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0, tf.float32)

@tf.function
def forward():
        return node1 + node2
    
out_a = forward()
print(out_a)

#
#intel 1
#intel 2
#intel 3
#intel 4
#intel 5

#main
#main
#main
#main


##########################################

hello = tf.constant("hello tensorflow!!")

str1 = tf.constant(3.0)
str2 = tf.constant(4.1,  tf.float32)

tf.print(str1 , str2)
tf.print(str1 + str2)