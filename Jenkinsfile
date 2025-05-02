pipeline {
  parameters {
    string(name: 'BRANCH', defaultValue: 'main', description: '빌드할 git branch')
  }
  agent any
  stages {
    stage('Checkout') {
      steps {
        git url: 'https://github.com/sey0203/jenkins-pipeline.git', branch: params.BRANCH
        echo "소스코드를 Git 저장소에서 성공적으로 가져왔습니다."
      }
    }
    stage('Setup') {
      steps {
        echo 'Python 환경을 설정합니다.'
        sh 'python3 -m venv venv'
        sh '. venv/bin/activate'
        sh 'pip install pytest'
        echo 'Python 환경설정 완료. (pytest 설치 완료)'
      }
    }
    stage('Test') {
      steps {
        echo 'Pytest를 사용해서 테스트를 실행합니다.'
        sh '. venv/bin/activate && pytest'
        echo '테스트 완료.'
      }
    }
  }
}