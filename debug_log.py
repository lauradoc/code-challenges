logs = [
    {
      'id': 3,
      'action': 'F'
    },
    {
      'id': 2,
      'action': 'D'
    },
    {
      'id': 1,
      'action': 'A'
    },
    {
      'id': 5,
      'action': 'A'
    },
    {
      'id': 3,
      'action': 'Q'
    },
    {
      'id': 4,
      'action': 'F'
    },
    {
      'id': 1,
      'action': 'B'
    },
    {
      'id': 3,
      'action': 'Z'
    },
    {
      'id': 1,
      'action': 'C'
    }
  ];


# write a function that takes in a log of user actions
# return a list of users that have hit a bug
# ex: a bug would be [A,B,C]

# return an empty list if no one encounters bug

# first create empty list
# loop through the log
# check to see if action A has occurred
# keep track of user id
# check to see if B occurred
# if user id matches tracked
# then check to see if C occurred
# if user id matches tracked then add to empty list

# PART 1
# def debug_log(log):
    
#     users = []
#     possible_users = {}

    
#     for i in range(len(log)):
        
#         if log[i]['action'] == 'A':
#             possible_users[log[i]['id']] = 'A'
#         elif log[i]['id'] in possible_users:
#             possible_users[log[i]['id']] += log[i]['action']
                
#     for key, value in possible_users.items():
#         if 'ABC' in value:
#             users.append(key)
            
#     return users

# print(debug_log(logs))

def debug_log(log, code):
    
    users = []
    possible_users = {}

    for i in range(len(log)):
        
        user_action = log[i]['action']
        user_id = log[i]['id']
        
        if user_action == code[0]:
            possible_users[user_id] = code[0]
        elif user_id in possible_users:
            possible_users[user_id] += user_action
                
    for key, value in possible_users.items():
        if code in value:
            users.append(key)
            
    return users

print(debug_log(logs, 'ABC'))

if __name__ == '__main__':    
    import doctest
    if doctest.testmod().failed == 0:        
        print('\n✨ ALL TESTS PASSED!\n')