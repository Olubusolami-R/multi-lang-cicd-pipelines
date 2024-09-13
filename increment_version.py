import sys
import subprocess

# File that stores the version number
VERSION_FILE = "VERSION_JAVA.txt"

# Function to increment the version
def increment_version(part):
    # Read current version
    with open(VERSION_FILE, "r") as f:
        version = f.read().strip()
    print("Current version " + version)
    # Split the version into major, minor, patch
    major, minor, patch = map(int, version.split("."))

    # Increment version part based on input
    if part == "major":
        major += 1
        minor = 0
        patch = 0
    elif part == "minor":
        minor += 1
        patch = 0
    elif part == "patch":
        patch += 1
    else:
        print("Invalid argument: use 'major', 'minor', or 'patch'")
        sys.exit(1)

    # Create new version string
    new_version = f"{major}.{minor}.{patch}"

    # Write new version back to the file
    with open(VERSION_FILE, "w") as f:
        f.write(new_version)

    return new_version

# Get version type (major, minor, patch) from the command line
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python increment_version.py [major|minor|patch]")
        sys.exit(1)

    version_type = sys.argv[1]
    new_version = increment_version(version_type)

    # Create a new Git tag
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", f"Bump version to {new_version}"])
    subprocess.run(["git", "tag", f"v{new_version}"])
    subprocess.run(["git", "push", "origin", "main", "--tags"])
