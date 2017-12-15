#!/usr/bin/env python
# -*- coding = utf-8 -*-

"""
 @ Creat Time: 2017/12/15
 @ Auther: songpo.zhang
 @ Target:
"""
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# x_data = np.random.rand(100).astype(np.float32)  # tensorflow 中大部分数据类型是float32
# y_data = x_data*0.1 + 0.3
#
# Weights = tf.Variable(tf.random_uniform([1],-1.0,1.0)) # [1] W 是一维 范围-1.0 1.0
# biases = tf.Variable(tf.zeros([1]))
#
# y = Weights * x_data + biases
#
# loss = tf.reduce_mean(tf.square(y - y_data))
#
# optimizer = tf.train.GradientDescentOptimizer(0.5)  # 学习效率为0.5
# train = optimizer.minimize(loss)
#
# init = tf.global_variables_initializer()
#
# sess = tf.Session()
# sess.run(init)
#
# for step in range(201):
#     sess.run(train)
#     if step % 20 == 0:
#         print(step,sess.run(Weights),sess.run(biases))



################ Variable
# state = tf.Variable(0,name='counter')
# # print(state.name) # print结果是 counter:0 这个0代表的是这是第一个变量
# one = tf.constant(1) # 常量
#
# new_value = tf.add(state, one)
# updata = tf.assign(state, new_value)
#
# init = tf.global_variables_initializer()
#
# with tf.Session() as sess:
#     sess.run(init)
#     for _ in range(3):
#         sess.run(updata)
#         print(sess.run(state))  # 不能是print(state)

#################### Placeholder
# input1 = tf.placeholder(tf.float32)
# input2 = tf.placeholder(tf.float32)
#
# output = tf.multiply(input1,input2)
#
# with tf.Session() as sess:
#     print(sess.run(output,feed_dict={input1:[7.],input2:[2.]}))


###################### Add Layer
# def add_layer(inputs, in_size, out_size, activation_function=None):
#     Weights = tf.Variable(tf.random_normal([in_size, out_size]))
#     biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
#     Wx_plus_b = tf.matmul(inputs, Weights) + biases
#     if activation_function is None:
#         outputs = Wx_plus_b
#     else:
#         outputs = activation_function(Wx_plus_b)
#     return outputs

# x_data = np.linspace(-1,1,300)[:,np.newaxis]
# noise = np.random.normal(0, 0.05, x_data.shape)
# y_data = np.square(x_data) - 0.5 + noise

# xs = tf.placeholder(dtype = tf.float32,shape = [None,1])
# ys = tf.placeholder(dtype = tf.float32,shape = [None,1])

# # hidden layer
# l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)
# # output layer
# prediction = add_layer(l1, 10, 1, activation_function=None)

# loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1]))

# train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

# init = tf.global_variables_initializer()
# sess = tf.Session()
# sess.run(init)

# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)
# ax.scatter(x_data, y_data)
# plt.ion()
# plt.show()

# for i in range(1000):
#     sess.run(train_step, feed_dict={xs:x_data, ys:y_data})
#     if i % 50 == 0:
#         #print(sess.run(loss, feed_dict={xs:x_data, ys:y_data}))
#         try:
#             ax.lines.remove(lines[0])
#         except Exception:
#             pass
#         prediction_value = sess.run(prediction, feed_dict={xs:x_data})
#         lines = ax.plot(x_data, prediction_value, 'r-', lw=5)
#         plt.pause(0.1)


#################### Tensorboard可视化
def add_layer(inputs, in_size, out_size, n_layer, activation_function=None):
    layer_name = 'layer%s'%n_layer
    with tf.name_scope(layer_name):
        with tf.name_scope('weights'):
            Weights = tf.Variable(tf.random_normal([in_size, out_size]), name='W')
            tf.summary.histogram(layer_name+'/weights',Weights)
        with tf.name_scope('biases'):
            biases = tf.Variable(tf.zeros([1, out_size]) + 0.1,name='b')
            tf.summary.histogram(layer_name+'/biases',biases)
        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b = tf.matmul(inputs, Weights) + biases
        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b)
        tf.summary.histogram(layer_name+'/outputs',outputs)
        return outputs

x_data = np.linspace(-1,1,300)[:,np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape)
y_data = np.square(x_data) - 0.5 + noise

# define placeholder for inputs to network
with tf.name_scope('inputs'):
    xs = tf.placeholder(dtype = tf.float32,shape = [None,1], name='x_input')
    ys = tf.placeholder(dtype = tf.float32,shape = [None,1], name='y_input')

# hidden layer
l1 = add_layer(xs, 1, 10, n_layer=1, activation_function=tf.nn.relu)
# output layer
prediction = add_layer(l1, 10, 1, n_layer=2, activation_function=None)

with tf.name_scope('loss'):
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1]))
    tf.summary.scalar('loss',loss)

with tf.name_scope('train'):
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)


init = tf.global_variables_initializer()
sess = tf.Session()
merged = tf.summary.merge_all()
writer = tf.summary.FileWriter("logs/",sess.graph)
sess.run(init)

for i in range(1000):
    sess.run(train_step, feed_dict={xs:x_data, ys:y_data})
    if i % 50 == 0:
        re = sess.run(merged, feed_dict={xs:x_data, ys:y_data})
        writer.add_summary(re, i)