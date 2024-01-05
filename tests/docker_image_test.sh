if [ -z "$DOCKER_IMAGE_NAME" ]; then
  echo "Error: DOCKER_IMAGE_NAME environment variable is not set."
  exit 1  # Mark the test as failed if the variable is not set
fi

# Check if the Docker image is present
if docker images -q "$DOCKER_IMAGE_NAME" &>/dev/null; then
  echo "Docker image '$DOCKER_IMAGE_NAME' is built successfully."
else
  echo "Docker image '$DOCKER_IMAGE_NAME' is not found. Build might have failed."
  exit 1  # Mark the test as failed if the image is not found
fi