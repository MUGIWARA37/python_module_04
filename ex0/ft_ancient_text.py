if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    file_name = "ancient_fragment.txt"

    try:
        print(f"Accessing Storage Vault: {file_name}")
        fi = open(file_name, "r")
        print("Connection established...\n")
        print(fi.read())
        fi.close()
        print("\nData recovery complete. Storage unit disconnected.")

    except FileNotFoundError:
        print("The file was not found.")

    except PermissionError:
        print("You don't have permission to read this file.")

    except OSError as e:
        print(f"An OS error occurred: {e}")
