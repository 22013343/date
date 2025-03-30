import requests
from bs4 import BeautifulSoup

# The URL of the GV movie listings page
url = "https://www.gv.com.sg/"

# Send a GET request to fetch the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Look for the movie elements (you'll need to adjust this based on actual structure)
movie_elements = soup.find_all('div', class_='movie-list')  # Example, adjust accordingly

movies = []
for movie in movie_elements:
    title = movie.find('h3').text  # Adjust based on the actual structure
    showtime = movie.find('span', class_='showtime').text  # Adjust accordingly
    movies.append({'title': title, 'showtime': showtime})

# Output the movie list
for movie in movies:
    print(f"Title: {movie['title']}, Showtime: {movie['showtime']}")
