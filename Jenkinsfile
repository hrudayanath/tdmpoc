pipeline {
    agent any 
    stages {
        stage('Build Stage') {
            steps {
                sh "echo 'Hello world!'"
                sh "users"
                sh "pylint"
            }
        }
        stage('Test Data Generation Stage') {
            container(""){
            steps {
                sh  ''' 
                   echo 'Generating Test Data!'
                   users
                   conda activate py3.8 
                   python3 -c 'import pandas;'
                   ls -ltra

                '''
            }
            }
        }

        stage('Integration Test Stage') {
            container("python3") {
                steps {
                    sh "echo 'Running Integration Testing'"
                    sh "users"
                    sh "ls"
               }
            }
        }
    }
}
