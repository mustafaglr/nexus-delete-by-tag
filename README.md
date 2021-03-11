# Nexus Save Last 5 Image Tags Which is Tagged as Branch-BuildNumber

Example tag; 

NEXUS_URL/IMAGE:master-1  
NEXUS_URL/IMAGE:master-2  
NEXUS_URL/IMAGE:master-3  
NEXUS_URL/IMAGE:master-4  
NEXUS_URL/IMAGE:master-5  
NEXUS_URL/IMAGE:master-6  

NEXUS_URL/IMAGE:master-6 will be deleted.

## Run Commands

```
sh +x delete-old-images-get-token.sh NEXUS_URL DOCKER_REPO USERNAME:PASSWORD
```

fill NEXUS_URL, USERNAME and PASSWORD in main.py

```
python main.py
```
