import tensorflow as tf

def get_landmark_model(saved_model="models/pose_model"):  # Adjust path if needed

    try:
        # Load the SavedModel
        model = tf.saved_model.load(saved_model)
        print("Model loaded successfully!")
        return model

    except Exception as e:  # Catch general exceptions
        print(f"Error loading model: {e}")

        # Add specific checks for common errors (optional):
        if "MissingArgument" in str(e):  # Example check for missing arguments
            print("Check if required arguments for the model are provided correctly.")
        # ... (add more checks based on potential error messages)

    return None  # Indicate failure to load
