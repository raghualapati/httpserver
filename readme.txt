To install goss and dgoss use the below command.
curl -fsSL https://goss.rocks/install | sudo sh
The test for the container and the application are written in the goss.yaml file which is available in the below path
https://github.com/raghualapati/httpserver/blob/master/goss.yaml
This test file makes sure the required packages and files and services are available once the container is started and also test the output of all the valid api calls.
To run the test run the below command
dgoss run -p 8020:8080 <<image name build using the dockerfile>>