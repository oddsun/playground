
def bubble_sort(array):
    """
    Sorts the given array using the bubble sort algorithm.

    Bubble sort repeatedly compares adjacent elements and swaps them if they are in the wrong order.
    This process is repeated for each element in the array until the entire array is sorted.

    Args:
        array (list): The unsorted array.

    Returns:
        list: The sorted array.
    """
    for i in range(len(array)):
        for j in range(len(array) - 1, i, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
    return array

def quick_sort(array):
    """
    Sorts the given array using the Quick Sort algorithm.

    Quick Sort is a divide-and-conquer algorithm that works by selecting a pivot element
    from the array and partitioning the other elements into two sub-arrays, according to
    whether they are less than or greater than the pivot. The sub-arrays are then sorted
    recursively. This process is repeated until the entire array is sorted.

    Args:
        array (list): The array to be sorted.

    Returns:
        list: The sorted array.

    """
    if len(array) < 2:
        return array
    pivot = array[0]
    left = [i for i in array[1:] if i <= pivot]
    right = [i for i in array[1:] if i > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

def merge_sort(array):
    """
    Sorts an array using the merge sort algorithm.

    Merge sort is a divide-and-conquer algorithm that works by dividing the input array into two halves, 
    sorting each half recursively, and then merging the sorted halves to produce a sorted array. 
    It has a time complexity of O(n log n), making it an efficient sorting algorithm for large datasets.

    Args:
        array (list): The array to be sorted.

    Returns:
        list: The sorted array.
    """
    if len(array) < 2:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)

def merge(left, right):
    """
    Merge two sorted lists into a single sorted list.

    Args:
        left (list): The first sorted list.
        right (list): The second sorted list.

    Returns:
        list: The merged sorted list.

    Algorithm:
        The merge function takes two sorted lists as input and merges them into a single sorted list.
        It compares the first elements of both lists and appends the smaller element to the result list.
        This process continues until one of the lists becomes empty.
        Then, it appends the remaining elements of the non-empty list to the result list.
        Finally, it returns the merged sorted list.
    """
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0)) # pop(0) is O(n)
        else:
            result.append(right.pop(0))
    if left:
        result.extend(left)
    if right:
        result.extend(right)
    return result

def heap_sort(array):
    """
    Sorts an array using the Heap Sort algorithm.

    The Heap Sort algorithm is an efficient comparison-based sorting algorithm
    that uses a binary heap data structure to sort elements in ascending order.

    Args:
        array (list): The unsorted array to be sorted.

    Returns:
        list: The sorted array in ascending order.

    Complexity:
        - Time Complexity: O(nlogn)
        - Space Complexity: O(1)
    """
    def heapify(array, n, i):
        """
        Rearranges the elements in the array to satisfy the heap property.

        Parameters:
        array (list): The array to be heapified.
        n (int): The size of the heap.
        i (int): The index of the current element.

        Returns:
        None
        """
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and array[left] > array[largest]:
            largest = left
        if right < n and array[right] > array[largest]:
            largest = right
        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            heapify(array, n, largest)
    n = len(array)
    for i in range(n//2 - 1, -1, -1):
        heapify(array, n, i)
    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)

def radix_sort(array):
    """
    Sorts the given array using the radix sort algorithm.

    Radix sort is a non-comparative sorting algorithm that sorts integers by grouping
    them by individual digits. It starts by sorting the least significant digit and
    progressively moves towards the most significant digit.

    Args:
        array (list): The unsorted array of integers.

    Returns:
        list: The sorted array.

    """
    RADIX = 10
    placement = 1
    max_digit = max(array)
    while placement < max_digit:
        buckets = [list() for _ in range(RADIX)]
        for i in array:
            tmp = int((i / placement) % RADIX)
            buckets[tmp].append(i)
        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                array[a] = i
                a += 1
        placement *= RADIX
    return array


def factor_prime(n):
    """
    Returns a list of prime factors of a given number.

    Parameters:
    n (int): The number to find prime factors for.

    Returns:
    list: A list of prime factors of the given number.
    """
    # Check if the number is less than 2
    if n < 2:
        return []

    factors = []
    # Divide the number by 2 until it is no longer divisible by 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Divide the number by 3 until it is no longer divisible by 3
    while n % 3 == 0:
        factors.append(3)
        n //= 3

    i = 5
    # Check for prime factors starting from 5
    while i * i <= n:
        # Divide the number by i until it is no longer divisible by i
        while n % i == 0:
            factors.append(i)
            n //= i
        # Divide the number by (i + 2) until it is no longer divisible by (i + 2)
        while n % (i + 2) == 0:
            factors.append(i + 2)
            n //= (i + 2)
        i += 6

    # If the number is still greater than 1, it is a prime factor itself
    if n > 1:
        factors.append(n)

    return factors


def prime_sieve(n):
    """
    Returns a list of prime numbers up to a given number.

    Parameters:
    n (int): The number to find prime numbers up to.

    Returns:
    list: A list of prime numbers up to the given number.
    """
    # Create a boolean array of size n + 1
    # and initialize all elements to True
    prime = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        # If prime[p] is True, then it is a prime number
        if prime[p]:
            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    # Return all prime numbers
    return [i for i in range(2, n + 1) if prime[i]]


def distributed_prime_factor()
