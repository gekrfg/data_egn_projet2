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
            powershell 'python test.py '
            }
        }
      }
	}
 }
