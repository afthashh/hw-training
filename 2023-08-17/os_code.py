# import os

# # Get the current working directory
# current_directory = os.getcwd()
# print("Current Directory:", current_directory)

# # Create a new directory
# new_directory = os.path.join(current_directory, 'new_folder')
# os.mkdir(new_directory)
# print("New Directory Created:", new_directory)

# # List contents of a directory
# directory_contents = os.listdir(current_directory)
# print("Directory Contents:", directory_contents)

# # Rename a file or directory
# os.rename('file.txt', 'new_file.txt')

# # Remove a file or directory
# os.remove('new_file.txt')
# os.rmdir(new_directory)

# import os

# # Get the value of an environment variable
# home_directory = os.environ.get('HOME')
# print("Home Directory:", home_directory)

# # Set an environment variable
# os.environ['MY_VARIABLE'] = 'Hello, World!'
# print("MY_VARIABLE:", os.environ['MY_VARIABLE'])

# # Check if an environment variable exists
# if 'MY_VARIABLE' in os.environ:
#     print("MY_VARIABLE exists.")

# # Delete an environment variable
# if 'MY_VARIABLE' in os.environ:
#     del os.environ['MY_VARIABLE']
#     print("MY_VARIABLE deleted.")

# import os

# # Execute a system command
# exit_code = os.system('ls -l')

# # Check the exit code
# if exit_code == 0:
#     print("Command executed successfully.")
# else:
#     print("Command execution failed.")


import os

# Get the system's name
system_name = os.name
print("System Name:", system_name)

# Get the value of the PATH environment variable
path_variable = os.environ.get('PATH')
print("PATH Environment Variable:", path_variable)

# Join path components
path = os.path.join('/home', 'user', 'documents', 'file.txt')
print("Joined Path:", path)

# Get the basename of a path
basename = os.path.basename(path)
print("Basename:", basename)

# Get the directory name of a path
dirname = os.path.dirname(path)
print("Directory Name:", dirname)

# Check if a path exists
exists = os.path.exists(path)
print("Path Exists:", exists)
