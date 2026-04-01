user_data = {}

def store_data(user_id, df):
    if user_id not in user_data:
        user_data[user_id] = []

    user_data[user_id].append(df)


def get_user_data(user_id):
    return user_data.get(user_id, [])