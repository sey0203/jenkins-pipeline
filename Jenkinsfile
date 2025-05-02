pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        echo 'Checking out code...'
      }
    }
    stage('Build') {
      steps {
        bat 'build.bat'
      }
    }
    stage('Test') {
      steps {
        sh 'echo "Simulating test command"'
      }
    }
  }
}