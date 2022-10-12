import pandas as pd
import math


# Function To Calculate Entropy Of Entire Dataset
def dataset_entropy(dataset):
    p = 0
    n = 0
    target = dataset.iloc[:, -1]
    targets = list(set(target))
    for i in target:
        if i == targets[0]:
            p = p + 1
        else:
            n = n + 1
    if p == 0 or n == 0:
        return 0
    elif p == n:
        return 1
    else:
        cal_entropy = 0 - ((p / (p + n)) * (math.log2(p / (p + n))) + (n / (p + n)) * (math.log2(n / (p + n))))
        return cal_entropy


# Function To Calculate The Entropy Of Attributes
def attribute_entropy(dataset, feature, attribute):
    p = 0
    n = 0
    target = dataset.iloc[:, -1]
    targets = list(set(target))
    for i, j in zip(feature, target):
        if i == attribute and j == targets[0]:
            p = p + 1
        elif i == attribute and j == targets[1]:
            n = n + 1
    if p == 0 or n == 0:
        return 0
    elif p == n:
        return 1
    else:
        cal_entropy = 0 - ((p / (p + n)) * (math.log2(p / (p + n))) + (n / (p + n)) * (math.log2(n / (p + n))))
        return cal_entropy


# Utility Function For Checking Purity And Impurity Of A Child
def counter(target, attribute, i):
    p = 0
    n = 0
    targets = list(set(target))
    for j, k in zip(target, attribute):
        if j == targets[0] and k == i:
            p = p + 1
        elif j == targets[1] and k == i:
            n = n + 1
    return p, n


# Function To Calculate The Information Gain
def information_gain(dataset, feature):
    distinct = list(set(feature))
    info_gain = 0
    for i in distinct:
        info_gain = info_gain + feature.count(i) / len(feature) * attribute_entropy(dataset, feature, i)
    info_gain = dataset_entropy(dataset) - info_gain
    return info_gain


# Function To Generates Children Of Selected Attribute
def generate_children(dataset, attribute_index):
    distinct = list(dataset.iloc[:, attribute_index])
    children = dict()
    for i in distinct:
        children[i] = counter(dataset.iloc[:, -1], dataset.iloc[:, attribute_index], i)
    return children


# Function To Modify The Dataset According To Impure Children
def modify_data_set(dataset, index, feature, impurity):
    sub_data = dataset[dataset[feature] == impurity]
    del (sub_data[sub_data.columns[index]])
    return sub_data


# Function To Return Attribute With The Greatest Information Gain
def greatest_information_gain(dataset):
    maximum = -1
    attribute_index = 0
    size = len(dataset.columns) - 1
    for i in range(0, size):
        feature = list(dataset.iloc[:, i])
        i_g = information_gain(dataset, feature)
        if maximum < i_g:
            maximum = i_g
            attribute_index = i
    return attribute_index


# Function To Construct Decision Tree
def construct_tree(dataset, tree):
    impure_children = []
    attribute_index = greatest_information_gain(dataset)
    children = generate_children(dataset, attribute_index)
    tree[dataset.columns[attribute_index]] = children
    targets = list(set(dataset.iloc[:, -1]))
    for k, v in children.items():
        if v[0] == 0:
            tree[k] = targets[1]
        elif v[1] == 0:
            tree[k] = targets[0]
        elif v[0] != 0 or v[1] != 0:
            impure_children.append(k)
    for i in impure_children:
        sub = modify_data_set(dataset, attribute_index, dataset.columns[attribute_index], i)
        tree = construct_tree(sub, tree)
    return tree


# Main Function
def main():
    df = pd.read_csv("Data.csv")
    tree = dict()
    result = construct_tree(df, tree)
    for key, value in result.items():
        print(key, " => ", value)


# Calling Main Function
if __name__ == "__main__":
    main()