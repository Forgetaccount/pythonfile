users=[]
f1=open('../in-yh//industry_yh_node_num_n.txt','r')
f2=open('../in-yh//计数_cora.txt','w')
for line in f1.readlines():
    line = line.strip()
    s = line.split()
    users.append(int(s[1]))
user_dict = {}
for user in users:
    if user not in user_dict:

        user_dict[user] = 1
    else:
        user_dict[user] +=1
for di in user_dict:
    f2.write(str(di)+" "+str(user_dict[di])+"\n" )