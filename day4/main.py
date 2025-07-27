n = int(input())
if n % 10 < 5:
    print((n // 10) * 10)
else:
    print((n // 10 + 1) * 10)
##
friend_details = ["John", 27, "Web Developer"]

print(friend_details)

##
movies = [
    ("Eternal Sunshine of the Spotless Mind", 2004),
    ("Memento", 2000),
    ("Requiem for a Dream", 2000)
]

##
"""
movies = [
    "Eternal Sunshine of the Spotless Mind", 2004,
    "Memento", 2000,
    "Requiem for a Dream", 2000
]
"""

##
#           0      1     2      3       4           index
#          -5     -4    -3     -2      -1
friends = ["Me", "You", "No", "Yes", "JFK"]  # element
friends.append("No")
friends.clear()
print(len(friends) == 0)

##
movies = ("Cu Lao Xac Song", "End Game",
          "Lord of The Ring", "Hai Phuong",
          "Lat Mat", "F1 The Movie"
                     "Bi Kip Luyen Rong", "Ong Trum Co Bac",
          "IP", "Xom Tro Kungfu")

print(id(movies))
movies = movies + ("Conan",)
print(id(movies))
print(movies)

##
lst = [
    [1, 2, 3],
    ('a', 'c', 'bcd'),
    "abc",
    True,
    [1.2, 3.4, "mix"]
]
lst[1] = lst[1][:2] + ("LTNS",)
print(lst[1])

##
movies = [("Conan", "Joshep", 2009, 2039032)]
title = input("Movie name: ")
director = input("Director name: ")
release_year = int(input("Release year: "))
budget = int(input("Budget: "))
movie = (title, director, release_year, budget)
print(f"title: {movie[0]}")
print(f"release_year: {movie[2]}")
movies.append(movie)
print(movies[0])
print(movies[1])
movies.remove(movies[0])
print(movies)
