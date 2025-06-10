# Remove Duplicates (List + Set + Loop)
# Write a function remove_duplicates(lst) that takes a list and returns a new list with duplicates removed, preserving original order.
# Use a set for lookup but return a list. Don’t use list(set(lst)) — do it manually.



def remove_duplicates(list):
    seen = set()
    result = []
    for item in list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

print(remove_duplicates([1,1,12,12,13,2,3,2,3,4,5,6,5,43]))