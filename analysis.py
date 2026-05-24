import pandas as pd
import matplotlib.pyplot as plt

# Load Netflix dataset
df = pd.read_csv('data/netflix_titles.csv')

# Remove missing values
df = df.dropna(subset=['type', 'country', 'rating'])

print("\n" + "=" * 60)
print("🎬        NETFLIX DATA ANALYSIS PROJECT")
print("=" * 60)

# ---------------------------------------------------
# Total Titles
# ---------------------------------------------------
total_titles = len(df)

print(f"\n📺 Total Titles Available on Netflix: {total_titles}")

# ---------------------------------------------------
# Movies vs TV Shows
# ---------------------------------------------------
content_type = df['type'].value_counts()

print("\n🎞 Content Type Distribution:")
for content, count in content_type.items():
    print(f"   ➜ {content}: {count}")

# Create Bar Chart
plt.figure(figsize=(6, 4))

content_type.plot(kind='bar')

plt.title("Netflix Content Type Distribution")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")

# Save graph
plt.savefig('graphs/content_type.png')

plt.show()

# ---------------------------------------------------
# Top 5 Countries
# ---------------------------------------------------
top_countries = df['country'].value_counts().head(5)

print("\n🌍 Top 5 Countries with Most Netflix Content:")
for country, count in top_countries.items():
    print(f"   ➜ {country}: {count}")

# Create Pie Chart
plt.figure(figsize=(7, 7))

top_countries.plot(kind='pie', autopct='%1.1f%%')

plt.title("Top 5 Countries on Netflix")
plt.ylabel("")

# Save graph
plt.savefig('graphs/top_countries.png')

plt.show()

# ---------------------------------------------------
# Top Ratings
# ---------------------------------------------------
top_ratings = df['rating'].value_counts().head(5)

print("\n⭐ Most Common Ratings:")
for rating, count in top_ratings.items():
    print(f"   ➜ {rating}: {count}")

# ---------------------------------------------------
# Popular Genres
# ---------------------------------------------------
genres = df['listed_in'].str.split(', ').explode()

top_genres = genres.value_counts().head(5)

print("\n🎭 Most Popular Genres:")
for genre, count in top_genres.items():
    print(f"   ➜ {genre}: {count}")

# ---------------------------------------------------
# Release Year
# ---------------------------------------------------
latest_year = df['release_year'].max()

print(f"\n📅 Latest Release Year in Dataset: {latest_year}")

# ---------------------------------------------------
# Final Insights
# ---------------------------------------------------
print("\n" + "=" * 60)

print("\n📌 PROJECT INSIGHTS")
print("--------------------------------------------------")

print("✔ Netflix has more Movies than TV Shows.")
print("✔ United States produces the highest Netflix content.")
print("✔ International Movies are highly popular.")
print("✔ TV-MA is the most common content rating.")
print("✔ Netflix contains content from multiple countries.")

print("\n✅ Analysis Completed Successfully")

print("=" * 60)