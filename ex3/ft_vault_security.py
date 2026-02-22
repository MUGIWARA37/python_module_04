if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    try:
        print("Initiating secure vault access...")
        test = open("example_file.txt", "w")
        test.close()
    except Exception as e:
        print(e)
    else:
        print("Vault connection established with failsafe protocols")
        with open("example_file.txt", "w") as example:
            example.write("Quantum encryption keys recovered\n")
            print("[CLASSIFIED] Quantum encryption keys recovered")
            example.write("Archive integrity: 100%")
            print("[CLASSIFIED] Archive integrity: 100%")
        print()

    try:
        print("SECURE PRESERVATION:")
        with open("classified_data.txt", "r") as example:
            contents = example.read()
            for line in contents.split("\n"):
                print(f"  [CLASSIFIED] {line}")

    except Exception as e:
        print(e)

    print("\nAll vault operations completed with maximum security.")
