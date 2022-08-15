get_duplicates_dic = {}
def get_and_remove_duplicates(list_c_ids):
    for list_c_id in list_c_ids:
        dup_sum = df[list_c_id].duplicated().sum()
        get_duplicates_dic[list_c_id] = dup_sum
        print(list_c_id,'has',dup_sum,'values.')
        #drop_duplocates = df[list_c_id].drop_duplicates() # all duplicates values has been removed
        #print(b,drop_duplocates)