if __name__ == "__main__":

    try:
        print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
        print("Initiating secure vault access...")
        print("Vault connection established with failsafe protocols")
        with open("example_file.txt", "w") as example:
            example.write("Quantum encryption keys recovered\n")
            print("[CLASSIFIED] Quantum encryption keys recovered")
            example.write("Archive integrity: 100%")
            print("[CLASSIFIED] Archive integrity: 100%")
        print()
        print("SECURE PRESERVATION:")
        with open("classified_data.txt", "r") as example:
            print(example.read())

        print("\nAll vault operations completed with maximum security.")

    except Exception as e:
        print(e)
