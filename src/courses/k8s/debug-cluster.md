---
license: © 2025 Tom Avenel under 󰵫  BY-SA 4.0
title: Debug du cluster
layout: '@layouts/CoursePartLayout.astro'
---

- Tester localement kubectl sur un control plane

```sh
export KUBECONFIG=/etc/kubernetes/admin.conf
kubectl get nodes -o wide
```

- Vérifier les logs du kubelet

```sh
systemctl kubelet
journalctl -xeu kubelet
```

- Inspecter les conteneurs

```sh
crictl --runtime-endpoint unix:///run/containerd/containerd.sock ps -a | grep -v pause
crictl --runtime-endpoint unix:///run/containerd/containerd.sock logs …
```

:::tip
En _k3s_, le _kubelet_ est directement intégré dans le service de _k3s_ => dans le service systemd `k3s` (_master_) ou `k3s-agent` (_worker_).
:::

