# Simple Phone Number Tracer

This is a simple phone number tracer API to help you find the phone number based on your input address

## Install

### Create python virtual environment

```bash
python3 -m venv <your venv path>
source <your venv path>/bin/activate

```

### Install required packages

```bash
pip install -r requirements.txt
```

### Prepare environment variables

Update file `.env` in `simple_phone_number_tracer/`folder according to the `.env_sample` file

```bash
SECRET_KEY=
API_KEY=
DEBUG=True
LOG_PATH=logs
```

### Run server

```bash
python manage.py runserver <your desire port (optional)>
```

## Demo

For example you want to get the phone number of this place `Computer History Museum Mountain View USA`

Go to URL

```bash
http://localhost:<port>/getphonenumber?address=Computer%20History%20Museum%20Mountain%20View%20USA
```

The response should contain the `formatted_phone_number` field

```json
{
  "results": [
    {
      "formatted_address": "1401 N Shoreline Blvd, Mountain View, CA 94043, USA",
      "formatted_phone_number": "(650) 810-1010",
      "name": "Computer History Museum",
      "place_id": "ChIJm7NJkla3j4AR8vR-HWRxgOo"
    }
  ]
}
```

## Testing

### Run the test

Run all testcases

```bash
python manage.py test
```

## Author

- hung1998pro@gmail.com
