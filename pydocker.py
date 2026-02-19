import os
import shutil
import sys
import subprocess


def run_command(cmd, capture_output=False, check=True, env=None):
    """Run a shell command and handle errors. Accepts list or string commands.

    Returns subprocess.CompletedProcess on success and exits on failure.
    """
    printable = cmd if isinstance(cmd, str) else " ".join(map(str, cmd))
    print(f"Running: {printable}")
    try:
        result = subprocess.run(
            cmd,
            shell=isinstance(cmd, str),
            check=check,
            capture_output=capture_output,
            text=True,
            env=env,
        )
        return result
    except subprocess.CalledProcessError as e:
        print(f"Error: Command failed with exit code {e.returncode}")
        if getattr(e, "stdout", None):
            print(e.stdout)
        if getattr(e, "stderr", None):
            print(e.stderr)
        sys.exit(e.returncode)


if shutil.which("docker") is None:
    print("Docker is not installed or not in PATH.")
    sys.exit(1)


class Docker:
    def __init__(self, docker_path="docker", env=None):
        self.docker_path = docker_path
        self.env = env

    def _run(self, args, capture_output=False):
        cmd = [self.docker_path] + list(map(str, args))
        return run_command(cmd, capture_output=capture_output, env=self.env)

    def command(self, *args):
        return self._run(list(args))

    def run(self, *args):
        return self._run(["run"] + list(args))

    def build(self, *args):
        return self._run(["build"] + list(args))

    def pull(self, *args):
        return self._run(["pull"] + list(args))

    def push(self, *args):
        return self._run(["push"] + list(args))

    def images(self, *args):
        return self._run(["images"] + list(args))

    def ps(self, *args):
        return self._run(["ps"] + list(args))

    def stop(self, *args):
        return self._run(["stop"] + list(args))

    def start(self, *args):
        return self._run(["start"] + list(args))

    def rm(self, *args):
        return self._run(["rm"] + list(args))

    def rmi(self, *args):
        return self._run(["rmi"] + list(args))

    def exec(self, *args):
        return self._run(["exec"] + list(args))

    def logs(self, *args):
        return self._run(["logs"] + list(args))

    def inspect(self, *args):
        return self._run(["inspect"] + list(args))

    def info(self, *args):
        return self._run(["info"] + list(args))

    def version(self, *args):
        return self._run(["version"] + list(args))

    def login(self, *args):
        return self._run(["login"] + list(args))

    def logout(self, *args):
        return self._run(["logout"] + list(args))

    def save(self, *args):
        return self._run(["save"] + list(args))

    def load(self, *args):
        return self._run(["load"] + list(args))

    def tag(self, *args):
        return self._run(["tag"] + list(args))

    def commit(self, *args):
        return self._run(["commit"] + list(args))

    def cp(self, *args):
        return self._run(["cp"] + list(args))

    def stats(self, *args):
        return self._run(["stats"] + list(args))

    def attach(self, *args):
        return self._run(["attach"] + list(args))

    def pause(self, *args):
        return self._run(["pause"] + list(args))

    def unpause(self, *args):
        return self._run(["unpause"] + list(args))

    # Grouped command namespaces
    def container(self, *args):
        return self._run(["container"] + list(args))

    def image(self, *args):
        return self._run(["image"] + list(args))

    def network(self, *args):
        return self._run(["network"] + list(args))

    def volume(self, *args):
        return self._run(["volume"] + list(args))

    def compose(self, *args):
        return self._run(["compose"] + list(args))

    def system(self, *args):
        return self._run(["system"] + list(args))

    def builder(self, *args):
        return self._run(["builder"] + list(args))

    def context(self, *args):
        return self._run(["context"] + list(args))

    def buildx(self, *args):
        return self._run(["buildx"] + list(args))
    
    def __getattr__(self, name):
        def method(*args):
            sub = name.replace("_", "-")
            return self._run([sub] + list(args))

        return method