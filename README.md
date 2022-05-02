# data-leak-protection
Monitor file system to prevent sharing of the files outside organisational purview without the admin approval.


# Get Started (Locally)

## Clone the project

```bash
  git clone https://github.com/nimrat02/data-leak-protection.git
  cd data-leak-protection/
```

## Install dependencies

For `Python 2:`
```bash
  pip install -r requirements.txt
```

For `Python 3:`
```bash
  pip3 install -r requirements.txt
```

`(Make sure pip/pip3 is installed in your system)`

## Run the main.py
For `Python 3:`
```bash
  python3 main.py <dirpath>
```
`<dirpath> should be path to root directory to be monitored`

**The data will be stored in file 'Events.csv' in the same directory where 'main.py' is present.
In the starting of the program, 'Monitoring starts' will be printed in the console. Similarly 'Monitoring Ends' is printed when the program ends.**


## Approach
1. Handler class handles the events occured.
2. Instance of the watchdog.observers.Observer thread class is created. Observer will monitor the desired directory and notifies Handler class, which will further execute its task according to the event occurred.
3. While there is no keyboard interruption, the program will monitor the Directory provided by the user.
4. Monitoring a single directory will be considered as a single process where a single thread is assigned for the task by the program. Same functionality can be provided for multiple directories where each will be assigned a thread.
5. The Handler class maintains the events occurred in a CSV file. It also keeps a record of current time, the events occuring, the file modified etc.

## Libraries Used
watchdog
csv