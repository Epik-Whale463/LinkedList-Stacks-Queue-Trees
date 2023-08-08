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
    
def merge(left, right):
    
    """
    Merges two linked lists sorting by data in the nodes and returns a new merged linked list 
    """
    
    # Create a new linked list that contains the nodes after sorting
    
    # merging left and right
    
    merged = LinkedList()
    
    # Add a fake head that is discarded later
    merged.add(0)
    
    # set current to the head of the linked list
    
    current = merged.head
    
    # obtain head nodes for left and right linked lists
    
    left_head  = left.head
    right_head = right.head
    
    # Iterate over left and right until we reach tail node of either
    
    while left_head or right_head:
        
        # if the head node of left is none , we're past the tail
        # Add the node from right to merged linked list 
        
        if left_head is None:
            current.next_node = right_head
            #Call next on right to set loop condition to false
            
            right_head = right_head.next_node
        
        # if the head node of right is None , we're past the tail
        # add the tail node from left to merged linked list
        
        elif right_head is None:
            current.next_node = left_head
            #Call next on left to set loop condition to false
            
            left_head  = left_head.next_node
        
        else:
            # Not at either tail node
            # Obtain node data to perform comparision operations
            
            left_data = left_head.data
            right_data = right_head.data
            
            # if data on left is less than right , set current to left node
            if left_data < right_data:
                current.next_node = left_head
            
                # Move left head to next node 
                left_head = left_head.next_node
            
            # if data on left is greater than right , set current to right node
            else:
                current.next_node = right_head
                
                # Move right head to next node
                right_head = right_head.next_node
                
        # Move current to next node
        current = current.next_node
     
    # Discard the fake head and set first merged node as head 
    head = merged.head.next_node
    merged.head = head
    return merged
                
            
            
l = LinkedList()
l.add(10)
l.add(2)
l.add(30)
l.add(16)
l.add(0)

print(l)

sorted_linked_list = MergeSort(l)
print(f"\nSorted Linked List : {sorted_linked_list}")