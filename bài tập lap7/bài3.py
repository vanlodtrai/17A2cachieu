str='Dog is a pet animal. It is the oldest friend of human beings. It watches our house. It is very faithful animal and never left his master. It is used by police to fight crime. Sheep- rearers also use them. Thus it is useful for us in many ways.'
a=str.lower()
print(str)
word_list=a.split()
word_count={}
for i in range(len(word_list)):
    count=0
    for j in range(len(word_list)):
        if word_list[i]==word_list[j]:
            count += 1
    word_count[word_list[i]]= count
tần_số_max=max(word_count,key=word_count.get)
tần_số_min=min(word_count,key=word_count.get)
print("Tần số xuất hiện nhiều nhất là :",tần_số_max)
print("Số lần từ xuất hiện là :",word_count[tần_số_max])
print("Tần Số xuất hiện ít nhất là :",tần_số_min)
print("Số lần từ xuất hiện là :",word_count[tần_số_min])