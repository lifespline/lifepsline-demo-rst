"""This is the project's task runner.
"""
from invoke import task

@task
def docs(ctx, step):
    """Generate documentation.
    """

    if step == 'launch':
        image_name = 'lifespline/docs-debug-lifespline-demo-rst'
        container_name = image_name
        volume_name = 'docs-debug-volume-lifespline-demo-rst'
        container_host = '0.0.0.0'
        container_port = 8080
        docker_run = f"""
        docker run \
            --rm -d \
            --mount type=volume,source={volume_name},target=/home \
            -p {container_host}:{container_port}:{container_port} \
            --name {container_name} \
            {image_name} {container_port} {container_host}
        """

        cmds = [
            'cd docs',
            f'docker volume create --name {volume_name}',
            f'docker build . -t {image_name}',
            docker_run,

        ]
    elif step == 'build':
        cmds = [
            "cd docs",
            "make html",
            "cp -a _build/html/. .",
            "make clean",
        ]
    
    ctx.run(';'.join(cmds))
