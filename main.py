# File paths for the content and user data files
content_file_path = './datas/content_features.csv'
user_file_path = './datas/user_content_views.csv'

# Output directory for saving the results
output_directory = './results/'

# Step 1: Load and clean data
pivot_table, scaled_data = load_and_clean_data(content_file_path, user_file_path)

# Step 2: Find the optimal number of clusters and perform clustering
optimal_k = find_optimal_k(scaled_data, max_clusters=15)
clusters, kmeans_model = perform_clustering(scaled_data, k=optimal_k)

# Step 3: Save the clustering results and additional analysis
save_results(pivot_table, clusters, kmeans_model, output_dir=output_directory)
