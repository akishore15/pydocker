import os
import shutil
import sys
import subprocess


def run_command(cmd, capture_output=False, check=True, env=None):

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
    run_command("curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh")



class Docker:

    def run(self, image):
        run_command(f"docker run -it {image} /bin/bash")

    def pull(self, image, tag):
        run_command(f"docker pull {image}:{tag}")

    def build(self, *args):
        return run_command(f"docker build {' '.join(args)}")

    def push(self, *args):
        return run_command(f"docker push {' '.join(args)}")

    def images(self, *args):
        return run_command(f"docker images {' '.join(args)}")

    def ps(self, *args):
        return run_command(f"docker ps {' '.join(args)}")

    def stop(self, *args):
        return run_command(f"docker stop {' '.join(args)}")

    def start(self, *args):
        return run_command(f"docker start {' '.join(args)}")

    def rm(self, *args):
        return run_command(f"docker rm {' '.join(args)}")

    def rmi(self, *args):
        return run_command(f"docker rmi {' '.join(args)}")

    def exec(self, *args):
        return run_command(f"docker exec {' '.join(args)}")

    def logs(self, *args):
        return run_command(f"docker logs {' '.join(args)}")

    def inspect(self, *args):
        return run_command(f"docker inspect {' '.join(args)}")

    def info(self, *args):
        return run_command(f"docker info {' '.join(args)}")

    def version(self, *args):
        return run_command(f"docker version {' '.join(args)}")

    def login(self, *args):
        return run_command(f"docker login {' '.join(args)}")

    def logout(self, *args):
        return run_command(f"docker logout {' '.join(args)}")

    def save(self, *args):
        return run_command(f"docker save {' '.join(args)}")

    def load(self, *args):
        return run_command(f"docker load {' '.join(args)}")

    def tag(self, *args):
        return run_command(f"docker tag {' '.join(args)}")

    def commit(self, *args):
        return run_command(f"docker commit {' '.join(args)}")

    def cp(self, *args):
        return run_command(f"docker cp {' '.join(args)}")

    def stats(self, *args):
        return run_command(f"docker stats {' '.join(args)}")

    def attach(self, *args):
        return run_command(f"docker attach {' '.join(args)}")

    def pause(self, *args):
        return run_command(f"docker pause {' '.join(args)}")

    def unpause(self, *args):
        return run_command(f"docker unpause {' '.join(args)}")

    # Grouped command namespaces
    def container(self, *args):
        return run_command(f"docker container {' '.join(args)}")

    def image(self, *args):
        return run_command(f"docker image {' '.join(args)}")

    def network(self, *args):
        return run_command(f"docker network {' '.join(args)}")

    def volume(self, *args):
        return run_command(f"docker volume {' '.join(args)}")

    def compose(self, *args):
        return run_command(f"docker compose {' '.join(args)}")

    def system(self, *args):
        return run_command(f"docker system {' '.join(args)}")

    def builder(self, *args):
        return run_command(f"docker builder {' '.join(args)}")

    def context(self, *args):
        return run_command(f"docker context {' '.join(args)}")

    def buildx(self, *args):
        return run_command(f"docker buildx {' '.join(args)}")
    
    def __getattr__(self, name):
        def method(*args):
            sub = name.replace("_", "-")
            return run_command(f"docker {sub} {' '.join(args)}")

        return method