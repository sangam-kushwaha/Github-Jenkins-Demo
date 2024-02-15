pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                echo 'hello world'
                echo 'Triggered webhook'
                echo "added one  line"
            }
        }
        stage('test'){
            steps{
                echo "running the build stage"
            }
        }
    }
}
