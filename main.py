import requests

local_repo_url = "http://localhost:42303"

list_of_images=["banzaicloud/fluentd","banzaicloud/logging-operator","bitnami/external-dns","bitnami/kubectl","bitnami/memcached","bitnami/postgresql","fluent/fluent-bit","fluxcd/helm-controller","fluxcd/kustomize-controller","fluxcd/notification-controller","fluxcd/source-controller","gitea/gitea","google_containers/kubernetes-dashboard-init-amd64","grafana/grafana","grafana/loki","helm/chartmuseum","ingress-nginx/kube-webhook-certgen","istio/install-cni","istio/operator","istio/pilot","istio/proxyv2","jaegertracing/all-in-one","jaegertracing/jaeger-operator","jetstack/cert-manager-cainjector","jetstack/cert-manager-controller","jetstack/cert-manager-webhook","jetstack/kube-oidc-proxy","jimmidyson/configmap-reload","kiali/kiali","kiali/kiali-operator","kiwigrid/k8s-sidecar","knative-nightly/knative.dev/net-istio/cmd/controller","knative-nightly/knative.dev/net-istio/cmd/webhook","knative-releases/knative.dev/serving/cmd/activator","knative-releases/knative.dev/serving/cmd/autoscaler","knative-releases/knative.dev/serving/cmd/autoscaler-hpa","knative-releases/knative.dev/serving/cmd/controller","knative-releases/knative.dev/serving/cmd/webhook","kube-state-metrics/kube-state-metrics","kubebuilder/kube-rbac-proxy","kubecost1/cost-model","kubecost1/frontend","kubecost1/server","kubernetes-multicluster/kubefed","kubernetes_incubator/nfs-provisioner","kubernetesui/dashboard","kubernetesui/metrics-scraper","library/nginx","library/traefik","mesosphere/cluster-observer","mesosphere/dex","mesosphere/dex-controller","mesosphere/dex-k8s-authenticator","mesosphere/dkp-diagnostics-node-collector","mesosphere/grafana-plugins","mesosphere/karma","mesosphere/kommander","mesosphere/kommander2-appmanagement","mesosphere/kommander2-federation-authorizedlister","mesosphere/kommander2-federation-controller-manager","mesosphere/kommander2-federation-webhook","mesosphere/kommander2-flux-operator","mesosphere/kommander2-kubetools","mesosphere/kommander2-licensing-controller-manager","mesosphere/kommander2-licensing-webhook","mesosphere/kubeaddons-addon-initializer","mesosphere/kubetunnel-controller","mesosphere/kubetunnel-webhook","mesosphere/pause-busybox","mesosphere/traefik-forward-auth","metallb/controller","metallb/speaker","minio/console","minio/mc","minio/minio","minio/operator","nginxinc/nginx-unprivileged","nvidia/dcgm-exporter","nvidia/k8s-device-plugin","openpolicyagent/gatekeeper","openpolicyagent/gatekeeper-crds","prometheus/alertmanager","prometheus/node-exporter","prometheus/prometheus","prometheus-adapter/prometheus-adapter","prometheus-operator/prometheus-config-reloader","prometheus-operator/prometheus-operator","stakater/reloader","thanos/thanos","thanosio/thanos","velero/velero","velero/velero-plugin-for-aws"]


for image in list_of_images:
    print(image)

    # get image tags
    http_request_url = f"{local_repo_url}/{image}/v2/tags/list"

    print(http_request_url)







