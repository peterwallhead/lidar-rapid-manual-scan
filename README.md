# LiDAR Rapid Scanning (Manual)
Enables fast and efficient generation of multiple scans of a space, supporting the development of SLAM-based autonomous navigation systems.

![LiDAR scanner mounted on a tripod](https://github.com/peterwallhead/lidar-rapid-manual-scan/blob/main/docs/images/lidar-tripod-mount.jpg)

## Install
```
pipenv install --dev
```
## Directory Structure
- Each scan session is stored in subdirectory of `/collections` where the subdirectory is named the current `Y-m-d-H-M` (this subdirectory is generated automatically when the scan session starts)
- Data from each scan is appended to `/collections/session-directory/frames.txt` as a dictionary where each element's key is the angle and the value is the distance measured in millimetres
- Scan preview images are added to `/collections/session-directory/frames/` as each scan is recorded

## Usage
```
pipenv run python __init__.py
```
