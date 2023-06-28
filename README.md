# Dagster Project to Fetch APIs and Save to CSV

This Dagster project fetches data from APIs for 5 contract addresses and saves the information to a CSV file. It utilizes Dagster, Dataframes (pandas), and interacts with APIs to fetch all available ABIs for the specified contract addresses.The code is written in Python and uses the Dagster library to orchestrate the pipeline.

## Features

*The project can fetch APIs for 5 contract addresses.
*The data is saved to a CSV file.
*There is scheduled pipeline, defined a job  and schedule to run assigned job at every hour.
*The project uses the File System I/O Manager to save the data to a permanent location.


First, install your Dagster code location as a Python package. By using the --editable flag, pip will install your Python package in ["editable mode"](https://pip.pypa.io/en/latest/topics/local-project-installs/#editable-installs) so that as you develop, local code changes will automatically apply.

```bash
pip install -e ".[dev]"
```

Then, start the Dagster UI web server:

```bash
dagster dev
```

Open http://localhost:3000 with your browser to see the project.

You can start writing assets in `dagster_project/assets.py`. The assets are automatically loaded into the Dagster code location as you define them.

## Development


### Adding new Python dependencies

You can specify new Python dependencies in `setup.py`.

### Unit testing

Tests are in the `dagster_project_tests` directory and you can run tests using `pytest`:

```bash
pytest dagster_project_tests
```

### Schedules and sensors

If you want to enable Dagster [Schedules](https://docs.dagster.io/concepts/partitions-schedules-sensors/schedules) or [Sensors](https://docs.dagster.io/concepts/partitions-schedules-sensors/sensors) for your jobs, the [Dagster Daemon](https://docs.dagster.io/deployment/dagster-daemon) process must be running. This is done automatically when you run `dagster dev`.

Once your Dagster Daemon is running, you can start turning on schedules and sensors for your jobs.

## Deploy on Dagster Cloud

The easiest way to deploy your Dagster project is to use Dagster Cloud.

Check out the [Dagster Cloud Documentation](https://docs.dagster.cloud) to learn more.
