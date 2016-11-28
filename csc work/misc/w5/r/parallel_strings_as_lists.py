def triangle_area(base, height):
    ''' (number, number) -> float
    
    Return the area of the triangle with base and height.
    
    >>> triangle_area(10, 8)
    40.0
    '''
    
    return (base * height) / 2
    
def calculate_areas(base_list, height_list):
    ''' (list of number, list of number) -> list of float
    
    Precondition: len(base_list) == len(height_list)
    
    Return a list of the triangle areas for triangles with a base in
    base_list and a height at the corresponding position of height_list.
    
    >>> calculate_areas([10, 5, 7.5], [8, 5, 7.5])
    [40.0, 12.5, 28.125]
    '''
    
    areas = []
    for i in range(len(base_list)):
        areas.append(triangle_area(base_list[i], height_list[i]))
    return areas
    
def stretch_string(s, stretch_factors):
    ''' (str, list of int) -> str

    Precondition: len(s) == len(stretch_factors) and the items of
                  stretch_factors are non-negative
     
    Return a string consisting of the characters in s in the same order as in s,
    repeated the number of times indicated by the item at the corresponding
    position of stretch_factors.
    
    >>> stretch_string('Hello', [2, 0, 3, 1, 1])
    'HHllllo'
    >>> stretch_string('echo', [0, 0, 1, 5])
    'hooooo'
    '''
    
    string = ''
    for i in range(len(s)):
        string += s[i] * stretch_factors[i]
    return string
    
def greatest_difference(nums1, nums2):
    ''' (list of number, list of number) -> number

    Precondition: len(nums1) == len(nums2) and nums1 != []

    Return the greatest absolute difference between numbers at corresponding
    positions in nums1 and nums2.

    >>> greatest_difference([1, 2, 3], [6, 8, 10])
    7
    >>> greatest_difference([1, -2, 3], [-6, 8, 10])
    10
    '''
    
    greatest = 0
    for i in range(len(nums1)):
        difference = max(nums1[i], nums2[i]) - min(nums1[i], nums2[i])
        if difference > greatest:
            greatest = difference
    return greatest
