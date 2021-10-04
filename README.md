# DATA RECOVERY
## Center for Cyber Security and Cyber Law

In this work, the data is recovered from the secondary memory drives and relevant technical background knowledge is given.
Using Python Script,
- Imaging
- Analyzing the MFT
- TimeStamps

## Features

- The secondary drive must be plugged-in to the system where the application runs.
- Consider the destination folder in which the memory capacity of the testing drive must be present
- Source drive and the destination drive must not be the same 
- After imaging run the NTFS script
- Using exif script timestamps are extracted

Most of the time we find ourselves in such undesirable circumstances where data gets deleted accidentally or intentionally. In the past, there was no way of accessing this data, but with the advancements in technology, we now have the chance to locate lost files from laptop or desktop computers. The most common scenarios are Operating System (OS) failures or accidental damages, then one has to copy the file to other devices and this can be done in many ways.


> The main goal of this work is to recover the data which is accidentally deleted from the secondary storage drives without loss of data. Now a days there is a huge demand and also expensive to recover the data. In this work, Python language script is used to develop the application for being accurate and efficient results.

## Tech

Data Recovery application uses the following open sources:

- [python.org] - Python Language for scripting.
- [code.visualstudio.com] - Text Editor used for python scripting.
- [exiftool.org] - Python Package for extracting the Timestamps.
- [ieeexplore.ieee.org] - IEEE website for refering the research papers.
- [scholar.google.com] - website for refereing the research papers.

And used the references from the many more open sources.

## Installation

Data Recovery Application requires 

[python.org](www.python.org) version 8 to run.

[code.visualstudio.com](https://code.visualstudio.com/) Windows version Text editor.              

## Development
[DD_Imager.py](https://drive.google.com/file/d/1J4mPRt0diSIyHlQ0Q6iASRZs4ixTKxQ-/view?usp=sharing) Python code for Imaging the memory device.

[ntfs_pattern.py](https://drive.google.com/file/d/13PYXC7GluImiUHeFPhJjB0C3juKYqu-y/view?usp=sharing) Python code for recovering the files from the dd image file.

## Observations
1. Data which is recently deleted has been recovered Successfully, without any data loss.
2. While capturing the clone image of the memory device the execution time(minutes) is equivalent to the capacity of the memory device. For example, 2GB of memory device takes 2 minutes of execution time approximately.

