# Sample user-item matrix 
ratings = [
    [5, 3, 0, 2, 0],
    [4, 0, 4, 0, 5],
    [0, 0, 5, 1, 2],
    [2, 0, 3, 0, 4],
    [0, 0, 0, 5, 0]
]

# Function to calculate similarity between two users
def cosine_similarity(user1, user2):
    dot_product = sum(user1[i] * user2[i] for i in range(len(user1)))
    magnitude_user1 = sum(user1[i] ** 2 for i in range(len(user1))) ** 0.5
    magnitude_user2 = sum(user2[i] ** 2 for i in range(len(user2))) ** 0.5
    return dot_product / (magnitude_user1 * magnitude_user2)

# Function to recommend movies to a user based on their preferences
def recommend_movies(user_id, num_recommendations=5):
    user_ratings = ratings[user_id]
    similar_users = []

    # Calculate similarity with other users
    for i in range(len(ratings)):
        if i != user_id:
            similarity = cosine_similarity(user_ratings, ratings[i])
            similar_users.append((i, similarity))

    # Sort users by similarity
    similar_users.sort(key=lambda x: x[1], reverse=True)

    # Find movies that the user has not rated
    unrated_movies = [i for i, rating in enumerate(user_ratings) if rating == 0]

    # Recommend movies based on similar users' ratings
    recommendations = []
    for user, _ in similar_users:
        for movie_id in unrated_movies:
            if ratings[user][movie_id] > 0:
                recommendations.append((movie_id, ratings[user][movie_id]))
            if len(recommendations) >= num_recommendations:
                return recommendations

# Ui
def main():
    user_id = int(input("Enter your user ID (0-4): "))

    recommendations = recommend_movies(user_id, num_recommendations=3)

    print(f"Recommended movies for User {user_id}:")
    for movie_id, rating in recommendations:
        print(f"Movie {movie_id}: Rating {rating}")

if __name__ == "__main__":
    main()
