# cryptographyTool

An **educational** Python project designed to learn cryptography and cybersecurity. This tool encrypts and decrypts `.txt` files in a specified folder and its subfolders using the `cryptography` library.

**WARNING**: This project is for educational purposes only. Do not use it on files without explicit authorization. Unauthorized use may violate laws.

## Features
- Encrypts all `.txt` files in a folder and its subfolders, overwriting them with encrypted content.
- Generates a secure key (`chave.key`) for symmetric encryption using Fernet (AES-128).
- Decrypts the files using the same key, restoring their original content.
- Includes error handling and user input for folder paths to ensure safe operation.

## Prerequisites
- Python 3.6 or higher
- `cryptography` library:
  ```bash
  pip install cryptography
  ```

## How to Use
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your_username/cryptographyTool.git
   cd cryptographyTool
   ```
2. Run the encryption script:
   ```bash
   python crypto.py
   ```
   - Enter the full path of the folder containing `.txt` files (e.g., `C:\Users\Users\Documents\MyFolder`).
   - A `chave.key` file will be generated in the project directory.
3. Run the decryption script:
   ```bash
   python decrypt.py
   ```
   - Enter the same folder path and ensure `chave.key` is in the project directory.
4. **Backup**: Always back up your files before encrypting, as the original content is overwritten.

## Project Structure
- `crypto.py`: Script to encrypt `.txt` files in the specified folder and subfolders.
- `decrypt.py`: Script to decrypt `.txt` files using `chave.key`.
- `tests/`: Folder containing sample `.txt` files for testing.
- `LICENSE`: MIT License for the project.
- `README.md`: This documentation.

## Example
```bash
$ python crypto.py
*** cryptographyTool - Educational Encryption ***
WARNING: Make a backup before encrypting!
Enter the folder path (e.g., C:\Users\Users\Documents\MyFolder): C:\Users\Users\cryptographyTool\tests
Key generated and saved as 'chave.key'.
Encrypted: C:\Users\Users\cryptographyTool\tests\file1.txt
Encrypted: C:\Users\Users\cryptographyTool\tests\file2.txt
Encrypted: C:\Users\Users\cryptographyTool\tests\subfolder\file3.txt
Total .txt files encrypted: 3
Keep 'chave.key' safe to decrypt!
```

## Notes
- **Backup**: Always create a backup of your files before testing, as encryption overwrites the original content.
- **Key Safety**: Store `chave.key` securely. Without it, decryption is not possible.
- **Testing**: Use the provided `tests/` folder or create your own `.txt` files for safe experimentation.
- **Environment**: For added safety, test in a virtual machine (e.g., VirtualBox).

## Learning Resources
This project supports the following learning objectives:
- **Cryptography**: Understanding symmetric encryption with Fernet (AES-128).
- **Cybersecurity**: Ethically simulating file encryption/decryption, inspired by ransomware concepts for educational purposes.
- **Python**: File manipulation with `os.walk()`, error handling, and user input.



## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Legal Disclaimer
This project is intended for **educational purposes only**. The author is not responsible for any misuse. Using this tool to encrypt or decrypt files without permission is illegal and may violate local laws.

---
Created by [SuLzr1b] as part of a cybersecurity learning journey.
