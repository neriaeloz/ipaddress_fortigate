def main():
    output_file = "fortigate_commands.txt"
    group_name = "VPN_Group"

    with open(output_file, "w") as f:
        while True:
            ip = input("Enter IP address (or press Enter to finish): ").strip()
            if ip == "":
                break

            # Replace / with - for object name compatibility
            obj_name = ip.replace("/", "-")

            f.write("config firewall address\n")
            f.write(f"    edit \"{obj_name}\"\n")
            f.write(f"        set subnet {ip} 255.255.255.255\n")
            f.write("    next\n")
            f.write("end\n\n")

            f.write("config firewall addrgrp\n")
            f.write(f"    edit \"{group_name}\"\n")
            f.write(f"        append member \"{obj_name}\"\n")
            f.write("    next\n")
            f.write("end\n\n")

    print(f"\n✅ Commands saved to {output_file}")


if __name__ == "__main__":
    main()
