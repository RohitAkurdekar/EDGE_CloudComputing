    diot@diot:~$ docker network inspect bridge 
    [
        {
            "Name": "bridge",
            "Id": "70956b36278f2b9ac5c19e11f4c41ee9a46a663028ec42b338d8bf35978ec54e",
            "Created": "2023-01-21T07:50:56.01789133+05:30",
            "Scope": "local",
            "Driver": "bridge",
            "EnableIPv6": false,
            "IPAM": {
                "Driver": "default",
                "Options": null,
                "Config": [
                    {
                        "Subnet": "172.17.0.0/16",
                        "Gateway": "172.17.0.1"
                    }
                ]
            },
            "Internal": false,
            "Attachable": false,
            "Ingress": false,
            "ConfigFrom": {
                "Network": ""
            },
            "ConfigOnly": false,
            "Containers": {
                "b535538cf725a50d5a4cda7ed27e2f7467ada8aa1e22a5ac54ef1d527a554441": {
                    "Name": "demo_nw_non",
                    "EndpointID": "c21363cc15ce882836eaa65bfa8bfc218bed86e00d643fbce703d2d78ff0ebdc",
                    "MacAddress": "02:42:ac:11:00:02",
                    "IPv4Address": "172.17.0.2/16",
                    "IPv6Address": ""
                }
            },
            "Options": {
                "com.docker.network.bridge.default_bridge": "true",
                "com.docker.network.bridge.enable_icc": "true",
                "com.docker.network.bridge.enable_ip_masquerade": "true",
                "com.docker.network.bridge.host_binding_ipv4": "0.0.0.0",
                "com.docker.network.bridge.name": "docker0",
                "com.docker.network.driver.mtu": "1500"
            },
            "Labels": {}
        }
    ]
