num_list=[]
mod_list=[]
for _ in range(10):
    num_list.append(int(input()))
for i in range(len(num_list)):
    a=num_list[i] % 42
    mod_list.append(a)
#print("mod_list:",mod_list)
new_list=set(mod_list)
#print("new_list:",new_list)
#print("len:",len(new_list))
print(len(new_list))