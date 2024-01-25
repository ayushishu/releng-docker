# test_workflow.py
import subprocess

def test_workflow_runs():
    # Test that the GitHub Actions workflow runs successfully
    result = subprocess.run(["act", "-n"], capture_output=True, text=True)
    assert "Job succeeded" in result.stdout, "Workflow failed to run."

def test_build_steps():
    # Test that the build steps in the workflow produce the expected output
    result = subprocess.run(["act", "-n"], capture_output=True, text=True)
    
    # Modify the following assertions based on your specific criteria
    assert "Building and testing..." in result.stdout, "Build steps are not correct."
    assert "Build successful" in result.stdout, "Build failed."


