# Exploring dictionaries
current_movies = {'The Grinch': '11:00',
                  'The Balls': '14:00',
                  'Rudolph': '21:00',
                  'Shining': '1:00'}

del current_movies['The Balls']

print('We\'re currently showing movies:')

for mv in current_movies:
    print(mv)

movie = input('\nWhat movie to show time for? ')
show_time = current_movies.get(movie)

if not show_time:
    print("This movie is not on the list of the movies we are showing")
else:
    print(movie, "is airing at", show_time)
