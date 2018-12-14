def show_info_xssposed():
    print("  Name: XSSposed Domain Lookup")
    print("  Path: modules/recon/domains-vulnerabilities/xssposed.py")
    print("Author: Tim Tomes (@LaNMaSteR53)")

show_info   =   input("[recon-ng][default][xssposed] > ")

if show_info  == "show info":
        show_info_xssposed()

        print("\nDescription: ")
        print("\tCheck XSSposed.com for XSS record associated with a domain.")
        print("\nOptions:")
        print("\tName    \tCurrent Value \tRequired  \tDescription")
        print("\t------  \t------------- \t--------  \t-----------")
        print("\tSOURCE  \tdefault       \tyes       \tsource of input (see 'show info' for details")
else:
    print("Opción invalida")