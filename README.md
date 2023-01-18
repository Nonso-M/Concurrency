# Currrency Converter API
Currency Convert API was made so that you can easily convert any of the available currencies!
This api api was made for a couple of reason:
- Convert from one currency to another using their iso code
- A route to check all currency and their Full names and iso

**Mongodb Atlas** dummy account was created and used to story history data
## Running the project
To run this project first download the link using the command.
```bash
git clone https://github.com/Nonso-M/Concurrency.git
```
Create a  virtual enviroment, depending on your system type, but for windows I used conda to be able to select my python version with
```bash
conda create -n <name of venv> python=3.10
```
Activate the virtual enviroment using
```bash
conda activate <name of venv>
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

The login details for thhe application is
- Username- Jonny
- pass - Done
The different routes are
- `/convert` - You provide query in the form of 
`/?from_currency=<currency iso>&to_currency<contry iso>&amount<enter integer> 
- `/currencies`  
- `/history`


##Testing
To test this project go on the terminal and type the followng commmand

```bash
python -m pytest tests
```

## Next Steps
- Enabling User signup
- Total Test Coverage
- Logging to a file
- Caching history route data and using it on when a user visits the route
- Better modularization

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)


### Api Docs
Exposed on /docs
