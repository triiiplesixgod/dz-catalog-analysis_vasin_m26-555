import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

def average_rating(movies_lst: list[dict]) -> float:
    if not movies_lst:
        return 0.0
    
    score = 0.0
    for movie in movies_lst:
        score += movie['rating']

    return round(score / len(movies_lst), 1)

def catalog_age_stats(movies_lst: list[dict], current_year: int = 2026) -> tuple[int, int, int]:
    if not movies_lst:
        return (0, 0, 0)

    ages: list[int] = []
    for movie in movies_lst:
        ages.append(current_year - movie['year'])

    oldest = max(ages)
    newest = min(ages)
    avg = math.ceil(sum(ages) / len(ages))

    return (oldest, newest, avg)

def duration_in_hours(minutes: int) -> str:
    hours = minutes // 60
    mins = minutes % 60
    return f'{hours}ч {mins}'



def rating_tier(rating: float) -> str:
    norm = rating if (rating >= 0 and rating <= 10) else 0.0

    if norm >= 9:
        return "шедевр"
    elif norm >= 7:
        return "хорошо"
    elif norm >= 5:
        return "средне"
    else:
        return "слабо"

def decade_label(year: int) -> str:
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "старые"


print()
print('Фильмы не жанра comedy:')
for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])

print()

i = 0
while i < len(movies):
    movie = movies[i]
    if movie["rating"] > 9.0:
        print(f"Первый фильм с рейтингом > 9.0: {movie['title']} ({movie['rating']})")
        break
    i += 1
else:
    print("Шедевров не найдено")

def count_long_movies(movies_lst: list[dict], threshold: int = 120) -> int:
    count = 0
    for movie in movies_lst:
        if movie['duration_min'] > threshold:
            count += 1
    return count



def normalize_title(title: str) -> str:
    words = title.split()
    normalized_words: list[str] = []

    for word in words:
        if not word:
            continue
        normalized_words.append(word[0].upper() + word[1:])

    return " ".join(normalized_words)

def make_slug(title: str) -> str:
    return title.strip().lower().replace(" ", "-")

def format_report_line(movie: dict) -> str:
    title = normalize_title(movie["title"])
    year = movie["year"]
    rating = movie["rating"]
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))

    return f"\"{title}\" ({year}) — {rating}/10, {duration}, жанры: {genres}"


def title_sorted_by_rating(movies_lst: list[dict]) -> list[str]:
    sorted_movies = sorted(movies_lst, key = lambda m: m['rating'], reverse=True)
    return [movie['title'] for movie in sorted_movies]

def top_n_by_rating(movies_lst: list[dict], n: int = 3) -> list[tuple[str, float]]:
    sorted_movies = sorted(movies_lst, key = lambda m: m["rating"], reverse=True)
    top = []
    for movie in sorted_movies[:n]:
        top.append((movie["title"], movie["rating"]))
    return top
