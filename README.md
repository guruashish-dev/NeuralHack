# NeuralHack

## 📜 **Description**
This project demonstrates how brute-force techniques work by incrementally cracking a password character by character. It is designed for **educational purposes only** and highlights the importance of strong password practices. 

> **Disclaimer:** This tool is for learning and controlled testing environments only. Unauthorized use of brute-force techniques is illegal and unethical.

---

## 🛠️ **Features**
- Cracks passwords incrementally, character by character.
- Supports alphanumeric characters and special symbols.
- Provides real-time feedback on progress.
- Displays the time taken to crack the password.

---

## 🚀 **Usage**

### **1. Prerequisites**
- Python 3.9.6 installed on your system.
- Basic knowledge of Python and file handling.

### **2. Project Setup**
1. Clone or download this repository:
   ```bash
   git clone https://github.com/guruashish-dev/NeuralHack.git
   cd NeuralHack
   ```
2. Create a `credentials.txt` file with the following format:
   ```plaintext
   <username>
   <password>
   ```
   Example:
   ```plaintext
   testuser
   Abc123!@
   ```

### **3. Run the Program**
Copy the directory from the file and then type
```bash
cd C:\Users\Your device name\file location
```
Them execute the script in the terminal:
```bash
python brutecode.py
```
This is for the first version of the script
type this if you want to run the first version of the code(no alphanumeric and no special characters)
```bash
python brutecodev2.py
```
### **4. Observe Output**
The program will:
- Read the username and password from `credentials.txt`.
- Incrementally brute-force the password, character by character.
- Print the cracked password and the time taken.
- ![image](https://github.com/user-attachments/assets/6948eb0d-cad7-497e-aeed-c8221ccfe2e4)


Example output:
```plaintext
Password cracked in 0.05 seconds.
Password cracked successfully!
Username: testuser, Password: Abc123!@
```

---

## ⚙️ **How It Works**
1. The program reads the username and password from the `credentials.txt` file.
2. Using a character set (letters, digits, and symbols), it brute-forces each position in the password incrementally.
3. The program stops when the full password is cracked.

---

## 📖 **Character Set**
The program uses the following character set:
- **Lowercase Letters:** a-z
- **Uppercase Letters:** A-Z
- **Digits:** 0-9
- **Special Characters:** `!@#$%^&*()_+-=[]{}|;':",.<>?/`

You can modify the character set by editing the `character_set` variable in `bruteforce.py`:
```python
character_set = string.ascii_letters + string.digits + string.punctuation
```

---

## 🛡️ **Disclaimer**
***This project is strictly for **educational purposes** and should only be used in controlled environments. Unauthorized use of brute-force techniques can lead to legal consequences. Always obtain proper permissions before testing any system.***

---

## 📜 **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🌟 **Contributing**
Contributions are welcome! Feel free to:
- Submit bug reports and feature requests.
- Fork the repository and submit a pull request with enhancements.

---

## 💬 **Feedback**
If you have any questions or suggestions, feel free to reach out via [GitHub Issues](https://github.com/guruashish-dev/NeuralHack/issues).
