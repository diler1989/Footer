import os,sys

print("------------------------------")
print("|        FooTer  v1.1        |")
print("------------------------------")

#global variables
awk="awk -F'/' '/open/{print $1}'"


def port_scan(ip):
    os.system("mkdir {}/port_scan".format(ip))
    print("------------------------------")
    print("|          PoRt ScaN         |")
    print("------------------------------")
    print("[Nmap quick:] start")
    os.system("nmap -o {}/port_scan/nmap_quick {}".format(ip,ip))
    print("[Nmap quick:] stop\n")

    print("[Nmap long:] start")
    os.system("nmap -sC -sV -oX {}/port_scan/nmap_long.xml {}".format(ip,ip))
    print("[Nmap long:] stop\n")
    
    print("[Nmap UDP T/N:]")
    udp = input(">")
    if udp == "T":
        print("[Nmap long:] start")
        os.system("nmap -sU {}".format(ip))
        print("[Nmap long:] stop\n")
    else:
        print("[Nmap finish]")
    #print("[Nmap all port:] start")
    #os.system("nmap -p- -o {}/port_scan/nmap_port {}".format(ip,ip))
    #print("[Nmap all port:] stop")

def banner_grab(ip):
    print("------------------------------")
    print("|      BannEr GraBBing       |")
    print("------------------------------")	
    os.system("cat {}/port_scan/nmap_quick | {} >{}/port_scan/banner_port".format(ip,awk,ip))
    os.system("while read port; do nc -v {} $port; done <{}/port_scan/banner_port".format(ip,ip))


def web_scan(ip):
    os.system("mkdir {}/web_scan".format(ip))
    print("------------------------------")
    print("|          WeB ScaN          |")
    print("------------------------------")

    print("[Dirb:] start")
    os.system("dirb http://{} -o {}/web_scan/dirb.out".format(ip,ip))
    print("[Dirb:] stop\n")  

    print("[Nikto:] start")
    os.system("nikto -h http://{} > {}/web_scan/nikto.out".format(ip,ip))
    print("[Nikto:] stop\n")

    print("[Gobuster:] start")
    os.system("gobuster -u http://{} -w /usr/share/dirb/wordlists/common.txt -o {}/web_scan/gobuster.out".format(ip,ip))
    print("[Gobuster:] stop\n")
 
def exploit_suggest(ip):
    os.system("mkdir {}/searchsploit".format(ip))
    print("------------------------------")
    print("|        ExPlOiT ScaN        |")
    print("------------------------------")
    print("[Searchsploit:] start")
    os.system("searchsploit --exclude='/dos/' --nmap {}/port_scan/nmap_long.xml".format(ip))
    print("[Searchsploit:] stop")

def main(ip):
    port_scan(ip)
    #banner_grab(ip)
    exploit_suggest(ip)
    web_scan(ip)


try:
    ip=sys.argv[1]
    os.system("mkdir {}".format(ip))
    main(ip)  
except:
    print("Usage: python3 footer.py xx.xx.xx.xx")     
