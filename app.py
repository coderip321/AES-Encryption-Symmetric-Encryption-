from flask import Flask, render_template, request, redirect, url_for, session, flash
import threading
import tkinter as tk
from tkinter import messagebox, filedialog
from Crypto.Cipher import AES
import os
from win10toast import ToastNotifier

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'uploads'

# Credentials
USERNAME = "root"
PASSWORD = "coderip321"

# Initialize ToastNotifier
toaster = ToastNotifier()

# AES Encryption Functionality
def encrypt_file(file_path, key):
    cipher = AES.new(key, AES.MODE_EAX)
    with open(file_path, 'rb') as f:
        plaintext = f.read()
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)

    # Write encrypted file
    with open(file_path + '.enc', 'wb') as f:
        f.write(cipher.nonce)
        f.write(tag)
        f.write(ciphertext)

def decrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        nonce, tag, ciphertext = [f.read(x) for x in (16, 16, -1)]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)

    # Write decrypted file
    with open(file_path[:-4], 'wb') as f:
        f.write(plaintext)

def show_aes_window():
    def encrypt():
        key = entry_key.get().encode('utf-8').ljust(16)  # Pad key
        if not selected_file.get():
            messagebox.showwarning("Warning", "Please select a file to encrypt.")
            return
        file_path = selected_file.get()
        encrypt_file(file_path, key)
        messagebox.showinfo("Success", "File encrypted successfully!")

    def decrypt():
        key = entry_key.get().encode('utf-8').ljust(16)  # Pad key
        if not selected_file.get():
            messagebox.showwarning("Warning", "Please select a file to decrypt.")
            return
        file_path = selected_file.get()
        decrypt_file(file_path, key)
        messagebox.showinfo("Success", "File decrypted successfully!")

    def select_file():
        file_path = filedialog.askopenfilename(title="Select a file")
        selected_file.set(file_path)

    # Initialize Tkinter window
    root = tk.Tk()
    root.title("AES Encryption Tool")
    root.geometry("400x300")

    label = tk.Label(root, text="Enter AES Key (16 chars):")
    label.pack(pady=10)

    entry_key = tk.Entry(root, width=40)
    entry_key.pack(pady=10)

    # Variable to hold the selected file path
    selected_file = tk.StringVar()

    # Select File button
    button_select = tk.Button(root, text="Select File", command=select_file)
    button_select.pack(pady=10)

    # Display selected file path
    label_selected_file = tk.Label(root, textvariable=selected_file, wraplength=350)
    label_selected_file.pack(pady=5)

    encrypt_button = tk.Button(root, text="Encrypt File", command=encrypt)
    encrypt_button.pack(pady=10)

    decrypt_button = tk.Button(root, text="Decrypt File", command=decrypt)
    decrypt_button.pack(pady=10)

    root.mainloop()

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    
    if username == USERNAME and password == PASSWORD:
        session['logged_in'] = True
        toaster.show_toast("Login Success", "You have logged into AES Encryption Tool", duration=10)
        return redirect(url_for('index'))
    else:
        flash('Incorrect username or password. Please try again.', 'error')  # Updated error message
        return redirect(url_for('login'))

@app.route('/index')
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/show-aes')
def show_aes():
    if session.get('logged_in'):
        threading.Thread(target=show_aes_window).start()
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    toaster.show_toast("Logout Success", "You have logged out from AES Encryption Tool", duration=10)
    flash('Logged out successfully.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
