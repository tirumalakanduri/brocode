# Frequency Counter (Dict + Loop + Condition)
# Write a function count_frequency(lst) that takes a list of elements and returns a dictionary where keys are elements and values are their frequencies.
# Example: ['a', 'b', 'a', 'c', 'b'] → {'a': 2, 'b': 2, 'c': 1}


def count_frequency(list):
    freq = {}
    for item in list:     # we are looping the given list
        if item in freq:   # checking weather the item in the list is present in the frequency
            freq[item] += 1  # if it is already present in the freq then it is incremented by 1(added by 1)
        else:
            freq[item] = 1   # if it is not present then the item will be added into the list
    return freq

print(count_frequency(['a', 'b', 'a', 'c', 'b']))