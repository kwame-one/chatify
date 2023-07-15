## API

---

### Software Requirements

1. Python 3.9.6
2. MySQL Server

---

### Instructions
1. Clone the repository
2. Make a copy of **.env.example** in the root directory and save it as **.env in the root directory**
3. Configure the database name and password in the **.env** file as below
```dotenv
DB_HOST=
DB_USER=
DB_PORT=
DB_PASSWORD=
DB_NAME=
```

### Setup
Open a terminal in the project's root directory and run the following commands 
1. Create a virtual environment
```shell
python -m venv path_to_virutal_env
```
2. Activate virtual environment
Unix
```shell
source path_to_virutal_env/bin/activate 
```
Windows (command prompt)
```shell
source path_to_virutal_env\bin\activate.bat
```
3. Install dependencies
```shell
pip install -r requirements.txt
```
4. Run migrations
```shell
alembic upgrade head
```
5. Run application
```shell
uvicorn main:app --reload
```
