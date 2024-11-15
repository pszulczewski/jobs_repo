from nautobot.apps.jobs import Job, register_jobs
from jobs.my_job import TestJobGit


register_jobs(TestJob)
