from model import User  #

def get_all_users():
    query = User.select()
    for user in query:
        print(user.num_pokazaina, user.Date_and_time, user.Chastota, user.Power, user.temp, user.number_stan)

if __name__ == '__main__':

    get_all_users()
