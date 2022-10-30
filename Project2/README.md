
Goal of this script: to print the contents of /var/log/firewalld to a webpage.

How to run:

First make sure you are running as root

"sudo su"

Then change the permissions of the log file to make sure it can be read from

"chmod 777 /var/log/firewalld"

Then run the server

"node Project2.js"

On web browser, go to 127.0.0.1:3000 to view page

To change the log file shown, simply repeat the chmod command on the selected log file you want, then change the parameter on line 9:

logdata = fs.readFileSync('/your/file/here')


The expected output should be the contents of the firewalld log file, or a file of your choosing.
