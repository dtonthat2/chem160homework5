def molemass2(mol):
    names=["H", "C", "N", "O", "P", "S", "K", "F"]
    masses=[1.0079,12.0107,14.0067,15.9994,30.9738,32.0660,39.0983,18.9984]
    Dict=dict(zip(names,masses))
    mmass=0
    celement = [mol[0]]
    for i in range(len(mol)):

        string = mol[i]
        if string.isdigit():
            massadd= Dict[celement]* (int(string)-1)
        else :
            celement = string
            massadd = Dict[celement]
            if i+1 >len(mol):
                check = mol[i+1]
                if check.isdigit():
                    continue
        mmass+= massadd
    return mmass