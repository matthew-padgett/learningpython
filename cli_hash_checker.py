import hmac
import hashlib

def get_file_hash():

    file_path = input("Enter the file path: ").strip()

    with open(file_path, "rb") as file: # "rb" = Read binary.
        file_hash = hashlib.file_digest(file, "sha256").hexdigest()
        return file_hash

def get_input_hash():

    input_hash = input("Enter in the SHA256 hash to compare with your file: ")
    return input_hash

def check_hash():

    file_hash = get_file_hash()
    input_hash = get_input_hash()

    checksums_match = hmac.compare_digest(file_hash, input_hash)

    return checksums_match, file_hash, input_hash

def print_result():

    green = "\033[32m"
    red = "\033[31m"
    bold = "\033[1m"
    reset = "\033[0m"

    checksums_match, file_hash, input_hash = check_hash()

    if checksums_match:
        print(f"{green}{bold}PASSED:{reset} Checksums match!")
        print(f"{green}{file_hash}{reset}")
        print(f"{green}{input_hash}{reset}")
    else:
        print(f"{red}{bold}!WARNING!:{reset} Checksums DO NOT match!")
        print(f"{red}{file_hash}{reset}")
        print(input_hash)

def main():
    print_result()

if __name__ == "__main__":
    main()