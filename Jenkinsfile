pipeline{
 agent any
 stages('Build app') {
 steps{
      powershell 'python webapp.py'
 }
 }

stages('Test'){
steps{
     powershell 'python test.py'
}
}


}
