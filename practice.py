# hero = ['Shazam', 'Superman', 'Batman', 'Flash', 'Dr Fate']
# added_hero = ['Green Lantern']  # Keep it as a list

# hero[len(hero) - 1] = added_hero  # Replacing last element

# # Convert to a string
# # hero_string = ', '.join(hero[:-1]) + ', ' + added_hero[0]

# print(hero)


# Display N Characters of a File Name Extension

# text = "I am learning Python programming"
# print(text[14:20])

# word = "hello"
# print(word[::-1])

# text = "abcdefghijkl"
# print(text[:-1:2])

# filename = "holiday_video.mp4"
# print (filename[-3:])

# word = "programming"
# print(word[:-3])

# sentence = "Python is amazing!"
# print(sentence[::2])

# numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# print(numbers[2:6])

# sentence = "Python is powerful!"
# print(sentence[:])

# numbers = [1, 2, 3, 4, 5]
# for i in range(len(numbers)):
#     print(numbers[i])

# n = [2, 4, 6, 8, 10, 0]
# count=0

# for num in n:
#   if num==0:
#     continue
#   print(len(n)) 

# list1 = [1, 2, 3, 4, 5]
# print(list1[3:])

# x = -5
# y = 10
# if x > 0:
#     if y > 0:
#         print("x and y are both positive")
#     else:
#         print("x is positive and y is non-positive")
# else:
#     print("x is non-positive")

# set_a = {1,2,6}
# set_b = {1,2,8}
# print(set_a - set_b)

def get_month_name(month_name):
  if month_name == 'January':
    print("31 days")
  elif month_name == 'February':
    print('28/29 days')
  elif month_name == 'March':
    print('31 days')
  elif month_name == 'April':
    print('30 days')
  elif month_name == "May":
    print('31 days')
  elif month_name == 'June':
    print ('30 days')
  elif month_name == 'July':
    print('31 days')
  elif month_name == 'August':
    print('31 days')
  elif month_name == 'September':
    print('30 days')
  elif month_name == 'October':
    print('31 days')
  elif month_name == 'November':
    print('30 days')
  elif month_name == 'December':
    print('31 days')
  else:
    print('Wrong month name')

get_month_name('September')