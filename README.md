# Auto-PR-Title-Generator

## Prerequisite:

1. Clone the project at <path_to_directory>
2. Download model from https://smu-my.sharepoint.com/:u:/g/personal/ivanairsan_smu_edu_sg/EYRCeoG9NyFFr2j6356ZZJQBKZtrmt1LamLHG4kFlYVuZQ?e=BMcnur
3. Put the unzipped model folder under <path_to_directory>/Auto-PR-Title


The structure is supposed to look like this:

<img width="175" alt="image" src="https://user-images.githubusercontent.com/7076833/174555290-0abfd8e9-db4b-423a-ac36-35ab0edd3227.png">


## Usage
1. Build the image: 

    ```docker build -t auto-pr-title .```

2. Start a container: 

    ```docker run --name <container_name> -p 8080:8080 -v <path_to_directory>/Auto-PR-Title:/app -itd auto-pr-title```

3. The web app can be accessed at localhost:8080


## App Flow
1. Create a new pull request from `Pull Request` tab
<img width="756" alt="image" src="https://user-images.githubusercontent.com/7076833/175185203-7ab54a2b-68f3-4ccd-aecc-daf97fc35f2d.png">
<img width="751" alt="image" src="https://user-images.githubusercontent.com/7076833/175185420-dd199fd0-9004-49b1-805b-9b88006e54ce.png">

2. Copy the comparing branch URL, and then paste it to AutoPRTitle web app
<img width="765" alt="image" src="https://user-images.githubusercontent.com/7076833/175185537-e8f8b864-e67e-44a4-ac39-1757f0d9c02d.png">

<img width="999" alt="image" src="https://user-images.githubusercontent.com/7076833/175185623-cc0aa52c-c9dd-4090-ba7b-4c21679b94f3.png">


3. Fill in issues and desciption details (if any)

4. Click `Generate PR Title` button

5. You'll get the result in a few seconds

<img width="997" alt="image" src="https://user-images.githubusercontent.com/7076833/175185701-2a6eb070-1002-4ae6-9fcb-8f472765116f.png">

