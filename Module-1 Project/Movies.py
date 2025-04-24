# Start with an empty list
movie_collection = []

# Add some movies to the collection using the append() method
movie_collection.append("Expendables") # Use your favourite movie names
movie_collection.append("Man of steel")
movie_collection.append("Ghost rider")
movie_collection.append("12 angry men")
movie_collection.append("Pearl Harbour")

# Print the current collection of movies
print("My Movie Collection:", movie_collection)

# Remove a movie from the collection using the pop() method
# Code to remove index 3 here
print("After removing movie 4:", movie_collection.pop(3))

# Count how many movies are in the collection using the count() method
num_movies = len(movie_collection)
print("Number of movies:", num_movies)

# Reverse the order of the list using the reverse() method
movie_collection.reverse()

print("Reversed movie collection:", movie_collection)
