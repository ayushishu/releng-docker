# tests/test_github_actions.py

import subprocess
import pytest

def test_docker_image_built():
    # Run the GitHub Actions workflow locally
    subprocess.run(["docker", "build", "-t", "ayushishu/odl-ubuntu-image", "."], check=True)

    # TODO: Add assertions based on your specific requirements
    assert True  # Placeholder assertion

def test_docker_image_pushed():
    # Run the GitHub Actions workflow locally
    subprocess.run(["docker", "build", "-t", "ayushishu/odl-ubuntu-image", "."], check=True)
    subprocess.run(["docker", "push", "ayushishu/odl-ubuntu-image"], check=True)

    # TODO: Add assertions based on your specific requirements
    assert True  # Placeholder assertion
