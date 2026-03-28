
To get from your laptop to the z/OS running on a server yo need to add the route

    sudo ip route add 172.26.1.0/24 via 10.1.0.3
