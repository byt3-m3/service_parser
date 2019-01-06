from configparser.client import ParserClient

if __name__ == "__main__":
    c = ParserClient(host="192.168.99.100", port="50052")

    c.load_config("files/config.conf")

    # results = c.find_blocks(line_spec="interface", config=config)
    results = c.find_parents_w_child("interface GigabitEthernet1", "switchport access")
    print(results)

    results = c.find_parents_wo_child("interface GigabitEthernet1", "switchport access")
    print(results)

    results = c.find_lines("interface")
    print(results)

    results = c.find_blocks("hostname")
    print(results)

    if results.status == 200:
        print("Successful")
    elif results.status == 417:
        print("Error with database write")
