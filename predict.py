import tensorflow as tf

from ReadData import take_test_set, LetterData

def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)


def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)


def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')


def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],
                          strides=[1, 2, 2, 1], padding='SAME')


def arry2letter(y):
    n = len(y)
    for i in range(n):
        if y [i] != 0:
            return chr(ord('a')+i)

letterdata = LetterData()

x = tf.placeholder(tf.float32, [None, 128])
w = tf.Variable(tf.zeros([128, 26]))
b = tf.Variable(tf.zeros(26))
y_ = tf.placeholder("float", [None, 26])

W_conv1 = weight_variable([8, 4, 1, 32])
b_conv1 = bias_variable([32])
x_image = tf.reshape(x, [-1, 16, 8, 1])
h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
h_pool1 = max_pool_2x2(h_conv1)


W_conv2 = weight_variable([8, 4, 32, 64])
b_conv2 = bias_variable([64])
h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
h_pool2 = max_pool_2x2(h_conv2)

W_fc1 = weight_variable([4 * 2 * 64, 256])
b_fc1 = bias_variable([256])
h_pool2_flat = tf.reshape(h_pool2, [-1, 4 * 2 * 64])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

W_fc2 = weight_variable([256, 26])
b_fc2 = bias_variable([26])
y_conv = tf.nn.softmax(tf.matmul(h_fc1, W_fc2) + b_fc2)

saver = tf.train.Saver()

with tf.Session() as sess:
    saver.restore(sess, './HandWritingModel/Model')
    graph = tf.get_default_graph()
    result = sess.run(y_conv, feed_dict={x: LetterData.data[0:20]})
    print('Model restored.')
    for letter in result:
        print(arry2letter(letter))