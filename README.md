# miniO_helm
A description of how to deploy miniO in the cloud


To deploy the miniO it was needed to create a helm chart and a template folder containing three manifestos: pvc, service and deployment.
The PVC makes a request to the storage class. 

The service type is loadbalancer. Some issues were faced when accessing to the service in the minikube and it was required to use kubectl port-forward. 

## Deployment

![](deployment.PNG)


The following figure contains an example of the deployment which was used to deploy the miniO. As we can see under the container we had to set the env variables which correspond to the login and password of the user. To mount the data, we had to create a volume mounts that will save the data of the container in a persistent state. The volume will claim the storage class that is defined in the persistent volume claim and volume mounts will consume that resource storage.


## Persistent Volume Claim

![](pvc.PNG)

The persistent volume claim is used to make a storage request in the cluster. It's bounded to a pod which you can define it on the deployment as shown above. To bind a volume claim you can do it dynamically or via static. If done via static, the cluster administrator creates a persistent volume according to the specifications that are set on the persistent volume claim. In our case, we opted for the dynamic binding. To do such, in the manisfest yaml you need to specify the name of the storage class (It's assumed your cluster already has a storage class, if not you need to create one) and the cluster will bind a persistent volume according to your specifications.

## Service

![](service.PNG)

The service type is a LoadBalancer. Service works as an abstraction of the Pods IP in the sense that if clients wanted to connect with a Pod directly, due to the short life cyle of pods, there would be constantly problems due to the pods restarting and shifting its IP. Service, in the other hand, allows for a static IP. To connect our Pod to the external world we can use either LoadBalancer or a NodePort. 

The target Port must correspond to the container Port because that's the port that the pod is listening to and the port that the service receives requests and sends it to the pod. To match a service with a pod the selector must be same as the pod's name.

The Port and TargetPort can be the same port or of different ports, only the Targetport and container port must match. The difference between the port and the targetPort is that the Port is the Port that the service listens to (service is open at a specific port) and the forwards the requests to TargerPort. Then the TargetPort is responsible to forward these requests to the container.
