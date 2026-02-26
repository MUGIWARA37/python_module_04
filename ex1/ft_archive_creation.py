def data_writing(file_name: str) -> None:
    data_list = [
        "[ENTRY 001] New quantum algorithm discovered",
        "[ENTRY 002] Efficiency increased by 347%",
        "[ENTRY 003] Archived by Data Archivist trainee"
    ]

    f = open(file_name, 'w')

    print("Storage unit created successfully...")
    print("\nInscribing preservation data...")

    for line in data_list:
        f.write(line)
        f.write("\n")
        print(line)

    f.close()
    print("\nData inscription complete. Storage unit sealed.")
    print(f"Archive '{file_name}' ready for long-term preservation.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    file_name = 'new_discovery.txt'
    try:
        print(f"Accessing Storage Vault: {file_name}")
        data_writing(file_name)
    except PermissionError:
        print(f"You don't have the permission to write in {file_name}")
    except OSError as e:
        print(f"An OS error occurred: {e}")
