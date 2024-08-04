def remove_duplicates(arr):
  """Removes duplicate elements from an array.

  Args:
    arr: The input array.

  Returns:
    A new array with duplicate elements removed.
  """

  return list(set(arr))

# Example usage
my_array = [1, 2, 2, 3, 4, 4, 5]
unique_array = remove_duplicates(my_array)
print(unique_array)