# just all of the sets below sharing some common element should be grouped together
# output should look like "[{3, 5}, {7}, {0, 1, 2, 4, 6, 8, 9}]"

countriesSet = [{0, 2}, {8, 1}, {1, 4}, {8, 2}, {2, 6}, {3, 5}, {9, 6}, {7}]

first = True
for i in countriesSet:
    cont = False
    similarElements = []
    for j in countriesSet:
        if(i!=j and (len(i.intersection(j)) > 0)):
            similarElements.append(i)
            similarElements.append(j)

    # append that merged element between all elements sharing some common inner element
    if(len(similarElements)>0):
        mergeEle = {}
        for i in similarElements:
            if(len(mergeEle) == 0):
                mergeEle = i
            else:
                mergeEle |= i

            if(countriesSet.__contains__(i)):
                countriesSet.remove(i)
        countriesSet.append(mergeEle)
print(countriesSet)