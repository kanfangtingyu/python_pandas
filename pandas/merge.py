import pandas as pd
# rating表的数据
df_ratings = pd.read_csv(
    "./datas/movielens-1m/ratings.dat",
    sep = "::",  # 分隔符
    engine = "python",   
    names = "UserID::MovieID::Rating::Timestamp".split("::")   # 这些名字是自己起的
)
print(df_ratings.head())

# 用户表的数据
df_users = pd.read_csv(
    "./datas/movielens-1m/users.dat",
    sep = "::",  # 分隔符
    engine = "python",   
    names = "UserID::Gender::Age::Occupation::Zip_code".split("::")
)
print(df_users.head())

# 电影本身的数据
df_movies = pd.read_csv(
    "./datas/movielens-1m/movies.dat",
    sep = "::",  # 分隔符
    engine = "python",   
    names = "MovieID::Title::Genres".split("::")
)
print(df_movies.head())

df_ratings_users_movies = pd.merge(
    df_ratings, df_users, left_on = "UserID", right_on = "UserID", how = "inner"
)
print(df_ratings_users_movies.head())