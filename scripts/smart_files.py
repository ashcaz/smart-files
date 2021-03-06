import click
from crontab import CronTab
from automation import (
    root_dir,
    get_files,
    main,
    add_cron_job,
    every_minute,
    daily,
    weekly,
    hourly,
    monthly
)


@click.group()
@click.version_option()
def smart_files():
    """Smart-files sorts all your downloaded files so you dont have to"""


@smart_files.command()
def show_files():
    """Will show you files currently in downloads file"""
    files = get_files(root_dir)

    if len(files) == 0:
        click.secho("\nAll files have been sorted!\n")
    else:
        print("\nFiles not yet sorted:\n")

        for item in files:
            click.secho(item, fg="magenta")

        print("\n")


@smart_files.command()
def run():
    """Run the Smart-files program on an ad hoc basis"""

    files = get_files(root_dir)

    if not len(files):
        click.secho("\nThere aren't any files to move. Great Job!\n")
    else:
        print("\nRunning Smart-files...\n\n")
        print("\nMoving Files Now... \n")
        main()
        print("\n\nSmart-files run complete!\n\n")


@smart_files.command()
@click.option(
    "--minutes",
    "-m",
    is_flag=True,
    help="Will create a cron job for Smart-files to run every minute",
)
@click.option(
    "--hour",
    "-h",
    is_flag=True,
    help="Will create a cron job for Smart-files to run every hour",
)
@click.option(
    "--day",
    "-d",
    is_flag=True,
    help="Will create a cron job for Smart-files to run once a day",
)
@click.option(
    "--week",
    "-w",
    is_flag=True,
    help="Will create a cron job for Smart-files to run once a week",
)
@click.option(
    "--month",
    "-o",
    is_flag=True,
    help="Will create a cron job for Smart-files to run once a month",
)
def cron(minutes, hour, day, week, month):
    """Adds a job to the time scheduler called cron"""
    if hour:
        add_cron_job(hourly)
    elif day:
        add_cron_job(daily)
    elif week:
        add_cron_job(weekly)
    elif month:
        add_cron_job(monthly)
    elif minutes:
        add_cron_job(every_minute)
    else:
        print(
            """Usage: smart-files cron [OPTIONS]\n\n\tAdds a job to the time scheduler called cron\n\nOptions:\n-m, --minutes  Will create a cron job for Smart-files to run every minute\n-h, --hour     Will create a cron job for Smart-files to run every hour\n-d, --day      Will create a cron job for Smart-files to run once every day\n-w, --week     Will create a cron job for Smart-files to run once a week\n-o, --month    Will create a cron job for Smart-files to run once a month\n--help         Show this message and exit."""
        )
