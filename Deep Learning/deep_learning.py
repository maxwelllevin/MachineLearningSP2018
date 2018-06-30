""""
CS 369: AI & Machine Learning
Lab #3: Deep Learning
April 26, 2018

In this project we build a powerful deep learning system for image recognition for tiny images in the CIFAR-10 data set.
https://www.cs.toronto.edu/~kriz/cifar.html

Max, Will, Peter, Ben
"""
import numpy as np
import tensorflow as tf
import pickle
import itertools
import datetime

# data_path = "/Users/peter/Dropbox/S18/aiml/deep learning/Data/cifar-10-batches-py/" #peter's laptop
# data_path = "/home/users/peter/files/cifar-10-batches-py/" #blt cluster
data_path = "Data/cifar-10-batches-py/"

learning_rate = 0.002

num_inputs = 32 * 32 * 3
num_classes = 10

epochs = 16
batch_size = 1000

# gather data for plots
training_accuracy_log = []
validation_accuracy_log = []


# import data
def unpickle(file):
	with open(file, 'rb') as fo:
		dict = pickle.load(fo, encoding='bytes')
		return dict


# prepare data
train = [unpickle(data_path + 'data_batch_{}'.format(i)) for i in [1, 2, 3, 4]]
training_images = np.concatenate([t[b'data'] for t in train], axis=0)
training_labels = np.array(list(itertools.chain(*[t[b'labels'] for t in train])))
valid = unpickle(data_path + 'data_batch_5')
validation_images = valid[b'data']
validation_labels = np.array(valid[b'labels'])

# test data
test = unpickle(data_path + "test_batch")
testing_images = np.array(test[b'data'])
testing_labels = np.array(test[b'labels'])

images = tf.placeholder(tf.float32, shape=(None, num_inputs), name="images")
labels = tf.placeholder(tf.int64, shape=(None), name="labels")

# layers
with tf.name_scope("dnn"):
	shaped = tf.transpose(tf.reshape(images, [-1, 3, 32, 32]), (0, 2, 3, 1))

	layer_1_filters = 48
	conv1 = tf.layers.conv2d(shaped, layer_1_filters, kernel_size=3, strides=1, padding='same', activation=tf.nn.elu)

	pool1 = tf.layers.max_pooling2d(conv1, pool_size=2, strides=2, padding='valid')

	layer_2_filters = 96
	conv2 = tf.layers.conv2d(pool1, layer_2_filters, kernel_size=3, strides=1, padding='same', activation=tf.nn.elu)

	pool2 = tf.layers.max_pooling2d(conv2, pool_size=2, strides=2, padding='valid')

	layer_3_filters = 192
	conv3 = tf.layers.conv2d(pool2, layer_3_filters, kernel_size=3, strides=1, padding='same', activation=tf.nn.elu)

	pool3 = tf.layers.max_pooling2d(conv3, pool_size=2, strides=2, padding='valid')

	flat = tf.reshape(pool3, [-1, 4 * 4 * layer_3_filters])
	logits = tf.layers.dense(flat, num_classes, name="outputs")

# loss function
with tf.name_scope("loss_function"):
	cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=labels, logits=logits)
	loss = tf.reduce_mean(cross_entropy, name="loss_function")

# optimizer
with tf.name_scope("train"):
	optimizer = tf.train.AdamOptimizer(learning_rate)
	training_optimizer = optimizer.minimize(loss)

# evaluate accuracy
with tf.name_scope("eval"):
	correct = tf.nn.in_top_k(logits, labels, 1)
	accuracy = tf.reduce_mean(tf.cast(correct, tf.float32))

# initialize our tensorflow network
network = tf.global_variables_initializer()

# Create a Saver to be able to save our network
saver = tf.train.Saver()

# run the network
with tf.Session() as sess:
	network.run()
	print("Training\tTraining\tValidation\tValidation")
	print("  Loss\t\tAccuracy\t   Loss\t\t Accuracy")
	for epoch in range(epochs):
		for batch in range(0, len(training_images), batch_size):
			batch_indices = range(batch, batch + batch_size)
			image_batch = training_images[batch_indices, :]
			label_batch = training_labels[batch_indices]
			sess.run(training_optimizer, feed_dict={images: image_batch, labels: label_batch})

		training_loss = loss.eval(feed_dict={images: training_images, labels: training_labels})
		training_accuracy = accuracy.eval(feed_dict={images: training_images, labels: training_labels})
		validation_loss = loss.eval(feed_dict={images: validation_images, labels: validation_labels})
		validation_accuracy = accuracy.eval(feed_dict={images: validation_images, labels: validation_labels})

		# add accuracy to lists for plotting
		training_accuracy_log.append(training_accuracy)
		validation_accuracy_log.append(validation_accuracy)

		# print loss and accuracy for training and validation data
		print("{0:.3f}".format(training_loss), "\t\t{0:.3f}".format(training_accuracy),
		      "\t\t{0:.3f}".format(validation_loss), "\t\t{0:.3f}".format(validation_accuracy))
		save_path = saver.save(sess, "./epoch", epoch)
	# print("Model saved in path: %s" % save_path)

	# print testing accuracy
	testing_accuracy = accuracy.eval(feed_dict={images: testing_images, labels: testing_labels})
	print("The testing accuracy is: ", testing_accuracy)

# export data for plotting
time = datetime.datetime.now().strftime("%d-%m-%Y %H-%M-%S")
text_file = open("epic_plot" + ".txt", "w")
out = ""
for i in range(len(training_accuracy_log)):
	out += str(training_accuracy_log[i]) + " " + str(validation_accuracy_log[i]) + "\n"
text_file.write(out)
text_file.close()
