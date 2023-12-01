import subprocess

#Maintainer: Nikhil Suryawanshi <suryawanshin74@gmail.com>

def get_local_usernames():
    try:
        with open("/etc/passwd", "r") as passwd_file:
            usernames = [line.split(":")[0] for line in passwd_file]
        return usernames
    except FileNotFoundError:
        print("Error: /etc/passwd file not found.")
        return []

def get_local_uids():
    try:
        with open("/etc/passwd", "r") as passwd_file:
            uids = [line.split(":")[2] for line in passwd_file]
        return uids
    except FileNotFoundError:
        print("Error: /etc/passwd file not found.")
        return []

def get_local_group_names():
    try:
        with open("/etc/group", "r") as group_file:
            group_names = [line.split(":")[0] for line in group_file]
        return group_names
    except FileNotFoundError:
        print("Error: /etc/group file not found.")
        return []

def get_local_gids():
    try:
        with open("/etc/group", "r") as group_file:
            gids = [line.split(":")[2] for line in group_file]
        return gids
    except FileNotFoundError:
        print("Error: /etc/group file not found.")
        return []

def getent_command(ldap_integration_method, type_str):
    return f"getent {type_str} -s {ldap_integration_method}"

def check_collision(entry, ldap_integration_methods, type_str, conflict_msg, no_collision_msg):
    collision_detected = False
    for ldap_integration_method in ldap_integration_methods:
        getent_cmd = getent_command(ldap_integration_method, type_str)
        output = subprocess.getoutput(f"{getent_cmd} {entry}")
        if output:
            print(conflict_msg.format(entry, ldap_integration_method))
            collision_detected = True
    return not collision_detected

def main():
    local_usernames = get_local_usernames()
    local_uids = get_local_uids()
    local_group_names = get_local_group_names()
    local_gids = get_local_gids()

    if not local_usernames or not local_uids or not local_group_names or not local_gids:
        return

    ldap_integration_methods = ["sss", "winbind", "ldap"]

    print(f"LDAP Integration Methods: {', '.join(ldap_integration_methods)}")

    no_collision_detected_usernames = all(check_collision(username, ldap_integration_methods, "passwd", "Collision of username '{}' detected in LDAP integration method '{}', collision is not supported.", "") for username in local_usernames)

    if no_collision_detected_usernames:
        print("No collision detected for any username.")

    no_collision_detected_uids = all(check_collision(uid, ldap_integration_methods, "passwd", "Collision of UID '{}' detected in LDAP integration method '{}', collision is not supported.", "") for uid in local_uids)

    if no_collision_detected_uids:
        print("No collision detected for any UID.")

    no_collision_detected_group_names = all(check_collision(group_name, ldap_integration_methods, "group", "Collision of group name '{}' detected in LDAP integration method '{}', collision is not supported.", "") for group_name in local_group_names)

    if no_collision_detected_group_names:
        print("No collision detected for any group name.")

    no_collision_detected_gids = all(check_collision(gid, ldap_integration_methods, "group", "Collision of GID '{}' detected in LDAP integration method '{}', collision is not supported.", "") for gid in local_gids)

    if no_collision_detected_gids:
        print("No collision detected for any GID.")

if __name__ == "__main__":
    main()
