import os
import subprocess

# B608: Possible SQL injection vector through string-based query construction
def get_user_data(user_id):
    # This is unsafe - using os.popen() for command execution with user input
    cmd = "ls -la /home/" + user_id
    os_stream = os.popen(cmd)  # B608: os.popen() call is vulnerable to shell injection
    output = os_stream.read()
    return output

# Example usage
def main():
    user_input = input("Enter username: ")
    user_data = get_user_data(user_input)
    print("User data:", user_data)

if __name__ == "__main__":
    main()
