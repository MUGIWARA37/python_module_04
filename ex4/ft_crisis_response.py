def crisis_handler(filename: str) -> None:
    try:
        with open(filename, "r") as archive:
            content = archive.read()
            print(f"\nROUTINE ACCESS: Attempting access to '{filename}'...")
            print(f"SUCCESS: Archive recovered - {content.strip()}")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print(f"\nCRISIS ALERT: Attempting access to '{filename}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print(f"\nCRISIS ALERT: Attempting access to '{filename}'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception as e:
        print(f"\nCRISIS ALERT: Attempting access to '{filename}'...")
        print(f"RESPONSE: Unexpected system anomaly detected - {e}")
        print("STATUS: Crisis handled, anomaly contained")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    crisis_handler("lost_archive.txt")
    crisis_handler("classified_vault.txt")
    crisis_handler("standard_archive.txt")

    print("\nAll crisis scenarios handled successfully. Archives secure.")
