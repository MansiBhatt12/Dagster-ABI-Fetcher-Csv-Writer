# Dagster Project to Fetch APIs and Save to CSV File 

This Dagster project fetches data from APIs for 5 contract addresses and saves the information to a CSV file. It utilizes Dagster, Dataframes (pandas), and interacts with APIs to fetch all available ABIs for the specified contract addresses.The code is written in Python and uses the Dagster library to orchestrate the pipeline.

## Features

* The project can fetch APIs for 5 contract addresses.
* The data is saved to a CSV file.
* The project includes scheduled pipeline, a predefined job and schedule to run the pipeline every hour. 
* The project uses the File System I/O Manager to store the fetched data in a directory called 'data' in your file system to a more permanent location. 

## How to Use

To run the project, you will need to have Dagster installed. Once you have Dagster installed in your python local environment, you can run the project by following these steps:

1. Clone the repository
```bash
git clone https://github.com/your-username/dagster-api-fetching.git](https://github.com/MansiBhatt12/Dagster_Project.git
```
   
2. Install the dependencies
```bash
pip install -e ".[dev]"
```
* Note: Don't forget to import, install necessary packages
```bash
pip install package_name
```

3. Run the command
```bash
dagster dev
```

This will start the Dagster UI on your local machine. You can then use the UI to interact with the project.

Open your web browser and navigate to http://localhost:3000 to access the Dagster UI.

Click on the Materialize in the Dagster UI and execute it. The pipeline will fetch data from the APIs, process it using pandas, and save it to a CSV file in your project directory.

