def evenAfterOdd(head) :
    #Your code goes here
    eh=None
    oh=None
    et=None
    ot=None
    temp=head

    while temp is not None:
        if temp.data%2==0:
            if eh==None:
                eh=temp
                et=eh
            else:
                et.next=temp
                et=temp 
            temp=temp.next
        else:
            if oh==None:
                oh=temp
                ot=oh
            else:
                ot.next=temp
                ot=temp 
            temp=temp.next
   
    if et is not None:
        et.next = None   # ?? Break even tail

    if ot is not None:
        ot.next = eh     # Attach even after odd

    return oh if oh is not None else eh

    