# Teesside University Student Future 2020 Machine Learning Workshop #

Author: Teng Fu, Jing Tang, Annalisa Occhipinti

## AIM ##

This repository consists the material used in Teesside University Student Future 2020 Machine Learning Workshop.

It aims to help students to understand:

- What is Machine Learning, AI and Deep Learning.

- How to implement it in real world.

## Workshop Links ##

The [Colab Notebook](https://colab.research.google.com/drive/15HHk9syF_4o8M5_exsAAc1p-3jEQE_a5) for the hands-on workshop consists the following content:

- ETL process for text data and building pipeline.

- Transfer Learning with BERT.

- Train and Evaluate text classifier.

- Server the trained model as REST API.

User must have a Google Account for executing this Notebook. User can click the "Open in Playground" link at top left corner of the web page, or "Copy to Driver" that saves this notebook to the private Google Driver and run it.

## Resource ##

- __raw_test_dataset.csv__ : This artifical dataset consists two columns of data, first as the commenter's ID along with its comment about movie. Comments are from [Large Movie Review Dataset](http://ai.stanford.edu/~amaas/data/sentiment/) dataset.

- __example__ : This directory includes following content in case unexpected error happens during Google Colab workshop: 

    - Generated BERT-Encoded numpy array for training and testing dataset.
    - Trained Keras MLP classifier.
    - [hug](https://www.hug.rest/) web server Python script for REST access for sentiment classifier.

## About Student Future Events ##

Student Futures is a school wide yearly event in Teesside University. Each department of the school is running its own version. Dr Myriam Mallet is responsible for organising the event for the CSIS (Computer Science and Information Systems) department in 2020. This year's plan is to offer workshops led by industry to students. There will be several workshops running in parallel i.e. one for CS students, one for CyberSecurity students and one for Web and IT students.

## Reading List ##

- [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)

- [A Comprehensive Guide to Convolutional Neural Networks — the ELI5 way](https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53)

- [Autoencoders](http://ufldl.stanford.edu/tutorial/unsupervised/Autoencoders/)

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)

- [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805)

- [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/abs/1910.10683)

- [ALBERT: A Lite BERT for Self-supervised Learning of Language Representations](https://arxiv.org/abs/1909.11942)

