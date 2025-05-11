import random
from google.adk.agents import LlmAgent

def recommend_by_genre(genre: str) -> dict:
    """Recommends movies based on the specified genre."""
    genre = genre.lower()
    movie_db = {
        "action": ["Mad Max: Fury Road", "John Wick", "Gladiator"],
        "comedy": ["Superbad", "The Grand Budapest Hotel", "Step Brothers"],
        "drama": ["The Shawshank Redemption", "Forrest Gump", "Fight Club"],
        "sci-fi": ["Inception", "The Matrix", "Interstellar"],
    }

    if genre in movie_db:
        recommendations = random.sample(movie_db[genre], 2)
        return {
            "status": "success",
            "report": f"Top {genre} movie recommendations: {', '.join(recommendations)}"
        }
    else:
        return {
            "status": "error",
            "error_message": f"No recommendations available for genre '{genre}'."
        }

recommend_by_genre_mcp_description = {
    "name": "recommend_by_genre",
    "description": "Recommends movies based on the specified genre.",
    "parameters": {
        "type": "object",
        "properties": {
            "genre": {
                "type": "string",
                "description": "The genre for which to recommend movies.",
            }
        },
        "required": ["genre"],
    },
    "returns": {
        "type": "object",
        "properties": {
            "status": {"type": "string", "enum": ["success", "error"]},
            "report": {"type": "string", "description": "Movie recommendations."},
            "error_message": {"type": "string", "description": "Error details if status is 'error'."},
        },
        "required": ["status"],
    },
}

def get_trending_movies() -> dict:
    """Returns a list of trending movies."""
    trending = ["Dune: Part Two", "Oppenheimer", "Barbie", "Spider-Man: Across the Spider-Verse"]
    return {
        "status": "success",
        "report": f"Trending movies right now: {', '.join(trending)}"
    }

get_trending_movies_mcp_description = {
    "name": "get_trending_movies",
    "description": "Returns a list of trending movies.",
    "returns": {
        "type": "object",
        "properties": {
            "status": {"type": "string", "enum": ["success"]},
            "report": {"type": "string", "description": "List of trending movies."},
        },
        "required": ["status"],
    },
}

def get_movie_info(title: str) -> dict:
    """Fetches basic information about a specified movie."""
    movie_info_db = {
        "inception": "Inception is a 2010 sci-fi film directed by Christopher Nolan. It explores the concept of dreams within dreams.",
        "the matrix": "The Matrix is a 1999 action sci-fi film where humans live unknowingly inside a simulated reality.",
        "barbie": "Barbie is a 2023 fantasy comedy film directed by Greta Gerwig, featuring Margot Robbie as the iconic doll.",
    }

    key = title.lower()
    if key in movie_info_db:
        return {"status": "success", "report": movie_info_db[key]}
    else:
        return {
            "status": "error",
            "error_message": f"No information found for movie '{title}'."
        }

get_movie_info_mcp_description = {
    "name": "get_movie_info",
    "description": "Fetches basic information about a specified movie.",
    "parameters": {
        "type": "object",
        "properties": {
            "title": {
                "type": "string",
                "description": "The title of the movie to fetch information for.",
            }
        },
        "required": ["title"],
    },
    "returns": {
        "type": "object",
        "properties": {
            "status": {"type": "string", "enum": ["success", "error"]},
            "report": {"type": "string", "description": "Information about the movie."},
            "error_message": {"type": "string", "description": "Error details if status is 'error'."},
        },
        "required": ["status"],
    },
}

# Define the root movie recommendation agent using LlmAgent
root_agent = LlmAgent(
    name="movie_recommendation_agent",
    model="gemini-2.0-flash",
    description="Agent that provides movie recommendations, trending lists, and movie details.",
    instruction="You are a helpful agent who recommends movies, lists trending titles, and provides movie info.",
    tools=[recommend_by_genre, get_trending_movies, get_movie_info],  # ADK uses these directly
    # You could potentially store the MCP descriptions here for documentation purposes
    
)
tool_descriptions={
        "recommend_by_genre": recommend_by_genre_mcp_description,
        "get_trending_movies": get_trending_movies_mcp_description,
        "get_movie_info": get_movie_info_mcp_description,
    }

# You can now access the MCP-style descriptions via root_agent.tool_descriptions
#print(root_agent.tool_descriptions["recommend_by_genre"])