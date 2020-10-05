def molemass(mol):
    names=["H", "C", "N", "O", "P", "S", "K", "F"]
    masses=[1.0079,12.0107,14.0067,15.9994,30.9738,32.0660,39.0983,18.9984]
    Dict=dict(zip(names,masses))
    mmass=0
    for i in range(len(mol)):
        element = mol[i]
        mmass+= Dict[element]
    return mmass