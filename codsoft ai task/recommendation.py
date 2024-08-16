import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler

# Create sample data
data = {
    'user_id': [1, 1, 1, 2, 2, 3, 3, 4, 4, 4],
    'movie_id': [1, 2, 3, 1, 4, 2, 5, 1, 3, 5],
    'rating': [5, 3, 4, 4, 5, 2, 4, 3, 4, 5]
}

df = pd.DataFrame(data)

# Create movie titles for reference
movies = {
    'movie_id': [1, 2, 3, 4, 5],
    'movie_title': ['Movie A', 'Movie B', 'Movie C', 'Movie D', 'Movie E']
}

movies_df = pd.DataFrame(movies)

# Create user-item matrix
user_item_matrix = df.pivot_table(index='user_id', columns='movie_id', values='rating')

# Fill NaN values with 0 (since we are using collaborative filtering)
user_item_matrix = user_item_matrix.fillna(0)

# Normalize the user-item matrix
scaler = StandardScaler()
user_item_matrix_scaled = scaler.fit_transform(user_item_matrix)

# Calculate cosine similarity between users
user_similarity = cosine_similarity(user_item_matrix_scaled)

# Convert similarity matrix to DataFrame
user_similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)

def recommend_movies(user_id, user_item_matrix, user_similarity_df, movies_df, top_n=3):
    # Get similar users
    similar_users = user_similarity_df[user_id].sort_values(ascending=False).index[1:]
    
    # Get the user's ratings
    user_ratings = user_item_matrix.loc[user_id]
    
    # Calculate weighted average ratings from similar users
    weighted_ratings = np.zeros(user_item_matrix.shape[1])
    similarity_sums = np.zeros(user_item_matrix.shape[1])
    
    for similar_user in similar_users:
        similar_user_ratings = user_item_matrix.loc[similar_user]
        mask = user_ratings == 0  # Only recommend movies that the user hasn't rated
        weighted_ratings[mask] += user_similarity_df.loc[user_id, similar_user] * similar_user_ratings[mask]
        similarity_sums[mask] += user_similarity_df.loc[user_id, similar_user]
    
    # Avoid division by zero
    predicted_ratings = weighted_ratings / (similarity_sums + 1e-9)
    
    # Get top N movie recommendations
    recommended_movie_indices = np.argsort(predicted_ratings)[::-1][:top_n]
    recommended_movies = movies_df[movies_df['movie_id'].isin(recommended_movie_indices + 1)]
    
    return recommended_movies

# Example usage
user_id = 1  # User for whom we want to recommend movies
recommended_movies = recommend_movies(user_id, user_item_matrix, user_similarity_df, movies_df)
print('Recommended Movies:')
print(recommended_movies)