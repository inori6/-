def display_orf(orfs,position):
    if not orfs:
        pass
    else:
        print(f'In reading frame{position}, the following open reading frame sequences were found:')
        for number,item in enumerate(orfs):
            print(f'''{number+1}    {item}''''')
