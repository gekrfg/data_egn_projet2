pipeline{
 agent any
 stages{
 
  stage('Build app') {
  steps{
      powershell 'python webapp.py'
  }
 }

  stage('Test'){
  steps{
     powershell 'python test.py'
     }
}
}

}
