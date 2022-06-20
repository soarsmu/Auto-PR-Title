# Auto-PR-Title-Generator

## Prerequisite:

    1. Clone the project at <path_to_directory>
    2. Download model from https://smu-my.sharepoint.com/:u:/g/personal/ivanairsan_smu_edu_sg/EYRCeoG9NyFFr2j6356ZZJQBKZtrmt1LamLHG4kFlYVuZQ?e=BMcnur
    3. Put the unzipped model folder under <path_to_directory>/Auto-PR-Title


The structure is supposed to look like this:
image.png

## Usage
1. Build the image: 

    ```docker build -t auto-pr-title .```

2. Start a container: 

    ```docker run --name <container_name> -p 8080:8080 -v <path_to_directory>/Auto-PR-Title:/app -itd auto-pr-title```

3. The web app can be accessed at localhost:8080