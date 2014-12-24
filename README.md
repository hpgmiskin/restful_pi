#restful_pi

RESTful Pi is a collection of Python code to enable a Raspberry Pi to act as simple RESTful web server using the Flask framework.

The front end interface through which this can be interacted is found in the [angular_pi](https://github.com/miskinh/angular_pi) repository. To allow Flask to host the front end both the 'angular_pi' directory and the 'restful_pi' directory must reside in the same parent directory.

##Overview

This RESTful web interface enables a correctly configured Raspberry Pi to serve as the following:

- Remote light control
- Internal network device manager
- GoPro camera controller

##To Run

To run this application its best to use a virtual environment. The requirements of the files that should be installed in the virtual environment can be found in `requirements.txt`. The process I suggest for this is as follows.

######Install Python 2.7 and Pip

######Install virtualenv by typing the following into the terminal

    $ pip install vitualenv

######Navigate to the local directory containing this repository in terminal

    $ cd FOLDER_PATH

######Create a new virtual environment in this directory

    $ virtualenv venv

######Activate the virtual environment

    $ source venv/bin/activate

######Install requirements using pip

    $ pip install -r requirements.txt --allow-all-external

######Run the server

    $ sudo python restServer.py&

######Open you internet browser and navigate to

    0.0.0.0

##Licence

Please feel free to use any code contained within the repository for non commercial purposes however I request that credit is given to myself for any direct copying.