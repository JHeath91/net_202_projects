# Define the dictionaries
windows_servers = {'management01': '10.10.10.2', 'sccm01': '10.10.10.3', 'domaincontroller01': '10.10.10.4',
                  'domaincontroller02': '10.10.10.5', 'sql01': '10.10.10.6', 'exchange01': '10.10.10.7'}

linux_servers = {'application01': '10.10.20.2', 'ftp01': '10.10.20.3', 'vulnscanner01': '10.10.20.4',
                'ldap01': '10.10.20.5', 'dns01': '10.10.20.6', 'dns02': '10.10.20.7',
                'dhcp01': '10.10.20.8'}


# 1. Write a function to determine the number of Windows and Linux servers. Print the length of each.
def count_servers():
    num_windows_servers = len(windows_servers)
    num_linux_servers = len(linux_servers)
    print(f"Number of Windows servers: {num_windows_servers}")
    print(f"Number of Linux servers: {num_linux_servers}")


# 2. Write a function that adds a new Windows server to the windows_servers dictionary.
def add_windows_server(name, ip_address):
    windows_servers[name] = ip_address
    print("Updated windows_servers dictionary:")
    print(windows_servers)


# 3. Write a function that returns a single list of every single IP address assigned to a server (both Windows and Linux servers).
def get_all_ips():
    all_ips = list(windows_servers.values()) + list(linux_servers.values())
    print("List of all IP addresses:")
    print(all_ips)


# 4. Write a function that returns a single list of every single server name (both Windows and Linux servers).
def get_all_servers():
    all_servers = list(windows_servers.keys()) + list(linux_servers.keys())
    print("List of all server names:")
    print(all_servers)


count_servers()
add_windows_server('new_server', '10.10.10.8')
get_all_ips()
get_all_servers()

