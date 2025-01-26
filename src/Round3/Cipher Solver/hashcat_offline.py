import os

def get_hashcat_command():
    print("""
    ==============================================
    Hashcat Command Builder - Offline Hash Cracking
    ==============================================
    This tool will help you build a Hashcat command step by step.
    Please provide the following information:
    """)

    # Initialize command parts
    command_parts = ['hashcat']

    # Hash Type (-m)
    print("\n[1/8] Hash Type (-m)")
    print("""Specify the hash type you're attacking.
    Common examples:
    0   = MD5
    1000 = NTLM (Windows)
    1800 = SHA-512 (Unix)
    2500 = WPA/WPA2
    3200 = bcrypt
    (See https://hashcat.net/wiki/doku.php?id=example_hashes for full list)""")
    while True:
        try:
            hash_mode = int(input("Enter hash type number: ").strip())
            break
        except ValueError:
            print("Please enter a valid number")
    command_parts.extend(['-m', str(hash_mode)])

    # Attack Mode (-a)
    print("\n[2/8] Attack Mode (-a)")
    print("""Choose attack type:
    0 = Straight (Dictionary attack)
    1 = Combination
    3 = Brute-Force/Mask
    6 = Hybrid Wordlist + Mask
    7 = Hybrid Mask + Wordlist
    (See hashcat --help for all options)""")
    while True:
        try:
            attack_mode = int(input("Enter attack mode number: ").strip())
            break
        except ValueError:
            print("Please enter a valid number")
    command_parts.extend(['-a', str(attack_mode)])

    # Hash File
    print("\n[3/8] Hash File")
    print("Path to file containing hashes to crack")
    while True:
        hash_file = input("Enter hash file path: ").strip()
        if os.path.exists(hash_file):
            break
        print(f"File not found: {hash_file}. Please check path.")

    # Attack Parameters
    print("\n[4/8] Attack Parameters")
    attack_params = []
    if attack_mode == 0:
        print("Dictionary Attack: Path to wordlist file")
        while True:
            wordlist = input("Enter wordlist path: ").strip()
            if os.path.exists(wordlist):
                attack_params.append(wordlist)
                break
            print(f"File not found: {wordlist}")
    elif attack_mode == 3:
        print("Mask Attack: Define character set and pattern")
        print("Example: ?a?a?a?a for 4-character mixed attack")
        mask = input("Enter mask pattern: ").strip()
        attack_params.append(mask)
    else:
        print(f"Attack mode {attack_mode} requires specific parameters")
        params = input("Enter required parameters (space-separated): ").strip()
        attack_params.extend(params.split())

    # Output File (-o)
    print("\n[5/8] Output File (optional)")
    print("Where to save cracked hashes (leave blank for none)")
    output_file = input("Enter output file path: ").strip()
    if output_file:
        command_parts.extend(['-o', output_file])

    # Rules (-r)
    print("\n[6/8] Rule Files (optional)")
    print("Rules modify words from wordlists (e.g., append numbers)")
    while True:
        rule = input("Enter rule file path (or blank to finish): ").strip()
        if not rule:
            break
        if os.path.exists(rule):
            command_parts.extend(['-r', rule])
        else:
            print(f"File not found: {rule}")

    # Workload (-w)
    print("\n[7/8] Workload Profile (-w)")
    print("""System performance vs responsiveness:
    1 = Low resource usage
    2 = Default balance
    3 = High performance (default)
    4 = Max power (may lock system)""")
    workload = input("Enter workload (1-4, default 3): ").strip() or '3'
    command_parts.extend(['-w', workload])

    # Advanced Options
    print("\n[8/8] Advanced Options")
    if input("Force attack even if unsafe? (y/n): ").lower() == 'y':
        command_parts.append('--force')
    if input("Hashes include usernames? (y/n): ").lower() == 'y':
        command_parts.append('--username')

    # Build final command
    command_parts.append(hash_file)
    command_parts.extend(attack_params)
    
    return ' '.join(command_parts)

if __name__ == "__main__":
    command = get_hashcat_command()
    print("\nYour Hashcat command is ready:")
    print(f"\n{command}\n")
    print("To execute, copy and paste this command in your terminal.")
    print("Note: Always test commands in a safe environment first!")