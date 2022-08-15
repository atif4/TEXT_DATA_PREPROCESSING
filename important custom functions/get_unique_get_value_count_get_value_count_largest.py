def get_unique(c_id):
    unique = df[c_id].unique()
    return unique
def get_value_count(c_id):
    value_count = df[c_id].value_counts()
    return value_count
def get_value_count_largest(c_id):
    value_count_largest = df[c_id].value_counts().nlargest(30)
    return value_count_largest