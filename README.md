# Currrency Converter API
Currency Convert API was made so that you can easily convert any of the available currencies!
This api api was made for a couple of reason:
- Convert from one currency to another using their iso code
- A route to check all currency and their Full names and iso


## Running the project
To run this project first download the link using the command.
```bash
git clone https://github.com/Nonso-M/Concurrency.git
```
Create a  virtual enviroment, depending on your system type, but for windows I used conda to be able to select my python version with
```bash
conda create -n myenv python=3.10
```

Install the requirement.txt file to get the dependencies into the virtual enviroment
```bash
pip install -r  requirements.txt
```

###Running the program/Usage
to run the program, open your command line and run the command below.
```bash
## main can be subtituted with the relative path to the main file 
uvicorn main:app --reload
```
The different routes are
- `/convert` - You provide query in the form of 
`/?from_currency=<currency iso>&to_currency<contry iso>&amount<enter integer> 
- `/currency`  
- `/history`


##Testing
To test this project go on the terminal and type the followng commmand

```bash
python -m pytest tests
```


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)


Currency Convert API
Currency Convert API was made so that you can easily convert any of the available currencies!

Running the project
The simplest and most straight-forward way to get this up and running is using Docker and Docker Compose.

Just run the following:

docker-compose up -d --build
The API will run on localhost, port 8000

Api Docs
Exposed on /docs

Intentionally left out
Since this is meant to be a small/quick task, some extra features and/or nice-to-have(s) have been left out, some of them being:

Time-series data (API limitations)
Unit testing (pytest)
Key obfuscation (the API key is at plain sight)
Use of .env for environment / config. variables
Logging to a file (loguru would work great w/ FastAPI)