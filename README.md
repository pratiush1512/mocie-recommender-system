# Movie-recommender-system
Content Based Movie Recommender System which recommends movies similar to the movie that user enter. It also provides various the details of the recommended movie such as overview, genres, year of release, ratings, alongwith that the IMDb hyperlink.

The details of the movies(including Poster, Titles, IMDb and Metacritic rating) is fetched using an API by OMDB, https://www.omdbapi.com/, and using the IMDb library, the IMDb link for each movies are fetched out.

Using Streamlit i have built the web app for the recommender system. I have dumped the movies list and the result of cosine similarity into the pickle files (*Link: https://drive.google.com/drive/folders/1d_fYyMNqvWJAAkVUSxQJMizXthigNkkO?usp=sharing*). These two files are used in the "app.py" file to fetch the data about movie. 

## How-to-run-the-project-:
1. Clone this repository in your local system.
2. Install various dependencies as per requirements
3. Open your terminal/command prompt from your project directory and enter the command "streamlit run.py".
4. A webpage will be pop up in your default browser.
5. Hurray! That's it.

## Dataset-:
*Link: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata*

## Web-App-Visual-:
![image](https://user-images.githubusercontent.com/92681193/190169719-aec61466-5448-46e8-b1f1-5b8c95359585.png)
