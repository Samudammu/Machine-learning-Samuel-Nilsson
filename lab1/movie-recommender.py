import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.neighbors import NearestNeighbors

# ===============================
# 1️⃣ Ladda datasetet
# ===============================
movies = pd.read_csv("ml-latest/movies.csv")

# Begränsa datasetet om du vill (valfritt)
# movies = movies.head(5000)  # kan tas bort om datorn klarar hela

# ===============================
# 2️⃣ Förbered genres
# ===============================
movies["genres"] = movies["genres"].apply(lambda x: x.split("|"))

mlb = MultiLabelBinarizer()
genre_matrix = mlb.fit_transform(movies["genres"])

# ===============================
# 3️⃣ Skapa NearestNeighbors-modell
# ===============================
nn = NearestNeighbors(n_neighbors=6, metric='cosine')  # 6 = 5 rekommendationer + inputfilmen
nn.fit(genre_matrix)

# ===============================
# 4️⃣ Funktion för rekommendationer
# ===============================
def recommend_movies(title):
    if title not in movies["title"].values:
        return f"Movie '{title}' not found"
    
    idx = movies[movies["title"] == title].index[0]
    distances, indices = nn.kneighbors([genre_matrix[idx]])
    
    # Exkludera inputfilmen själv och ta topp 5
    recommended = [movies["title"].iloc[i] for i in indices[0] if i != idx]
    return recommended[:5]

# ===============================
# 5️⃣ Kör som script
# ===============================
if __name__ == "__main__":
    input_movie = "Cars (2006)"  # byt till valfri film
    recommendations = recommend_movies(input_movie)

    print(f"Recommended movies for '{input_movie}':")
    for i, movie in enumerate(recommendations, 1):
        print(f"{i}. {movie}")