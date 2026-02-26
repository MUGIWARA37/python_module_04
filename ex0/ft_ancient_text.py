if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    file_name = "ancient_fragment.txt"

    try:
        print(f"Accessing Storage Vault: {file_name}")
        fi = open(file_name, "r")
        print("Connection established...\n")
        print("RECOVERED DATA:")
        print(fi.read())
        fi.close()
        print("\nData recovery complete. Storage unit disconnected.")

    except FileNotFoundError:
        print("Error: Storage vault not found.")

    except PermissionError:
        print("Error: You don't have permission to read this file.")

    except OSError as e:
        print(f"Error an OS error occurred: {e}")
