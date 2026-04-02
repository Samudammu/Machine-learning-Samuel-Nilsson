# Filmrekommendationssystem – Lab 1

## 1. Introduktion
I denna laboration har jag byggt ett enkelt rekommendationssystem för filmer med hjälp av "content-based filtering" baserat på filmgenres. Systemet tar en film som input och rekommenderar fem liknande filmer.  

Datasetet som används är "MovieLens ml-latest", där varje film har en titel och tillhörande genres.



## 2. Dataset
Datasetet innehåller följande filer:  
- "movies.csv" – lista med filmer och deras genres  
- "ratings.csv" – användarvärderingar (ej använda i denna version)  
- "tags.csv" – taggar för filmer (ej använda i denna version)  

För denna laboration används endast "movies.csv".  

Mappen "ml-latest" ligger lokalt och är ".gitignore:ad" för att undvika att ladda upp stora filer till GitHub.

För att minska minnesanvändningen och kunna köra skriptet på en vanlig dator har datasetet begränsats till de första 5000 filmerna med:

"movies = movies.head(5000)"

Denna begränsning kan tas bort om datorn klarar att hantera hela datasetet.



## 3. Metod
1. **Förbered data**  
   - Dela upp genre-strängen för varje film i en lista.
   - Använd "MultiLabelBinarizer" för att skapa en "one-hot representation" av genres.

2. **Beräkna likheter**  
   - Använd "NearestNeighbors" från "sklearn" med cosine similarity för att hitta de fem mest liknande filmerna.

3. **Rekommendationsfunktion**  
   - Funktionen "recommend_movies(title)" tar en film som input.  
   - Returnerar en lista med fem filmer som har mest liknande genres.



## 4. Visualisering / Exempel
Exempel på hur systemet fungerar:

Input: "Cars (2006)"

Rekommenderade filmer:
1. Rugrats in Paris: The Movie (2000)
2. Bamse and the Volcano Island (2021)
3. Hare Tonic (1945)
4. Garfield: A Tail of Two Kitties (2006)
5. I Haven't Got a Hat (1935)