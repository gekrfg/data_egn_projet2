pipeline{
  agent any
  stages {
    stage('Build application'){
      steps{
        
            powershell 'docker build -t data-eng-proj2 .'
          
        }
      }  
    
    stage('Run image'){
      steps{
	  
            powershell 'docker run -p 5000:5000 data-eng-proj2'
      }
    }
    stage('Unittest'){
      steps{
        script{
		  if (env.BRANCH_NAME == 'dev'){
            powershell 'python stress_test.py '
            }
        }
      }
	}
	
    
    stage('User acceptance'){
      steps{
        script{
          if (env.BRANCH_NAME == 'main' ) {
            input 'Do you want to push?'
          }
        }
      }
    }
	
	stage('Release'){
      steps{
        script{
          if (env.BRANCH_NAME == 'dev') {
            echo 'Push to release '
          }
          else if (env.BRANCH_NAME == 'main') {
            echo 'Already in release'
          }
        }  
      }
    }
	
    stage('Merger'){
      steps{
        script{
          if (env.BRANCH_NAME == 'main') {
            echo 'Merge'
          }
        }
      }
    }
	}

  }
