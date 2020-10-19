### Tracking Pittsburghs Busess Never Been so Easy.

The purpose of this application is to spin up and track bus locations across the entire Port Authority System.

## Pittsburgh Port Authority Requirements

You need to have an API key through: https://truetime.portauthority.org/bustime/home.jsp

This will allow you to ping the live data from Port Authority.

## History

We need a backstop for History.  We dont need to know ALL history indefinately, so to keep the Elasticsearch Database small, the backstop will be 1 Month.  This is defined in the Config file, so each user can choose to save more or less data.  1 Month is enough because you will generally see Routes of all buses and garage stops.  Using Kibana or ES to do ML to determine hiccups in routes will easily be determined with a month of history.  It will project traffic and hiccups with a month of routes and timelines.

## Set Up / Install
Standing up the full cluster will be done by doing the following:
- Install Docker.
- Enable Kubernetes
- Update the configuration hardware for the cluster.  Give it additional ram, space, threads.
- Restart the cluster to save the infomration.
- Ensure that `kubectl` is pointing to the Docker for [Platform] correctly.
```
kubectl congif get-contexts
kubectl config use-context docker-for-desktop
```
- You need an ID for Pittsburgh's Data API.
- Now you need to apply the elastic to this cluster, filling out the part where it says: TRANSIT_API
```
kubectl apply -f elastic.yaml
```
This will create the cluster for monitoring the system.  We will need to do some additional things though.

To do the following Kibana items as well as access maps, you need to set up the proxy for it.  This is done with the following information:

```
PASSWORD=$(kubectl get secret elasticsearch-es-elastic-user -o go-template='{{.data.elastic | base64decode}}')
echo "Username: elastic"
echo "Password: $PASSWORD"
kubectl port-forward service/kibana-kb-http 5601
```

- Go into Kibana and set up a Lifecycle policy for index retention.
- Go into Kibana and set up mapping for the following:
  - You will need to create a mappingg for:  bustime-response.vehicle.location which will be of type: 'Geo Point'

## TODO
Implement a mechanism to update elasticsearch with Lifecycle policy and mapping index templates.
