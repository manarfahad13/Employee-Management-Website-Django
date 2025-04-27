# Employee Management Website by using Django

A web-based Employee Management System built with __Django__ , The system allows users to manage employee data and their associated devices, Emails , and servers across multiple branches.

 
## Features

- Dashboard: Quick overview of the number of employees, devices, Emails, and servers.

![new-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/c2df9449-90be-4ca3-a97d-d077f3f3e38f)

- Employee Management: Add, edit, delete, and view employees.

![14 04 2025_15 06 08_REC](https://github.com/user-attachments/assets/f2874fa6-aa13-4a33-a394-845b5bacaeb1)

- Emails Management: Add and manage employee email addresses.

![emails](https://github.com/user-attachments/assets/2742df16-b473-43c9-9500-6fff909b2023)



- Device Management: Manage employee devices (like laptops, desktops, etc.).

![14 04 2025_15 44 55_REC](https://github.com/user-attachments/assets/a4e79414-b2b5-4498-80b2-6f6ac1882e45)


-  Server Management: Add and manage server information across branches.

![14 04 2025_15 45 14_REC](https://github.com/user-attachments/assets/41ee131d-e1f0-4448-b80a-207bca7cb92f)

-  Branch Filtering: Easily view employees and devices filtered by branch (Khobar, Riyadh, Jeddah).

  ![branches](https://github.com/user-attachments/assets/695abf1c-5692-4776-b450-34bc18413763)

-   User-Friendly Interface: Clean and responsive design using Bootstrap.

## Technologies Used:
- Python 3
- Django
- SQLite3
- HTML
- CSS
-  Bootstrap
-  FontAwesome (icons)





### Prerequisites

Install the following prerequisites:

1. [Python 3.8-3.11](https://www.python.org/downloads/)
<br> This project uses **Django v4.2.4**. For Django to work, you must install a correct version of Python on your machine. More information [here](https://django.readthedocs.io/en/stable/faq/install.html).
2. [Visual Studio Code](https://code.visualstudio.com/download)


### Installation

#### 1. Create a virtual environment

From the **root** directory, run:

```bash
python -m venv venv
```

#### 2. Activate the virtual environment

From the **root** directory, run:

On macOS:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\scripts\activate
```

#### 3. Install required dependencies

From the **root** directory, run:

```bash
pip install -r requirements.txt
```

#### 4. Run migrations

From the **root** directory, run:

```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```

#### 5. Create an admin user to access the Django Admin interface

From the **root** directory, run:

```bash
python manage.py createsuperuser
```

When prompted, enter a username, email, and password.


### Run the application

From the **root** directory, run:

```bash
python manage.py runserver
```


### Run the tests

From the **root** directory, run:

```bash
python manage.py test --pattern="tests.py"

```


### View the application

Go to http://127.0.0.1:8000/ to view the application.


### Copyright and License
This project is originally based on a project by Bob's Programming Academy (© 2022), released under the MIT License.
I have made modifications, improvements, and added new features to suit my own learning and project 
