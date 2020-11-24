import webbrowser as wb
import speech_recognition as sr
import pyttsx3
import os                                         # os module for linux commands
from pyfiglet import Figlet                       #figlet library for banner fonts
#import subprocess as sp
from termcolor import colored
import getpass




def dockerconf():
    global ip
    print("-----------DOCKER----------")
    print("1. Docker daemon start/stop/status")
    print("2. Show docker process")
    print("3. Show docker images")
    print("4. Download imag on docker.")
    print("5. Launch O.S on docker hub")
    print("7. Stop docker container")
    print("8. Delete docker image")
   
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            pyttsx3.speak("start speaking...and tell me next.")
            print("I am capturing Your requirement..")
            audio = r.listen(source)
            print("Your requirement is captured.")
        select = r.recognize_google(audio)
        if ("start" in select):
            os.system('ssh root@{} systemctl start docker'.format(ip))
        elif ("stop" in select):
                os.system('ssh root@{} systemctl stop docker'.format(ip))
        elif ("status" in select):
                os.system('ssh root@{} sytemctl status docker'.format(ip))
        elif ("recent" in select):
                os.system('ssh root@{} docker ps'.format(ip))
        elif ("all" in select):
                os.system('ssh root@{} docker ps -a'.format(ip))
        elif ("images" in select):
            os.system('ssh root@{} docker images'.format(ip))
        elif ("download" in select):
            im = input('image name - ')
            os.system('ssh root@{0} docker pull {1}'.format(ip,im))
        elif ("launch" in select):
            im = input('image name - ')
            os.system('ssh root@{0} docker run -it {1} &'.format(ip,im))
        elif ("container" in select):
            im = input('image name - ')
            os.system('ssh root@{0} docker stop {1}'.format(ip,im))
        elif ("delete" in select):
            im = input('image name - ')
            os.system('ssh root@{0} docker rmi {1}'.format(ip,im))
        elif ("thanks" in select):
            pyttsx3.speak("okay thank you for visiting")
            return
        else:
            print('Error')


def lvmconf():
    global ip
    os.system("ssh root@192.168.43.249 tput setaf 2")
    print("\t\t----------------------------------------")
    print("\t\t\t\tAVAILABLE MENUS")
    print("\t\t-----------------------------------------")
    os.system("ssh root@192.168.43.249 tput setaf 7")
    print("\t\t\t1. Check available disks")
    print("\t\t\t2. Create physical volumes(PV)")
    print("\t\t\t3. Create Volume Group (VG)")
    print("\t\t\t4. Create Logical volumes(LV)")
    print("\t\t\t5. Format the created LV")
    print("\t\t\t6. Mount the LV")
    print("\t\t\t7. Extend Volume Group")
    print("\t\t\t8. Format the extende volume")
    print("\t\t\t9. To display volume group.")
    print("\t\t\t0. to display Logical volume.")
    pyttsx3.speak("How I can help you ?")
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            pyttsx3.speak("start speaking...and tell me next.")
            print("I am capturing Your requirement..")
            audio = r.listen(source)
            print("Your requirement is captured.")
        select = r.recognize_google(audio)
        if ("disk" in select):
            p = os.system('ssh root@{} fdisk -l'.format(ip))
            print(p)
        elif ("pv" in select) and ("creat" in select):
            y = int(input("How many hard disks do you want to convert into PV:"))
            for i in range(y):
                r = str(i + 1)
                p = input("Enter the name of disk no " + r + " :")
                q = os.system("ssh root@{0} pvcreate {1}".format(ip,p))
                print(q)
                input()
        elif ("vg"in select) and ("creat" in select):
            a = input("Enter the name for volume group which is to be created :")
            b = input(
                "Enter name of physical volume (please separate the names by giving space if you want to give more than one):")
            s = os.system("ssh root@{0} vgcreate {1} {2} ".format(ip,a, b))

        elif (("Logical" in select) or ("LV" in select)) and ("creat" in select):
            e = input("Enter size for LV in (G/M/T):")
            d = input("Enter name for LV :")
            f = input("Enter name of created volume group: ")
            lv = os.system("ssh root@{0} lvcreate --size {1} --name {2} {3}".format(ip,e, d, f))
        elif ("format" in select) and ("lv" in select):
            vg_nm = input("Enter Created VG name :")
            lv_nm = input("Enter Created LV name :")
            frmt = os.system("ssh root@{0} mkfs.ext4 /dev/{1}/{2}".format(ip,vg_nm, lv_nm))
        elif ("mount" in select):
            vg = input("Enter created name of volume group.")
            ln = input("Enter Created LV name :")
            dr = input("Enter name to create directory:")
            os.system("ssh root@{0} mkdir /{1}".format(ip,dr))
            print("mounting your partition on created directory...")
            os.system("ssh root@{0} mount /dev/{1}/{2} /{3}".format(ip,vg, ln, dr))
            print("partition mounted successfully")
            input()
        elif ("extend" in select) and (("LV" in select) or ("logical" in select)):
            u = input("Howm much size do you want to extend ,Enter size in (G/M/T):")
            w = input("Enter name of created volume group: ")
            v = input("Enter name of created LV :")
            resize = os.system("ssh root@{0} lvextend --size +{1}  /dev/{2}/{3}".format(ip,u, w, v))
            print(resize)
            input()
        elif ("volume" in select):
            r_v = input("Enter name of created volume group: ")
            r_l = input("Enter name of created LV :")
            re_frmt = os.system("ssh root@{0} resize2fs /dev/{1}/{2}".format(ip,r_v, r_l))
            print(re_frmt)
            input()
        elif ("display" in select) and ("vg" in select):
            vgname = input("enter vg name:")
            v_disp = os.system("ssh root@{0} vgdisplay {1}".format(ip,vgname))
            print(v_disp)
            input()
        elif ("display" in select) and ("lv" in select):
            vgname2 = input("Enter vg name:")
            lvname = input("Enter lv name:")
            lv_display = os.system("ssh root@{0} lvdisplay {1}/{2}".format(ip,vgname2, lvname))
            print(lv_display)
            input()
        elif ("stop" in select):
            pyttsx3.speak("okay have a nice day")
        else:
            pyttsx3.speak("I am not getting to you.please tell me again.")
            print("I am not getting to you.")




def awsconf():
    While True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        pyttsx3.speak("start speaking...and tell me next.")
        print("I am capturing Your requirement..")
        audio = r.listen(source)
        print("Your requirement is captured.")

    select = r.recognize_google(audio)
    try:
        if ("can" in select) and ("help" in select):
            pyttsx3.speak("I can create key pair.")
            print("I can create key pair.")
            pyttsx3.speak("I can create securty group as well.")
            print("I can create securyity group.")
            pyttsx3.speak("also i can launch instances on aws cloud.")
            print("I can launch instances")
            pyttsx3.speak(" i can create EBS volume as well as i can attach volume to instance. ")
            print("I can create EBS volume and attach also with instance.")
        elif ("create" in select) and ("key" in select):
            pyttsx3.speak("Enter name for key")
            key_name = input("enter key name : ")
            p = os.system("aws ec2 create-key-pair --key-name {0}".format(key_name))
            print(p)
            pyttsx3.speak("Key pair has created.")
        elif ("create" in select) and ("security" in select):
            pyttsx3.speak("Enter name for security group")
            se_group_name = input("enter name for security group : ")
            pyttsx3.speak("enter description for security group.")
            se_disc = input("Enter discription for security group : ")
            s = os.system(
                "aws ec2 create-security-group --group-name {0} --description {1}".format(se_group_name, se_disc))
            print(s)
            pyttsx3.speak("security group has created")
        elif ("launch" in select) and ("new" in select) and ("instance" in select):
            pyttsx3.speak("Enter image id here.")
            img_id = input("Enter image id : ")
            pyttsx3.speak("Enter type of image.")
            img_type = input("Enter image type : ")
            pyttsx3.speak("Enter subnet id :")
            subnet_id = input("Enter subnetId : ")
            pyttsx3.speak("Enter id of security group.")
            se_id = input("Enter security group id : ")
            pyttsx3.speak("Enter name of key.")
            key_name = input("Enter created  key name : ")
            i = os.system(
                "aws ec2 run-instances --image-id {0} --instance-type {1} --subnet-id {2} --security-group-id {3} --key-name {4}".format(
                    img_id, img_type, subnet_id, se_id, key_name))
            print(i)
            pyttsx3.speak("instance has launched")
        elif ("create" in select) and ("volume" in select):
            pyttsx3.speak("give me volume type and size .")
            vt = input("Enter the type of volume : ")
            size = input("Enter the size of volume :")
            zone = input("Enter the name of avaiability zone :")
            e = os.system(
                "aws ec2 create-volume --volume-type {0} --size {1}  --availability-zone {2}".format(vt, size, zone))
            print(e)
            pyttsx3.speak("volume of 1gb has created")
        elif ("attach" in select) and ("attach" in select):
            pyttsx3.speak("please enter volume id and instance id.")
            vol_id = input("Enter volume id: ")
            instance_id = input("Enter instance id : ")
            dev_name = input("Enter device name or drive name : ")
            a = os.system(
                "aws ec2 attach-volume --volume-id {} --instance-id {} --device {}".format(vol_id, instance_id,
                                                                                           dev_name))
            print(a)
            pyttsx3.speak("volume has attched succesfully.")
        elif ("show" in select) and ("pair" in select):
            wb.open("https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#KeyPairs:")
        elif ("show" in select) and ("group" in select):
            wb.open("https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#SecurityGroups:")
        elif ("launched" in select) and ("running" in select) and ("instance" in select):
            wb.open("https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#Instances:")
        elif ("show" in select) and ("volume" in select):
            wb.open(
                "https://ap-south-1.console.aws.amazon.com/ec2/v2/home?region=ap-south-1#Volumes:sort=desc:createTime")
        elif ("thank" in select) or ("stop" in select):
            pyttsx3.speak("okay  bye have a nice day.")
        else:
            pyttsx3.speak("I am not getting to you.please tell me again.")
            print("I am not getting to you.")
    except KeyboardInterrupt:
        print("done")

def menu():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            pyttsx3.speak("start speaking...and tell me next.")
            print("I am capturing Your requirement..")
            audio = r.listen(source)
            print("Your requirement is captured.")
        select = r.recognize_google(audio)
        if ("what" in select):
            pyttsx3.speak("I can help you  to use some technologies like.")
            pyttsx3.speak("Container technology docker")
            print("Docker Services")
            pyttsx3.speak("LVM PARTITIONS")
            print("LVM partitions")
            pyttsx3.speak("AWS services")
            print("AWS services")
            pyttsx3.speak("Hadoop Services")
            print("Hadoop services")

        elif ("docker" in select):
            dockerconf()

        elif("lvm" in select):
            lvmconf()

        elif ("aws" in select):
            awsconf()
        else:
            exit()

def render(text,style):
	f=Figlet(font=style)
	print('\n'*1)
	print(f.renderText(text))
os.system("clear")
os.system("tput setaf 3")
render('ARTH TEAM TASK','epic')
os.system("tput setaf 7")

os.system("tput setaf 10")
render('\t by ARTH2020.1.17','digital')
pyttsx3.speak("Welcome to voice  assistant a i am your voice assistant greg")
pyttsx3.speak("")
ip = input("Enter IP of system :")
pyttsx3.speak("Tell me what can i do for you ?")
menu()







