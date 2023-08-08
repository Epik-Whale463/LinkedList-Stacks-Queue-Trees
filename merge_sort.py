def merge_sort(lst):
    '''
    
    Sorts a list in ascending order
    Returns a new sorted list 
    
    Divide : Find the midpoint of the list and divide into sub lists
    Conquer : Recursive sort the sub lists created in the previous step
    Combine : Merge the sorted sub lists created in the previous step
    
    
    Final run time  = O (n log n)
    
    '''
    
    if len(lst) <=1:
        return lst
    
    left_half, right_half = split(lst)
    
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    return merge(left, right)



def split(lst):
    '''
    Divide the unsorted list at the midpoint into sub lists
    Returns two sublists , left and right
    
    Takes O(log n) time
    '''
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    
    return left, right

def merge(left,right):
    """
    Merge two lists/arrays , sorting them in the process
    Returns a new merged list
    
    Runs in overal O(n) time
    """
    new_lst = []
    
    i,j=0,0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new_lst.append(left[i])
            i += 1
        else:
            new_lst.append(right[j])
            j +=1
    
    while i <len(left):
        new_lst.append(left[i])
        i +=1
    
    while j < len(right):
        new_lst.append(right[j])
        j +=1
        
    return new_lst

def verify_sorted(lst):
    n = len(lst)
    
    if n == 0 or n == 1:
        return True
    
    return lst[0] <= lst[1] and verify_sorted(lst[1:])  


alist = [54,23,256,23,42,144,3535]
sorted_list = merge_sort(alist)
print(verify_sorted(alist))
print(verify_sorted(sorted_list))