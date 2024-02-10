 **README for hash_password_hack.py**

**Purpose:**

- Attempts to crack four-digit numeric passwords stored as SHA-256 hashes.
- Reads hashes and usernames from a CSV input file.
- Writes cracked passwords to a CSV output file.

**Usage:**

1. Save the script as `hash_password_hack.py`.
2. Install required libraries: `pip install hashlib csv`
3. Run from the command line: `python hash_password_hack.py input_file_name.csv output_file_name.csv`
    - Replace placeholders with actual file names.

**Input File Format:**

- CSV file with two columns:
    - First column: usernames (text)
    - Second column: corresponding SHA-256 password hashes (text)
- Example:

```csv
john.doe,2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
jane.smith,5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8
```

**Output File Format:**

- CSV file with two columns:
    - First column: usernames (text)
    - Second column: cracked passwords (numeric)
- Example:

```csv
john.doe,1234
jane.smith,5678
```

**Limitations:**

- Only attempts to crack four-digit passwords.
- Uses a brute force approach, which may be slow for larger password spaces.
- Does not consider salted hashes or more secure hashing algorithms.

**Ethical Considerations:**

- Use this script for educational or authorized security testing purposes only.
- Do not use it for malicious activities or without explicit permission.
- Respect password security guidelines and responsible disclosure practices.
