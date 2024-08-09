# RECOMMENDATION SYSTEM

# Create a simple recommendation system that suggests items
# to users based on their preferences. You can use techniques
# like collaborative filtering or content-based filtering to
# recommend movies, books, or products to users.

import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Load the dataset from a file

data = []
users=[]

with open(r"C:\Users\aksha\OneDrive\Documents\MYDAILYWORK\Task 4\reviews.txt", 'r') as file:
    for line in file:
        d=line.strip().split()
        user=d[0]
        rating=d[-1]
        movie=" ".join(d[1:-1])
        rating = int(rating)
        users.append(user)
        data.append((user, movie, rating))
        
users=list(set(users))
# Convert the data into a DataFrame
ratings_df = pd.DataFrame(data, columns=['User', 'Movie', 'Rating'])

# Pivot the DataFrame to create a user-movie matrix
user_movie_matrix = ratings_df.pivot(index='User', columns='Movie', values='Rating').fillna(0)

# Step 2: Calculate Similarity (User-Based Collaborative Filtering)
user_similarity = cosine_similarity(user_movie_matrix)

# Create a DataFrame for the similarity matrix
user_similarity_df = pd.DataFrame(user_similarity, index=user_movie_matrix.index, columns=user_movie_matrix.index)

# Step 3: Generate Recommendations
def recommend_movies(user, ratings_matrix, similarity_matrix, num_recommendations=5):
    # Get the similarity scores for the user
    user_index = ratings_matrix.index.get_loc(user)
    similarity_scores = similarity_matrix.iloc[user_index]

    # Multiply the similarity scores with the ratings
    weighted_ratings = ratings_matrix.mul(similarity_scores, axis=0)

    # Sum up the weighted ratings and normalize by the sum of the similarities
    recommendation_scores = weighted_ratings.sum(axis=0) / similarity_scores.sum()

    # Remove movies that the user has already rated
    user_rated_movies = ratings_matrix.loc[user]
    recommendations = recommendation_scores[user_rated_movies == 0].sort_values(ascending=False)

    return recommendations.head(num_recommendations)

# Example: Recommend 5 movies for "Alice"
print("\n\t\t\t\tMovie Recommendations\n")
while(True):
    user_name=input("Enter the user Name:").title()
    if user_name in users:
        print("Recommendations for ",user_name,":")
        break
    else :
        print("The user does not exist,Enter any existing user name")

recommendations = recommend_movies(user_name, user_movie_matrix, user_similarity_df, 5)
# Print each movie and score
for movie, score in recommendations.items():
    score=score*10
    print(f"{movie}  {score:.2f}")
