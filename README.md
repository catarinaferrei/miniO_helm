# miniO_helm
A description of how to deploy miniO in the cloud


To deploy the miniO it was needed to create a helm chart and a template folder containing three manifestos: pvc, service and deployment.
The PVC makes a request to the storage class. The service type is loadbalancer. Some issues were faced when accessing to the service in the minikube and it was required to use kubectl port-forward. 
