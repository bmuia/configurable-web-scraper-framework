pipeline {
    agent any

    environment {
        VENV = "venv"
    }

    stages {
        stage("Checkout") {
            steps {
                checkout scm
            }
        }

        stage("Setup environment") {
            steps {
                sh """
                    python3 -m venv ${VENV}
                    . ${VENV}/bin/activate
                """
            }
        }

        stage("Initialize dependencies") {
            steps {
                sh """
                    . ${VENV}/bin/activate
                    ${VENV}/bin/pip install --upgrade pip
                    ${VENV}/bin/pip install -r requirements.txt
                """
            }
        }

        stage("Run tests") {
            steps {
                sh """
                    . ${VENV}/bin/activate
                    ${VENV}/bin/python -m unittest discover -v
                """
            }
        }

        stage("Successfully built") {
            steps {
                echo "✅ Happy coding!"
            }
        }
    }
}
