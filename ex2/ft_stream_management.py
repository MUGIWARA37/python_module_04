import sys

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    input_ar = input("Input Stream active. Enter archivist ID: ")
    input_rep = input("Input Stream active. Enter status report: ")
    print()

    print(f"[STANDARD] Archive status from {input_ar}: {input_rep}")
    print("[ALERT] System diagnostic: Communication channels verified",
          file=sys.stderr)
    print("[STANDARD] Data transmission complete\n")

    print("Three-channel communication test successful.")
