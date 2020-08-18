import os
os.system ("clear")

print("                    Hello dear, Wolcome to Mr Kali Hacking tool")
import Banner
print("                               created by Mr kali")
print("                            instagram: mr_kali_official")
print("                             Youtube channel: Mr kali")
passwd = ("Mr_Kali")
print('                                password: ' + passwd)
#Login
password = input('                            Please Type The Password tool: \n                                     ')
if password == passwd:
    print("                                      Ok Done....")
    print('                         ----Welcome To Mr Kali Tool----')
else:
    print("Sorry but Your password is Wrong,Try again :)")
    exit('hope to see you Hacking :)')
#----------------------------------------------------------------------------------------
import skull
#----------------------------------------------------------------------------------------
print("\n \033[0;34m[1]Install Hacking Tools ")
print("\n \033[0;34m[2]Update & Upgrade Termux ")
print("\n \033[0;34m[3]Update & Upgrade Kali Linux ")
print("\n \033[0;34m[4]Exit ")
nm = input ("\n Select a Number > ")
if nm == "1":
    print("  \033[0;32m          tool + Termux = Work only with Termux and for kali linux users\n\033[0;32m                            tool = Work only on Kali Linux")
    print ("\n \033[0;34m[1] Metasploit Termux:\033[0;37m Powerful exploitation tool")
    print ("\n \033[0;94m[2] \033[0;34m sqlmap Termux:\033[0;37m websites vunirabilities scanner")
    print ("\n \033[0;34m[3] AdvPhishing Termux:\033[0;37m Powerful phishing tools")
    print ("\n \033[0;34m[4] Nmap Termux:\033[0;37m Hacking Tool, it is widely used by Hackers, Pentesters, Security Researchers,")
    print ("\n \033[0;34m[5] Hydra Termux:\033[0;37m hydra is a powerful brute force tool to guess and crack valid passwords")
    print ("\n \033[0;34m[6] Social Engineer Tool Termux:\033[0;37m Social engineer tool is a powerful tool to perform several social engineering attacks, including spoofing and more")
    print ("\n \033[0;34m[8] Xerxes DDoS Tool Termux:\033[0;37m Xerxes is a powerful DDoS tool ")
    print ("\n \033[0;34m[9] instabrute install Termux:\033[0;37m Powerful Instagram bruteforce")
    print ("\n \033[0;34m[10]Bombers:\033[0;37m SMS/Email/whatsapp Bombers/spammer Collection. ")
    print ("\n \033[0;34m[11]Sherlock:\033[0;37m Find Any Social media account with this tool ")
    print ("\n \033[0;34m[12]Admin-Page-Finder:\033[0;37m powerful tool to find admin control panels websites ")
    print ("\n \033[0;34m[13]evillimiter:\033[0;37m kick or analyze wifi with this Powerful tool ")
    print ("\n \033[0;34m[14]quack:\033[0;37m Powerful tool for sms bomber and HTTP/TCP attacks")
    print ("\n \033[0;34m[15]seeker Termux:\033[0;37m Locate phones Location with this tool")
    print ("\n \033[0;34m[16]seeker:\033[0;37m Locate phones Location with this tool")
    print ("\n \033[0;34m[00]Ghost : Powerful Ip Exploitation tool ")
    print ("\n \033[0;34m[00]exit ")
#update & upgrade Termux
if nm == "2":
    os.system("apt update")
    os.system("apt upgrade")
    os.system("apt-get update")
    os.system("apt-get upgrade")
    os.system("pkg update ")
    os.system("pkg upgrade")
#update & upgrade Kali Linux
if nm == "3":
    os.system("sudo apt update")
    os.system("sudo apt upgrade")
    os.system("sudo apt-get update")
    os.system("sudo apt-get upgrade")
#exit
if nm == "4":
    exit("\033[0;32mThanks For Using My Tool ^^")
#-----------------------------------------------------------------------------------
num = input ("\033[0;36mChoose a Number: ")
#metasploit install Termux
if num == "1":
    os.system("pkg update && pkg upgrade -y")
    os.system("pkg install git ")
    os.system("pkg install python ")
    os.system("cd $HOME")
    os.system("pkg install wget")
    os.system("wget https://Auxilus.github.io/metasploit.sh")
    os.system("bash metasploit.sh")
    os.system("msfconsole")
    print ("\033[0;32mType :'msfconsole' To run the tool")
#sqlmap install Termux
if num == "2":
    os.system("pkg update && pkg upgrade -y")
    os.system("pkg install git ")
    os.system("pkg install python ")
    os.system("cd ")
    os.system("git clone https://github.com/sqlmapproject/sqlmap.git ")
    print ("\033[0;32mType :'cd sqlmap'after type 'python2 sqlmap.py' To run the tool")
#AdvPhishing install Termux
if num == "3":
    os.system("pkg update && pkg upgrade ")
    os.system("pkg install git ")
    os.system("pkg install python ")
    os.system("cd ")
    os.system("git clone https://github.com/Ignitetch/AdvPhishing.git")
    print("\033[0;32mType: 'cd AdvPhishing'after type'chmod 777 start.sh' and './start.sh in the final './An-AdvPhishing.sh' to run the tool")
#nmap install termux
if num == "4":
    os.system("pkg update && pkg upgrade -y")
    os.system("pkg install git ")
    os.system("pkg install python ")
    os.system("pkg install curl")
    os.system("cd ")
    os.system("pkg install nmap")
    print("\033[0;32mType: 'nmap'to run the tool ")
#Hydra install Termux
if num == "5":
    os.system("pkg update && pkg upgrade -y")
    os.system("pkg install git ")
    os.system("pkg install python ")
    os.system("cd ")
    os.system("pkg install hydra")
    print("\033[0;32mType: 'hydra' to run the tool")
#Social Engineer Tool install termux
if num == "6":
    os.system("pkg update && pkg upgrade -y")
    os.system("pkg install git ")
    os.system("pkg install python ")
    os.system("pkg install curl")
    os.system("cd ")
    os.system("curl -LO https://raw.githubusercontent.com/Hax4us/setoolkit/master/setoolkit.sh")
    os.system("sh setoolkit.sh ")
    print("\033[0;32mType: 'cd setoolkit'after Type './setup.py' finally Type './setoolkit'")
#Xerxes DDoS Tool install termux
if num == "7":
    os.system("pkg update && pkg upgrade -y")
    os.system("pkg install git ")
    os.system("pkg install python ")
    os.system("cd ")
    os.system("git clone https://github.com/zanyarjamal/xerxes")
    os.system("clang xerxes.c -o xerxes")
    print("\033[0;32mNow you can run Xerxes by typing 'cd xerxes'after type './xerxes'")
#AK47 Facebook Brute Forcing Tool install Termux
if num == "8":
    os.system("pkg update && pkg upgrade -y")
    os.system("pkg install git ")
    os.system("pkg install python2 ")
    os.system("cd ")
    os.system("git clone https://github.com/nasirxo/AK47")
    print("\033[0;32mType: 'cd AK47'after type 'chmod +x *'finally type 'python2 ak47.py' ")
#instabrute install Termux
if num == "9":
    os.system("pkg update && pkg upgrade -y")
    os.system("pkg install git ")
    os.system("pkg install python ")
    os.system("pip install requests")
    os.system("pip install bs4")
    os.system("cd ")
    os.system("git clone https://github.com/TERMUXID3/instabrute")
    print("\033[0;32mType: 'cd instabrute'after type 'python run.py'")
#Bombers install Termux
if num == "10":
    os.system("pkg update && pkg upgrade -y")
    os.system("pkg install git ")
    os.system("pkg install python ")
    os.system("cd ")
    os.system("git clone https://github.com/bhattsameer/Bombers.git")
    print("\033[0;32mType: 'cd Bombers'after type 'python SMS_bomber.py'or any commande you would execute it")
#Sherlock install 
if num == "11":
    os.system("pkg update && pkg upgrade -y")
    os.system("pkg install git ")
    os.system("pkg install python ")
    os.system("cd ")
    os.system("git clone https://github.com/sherlock-project/sherlock.git")
    print("\033[0;32mType: 'cd sherlock'after Type 'python3 -m pip install -r requirements.txt' and you are done use it with 'python3 sherlock --help'")
#Admin-Page-Finder install
if num == "12":
    os.system("pkg update && pkg upgrade -y")
    os.system("pkg install git ")
    os.system("pkg install python ")
    os.system("cd ")
    os.system("git clone https://github.com/The404Hacking/Admin-Page-Finder.git")
    print("\033[0;32mType 'cd admin-page-finder' after type 'python admin-page-finder.py' to run it")
#evillimiter install
if num == "13":
    os.system("pkg update && pkg upgrade -y")
    os.system("pkg install git ")
    os.system("pkg install python ")
    os.system("cd ")
    os.system("git clone https://github.com/bitbrute/evillimiter.git")
    print("\033[0;32mType 'cd evillimiter' after type 'sudo python3 setup.py install' to install requirements and finally type 'evillimiter' run it")
#quack install
if num == "14":
    os.system("pkg update && pkg upgrade -y")
    os.system("pkg install git ")
    os.system("pkg install python ")
    os.system("cd ")
    os.system("git clone https://github.com/entynetproject/quack.git")
    print("\033[0;32mType 'cd quack' after type 'chmod +x install.sh' and './install.sh' to install requirements and finally type 'quack' run it")
#Seeker Install Termux
if num == "15":
    os.system("pkg update && pkg upgrade -y")
    os.system("pkg install git ")
    os.system("pkg install python ")
    os.system("cd ")
    os.system("git clone https://github.com/thewhiteh4t/seeker.git")
    print("\033[0;32mType 'cd seeker'after type 'chmod 777 termux_install.sh'and finally './termux_install.sh' to run it 'python3 seeker.py -h'")
#seeker install
if num == "16":
    os.system("pkg update && pkg upgrade -y")
    os.system("pkg install git ")
    os.system("pkg install python ")
    os.system("cd ")
    os.system("git clone https://github.com/thewhiteh4t/seeker.git")
    print("\033[0;32mType 'cd seeker'after type 'chmod 777 termux_install.sh'and finally './install.sh' to run it 'python3 seeker.py -h'")
#ghost install
os.system("pkg update && pkg upgrade -y")
    os.system("pkg install git ")
    os.system("pkg install python ")
    os.system("cd")
    os.system("https://github.com/entynetproject/ghost.git")
    print("\033[0;32mType 'cd ghost' after Type'chmod +x install.sh' after './install.sh' and to run it Type 'ghost' ")
#Exit
if num == "00":
    exit("\033[0;32mThanks For Using My Tool ^^")
