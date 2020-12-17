pipeline{
  agent any
  stages {
    stage('Build application'){
      steps{
	    script{
            if (env.BRANCH_NAME == 'dev'||env.BRANCH_NAME == 'realease'){
            bat 'docker build -t data-eng-proj2 .'
			}
          }
        }
      }  
    
    stage('Run image'){
      steps{
	    script{
	        if (env.BRANCH_NAME == 'dev'||env.BRANCH_NAME == 'realease'){
            bat 'docker run -p 5000:5000 data-eng-proj2'
			}
		}
      }
    }
    stage('Unittest'){
      steps{
        script{
		  if (env.BRANCH_NAME == 'dev'){
            bat 'python test.py '
            }
        }
      }
	}
	
	stage('Stresstest'){
      steps{
        script{
		  if (env.BRANCH_NAME == 'dev'){
            bat 'python stress_test.py '
            }
        }
      }
	}
	
    
    stage('User acceptance'){
      steps{
        script{
          if (env.BRANCH_NAME == 'realease' ) {
            input 'Do you want to push?'
          }
        }
      }
    }
	
	
    stage('Merger'){
      steps{
        script{
          if (env.BRANCH_NAME == 'realease') {
            echo 'Merge'
          }
        }
      }
    }
	
	
	}

  }
