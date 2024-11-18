# TODO: Implement the following functions based on the descriptions.

def reverse_list(lst):
    lst = lst[::-1]
    return lst
    """
    Reverses the given list.
    :param lst: List of integers.
    :return: A list with elements in reverse order.
    """
    
#print(reverse_list([1,2,3,4,5,6]))
             

def count_occurrences(lst, element):
    
    count_list = lst.count(element)
    return count_list
    """
    Counts how many times the given element appears in the list.
    :param lst: List of elements.
    :param element: Element to count.
    :return: Integer count of occurrences.
    """
    

#print(count_occurrences([1,2,3,4,5,6,6,6], 6))

def get_keys_with_value(dct, value):
    dct = {'a': 1, 'b': 2, 'c': 1}
    dct = dct.keys()
    
    
    return list(dct)
    """
    Returns a list of keys that have the given value in the dictionary.
    :param dct: Dictionary to search.
    :param value: Value to find.
    :return: List of keys.
    """

#print(get_keys_with_value({'a': 1, 'b': 2, 'c': 1},1))




def merge_sorted_lists(lst1, lst2):
    lst3 = lst1 + lst2
    lst3 = sorted(lst3)
    return lst3
    """
    Merges two sorted lists into one sorted list.
    :param lst1: First sorted list.
    :param lst2: Second sorted list.
    :return: Merged sorted list.
    """


#print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))



def find_second_largest(numbers):
    if len(numbers) == 1:
        return None
    elif len(set(numbers)) ==1:
        return None
    else:
        numbers = sorted(numbers)
        return numbers[-2]


    """
    Finds the second largest number in a list.
    :param numbers: List of integers.
    :return: The second largest integer.
    """

#print(find_second_largest([1,2,3,4,5]))

def is_anagram(str1, str2):

    #if len(str1) == len(str2):
    
    """
    Checks if two strings are anagrams.
    
    An anagram is a word or phrase formed by rearranging the letters of another,
    using all the original letters exactly once. For example, "listen" and "silent"
    are anagrams because they use the same letters in a different order.
    
    :param str1: First string.
    :param str2: Second string.
    :return: True if the strings are anagrams, False otherwise.
    """
#print(is_anagram("listen", "silent"))


def flatten_list(nested_list):
    nested_list = tuple(nested_list)
    return nested_list
    """
    Flattens a nested list into a single list.
    :param nested_list: List of lists.
    :return: A flat list with all elements.
    """
print(flatten_list([[1, 2], [3, 4]]))


def remove_duplicates(lst):
    lst = set(lst)
    no_duplicates_lst = list(lst)
    return no_duplicates_lst

    """
    Removes duplicates from the list while maintaining order.
    :param lst: List of elements.
    :return: List without duplicates.
    """
#print(remove_duplicates([1, 2, 2, 3, 3]))

def find_common_elements(lst1, lst2):
    lst1 = set(lst1)
    lst2 = set(lst2)
    lst3 = lst1.intersection(lst2)
    return list(lst3)

    
    """
    Finds common elements between two lists.
    :param lst1: First list.
    :param lst2: Second list.
    :return: List of common elements.
    """
#print(find_common_elements([1, 2, 3], [3, 4, 5]))