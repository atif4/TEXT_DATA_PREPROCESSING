dic_hl = {}
def get_boundary_value(list_c_ids):
    for list_c_id in list_c_ids:
        higher = df[list_c_id].mean() + 3*df[list_c_id].std()  
        print('Highest Allow',list_c_id,higher)
        lower = df[list_c_id].mean() - 3*df[list_c_id].std()
        print('Lowest Allow',list_c_id,lower)
        dic_hl[list_c_id] = [higher,lower]
get_boundary_value(['user_followers','user_friends','user_favourites'])
for k , v in dic_hl.items():
    if k == 'user_followers':
        user_followers23 = df[(df[k] > v[0]) | (df[k] < v[1])]
        print(len(user_followers23),v)
    elif k == 'user_friends':
        user_friends23 = df[(df[k] > v[0]) | (df[k] < v[1])]
        print(len(user_friends23),v)
    elif k == 'user_favourites':
        user_favourites23 = df[(df[k] > v[0]) | (df[k] < v[1])]
        print(len(user_favourites23),v)
 #get_boundary_value(['user_followers','user_friends','user_favourites'])
for k , v in dic_hl.items():
    if k == 'user_followers':
        user_followers23 = df[(df[k] < v[0]) & (df[k] > v[1])]
        print(k,len(user_followers23),v)
    elif k == 'user_friends':
        user_friends23 = df[(df[k] < v[0]) & (df[k] > v[1])]
        print(k,len(user_friends23),v)
    elif k == 'user_favourites':
        user_favourites23 = df[(df[k] < v[0]) & (df[k] > v[1])]
        print(k,len(user_favourites23),v)