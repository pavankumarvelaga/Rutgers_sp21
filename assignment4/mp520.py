import inspect
import sys
import numpy as np
import math
p_of_y = []
from collections import defaultdict
conditional_prob_table = defaultdict(list)


"""
Raise a "not defined" exception as a reminder 
"""


def _raise_not_defined():
    print("Method not implemented: %s" % inspect.stack()[1][3])
    sys.exit(1)


"""
Extract 'basic' features, i.e., whether a pixel is background or
forground (part of the digit) 
"""


def extract_basic_features(digit_data, width, height):
    features = []
    # Your code starts here
    # You should remove _raise_not_defined() after you complete your code
    for i in range(height):
        for j in range(width):
            # features.append(1 if digit_data[i][j] > 0 else 0)
            features.append(digit_data[i][j])
    # Your code ends here
    # _raise_not_defined()
    # [1]
    return features


"""
Extract advanced features that you will come up with 
"""


def extract_advanced_features(digit_data, width, height):
    features = []
    # Your code starts here
    # You should remove _raise_not_defined() after you complete your code
    # Your code ends here
    _raise_not_defined()
    return features


"""
Extract the final features that you would like to use
"""


def extract_final_features(digit_data, width, height):
    features = []
    # Your code starts here
    # You should remove _raise_not_defined() after you complete your code
    # Your code ends here
    _raise_not_defined()
    return features


"""
Compupte the parameters including the prior and and all the P(x_i|y). Note
that the features to be used must be computed using the passed in method
feature_extractor, which takes in a single digit data along with the width
and height of the image. For example, the method extract_basic_features
defined above is a function than be passed in as a feature_extractor
implementation.

The percentage parameter controls what percentage of the example data
should be used for training. 
"""


def compute_statistics(data, label, width, height, feature_extractor, percentage=100.0):
    # Your code starts here
    # You should remove _raise_not_defined() after you complete your code
    num_records = math.ceil(percentage/100.0 * len(data)) 
    data = data[:num_records]
    label = label[:num_records]
    features = []
    global p_of_y
    p_of_y = []
    k = 1e-20
    global conditional_prob_table
    conditional_prob_table = defaultdict(list)
    for i in data:
        features.append(feature_extractor(i, width, height ))
    features = np.array(features)
    # print(features[0])
    
    for i in range(10):
        p_of_y.append(len([m for m in label if m == i])/len(label))
        p_list_temp = []
        p_dict_temp = defaultdict(list)
        idxs = [idx for idx, e in enumerate(label) if e == i]
        for f in np.unique(features[0]):
            for j in range(len(features[0])):
                p_list_temp.append((sum(features[idxs][:,j] == f)+k)/(len(idxs)+k))
            p_dict_temp[f] =  p_list_temp
            p_list_temp = []
        conditional_prob_table[i] = p_dict_temp
    
    # Your code ends here
    # _raise_not_defined()


"""
For the given features for a single digit image, compute the class 
"""


def compute_class(features):
    predicted = -1
    # Your code starts here
    log_y_given_p = []
    # print(p_of_y)
    for i in range(10):
        tmp = 0.0
        for j in range(len(features)):
            tmp += math.log(conditional_prob_table[i][features[j]][j])
        log_y_given_p.append(math.log(p_of_y[i])+tmp)   
    predicted = np.argmax(log_y_given_p)
    # print(log_y_given_p,predicted)

    # You should remove _raise_not_ßdefined() after you complete your code
    # # Your code ends here
    # _raise_not_defined()
    return predicted


"""
Compute joint probaility for all the classes and make predictions for a list
of data
"""


def classify(data, width, height, feature_extractor):

    predicted = []
    for i in data:
        features = feature_extractor(i,width,height)
        predicted.append(compute_class(features))



    # Your code starts here
    # You should remove _raise_not_defined() after you complete your code
    # Your code ends here
    # _raise_not_defined()
    # print(predicted)

    return predicted
