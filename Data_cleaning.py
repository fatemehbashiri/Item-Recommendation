import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_and_clean_data(content_path: str, user_path: str):
    """
    Load and clean content and user data files.
    
    Parameters:
        content_path (str): Path to the content features CSV file.
        user_path (str): Path to the user view history CSV file.
        
    Returns:
        cleaned_pivot_table (DataFrame): A pivot table with user behavior data cleaned and formatted.
    """
    # Load content and user data
    content_data = pd.read_csv(content_path)
    user_data = pd.read_csv(user_path)

    # Cleaning content data: Remove missing values
    content_data = content_data.dropna()
    
    # Cleaning user data: Remove missing values
    user_data = user_data.dropna()

    # Aggregate content categories based on features like genre, country, etc.
    category_mapping = content_data.set_index('content_id')['category']

    # Map content categories to user data
    user_data['category'] = user_data['content_id'].map(category_mapping)

    # Create a pivot table where rows are users and columns are content categories
    pivot_table = pd.pivot_table(user_data, index='user_id', columns='category', aggfunc='size', fill_value=0)

    # Standardize the data for clustering
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(pivot_table)
    
    # Return the cleaned pivot table and scaled data
    return pivot_table, scaled_data
