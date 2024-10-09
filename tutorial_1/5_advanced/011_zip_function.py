# zip(*iterables) = aggregate elements from two or more iterables (list, tuples, sets, etc. )
#                   creates a zip object with paired elements stored in tuples for each element


usernames = ['Dude', 'Bro', 'Mister']
passwords = ('password', 'abc123', 'guest')
login_date = ['2020-01-01', '2020-01-02', '2020-01-03']


# # two itetrables of usernames and passwords
# users = zip(usernames, passwords)
# users = list(zip(usernames, passwords))  # zip object convert to list
# users = dict(zip(usernames, passwords))  # zip object convert to dict
# print(users, type(users))

# for i in users:
#     print(i)

# for key, value in users.items():
#     print('{}: {}'.format(key, value))


# # three itetrables of usernames, passwords and login_date
# users_2 = zip(usernames, passwords, login_date)

# for item in users_2:
#     print(item)

# for key, value, dates in users_2:
#     print('{}: {}: {}'.format(key, value, dates))
