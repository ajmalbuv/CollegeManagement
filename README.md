# EduManage 
[//]:![EduManage-Logo](Logo-Official.png)
<div align="center">
  <img src="Logo-Official.png" alt="Project Logo" width="200" />
</div>

A college management system built using **Django** framework. It is designed for interactions between students and teachers. Features include attendance, marks and time table.

## Installation

Python and Django need to be installed

```bash
pip install -r requirements.txt
```

## Usage

Go to the EduManage folder and add a Postgres url in .env or uncomment the sqlite database lines for local db.

### Example .env

```
SECRET_KEY ="##################################################" #generate a JWT Secret Online
DEBUG = "True" # Keep False in deployment,True Only in develepment
POSTGRES_URL_NO_SSL="postgres://username:password@HOSTIP:5432/DBName"
```

### create SuperUser

```bash
python manage.py createsuperuser
```

### Run Server

```bash
python manage.py runserver
```

Then go to the browser and enter the url **http://127.0.0.1:8000/**

## Login

The login page is common for students, teachers and Admins.

You can access the django admin page by logging in using the superuser username and password.

## Users

New students and teachers can be added through the admin page. A new user needs to be created for each.
Default password for the teachers and students will be 'project123'.

The admin page is used to modify all models such as Students, Teachers, Departments, Courses, Classes etc.

**For more details regarding the system and features please refer the reports included.**

## Update (11/07/2024)

Added method to reset attendance time range in Django Admin page.

![alt_text](https://i.imgur.com/0xOWmUZ.png)

This is present in Django Admin -> Attendance (http://127.0.0.1:8000/admin/info/attendanceclass/).  
Start Date: Start Date of Attendance period  
End Date: End Date of Attendance period

This will delete all present attendance data and create new attendance objects for the given time range.

## Screenshots

### Login Screen

![Login Screen](https://imgur.com/WHXZ7hm.png)

### Teacher Page

![Teacher DashBoard](https://imgur.com/lhRQnnE.png)

![Teacher Attendance](https://imgur.com/N4VVbVR.png)

![Attendance Marking](https://imgur.com/9GKsdBP.png)

![Attendence View](https://imgur.com/88TThj6.png)

![Enter Marks](https://imgur.com/OmrNNU4.png)

![Teacher TimeTable](https://imgur.com/pJcXVI5.png)

### Student Page

![Student Dashboard](https://imgur.com/219KXjZ.png)

![Student Attendancet](https://imgur.com/lv9V7gP.png)

![Student Attendance Detail](https://imgur.com/ygo5d8U.png)

![Student Markst](https://imgur.com/BLhUmp4.png)

![Student Timetable](https://imgur.com/FczljbU.png)

### Admin Page

![Admin Dashboard](https://imgur.com/nRobbTj.png)

![Assigns](https://imgur.com/MzILYWA.png)

![Add Teacher](https://imgur.com/7vDvgim.png)

![Add Student](https://imgur.com/psox5xA.png)
