# collision checker

Collision is not supported in Linux, it confuses the NSS process and it creates intermittent issues when user information is requested by `id` or `getent` or similar commands or using system calls like ` getpwnam()` etc.
This Python script is designed to detect this collisions between local linux system entries (such as usernames, UIDs, group names, and GIDs) and their counterparts in an LDAP (Lightweight Directory Access Protocol) integrated environment. The script checks for collisions across multiple LDAP integration methods (e.g., SSSD, Winbind, LDAP) to ensure the consistency of user and group information between the local system and LDAP.

# Features:

- Detects collisions for usernames, UIDs, group names, and GIDs.
- Supports multiple LDAP integration methods.
- Provides informative messages for detected collisions.
- Ensures data consistency between the local system and LDAP.

# Usage:

1. Ensure the script has the necessary permissions to read /etc/passwd and /etc/group.
2. The script must have executable permission.
`# chmod +x collision_checker.py`
4. Run the script to check for collisions with LDAP entries.
Example:

`$ python collision_checker.py`

# Note: 
This script is intended for systems integrated with LDAP, and it helps administrators maintain a clean and consistent user and group database.

Feel free to contribute, report issues, or suggest improvements!
