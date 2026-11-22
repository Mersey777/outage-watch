// Sprint 1 version: deploys status_check.py. Sprint 2 swaps in `pip install .`
pipeline {
  agent any
  triggers { githubPush() }  // also tick "GitHub hook trigger for GITScm polling"
  environment {
    WEBEX_TOKEN   = credentials('webex-bot-token')   // Secret text
    WEBEX_ROOM_ID = credentials('webex-room-id')     // Secret text
    PROD_DIR      = '/var/jenkins_home/outagewatch-prod'
  }
  stages {
    stage('Checkout') { steps { checkout scm } }
    stage('Setup') {
      steps { sh 'mkdir -p reports && python3 -m venv .venv && .venv/bin/pip install -q -r requirements-dev.txt' }
    }
    stage('Lint') { steps { sh '.venv/bin/flake8 status_check.py ci tests' } }
    stage('Unit tests') {
      steps { sh '.venv/bin/pytest --junitxml=reports/junit.xml' }
      post { always { junit allowEmptyResults: true, testResults: 'reports/junit.xml' } }
    }
    stage('Deploy') {
      steps {
        sh 'python3 -m venv $PROD_DIR/venv && $PROD_DIR/venv/bin/pip install -q -r requirements.txt'
        sh 'cp status_check.py $PROD_DIR/'
      }
    }
    stage('Smoke run') {
      steps { sh '$PROD_DIR/venv/bin/python $PROD_DIR/status_check.py | tee reports/smoke.txt' }
    }
  }
  post {
    success { sh 'python3 ci/announce.py --status SUCCESS' }
    failure { sh 'python3 ci/announce.py --status FAILURE' }
  }
}
