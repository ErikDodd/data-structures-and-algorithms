

movies = [
  {
    "title": "Beetlejuice",
    "year": 1988,
    "genres": ["Comedy", "Fantasy"],
  },
  {
    "title": "The Cotton Club",
    "year": 1984,
    "genres": ["Crime", "Drama", "Music"],
  },
  {
    "title": "The Shawshank Redemption",
    "year": 1994,
    "genres": ["Crime", "Drama"],
  },
  {
    "title": "Crocodile Dundee",
    "year": 1986,

    "genres": ["Adventure", "Comedy"],
  },
  {
    "title": "Valkyrie",
    "year": 2008,
    "genres": ["Drama", "History", "Thriller"],
  },
  {
    "title": "Ratatouille",
    "year": 2007,
    "genres": ["Animation", "Comedy", "Family"],
  },
  {
    "title": "City of God",
    "year": 2002,

    "genres": ["Crime", "Drama"],
  },
  {
    "title": "Memento",
    "year": 2000,

    "genres": ["Mystery", "Thriller"],
  },
  {
    "title": "The Intouchables",
    "year": 2011,

    "genres": ["Biography", "Comedy", "Drama"],
  },
  {
    "title": "Stardust",
    "year": 2007,
    "genres": ["Adventure", "Family", "Fantasy"],
  },
]


def sort_by_recent_year(movies_list):
    results_list = []
    results = sorted(movies_list, key=lambda movie: movie['year'], reverse=True)
    for movie in results:
        movie_to_append = movie['title']
        results_list.append(movie_to_append)
    return results_list

def sort_by_title_alphabetically(movies_list):
    results_list = []
    remove_word = ["The", "A", "An"]
    results = sorted(movies_list, key=lambda movie: movie['title'])
    # print(results)
    for movie in range(len(results)):
        title = results[movie]["title"]
        title_split = title.split(" ")
        if title_split[0] in remove_word:
            title_split.remove(title_split[0])
            # print(title_split[0])
        results[movie] = " ".join(title_split)
    print(results)







# sort_by_recent_year(movies)
sort_by_title_alphabetically(movies)
