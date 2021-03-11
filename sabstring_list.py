mainStr="the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
substr=mainStr.split()
var="over"
i=0
while i<len(substr):
    if substr[i]==var:
        substr.remove(var)
        substr.insert(i,"on")
    i+=1
print(substr)



    

    