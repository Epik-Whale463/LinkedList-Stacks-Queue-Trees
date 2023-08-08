from linked_list import LinkedList

def MergeSort(linked_list):
    '''
    This function sorts the linked list in ascending order.
    - Recusively divide the linked list into sub lists  containing a single node
    Then we repetitively merge the sublists together to produce sorted sublists until one remains
    Finally it returns a sorted linked list 
    '''
    
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list
    
    left_half, right_half = split(linked_list)
    
    left = MergeSort(left_half)
    right = MergeSort(right_half)
    
    return merge(left, right)
    
def split(linked_list):
    """
    Divide the unsorted list at midpoint into sub(linked)lists
    """
    if linked_list ==None or linked_list.head == None:
        left_half = linked_list
        right_half = None
    
        return left_half, right_half
    
    else:
        size = linked_list.size()
        mid = size //2
        
        mid_node  = linked_list.node_at_index(mid-1)
        
        left_half = linked_list
        right_half = LinkedList()
        
        right_half.head = mid_node.next_node
        mid_node.next_node = None
        
        return left_half, right_half
    
def merge():
    pass
        