# Hashcat Parameters Explained (Basic Overview)

## Basic Command Structure

```bash
hashcat [options] <hashfile> <mask/wordlist/directory>
```

### 1. General Options

```bash
-m <num>          : Hash type (e.g., 0=MD5, 1000=NTLM, 2500=WPA/WPA2)
                    * Must come early in command
                    * Full list: [Hashcat Example Hashes](https://hashcat.net/wiki/doku.php?id=example_hashes)

-a <num>          : Attack mode:
                    - 0 = Dictionary (default)
                    - 1 = Combinator
                    - 3 = Brute-force
                    - 6 = Hybrid (Wordlist + Mask)
                    - 7 = Hybrid (Mask + Wordlist)

-o <file>         : Output file for cracked passwords
--force           : Ignore warnings/errors (not recommended)
--version         : Show version info
--help            : Show basic help
-V                : Verbose output
-q                : Quiet mode (less output)
```

### 2. Performance Options

```bash
-w <num>          : Workload profile (1-5):
                    - 1 = Low    (Default)
                    - 3 = Medium
                    - 4 = High
                    - 5 = Nightmare (may lock up PC)

-n <num>          : Thread count (for CPU-only attacks)
-u <num>          : Select specific GPU devices (e.g., -u 1)
```

### 3. Output Options

```bash
--show            : Show cracked passwords from potfile
--outfile-format <num> : Format for output file:
                    - 1 = hash:password
                    - 2 = plain passwords only
                    - 3 = hash:password:hex_salt
```

### 4. Session Management

```bash
--session <name>  : Save/Resume session
--restore         : Restore previous session
```

### 5. Rule Options

```bash
-r <file.rule>    : Use rule file for word mutations
                   (Common rules: best64.rule, dive.rule)
```

### 6. Miscellaneous

```bash
--status          : Show real-time status updates
--potfile-path    : Custom potfile location (stores cracked hashes)
```

## Common Examples

1. **Dictionary attack:**

```bash
hashcat -m 0 -a 0 hashes.txt wordlist.txt
```

2. **Brute-force 4-digit PIN:**

```bash
hashcat -m 0 -a 3 hashes.txt ?d?d?d?d
```

3. **Show cracked passwords:**

```bash
hashcat -m 0 hashes.txt --show
```

## Notes

- Most options go **BEFORE** the hash file.
- Attack-specific parameters (masks/wordlists) come **AFTER** the hash file.
- Always check documentation for your specific hash type/attack mode.

For full details: `hashcat --help`

```
hashcat -m 0 hashes.txt --show
```

## Notes

- Most options go **BEFORE** the hash file.
- Attack-specific parameters (masks/wordlists) come **AFTER** the hash file.
- Always check documentation for your specific hash type/attack mode.

For full details: `hashcat --help`
