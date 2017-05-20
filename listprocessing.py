def load_int_list(filename):
    """ Reads a collection of integers stored in a text file 
        named filename. Stores the elements in a list in the 
        same order they appear in the file.  Returns the 
        list of elements. """
    lst = []        ## Create empty list
    
    with open(filename, 'r') as infile:      ## Open file
        for line in infile:                ## Read each line
            line = line.strip('\n')        ## Remove new line character
            line = line.split()            ## Split on white space
            for i in line:                 ## For lines that contian multiple lists
                lst.append(int(i))         ## append the list
    
    return lst    ## Return completed list

def missing(checklist, mainlist):
    """ Returns the list containing all the elements of list 
        checklist that are not found in list mainlist.  If
        mainlist contains all the elements in checklist, the 
        function returns the empty list. This function does
        not modify the lists passed to it. """
    difflist = []
    
    for elem in checklist:
        if elem not in mainlist:
            difflist.append(elem)
        
    return difflist
    

def missing2(checklist, mainlist):
    """ Returns the list containing all the elements of list 
        checklist that are not found in list mainlist.  If
        mainlist contains all the elements in checklist, the 
        function returns the empty list. This function does
        not modify the lists passed to it. """
    return [x for x in checklist if x not in mainlist]
    

def rotate(lst, dist):
    """ Physically rearranges the elements of list lst, shifting 
        all the elements towards the back by the distance dist. 
        As an element "falls off" the rear, the function
        places it at the front in the space vacated when it shifted
        the first element backwards.

        For example, if list a contains the elements 
        [1, 2, 3, 4, 5, 6], the call rotate(a, 2) 
        rearranges the elements in a to contain [5, 6, 1, 2, 3, 4].
        Notice that if dist is equal to the length of the list, 
        after the rotation all the elements rotate to 
        their original locations.

        If dist is negative, the function shifts elements forward 
        dist spots instead of backwards. As an element "falls off" 
        the front the function places it on the rear in the space 
        vacated when it shifted the last element forwards.

        For example, if list a contains the elements 
        [1, 2, 3, 4, 5, 6], the call rotate(a list, -2) 
        rearranges list a to contain [3, 4, 5, 6, 1, 2]. 

        This function necessariy can modify the list passed by 
        the caller. """
    
    lst[:] = lst[-dist:] + lst[:-dist] 


def pairwise_sum(seq, n):
    """ Returns a list of 2-tuples (a, b) where a and b both
        are elements of list seq, a + b = n, and a <= b.  
        The result should contain no duplicate 2-tuples.  The 
        order of the 2-tuples within the result is unspecified.
        The function returns the empty list if seq is empty, and
        the function's behavior is undefined if seq contains 
        at least one non-number. """
        sums = []
        for x in seq:
            for y in seq:
                if x + y == n and x<= y:
                    i = (x, y)
                    if i not in sums:
                        sums.append(i)
    return sums


def main():
    """ Exercises the load_int_list and missing functions with
        two small sample files. """
    # Get the file names from the user
    file1 = input("Enter first file name: ")
    file2 = input("Enter second file name: ")
    
    # Load the files' contents into their respective lists
    lst1 = load_int_list(file1)
    lst2 = load_int_list(file2)
    
    # Determine the elements in lst1 that are missing from lst2
    mis = missing(lst1, lst2)
    mis2 = missing2(lst1, lst2)
    
    # Report the results
    print("Sequence 1:", lst1)
    print("Sequence 2:", lst2)
    print("Elements in sequence 1 missing from sequence 2:", mis)
    print("                                               ", mis2)
    
    # Rotate the lists
    rotate(lst1, 3)
    rotate(lst2, -5)
    print("Sequence 1 rotated 3:", lst1)
    print("Sequence 2 rotated -5:", lst2)

    # Exercise pairwise sums
    lst1 = list(range(0, 25))
    print("The pairwise sums to", 12, "in", lst1, "are")
    print("    ", pairwise_sum(lst1, 12))
    print("The pairwise sums to", 18, "in", lst1, "are")
    print("    ", pairwise_sum(lst1, 18))


if __name__ == "__main__":
    main()

