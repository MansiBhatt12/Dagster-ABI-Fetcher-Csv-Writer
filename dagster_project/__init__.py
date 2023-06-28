from dagster import (
    AssetSelection,
    Definitions,
    ScheduleDefinition,
    define_asset_job,
    load_assets_from_modules,
    FilesystemIOManager,  # Update the imports at the top of the file to also include this
)

from . import assets

all_assets = load_assets_from_modules([assets])

# Addition: define a job that will materialize the assets
fetch_job = define_asset_job("fetch_job", selection=AssetSelection.all())

# Addition: a ScheduleDefinition the job it should run and a cron schedule of how frequently to run it
fetch_schedule = ScheduleDefinition(
    job=fetch_job,
    cron_schedule="0 * * * *",  # every hour
)

io_manager = FilesystemIOManager(
    base_dir="data",  # Path is built relative to where `dagster dev` is run
)


defs = Definitions(
    assets=all_assets,
    jobs=[fetch_job],  # Addition: add the job to Definitions object (see below)
    schedules=[fetch_schedule],
    resources={
        "io_manager": io_manager,
    },
)

