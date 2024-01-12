from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import tensorflow as tf


#please just lemme commit
def main():
    print("This function Does nothing")

msg = tf.string_join(["Hello" , "TensorFlow"])
with tf.Session() as sess:
    print(sess.run(msg))

