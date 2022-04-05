# Django Youtube Clone
This project is basically an endpoint or Django api to fetch latest videos from youtube. The videos are sorted in reverse chronological order of their trending status from YouTube. You can also view details of a particular video.



## Setup Guide
- Clone the project
- Make virtual environment using the command `python3 -m venv env`. So, by this a virtual environment named env will be     created in your system.
- Install all dependencies by using typing `pip install -r requirements.txt`.
- Inside the `setting.py` file, fill the variable `GOOGLE_API_KEYS` with the API Keys available,the list is like this => `['API_KEY_1','API_KEY_2','API_KEY_3','API_KEY_4'...]`
- You can get API key from [this](https://developers.google.com/youtube/v3/getting-started)
- Apply migrations by running `python manage.py makemigrations`.
- Now run `python manage.py migrate`.
- Run the server using `python mange.py runserver`

