def data_writing(file_name: str) -> None:
    data_list = [
        "New quantum algorithm discovered",
        "Efficiency increased by 347%",
        "Archived by Data Archivist trainee"
    ]
    print("\nInscribing preservation data...")
    f = open(file_name, 'w')
    i = 1
    for line in data_list:
        f.write(line)
        f.write("\n")
        print(f"[ENTRY 00{i}] {line}")
        i += 1
    f.close()
    print("\nData inscription complete. Storage unit sealed.")
    print(f"Archive '{file_name}' ready for long-term preservation.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    file_name = 'new_discovery.txt'
    try:
        print(f"Accessing Storage Vault: {file_name}")
        test = open(file_name, 'w')
        test.close()
    except PermissionError:
        print(f"You don't have the permission to write in {file_name}")
    except OSError as e:
        print(f"An OS error occurred: {e}")
    else:
        print("Connection established...")
        data_writing(file_name)
