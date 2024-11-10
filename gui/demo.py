import kagglehub

# Download latest version
path = kagglehub.dataset_download("harvard-university/course-enrollment-stats")

print("Path to dataset files:", path)