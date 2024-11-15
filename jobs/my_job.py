from nautobot.apps.jobs import Job, register_jobs


class TestJobGit(Job):

    class Meta:  # pylint: disable=too-few-public-methods
        """Information about the Job."""

        name = "TEST DEV JOB from GIT"
        description = "Sync information from Citrix ADM/SDX to Nautobot"

    def run(self, *args, **kwargs):
        pass


register_jobs(TestJobGit)

