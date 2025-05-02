pipeline {
  parameters {
    string(name: 'BRANCH', defaultVlaue: 'main', description: 'test...')
  }
  agent any
  stages {
    stage('Checkout') {
      steps {
        echo 'Building branch: ${params.BRANCH}'
      }
    }
    stage('Build') {
      steps {
        sh 'chmod +x build.sh && ./build.sh'
      }
    }
    stage('Test') {
      steps {
        sh 'echo "Simulating test command"'
      }
    }
  }
}