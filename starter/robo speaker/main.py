import os
if __name__=="__main__":
    print("welcome to RoboSpeaker By Rishabh")
    while True:
        x=input("what do you want to say:")
        if x=="quit":
            os.system("say 'Bye Bye! Thanks for using RoboSpeaker'")
            break
        command=f"say {x}"
        os.system(command)


 