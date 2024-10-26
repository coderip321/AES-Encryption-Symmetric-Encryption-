# AES Encryption Tool

## Instructions
- **Login Note**: After logging in, please wait for 5 to 10 seconds for the system to process and load the AES Encryption Tool interface.

## Project Overview
The **AES Encryption Tool** is a user-friendly application that enables users to encrypt and decrypt files using the AES symmetric encryption algorithm. Built with Flask and Tkinter, this project aims to provide an intuitive interface for file encryption and decryption, making it accessible for cybersecurity-focused users.

## Features
- **User Authentication**: Secure login with username and password.
- **File Encryption/Decryption**: Encrypt and decrypt files using AES encryption.
- **File Selection**: Easily select files for encryption or decryption through a graphical interface.
- **Windows Notifications**: Toast notifications to confirm successful login and logout actions.
- **Responsive Design**: Professional layout for enhanced user experience.

## Project Structure
```
project_folder/
├── app.py                   # Main Flask application file
├── templates/
│   ├── index.html           # Main page for file upload and encryption/decryption options
│   ├── result.html          # Result page for download links or success message
└── static/
    ├── css/
    │   └── style.css        # CSS for styling
```

## Installation
To run this project, ensure you have Python installed on your machine. Install the required libraries using the following command:

```bash
pip install Flask pycryptodome win10toast
```

## Usage
1. Clone the repository or download the project files.
2. Navigate to the project folder and run the following command:
   ```bash
   python app.py
   ```
3. Open your browser and go to `http://127.0.0.1:5000`.
4. Log in using the credentials:
   - Username: `root`
   - Password: `coderip321`
5. After logging in, wait for 5 to 10 seconds to load the AES Encryption Tool interface.

## About the Creator
This project is developed by **Coderip**, a passionate tech enthusiast focused on cybersecurity and innovative programming. For more information about my work, visit my [GitHub profile](https://github.com/coderip321).

## Contact Information
- **Email**: your-email@example.com
- **LinkedIn**: your-linkedin-profile

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
