if __name__ == "__main__":

    try:
        print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
        print("Initiating secure vault access...")
        print("Vault connection established with failsafe protocols")
        with open("classified_data.txt", "w") as example:
            example.write("[CLASSIFIED] Quantum encryption keys recovered\n"
                          "[CLASSIFIED] Archive integrity: 100%")
        with open("classified_data.txt", "r") as example:
            print(example.read())
        print()
        print("SECURE PRESERVATION:")
        with open("security_protocols.txt", "r") as example:
            print(example.read())
            print("Vault automatically sealed upon completion")

        print("\nAll vault operations completed with maximum security.")

    except Exception as e:
        print(e)
