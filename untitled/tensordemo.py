#!/usr/bin/env python
# -*- coding = utf-8 -*-

"""
 @ Creat Time: 2017/12/15
 @ Auther: songpo.zhang
 @ Target:
"""
import tensorflow as tf
import numpy as np

x_data = np.random.rand(100).astype(np.float32)  # tensorflow 中大部分数据类型是float32
y_data = x_data*0.1 + 0.3

Weights = tf.Variable(tf.random_uniform([1],-1.0,1.0)) # [1] W 是一维 范围-1.0 1.0
biases = tf.Variable(tf.zeros([1]))

y = Weights * x_data + biases

loss = tf.reduce_mean(tf.square(y - y_data))

optimizer = tf.train.GradientDescentOptimizer(0.5)  # 学习效率为0.5
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step,sess.run(Weights),sess.run(biases))