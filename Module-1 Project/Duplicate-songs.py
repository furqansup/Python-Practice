# Here's an example list of songs
songs = ['Bohemian Rhapsody', 'Stairway to Heaven', 'Bohemian Rhapsody', 'Hotel California', 'November Rain', 'Stairway to Heaven', 'Sweet Child O\' Mine']

# Write your code here

# Creating a list of songs that contains duplicate names.

duplicate_songs = {song for song in songs if not song.startswith('S') and not song.endswith('n')}

print(duplicate_songs)