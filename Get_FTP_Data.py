import paramiko
import FTPData


def display_folders():
    # Create an SSH client
    client = paramiko.SSHClient()

    # Automatically add the server's host key (not recommended for production)
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the SFTP server
    hostname, port, username, password = FTPData.getlogindata()
    client.connect(hostname, port, username, password)

    # Open an SFTP session
    sftp = client.open_sftp()

    # Get a list of all folders in the current directory
    folder_list = sftp.listdir()

    # Close the SFTP session and the SSH connection
    sftp.close()
    client.close()
    print("Closed Connection to FTP.")
    return folder_list


def get_folder_contents(selected_folder):
    # Create an SSH client
    client = paramiko.SSHClient()
    hostname, port, username, password = FTPData.getlogindata()

    # Automatically add the server's host key (not recommended for production)
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the SFTP server
    client.connect(hostname, port, username, password)

    # Open an SFTP session
    sftp = client.open_sftp()

    # Change the working directory to the selected folder
    sftp.chdir(selected_folder)

    # Get a list of all items (files and folders) in the current directory
    item_list = sftp.listdir()

    # Close the SFTP session and the SSH connection
    sftp.close()

    client.close()
    print("Closed Connection to FTP.")

    return item_list


def get_subfolder_contents(current_folder, subfolder):
    # Create an SSH client
    client = paramiko.SSHClient()
    hostname, port, username, password = FTPData.getlogindata()

    # Automatically add the server's host key (not recommended for production)
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the SFTP server
    client.connect(hostname, port, username, password)

    # Open an SFTP session
    sftp = client.open_sftp()

    # Change the working directory to the selected folder
    sftp.chdir(f"{current_folder}/{subfolder}")

    # Get a list of all items (files and folders) in the current directory
    item_list = sftp.listdir()

    # Close the SFTP session and the SSH connection
    sftp.close()

    client.close()
    print("Closed Connection to FTP.")

    return item_list
